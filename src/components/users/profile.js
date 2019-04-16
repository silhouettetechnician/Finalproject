import React from 'react'
import axios from 'axios'
import 'bulma'
import Comments from '../common/comments'
import { Link } from 'react-router-dom'
import Auth from '../auth/userAuth'


class Profile extends React.Component{
  constructor(){
    super()
    this.state = {}
  }

  componentDidMount(){
    this.getData()
  }

  getData(){
    axios.get(`/api/users/${Auth.getPayload().sub}`)
      .then(res => this.setState({ user: res.data }))
  }



  render() {
    console.log(this.state.user, 'user')
    if (!this.state.user) return null
    const { user } = this.state
    console.log(user)
    return(
      <main className="section">
        <div className="container">
          <div className="title-container">


          </div>
          <hr />
          <h4 className="title is-4">My Posts</h4>
          {user.created_posts && user.created_posts.map((user, id) => (
            <div key={id} className="posts">
              <Link to={`/user/${user.id}`}>
                <div>{user.created_posts}</div>
              </Link>
            </div>
          ))}
          <div className="columns">
            <div className="column is-half">


            </div>
            <div className="column is-half">
              <h5 className="title is-5">Contact Email</h5>
              <p className="subtitle">{user.email}</p>
              <hr />
              <h5 className="title is-5">Discounts available</h5>
              <p>{user.discounts}</p>
              <hr />
              <h5 className="title is-5">Designer interests</h5>
              <p className="subtitle">{user.email}</p>
              <hr />
              <h5 className="title is-5">Discounts available</h5>
              <p>{user.discounts}</p>
              <hr />

              <hr />
              <h2 className="title is-4">Comments</h2>

              {user.comments && user.comments.map(
                comment => (
                  <div key={comment.itemPost_id}>
                    <p>{comment.content}</p>
                  </div>
                )
              )}
            </div>
          </div>
        </div>
      </main>

    )
  }
}

export default Profile
