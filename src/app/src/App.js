import './App.scss';
import TodoList from './TodoList';
import Selector from './Selector.js';
import Header from './Header.js';

import { useState, useRef, useEffect } from 'react'
import { v4 as uuidv4 } from 'uuid';

const fetch = require('node-fetch');

const LOCAL_STORAGE_KEY = 'todoApp.todos'

const App = () => {
  const [plotData, setPlotData] = useState([])

  useEffect(() => {
    fetch( )
  }, [])


  const [todos, setTodos] = useState([])

  const todoNameRef = useRef()

  useEffect(() => {
    const storedTodos = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))
    if (storedTodos) setTodos(storedTodos)
  }, [])

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

  return (
    <>
      <Header />
      <div className="app">
        <div className="wrapper">
          <div>
            <Selector />
          </div>
          <div>
            <h3>
              Recurrence plot
            </h3>
          </div>
          <div>
            <h1>Viewer</h1>
            <TodoList todos={todos} toggleTodo={toggleTodo}/>
            <input ref={todoNameRef} type="text"/>
            <button onClick={handleAddTodo}>Add data</button>
            <button onClick={handleClearTodos}>Clear stuff</button>
            <div>{todos.filter(todo => !todo.complete).length} left to do</div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
