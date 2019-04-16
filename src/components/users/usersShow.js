import React from 'react'
import axios from 'axios'
import StarRatings from 'react-star-ratings'

import { Link } from 'react-router-dom'

class UsersShow extends React.Component{
  constructor(){
    super()
    this.state = {}
  }

  componentDidMount(){
    axios.get('/api/users')
      .then(res => this.setState({ users: res.data }))
  }

  changeRating( newRating ) {
    this.setState({
      rating: newRating
    })
  }
  render() {
    if(!this.state.users) return null
    return  (
      <main  className="section">
        <div className="container">
          <div className="columns is-mobile is-multiline">
            {!this.state.users && <p>...loading</p>}
            {this.state.users && this.state.users.map(user =>
              <div key={user.id} className="column is-one-third-desktop is-one-third-tablet is-half-mobile">
                <Link to={`/users/${user.id}`}>
                  <div className="card">
                  </div>
                  <div className="card-image">
                    <h4 className="card-header-title1">{user.name}</h4>
                    <h6 className="card-header-title">{user.username}</h6>
                    <figure className="imageHolder">
                      <img src={user.image} alt={user.name} />
                    </figure>
                  </div>
                </Link>
                <div className="card-content">
                  <StarRatings
                    rating={3.4}
                    starDimension="30px"
                    starSpacing="5px"
                    name='rating'
                    value={user.liked_by}
                    numberOfStars={5}
                  />
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    )
  }

}
export default UsersShow
