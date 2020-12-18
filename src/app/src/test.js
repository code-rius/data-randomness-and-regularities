const fetch = require('node-fetch');
require('dotenv').config()


fetch('http://127.0.0.1:4000/plot_data')
  .then(res => {
    console.log(process.env.REACT_APP_GET_PLOT_DATA_SERVER_URL)

    return res.json()
  }).then(damn => {
    console.log("bbb")

    console.log(damn)
  }).catch(e => {
    console.log(e)
  })