import React from 'react'
import axios from 'axios'
import Auth from './userAuth'
import { Button, Modal, Icon } from 'react-materialize'
import { Link } from 'react-router-dom'
import m from 'materialize-css'


class Register extends React.Component {
  constructor() {
    super()

    this.state = {
      showModal: false,
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: ''
      },
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleDone = this.handleDone.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: { name , value }}) {
    const data = {...this.state.data, [name]: value}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleDone(e){
    e.preventDefault()
    this.props.history.push('/login')
  }

  componentDidMount() {
    const trigger = <Button id="triggerbutton" type="submit" waves="light" className="left orange">D<Icon right>send</Icon></Button>
    this.setState({trigger}, () => document.getElementById('triggerbutton').click())
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('api/register', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
      })
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.message))
  }

  render() {
    return(
      <Modal
        header="Register"
        backdrop='static'
        trigger={this.state.trigger}>
        <div className="row">
          <form className="col s12" onSubmit={this.handleSubmit}>
            <div className="input-field col s12">
              <input
                id="username"
                type="text"
                name="username"
                value={this.state.data.username}
                onChange={this.handleChange}
              />
              <label htmlFor="name">Username</label>
            </div>
            <div className="input-field col s12">
              <input
                id="email"
                type="email"
                className="validate"
                name="email"
                value={this.state.data.email}
                onChange={this.handleChange}
              />
              <label htmlFor="email">Email</label>
            </div>
            <div className="input-field col s12">
              <input id="password"
                type="password"
                className="validate"
                name="password"
                value={this.state.data.password}
                onChange={this.handleChange}
              />
              <label htmlFor="password">Password</label>
              <span className="helper-text" data-error="wrong" data-success="enough characters"></span>
            </div>
            <div className="input-field col s12">
              <input
                id="passwordConfirmation"
                type="password"
                className="validate"
                name="password_confirmation"
                value={this.state.data.password_confirmation}
                onChange={this.handleChange}
              />
              <label htmlFor="password">Password Confirmation</label>
              <span className="helper-text" data-error="wrong" data-success="enough characters"></span>
            </div>
            <p>Already Registered? <Link to='/login'>Login Here</Link></p>
            <Button type="submit" waves="light" className="right">
              Register
              <Icon right>
              send
              </Icon>
            </Button>
          </form>
        </div>
      </Modal>
    )
  }
}

export default Register
