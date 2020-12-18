import { React, useState, useEffect } from 'react'
import './Selector.scss'

const fetch = require('node-fetch')
const { URLSearchParams } = require('url')

const Selector = ({updatePlot}) => {
  const [plotDatas, setPlotDatas] = useState([])
  const [dataSelect, setDataSelect] = useState({_id:''})
  const [compareMode, setCompareMode] = useState('1')
  const [M, setM] = useState('3')
  const [N, setN] = useState('2')
  const [deviation, setDeviation] = useState('1')

  const handleM = (event) => {
    if (!event.target.value) {
      setM(3)
    } 
    setM(event.target.value)
  }

  const handleN = (event) => {
    if (!event.target.value) {
      setN(3)
    }
    setN(event.target.value)
  }

  const handleDeviation = (event) => {
    if (!event.target.value) {
      setDeviation(3)
    }
    setDeviation(event.target.value)
  }

  const handleSubmit = () => {
    console.log('Clicked')

    fetch(process.env.REACT_APP_GET_PLOT_IMAGE_URL + dataSelect).then( res => {
      console.log('Success?')
      return res.json()
    }).then(json =>{
      console.log('Success2?')
      if (json.fileUrl){
        console.log('Success3?')
        const url = process.env.REACT_APP_GET_PLOT_BASE_URL + json.fileUrl
        console.log(url)
        updatePlot(url)
      } else {
        console.log('No plot data image received.')
      }
    })
    // console.log(M)
    // console.log(N)
    // console.log(compareMode)
    // console.log(deviation)
    // console.log(dataSelect)
  }

  useEffect(() => {
    fetch(process.env.REACT_APP_GET_PLOT_DATA_URL)
      .then(res => {
        return res.json()
      }).then(json => {
        setPlotDatas(json)
        setDataSelect(json[0]._id)
      }).catch(e => {
        console.log(e)
      })
  }, [])

  return (
    <div className='selector'>
      <div className='field'>
        <h3>Data</h3>
        <select value={dataSelect} onChange={e => {setDataSelect(e.target.value)}}>
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
          <h3>M</h3>
          <input
            type='text' 
            className='input--mini' placeholder='3'
            onChange={handleM}
          />
        </div>
        <div className='column'>
          <h3>N</h3>
          <input
            type='text'
            className='input--mini' placeholder='2'
            onChange={handleN}
          />
        </div>
        <div className='column'>
          <h3>Deviation</h3>
          
          <input 
            type='text' 
            className='input--mini' placeholder='1'
            onChange={handleDeviation}
          />
        </div>
      </div>
      <div className='field'>
        <button className='button-submit' onClick={handleSubmit}>
          Plot!
        </button>
      </div>
    </div>
  )
}

export default Selector