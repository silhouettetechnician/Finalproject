import React from 'react'
import axios from 'axios'
import 'bulma'
import { Link } from 'react-router-dom'
import Comments from '../common/comments'

class UsersEach extends React.Component{
  constructor(){
    super()
    this.state = {}

  }

  componentDidMount(){
    axios.get(`/api/users/${this.props.match.params.id}`)
      .then(res => this.setState({ user: res.data }))
  }

  render(){
    console.log(this.state)
    if(!this.state.user) return null
    const { user } = this.state
    return(
      <main className="section">
        <div className="container">
          <h3 className="title">{user.username}</h3>
          <hr />
          <div className = "columns">
            <div className="columns is-half">

              <figure className="image">
                <img src={user.image} />
              </figure>

            </div>
            <div className="columns is-half">
              <div><h4 className="row is-4">Username: {user.username}</h4></div><br />
              <div><h4 className="row is-4">Email: {user.email}</h4></div><br />
              <div><h4 className="title is-4">Discounts: {user.discounts}</h4></div><br />
              <div><h4 className="title is-4">Interested in: {user.brand_likes}</h4></div>
            </div>
          </div>
          <h1>Comments</h1>
          {user.comments && user.comments.map(
            comment => (

              <div key=''>
                <p>{comment.content}</p>
                <p>{comment.creator.username}</p>
              </div>
            )
          )}
          <div className="comment-box">
          
          </div>

          <div className="profile-header"><h1>Your Posts</h1></div>
          {user.posts && user.posts.map((user, id) => (
            <div key={id} className="posts">
              <div>{user.posts}</div>
              <Link to={`/user/${user.id}`}>
              </Link>

            </div>
          ))}


        </div>
      </main>
    )

  }
}

export default UsersEach
