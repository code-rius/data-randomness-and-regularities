const express = require('express')
const bodyParser = require('body-parser')
const fetch = require('node-fetch');
const PlotData = require('./models/plotdata')

const jsonParser = bodyParser.json()
const app = express()

require('dotenv').config()
require('./db/mongoose')

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.post('/plot_data', jsonParser, (req, res) => {
  console.log("We have a request")
  if (!req.body) {
    console.log('Bad request')
    res.status(400).send('Must provide a JSON body')
  }

  console.log("Good request")
  const plotdata = new PlotData(req.body)
  plotdata.save().then( () => {
    res.send(plotdata)
  }).catch( e => {
    res.status(400).send(e)
  })
})

app.post('/generate_plot/', jsonParser, (req, res) => {
  if (!req.body){
    console.log('Bad request')
    res.status(400).send('Bad request')
  }

  fetch(process.env.RECURRENCE_PLOT_ENDPOINT_URL, {
    method: 'post',
    body: JSON.stringify({
      'params': req.body.params,
      'data': req.body.data
    }),
    headers: { 'Content-Type': 'application/json' }
  })
  .then(resp => {
    return resp.json()
  })
  .then(json => {
    res.type('application/json')
    res.status(200).send(json)

  })
  .catch(e => {
    console.log(`We've encountered an error:`)
    res.status(500).send('Error 500!')
  })
})

app.listen(4000)