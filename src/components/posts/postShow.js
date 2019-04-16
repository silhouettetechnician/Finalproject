import React from 'react'
import axios from 'axios'
import 'bulma'
import { Link } from 'react-router-dom'
import Auth from '../auth/userAuth'

class PostShow extends React.Component{
  constructor(){
    super()
    this.state = {
    }

    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleDelete = this.handleDelete.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  componentDidMount(){

    this.getInfo()
  }

  getInfo(){
    axios.get(`/api/posts/${this.props.match.params.id}`)
      .then(res => this.setState({ post: res.data }))
    const postId = this.props.match.params.id
    this.setState({ itemPost: postId })
  }

  handleSubmit(e){
    e.preventDefault()
    axios.post(`/api/posts/${this.props.match.params.id}/comments`, this.state, { headers: { Authorization: `Bearer ${Auth.getToken()}`}})
      .then(res => this.setState({ content: ''}, this.getInfo))
      .catch(err => this.setState({ errors: err.response.data.errors}))

    console.log(res)
  }

  handleAddComment(comment){
    this.setState(prevState => {
      return {
        comments: prevState.comments.concat(comment)
      }
    })
  }

  handleDelete() {
    axios.delete(`/api/posts/${this.props.match.params.id}`,{ headers: { Authorization: `Bearer ${Auth.getToken()}`}})
      .then(()=> {
        this.props.history.push('/posts')
      })
      .catch(err => console.log(err))
  }

  handleChange({ target: { name, value }}) {
    this.setState({ [name]: value})
  }



  isOwner() {
    return Auth.isAuthenticated() && this.state.post.creator_id === Auth.getPayload().sub
  }


  render() {
    console.log(this.state.post, 'post')
    if (!this.state.post) return null
    const { post } = this.state
    console.log(this.state)
    return(
      <main className="section">
        <div className="container">
          <h2 className="title">{post.title}

            <Link to={`/user/${post.creator.id}`}>
              <figure className="snip1578">
                <img src={post.creator.image} alt="profile-sample6" />
                <figcaption>
                  <h3>{post.creator.username}</h3>
                  <div className="icons"><a href="#"><i className="ion-social-twitter"></i></a>
                    <a href="#"> <i className="ion-social-instagram-outline"></i></a>
                    <a href="#"> <i className="ion-social-github"></i></a>
                  </div>
                </figcaption>
              </figure>
            </Link>
          </h2>
          {post.designers.map(designer =>
            <h4 className="title is-4" key=''>
              <p>{designer.name}</p>
            </h4>
          )}
          <div className="rows">
            <div className="row is-three-quarter">
              <hr />
              <div className="carousel">
                <img src={post.image1} />
                <img src={post.image2} />
                <img src={post.image3} />
              </div>

            </div>
            <div className="row is-half">
              <h4 className="title is-4"></h4>
              <p>{post.size}    {this.isOwner() && <Link className="button is-warning" to={`/posts/${post.id}/edit`}>Edit</Link>}
                {this.isOwner() && <button className="button is-danger" onClick={this.handleDelete}>Delete</button>}</p>
              <hr />
              <h4 className="title is-4"></h4>
              <p>{post.description}</p>
              <hr />
              <h4 className="title is-4"></h4>

              <hr />
              <h1 className='title is-4'>Comments</h1>
              <form
                onSubmit={this.handleSubmit}

              >
                <input
                  onSubmit={this.handleAddComment}
                  onChange={this.handleChange}
                  value={this.state.content || ''}
                  name='content'
                  placeholder="Ask a question.."
                />

              </form>
              <div className="comments">
                {post.comments && post.comments.map(
                  comment => (
                    <div className="comments" key={comment.id}>
                      <ul>{comment.content}</ul><span>{post.creator.username}</span>
                    </div>

                  )
                )}

              </div>

            </div>
          </div>
        </div>
      </main>

    )
  }
}
export default PostShow
