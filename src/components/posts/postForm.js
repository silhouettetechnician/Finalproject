import React from 'react'
import 'bulma'
import CreatableSelect from 'react-select/lib/Creatable'
import Select from 'react-select'



class PostForm extends React.Component{
  constructor(){
    super()
    this.state = {}
  }
  render(){
    const { data, errors, handleChange, handleSubmit, handleCategorySelect, handleDesignerSelect, designers, categories } = this.props
    return (
      <div className='wrapper'>
        <form onSubmit={handleSubmit}>
          <div className="field">
            <label className="label">TITLE</label>
            <div className="control">
              <input
                className={`input ${errors.title ? 'is-danger': ''}`}

                name="title"
                onChange={handleChange}
                value={data.title || ''}
              />
            </div>
            {errors.title && <small className="help is-danger">{errors.title}</small>}
          </div>
          <div className="field">
            <label className="label">DESCRIPTION</label>
            <div className="control">
              <textarea
                className={`input ${errors.description ? 'is-danger': ''}`}

                name="description"
                onChange={handleChange}
                value={data.description || ''}
              />
              {errors.description && <small className="help is-danger">{errors.description}</small>}
            </div>
          </div>
          <div className="field">
            <label className="label">CATEGORY</label>
            <Select
              name="categories"
              options={categories}
              onChange={handleCategorySelect}
          >
          </Select>
        </div>
        <div className="field">
          <label className="label">DESIGNER</label>
          <CreatableSelect
            isClearable
            name="designer_idw"
            options={designers}
            onChange={handleDesignerSelect}
          >
          </CreatableSelect>
        </div>
        <div className="field">
          <label className="label">SIZE</label>
          <div className="control">
            <input
              className={`input ${errors.origin ? 'is-danger': ''}`}
              placeholder="Origin"
              name="origin"
              onChange={handleChange}
              value={data.origin || ''}
            />
          </div>
        </div>

          <button value='submit' className="button is-info">SUBMIT</button>

      </form>
      </div>
    )

  }


}


export default PostForm
