import React from 'react'
import axios from 'axios'
import Likes from '../common/likes'

import { Link } from 'react-router-dom'

class PostIndex extends React.Component{
  constructor(){
    super()
    this.state = {
      like: false
    }
  }

  componentDidMount(){
    axios.get('/api/posts')
      .then(res => this.setState({ content: res.data }))
  }

  handleLike(e){
    e.preventDefault()
    axios.post(`/api/posts/${this.props.match.params.id}/likes`
    )
  }

  render() {
    if(!this.state.posts) return null
    return  (
      <main  className="section">
        <div className="container">
          <div className="columns is-mobile is-multiline">
            {!this.state.posts && <p>...loading</p>}
            {this.state.posts && this.state.posts.map(post =>
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
                <Likes />

              </div>
            )}
          </div>
        </div>
      </main>
    )
  }

}
export default PostIndex
