import './Image.scss'

const Image = ({ imageRef, plotUrl}) => {
  return (
    <img
      ref={imageRef}
      key={Date.now()}
      src={plotUrl}
      alt=''
      className='plot-image' />
  )
}

export default Image