//
// <header>
// <div className="header">
//     <Link to='/'><img className="logo" src="../../assets/logo-dark.png" /></Link>
//     <nav className="nav">
//       <Link to='/map'>Map</Link>
//       {!Auth.isAuthenticated() && <Link to='/register'>Register</Link>}
//       {!Auth.isAuthenticated() && <Link to='/login'>login</Link>}
//       {Auth.isAuthenticated() && <Link to='/users/:id'>Account</Link>}
//       {Auth.isAuthenticated() && <Link to='/spaces/new'>Create</Link>}
//       {Auth.isAuthenticated() && <Link to='/' onClick={this.logout}>Logout</Link>}
//     </nav>
//   </div>
//   </header>




postfour = ItemPost(title='Navy Acne Ayan Satin A/W17', description="""Ayan Satin chinos are cut in a slim fit and have a total of four functional pockets to the front and back. This wearable cotton blend style is finished with zipper and button fastenings.""", size="""Size: US 30 / EU 46""", designers=[Acne_Studios])

  postfive = ItemPost(title='Workwear SHIR000005 *last drop', description="""NWT Size 44/XS-S Hazel Beige Retail $240 Fits oversize""", size="""XS, 20” Chest""", designers=[Acne_Studios])

  postsix = ItemPost(title='BNWT Adidas x Alexander Wang Track Pants', description="""Limited edition Alexander Wang collaboration Track Pants, I'm looking for the best discount i can get, check out my profile for swaps""", size="""Size: US 30 / EU 46""", designers=[Alexaner_Wang, Adidas])

  postseven = ItemPost(title='Gucci Angry Cat Sweater', description="""Gucci sweater needed asap, will offer discount or more than willing to pay in bank transfer please check out my account and let me know""", size="""Size: US L / EU 52-54 / 3""", designers=[Gucci])

  posteight = ItemPost(title='Common Projects Achilles Low White Leather ', description="""White Common Projects low sneakers wanted, willing to offer a discount swap if you're interested in my discount list""", size="""Size: US 7 / EU 40""", designers=[Common_Projects])


  updateLikes() {

    if(!this.state.updated) {
      this.setState((prevState, props) => {
        return {
          likes: prevState.likes + 1,
          updated: true
        }
      })

    } else {

      this.setState((prevState, props) => {
        return {
          likes: prevState.likes - 1,
          updated: false
        }
      })

    }
  }


Likes
<span className="price">Liked by</span>
<div><a onClick={ ()=>this.setState({ isLiked: !this.state.isLiked })}>
  { this.state.isLiked
    ? <i className="far fa-heart"></i>
    : <i className="fas fa-heart"></i>} {post.liked_by.length}</a>
</div>




  https://cdn.shopify.com/s/files/1/0293/9277/products/10-29-18_Studio_2_10-57-59_P633_MediumBlueWash0475_JD.jpg?v=1551316840



  import React from 'react'
  import axios from 'axios'

  class Profile extends React.Component{
    constructor(){
      super()



      render(){
        return(
          <h1>hello</h1>
        )
      }


      }
    }


  export default Profile



  import React from 'react'
  import 'bulma'
  import axios from 'axios'

  class Comments extends React.Component {
    constructor(){
      super()
      this.state = {}
    }

    handleCommentSubmit(event) {
      event.preventDefault()
      axios.post(`/api/posts/${this.props.match.params.id}/comments`,
        this.state.data,
        { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
        .then((res) => {
          const { content, created_at, id, creator: {id: creator_id, username }} = res.data
          const newComment = { content, created_at, id, creator_id}
          const newComments = [...this.state.posts.comments, newComment]
          const newPost = {...this.state.posts}
          newPost.comments = newComments
          this.setState({ post: newPost, data: { content: ''} })
        })
        .catch(err => console.log(err))
     }
    render(){
      return(

        <article className="media">

          <div className="media-content">
      <div className="field">
        <p className="control">
          <textarea className="textarea" placeholder="Add a comment..."></textarea>
        </p>
      </div>
      <div>
        <div className="level-left">
          <div className="level-item">
            <a className="button is-info">Submit</a>
          </div>
        </div>
        <div className="level-right">
          <div className="level-item">
            <label className="checkbox">
              <input type="checkbox" /> Press enter to submit
            </label>
          </div>
        </div>
      </div>
    </div>
  </article>
  )
  }
  }

  export default Comments
