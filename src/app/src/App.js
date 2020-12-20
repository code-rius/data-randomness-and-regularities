import './App.scss';
import Selector from './components/Selector.js';
import Loader from './components/Loader.js'
import Header from './components/Header.js';
import Image from './components/Image.js';

import { useState, useRef, useEffect } from 'react'

const App = () => {
  const [plotUrl, setPlotUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const imageRef = useRef()
  
  const updatePlot = (url) => {
    setPlotUrl(url)
  }

  useEffect(() => {
    const current = loading
    setLoading(!current)
    console.log("Loading state:\t", loading)
  }, [plotUrl]);

  return (
    <>
      <Header />
      <div className='app'>
        <div className='wrapper'>
          <div className="box">
            <Selector updatePlot={updatePlot} />
          </div>
          <div className="box">
            <h3>Recurrence plot</h3>
            {loading ? <Loader /> : <Image imageRef={imageRef} plotUrl={plotUrl} />}
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
