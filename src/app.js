import React from 'react'
import ReactDOM from 'react-dom'
import './stylesheets/style.scss'
import { BrowserRouter as Browser, Route, Switch } from 'react-router-dom'

import SecureRoute from './components/common/secureRoute'
import Login from './components/auth/login'
import Register from './components/auth/register'

import DesignerIndex from './components/designers/designerIndex'
import DesignerShow from './components/designers/designerShow'
import UsersEach from './components/users/usersEach'
import UsersShow from './components/users/usersShow'
import PostShow from './components/posts/postShow'
import PostNew from './components/posts/postNew'
import PostEdit from './components/posts/PostEdit'
import PostIndex from './components/posts/postIndex'
import Profile from './components/users/profile'
import Home from './components/pages/home'
import FlashMessages from './components/common/flashMessages'
import Nav from './components/common/nav'
import Footer from './components/common/footer'

class App extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <Browser>
        <Nav />
        <FlashMessages />
        <Switch>
          <Route exact path= "/" component={Home} />
          <Route path="/profile" component={Profile} />
          <Route path="/designers/:id" component={DesignerShow} />
          <Route path="/designers" component={DesignerIndex} />
          <Route path="/users/:id" component={UsersEach} />
          <Route exact path= "/posts" component={PostIndex} />
          <SecureRoute exact path= '/posts/new' component={PostNew} />
          <Route path='/posts/:id' component={PostShow} />
          <SecureRoute path='/posts/:id/edit' component={PostEdit} />
          <Route path='/users' component={UsersShow} />
          <Route path='/register' component={Register} />
          <Route path='/login' component={Login} />
        </Switch>
        <Footer />
      </Browser>
    )
  }

}


ReactDOM.render(
  <App />,
  document.getElementById('root')
)
