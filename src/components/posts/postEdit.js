import React from 'react'
import axios from 'axios'
import 'bulma'
import Auth from '../auth/userAuth'
import PostForm from './postForm'

class PostEdit extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {
        title: '',
        description: '',
        size: '',
        designers: '',
        categories: '',
        image1: '',
        image2: '',
        image3: ''
      },
      errors: {}
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleCategorySelect = this.handleCategorySelect.bind(this)
    this.handleDesignerSelect = this.handleDesignerSelect.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handlePhotoModal = this.handlePhotoModal.bind(this)
  }

  componentDidMount(){
    axios.get(`/api/posts/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err))
  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleCategorySelect({ value }) {
    const data = { ...this.state.data, categories: value }
    this.setState({ data })
  }

  handleDesignerSelect({ value }){
    const data = {...this.state.data, designers: value }
    this.setState({ data })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log(this.props)
    axios.put(`/api/posts/${this.props.match.params.id}`,
      this.state.data,
      { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
      .then(() => {
        this.props.history.push(`/posts/${this.props.match.params.id}`)
      })
      .catch(err => this.setState({errors: err.response.data.errors}))
  }

  render(){
    return(
      <main>
        <PostForm
          handlePhotoModal={this.handlePhotoModal}
          handleDesignerSelect={this.handleDesignerSelect}
          handleCategorySelect={this.handleCategorySelect}
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}
          data={this.state.data}
          errors={this.state.errors}

        />
        <button>delete</button>
        <button>edit</button>
      </main>
    )
  }
}
export default PostEdit
