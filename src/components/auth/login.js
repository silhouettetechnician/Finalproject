import React from 'react'
import axios from 'axios'
import Auth from './userAuth'
import Flash from './flash'
import { Button, Modal, Icon } from 'react-materialize'
import m from 'materialize-css'


class Login extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: ''
      }
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleDone = this.handleDone.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: { name , value }}) {
    const data = {...this.state.data, [name]: value}
    this.setState({ data })
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
    axios.post('/api/login', this.state.data)
      .then(res => {
        Flash.setMessage('success', res.data.message)
        Auth.setToken(res.data.token)
        this.props.history.push('/')
      })
      .catch(() => {
        this.setState({ error: 'Invalid Credentials'})
      })
  }

  render() {
    return(
      <div>
        <Modal header="Login" trigger={this.state.trigger}>
          <div className="row">
            <form className="col s12" onSubmit={this.handleSubmit}>
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
                <span className="helper-text" data-error="wrong" data-success="3 plus digits">2 plus digits</span>
              </div>
              <Button type="submit" waves="light" className="right">
                Login
                <Icon right>
                send
                </Icon>
              </Button>
            </form>
          </div>
        </Modal>
        <div className="home-container2"></div>
      </div>
    )
  }
}

export default Login
