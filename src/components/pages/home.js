import React from 'react'
import Slideshow from '../pages/carousel'

class Home extends React.Component {
  constructor() {
    super()
  }



  render(){
    return(
      <main>
        <div className="home-container1">
          <div className="slideshow-container">
            <Slideshow />

          </div>
        </div>

      </main>
    )
  }


}

export default Home
