import './App.scss';
import TodoList from './TodoList';
import Selector from './Selector.js';
import Header from './Header.js';
import Image, { Shimmer } from 'react-shimmer'

import { useState, useRef, useEffect } from 'react'
import { v4 as uuidv4 } from 'uuid';

const fetch = require('node-fetch');

const LOCAL_STORAGE_KEY = 'todoApp.todos'

const App = () => {
  // const [plotUrl, setPlotUrl] = useState('https://icatcare.org/app/uploads/2018/07/Helping-your-new-cat-or-kitten-settle-in-1.png')
  const [plotUrl, setPlotUrl] = useState('https://i.pinimg.com/736x/1e/8d/df/1e8ddf7c50b4b55a60a9a10976c4b0a2.jpg')
  const [todos, setTodos] = useState([])

  const imageRef = useRef()

  const todoNameRef = useRef()

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  }, [todos])
  
  const toggleTodo = (id) => {
    const newTodos = [...todos]
    const todo = newTodos.find(todo => todo.id ===id)
    todo.complete = !todo.complete
    setTodos(newTodos)
  }

  const handleAddTodo = () => {
    const name = todoNameRef.current.value

    if (name === '') return
    setTodos(prevTodos => {
      return [...prevTodos, { id: uuidv4(), name: name, complete: false}]
    })
    todoNameRef.current.value = null
  }

  const handleClearTodos = () => {
    const newTodos = todos.filter(todo => !todo.complete)
    setTodos(newTodos)
  }

  const updatePlot = (url) => {
    console.log("We are in the partent function")
    console.log("Parent url:", url)
    console.log(imageRef.current.setAttribute('src', url))
    // setPlotUrl(url)
  }

  return (
    <>
      <Header />
      <div className="app">
        <div className="wrapper">
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
                alt="Plot data" 
                className="plot-image"/>
            </div>
          </div>
          {/* <div>
            <h1>Viewer</h1>
            <TodoList todos={todos} toggleTodo={toggleTodo}/>
            <input ref={todoNameRef} type="text"/>
            <button onClick={handleAddTodo}>Add data</button>
            <button onClick={handleClearTodos}>Clear stuff</button>
            <div>{todos.filter(todo => !todo.complete).length} left to do</div>
          </div> */}
        </div>
      </div>
    </>
  );
}

export default App;
