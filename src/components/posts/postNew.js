import React from 'react'
import Auth from '../auth/userAuth'
import axios from 'axios'
// import * as filestack from 'filestack-js'

import PostForm from './postForm'



class PostNew extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {
        title: '',
        description: '',
        size: '',
        designer_id: '',
        category_id: '',
        image1: '',
        image2: '',
        image3: ''
      },
      errors: {},
      designers: [],
      categories: []
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleCategorySelect = this.handleCategorySelect.bind(this)
    this.handleDesignerSelect = this.handleDesignerSelect.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get('/api/designers')
      .then(res => res.data)
      .then(res => res.map(des => ({ value: des.id, label: des.name})))
      .then(designers => this.setState({ designers }), this.getCategories())
  }

  getCategories() {
    axios.get('/api/categories')
      .then(res => res.data.map(cat => ({ value: cat.id, label: cat.name})))
      .then(categories => this.setState({ categories }))
  }

  handleChange({target: { name, value }}){
    const data = {...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }


  handleCategorySelect({ value }) {
    const data = { ...this.state.data, category_id: value }
    this.setState({ data })
  }

  handleDesignerSelect({ value }){
    const data = {...this.state.data, designer_id: value }
    this.setState({ data })
  }

  handleSubmit(e){
    console.log('posting')
    e.preventDefault()
    axios.post('/api/posts', this.state.data,
      { headers: {Authorization: `Bearer ${Auth.getToken()}` }})
      .then(res => console.log(res))
      .then(() => this.props.history.push('/posts'))
      .catch(err => console.log(err))
  }

  render(){
    console.log(this.state)
    return(
      <PostForm
        handleDesignerSelect={this.handleDesignerSelect}
        handleCategorySelect={this.handleCategorySelect}
        designers={this.state.designers}
        categories={this.state.categories}
        handleChange={this.handleChange}
        handleSubmit={this.handleSubmit}
        data={this.state.data}
        errors={this.state.errors}
      />

    )
  }
}

export default PostNew
