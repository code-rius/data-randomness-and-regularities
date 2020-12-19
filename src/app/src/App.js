import './App.scss';
import Selector from './Selector.js';
import Header from './Header.js';

import { useState, useRef } from 'react'

const App = () => {
  const [plotUrl, setPlotUrl] = useState('')

  const imageRef = useRef()
  
  const updatePlot = (url) => {
    setPlotUrl(url)
  }

  return (
    <>
      <Header />
      <div className='app'>
        <div className='wrapper'>
          <div>
            <Selector updatePlot={updatePlot} />
          </div>
          <div>
            <h3>
              Recurrence plot
            </h3>
            <div>
              <img 
                ref={imageRef}
                key={Date.now()} 
                src={plotUrl} 
                alt='' 
                className='plot-image'/>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
