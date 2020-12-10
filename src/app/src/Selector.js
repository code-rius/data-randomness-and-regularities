import './Selector.scss'
import React from 'react'

function Selector() {
  return (
    <div className="selector">
      <div className="field">
        <h3>Data</h3>
        <select>
          <option>Dow Jones</option>
          <option>S&P 500</option>  
          <option>Tesla</option> 
        </select>
      </div>
      <div className="field">
        <h3>Compare mode</h3>
        <select>
          <option>Maximum</option>
          <option>Euclidean</option>
        </select>
      </div>
      <div className="field multi--data">
        <div className="column">
          <h3>M</h3>
          <input className="input--mini" placeholder="3"></input>
        </div>
        <div className="column">
          <h3>N</h3>
          <input className="input--mini" placeholder="2"></input>
        </div>
        <div className="column">
          <h3>Deviation</h3>
          <input className="input--mini" placeholder="0.1"></input>
        </div>
      </div>
      <div className="field">
        <button className="button-submit">
          Plot!
        </button>
      </div>
    </div>
  )
}

export default Selector