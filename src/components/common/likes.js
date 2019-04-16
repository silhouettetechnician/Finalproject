import React from 'react'
import axios from 'axios'

class Likes extends React.Component {

  constructor(props){

    super(props)
    this.state = {
      likes: '',
      isLiked: false
    }

  }

  handleLike(e){
    e.preventDefault()
    axios.post(`/api/posts/${this.props.match.params.id}/likes`
    )
      .then(res => this.setState({ creator: res.data }))
  }



  render(){
    const { post } = this.state
    return(
      <main>
        <span className="price">Liked by</span>
        <div><a onClick={ ()=>this.setState({ isLiked: !this.state.isLiked })}>
          { this.state.isLiked
            ? <i className="far fa-heart"></i>
            : <i className="fas fa-heart"></i>} {post.liked_by.length}</a>
        </div>
      </main>
    )
  }
}



export default Likes
