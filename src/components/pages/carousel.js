import React from 'react'
import { Slide } from 'react-slideshow-image'

const slideImages = [
  '../../assets/assets/images/newlogo.jpg',
  '../../assets/assets/images/login2.jpeg',
  '../../assets/assets/images/logo3.jpg'
]

const properties = {
  duration: 3000,
  transitionDuration: 500,
  infinite: true
}


const Slideshow = () => {
  return (
    <Slide {...properties}>

      <div className="each-slide">
        <div style=
          {{'backgroundImage': `url(${slideImages[0]})`}}>

          </div>
      </div>
        <div className="each-slide">
          <div style={{'backgroundImage': `url(${slideImages[1]})`}}>

          </div>
        </div>
        <div className="each-slide">
          <div style={{'backgroundImage': `url(${slideImages[2]})`}}>

          </div>
        </div>

    </Slide>
  )
}

export default Slideshow
