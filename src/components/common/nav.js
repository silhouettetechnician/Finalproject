import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../auth/userAuth'
import 'bulma'
class Nav extends React.Component{
  constructor(){
    super()
    this.logout = this.logout.bind(this)
  }

  logout(){
    Auth.logout()
    this.props.history.push('/')
  }



  render(){
    return(
      <header>
        <nav className="nav-extended" id="navbar">
          <div className="nav-wrapper">
            <a href="#" data-target="mobile-demo" className="sidenav-trigger"><i className="material-icons">menu</i></a>




            <div id="nav-mobile" className="right hide-on-med-and-down">
              {Auth.isAuthenticated() && <Link to='/posts/new'>POST ITEM</Link>}
              {Auth.isAuthenticated() && <Link to='/profile'>MY PROFILE</Link>}
              {!Auth.isAuthenticated() &&<Link to='/register'>REGISTER</Link>}
              {!Auth.isAuthenticated() && <Link to='/login'>LOGIN</Link>}
              {Auth.isAuthenticated() && <a onClick={this.logout}>LOGOUT</a>}
            </div>
          </div>

          <div className="nav-content">
            <Link to='/'><img className="logo" src="../../assets/assets/images/logo_transparent_background.png" /></Link>
            <div className="tabs tabs-transparent">
              <Link to='/' className="tab">Home</Link>
              <Link to='/designers' className="tab">Designers</Link>
              <Link to='/posts' className="tab">Recent Posts</Link>
              <Link to='/users' className="tab">Top Swappers</Link>
            </div>
          </div>
          <div className="sidenav" id="mobile-demo">
            {Auth.isAuthenticated() && <Link to='/posts/new'>Post Item</Link>}
            {Auth.isAuthenticated() && <Link to='/profile'>My Profile</Link>}
            {!Auth.isAuthenticated() &&<Link to='/register'>Register</Link>}
            {!Auth.isAuthenticated() && <Link to='/login'>Login</Link>}
            {Auth.isAuthenticated() && <a onClick={this.logout}>Logout</a>}
          </div>
        </nav>
      </header>
    )
  }
}

export default withRouter(Nav)
