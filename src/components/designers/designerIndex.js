import { Link } from 'react-router-dom'
import React from 'react'
import axios from 'axios'
import 'bulma'

class DesignerIndex extends React.Component{
  constructor(){
    super()
    this.state = {}
  }


  componentDidMount(){
    axios.get('api/designers')
      .then(res => this.setState({ designers: res.data }))
  }

  render(){
    if(!this.state.designers) return null
    return  (
      <main  className="section">
        <div className="container">
          <div className="columns is-mobile is-multiline">
            {!this.state.designers && <p>...loading</p>}
            {this.state.designers && this.state.designers.map(designer =>
              <div key={designer.id} className="column is-one-quarter-desktop is-one-third-tablet is-half-mobile">

                <Link to={`/designers/${designer.id}`}>
                  <div className="cardo">
                    <div className="card-headder">
                    </div>
                    <div>
                      <br />
                      <img src={designer.image} />
                    </div>
                  </div>
                </Link>
              </div>
            )}
          </div>
        </div>
      </main>
    )
  }
}
export default DesignerIndex
