import { Link } from 'react-router-dom'
import React from 'react'
import axios from 'axios'
import 'bulma'

class DesignerShow extends React.Component{
  constructor(){
    super()
    this.state = {}

    this.filterDesign = this.filterDesign.bind(this)
  }


  componentDidMount(){
    console.log(this.props.match.params.id, 'the props')
    axios.get('/api/posts')
      .then(res => this.setState({ posts: res.data }, () => this.filterDesign()))
  }

  filterDesign(){
    const currentDesigner = this.props.match.params.id
    const filteredPosts = []
    const posts = this.state.posts
    console.log(posts)
    posts.forEach(function(post){
      if(post.designers[0].id === parseInt(currentDesigner)){
        filteredPosts.push(post)
      }
    }
    )
    this.setState({ filteredPosts: filteredPosts })
  }


  render(){
    if(!this.state.filteredPosts) return null
    return  (
      <main  className="section">
        <div className="container">
          <div className="columns is-mobile is-multiline">
            {!this.state.filteredPosts && <p>...loading</p>}
            {this.state.filteredPosts && this.state.filteredPosts.map(post =>
              <div key={post.id} className="column is-one-quarter-desktop is-one-third-tablet is-half-mobile">

                <Link to={`/posts/${post.id}`}>
                  <div className="card">
                    <div className="card-headder">
                    </div>
                    <div>
                      <div id="image-container-shop">
                        <img className="homepage-image" src={post.image1}  />
                        <div className="overlay">
                          <div className="hover-over">
                            {post.title} <br />
                            {post.price}
                          </div>
                        </div>
                      </div>


                    </div>
                  </div>
                </Link>

                <div><a onClick={ ()=>this.setState({ isLiked: !this.state.isLiked })}>
                  { this.state.isLiked
                    ? <i className="far fa-heart"></i>
                    : <i className="fas fa-heart"></i>} {post.liked_by.length}</a>
                <span className="price">{post.price}</span>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    )
  }
}
export default DesignerShow
