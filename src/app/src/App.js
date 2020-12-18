import './App.scss';
import Selector from './Selector.js';
import Header from './Header.js';

import { useState, useRef } from 'react'

const App = () => {
  const [plotUrl, setPlotUrl] = useState('https://i.pinimg.com/736x/1e/8d/df/1e8ddf7c50b4b55a60a9a10976c4b0a2.jpg')

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
                alt='Recurrence plot' 
                className='plot-image'/>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
