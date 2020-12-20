import './Loader.scss'

const Loader = () => {
  return(
    <div className="spinner-container">
      <div className="spinner">
        <div className="spinner-item"></div>
        <div className="spinner-item"></div>
        <div className="spinner-item"></div>
      </div>
    </div>
  )
}

export default Loader