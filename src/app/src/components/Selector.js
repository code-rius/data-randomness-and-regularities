import { React, useState, useEffect } from 'react'
import './Selector.scss'

const fetch = require('node-fetch')
const querystring = require('querystring');

const Selector = ({ updatePlot }) => {
  const [plotDatas, setPlotDatas] = useState([])
  const [selectedID, setSelectedID] = useState({_id:''})
  const [compareMode, setCompareMode] = useState('1')
  const [D, setD] = useState('3')
  const [d, setd] = useState('2')
  const [pixelTarget, setPixelTarget] = useState('17.5')
  const [chaotic, setChaotic] = useState('')
  const [periodic, setPeriodic] = useState('')
  const [trending, setTrending] = useState('')

  const handleD = (event) => {
    if (!event.target.value) {
      setD(3)
    } 
    setD(event.target.value)
  }

  const handled = (event) => {
    if (!event.target.value) {
      setd(3)
    }
    setd(event.target.value)
  }

  const handlePixelTarget = (event) => {
    if (!event.target.value) {
      setPixelTarget(3)
    }
    setPixelTarget(event.target.value)
  }

  const updateClassifications = (classifications) => {
    setChaotic(numberToPercentage(classifications.chaotic))
    setPeriodic(numberToPercentage(classifications.periodic))
    setTrending(numberToPercentage(classifications.trend))
  }

  const numberToPercentage = (inputNumber) => {
    return String(Math.round(inputNumber*10000)/100)+ '%'
  }

  const handleSubmit = async () => {
    updatePlot('')
    const query = "?" + querystring.stringify({ D, d, compareMode, pixelTarget })

    console.log(process.env.REACT_APP_GET_PLOT_IMAGE_URL + selectedID + query)
    fetch(process.env.REACT_APP_GET_PLOT_IMAGE_URL + selectedID + query).then( res => {
      return res.json()
    }).then(json =>{
      if (json.fileUrl){
        const url = process.env.REACT_APP_GET_PLOT_BASE_URL + json.fileUrl + '?' + Date.now()
        updatePlot(url)
        updateClassifications(json.classifications)
        console.log(json)
      } else {
        console.log('No plot data image received.')
      }
    })
  }

  useEffect(() => {
    fetch(process.env.REACT_APP_GET_PLOT_DATA_URL)
      .then(res => {
        return res.json()
      }).then(json => {
        setPlotDatas(json)
        setSelectedID(json[0]._id)
      }).catch(e => {
        console.log(e)
      })
  }, [])

  return (
    <div className='selector'>
      <div className='field'>
        <h3>Data</h3>
        <select value={selectedID} onChange={e => { setSelectedID(e.target.value)}}>
          {plotDatas.map((option) => (
            <option key={option._id} value={option._id}
            >{option.name}</option>
          ))}
        </select>
      </div>
      <div className='field'>
        <h3>Compare mode</h3>
        <div className='radio-split'>
          <div className='radio-column'>
            <label>Maximum</label><br />
            <input type='radio'
              checked={compareMode === '1'}
              value='1'
              onChange={e => { setCompareMode(e.target.value) }} />
          </div>
          <div className='radio-column'>
            <label>Euclidien</label><br />
            <input type='radio'
              checked={compareMode === '0'}
              value='0'
              onChange={e => { setCompareMode(e.target.value) }} />
          </div>
        </div>
      </div>
      <div className='field multi--data'>
        <div className='column'>
          <h3>D</h3>
          <input
            type='text' 
            className='input--mini' placeholder='3'
            onChange={handleD}
          />
        </div>
        <div className='column'>
          <h3>d</h3>
          <input
            type='text'
            className='input--mini' placeholder='2'
            onChange={handled}
          />
        </div>
        <div className='column'>
          <h3>Target</h3>
          
          <input 
            type='text' 
            className='input--mini' placeholder='17'
            onChange={handlePixelTarget}
          />
        </div>
      </div>
      <div className='field'>
        <button className='button-submit' onClick={handleSubmit}>
          Plot!
        </button>
      </div>
      {periodic != '' && <div className='field multi--data--classification'>
        <div className='column'>
          <h3>Periodic</h3>
          <h3 className='percentage'>{periodic}</h3>
        </div>
        <div className='column'>
          <h3>Trending</h3>
          <h3 className='percentage'>{trending}</h3>
        </div>
        <div className='column'>
          <h3>Chaotic</h3>
          <h3 className='percentage'>{chaotic}</h3>
        </div>
        </div>}
    </div>
  )
}

export default Selector