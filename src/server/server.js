const express = require('express')
const bodyParser = require('body-parser')
const fetch = require('node-fetch')
const PlotData = require('./models/plotdata')
const ObjectId = require('mongoose').Types.ObjectId
const { ObjectID } = require('mongodb')
const fs = require('fs')
const cors = require('cors')

const jsonParser = bodyParser.json()
const app = express()

require('dotenv').config()
require('./db/mongoose')

app.use(express.static('public'))
app.use(cors())

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.get('/plot_data', jsonParser, (req, res) => {
  PlotData.find({}).then( plot_datas => {
    res.json(plot_datas)
  }).catch( e => {
    res.status(500).send(e)
  })
})

app.get('/plot_data/:id', (req, res) => {
  const _id = req.params.id
  if (!ObjectID.isValid(_id)){
    res.status(400).send({ error: process.env.ERROR_BAD_OBJECT_ID} )
  }

  PlotData.findById(_id).then( plotdata => {
    if (!plotdata) {
      return res.status(404).send()
    }

    res.send(plotdata)
  }).catch( e => {
    res.status(500).send(e)
  })
})

app.delete('/plot_data/:id', (req, res) => {
  const _id = req.params.id
  if (!ObjectID.isValid(_id)) {
    res.status(404).send({ error: process.env.ERROR_BAD_OBJECT_ID })
  }

  PlotData.findByIdAndDelete(_id).then(plotdata => {
    if (!plotdata) {
      return res.status(404).send()
    }

    res.send(plotdata)
  }).catch(e => {
    res.status(500).send(e)
  })
})

app.patch('/plot_data/:id', jsonParser, async (req, res) => {
  const _id = req.params.id
  if (!ObjectID.isValid(_id)) {
    res.status(404).send({ error: process.env.ERROR_BAD_OBJECT_ID })
  }
  try { 
    const plotdata = await PlotData.findByIdAndUpdate(_id, req.body, 
      { new: true, runValidators: true, useFindAndModify: false} )

    if (!plotdata) {
      return res.status(404).send()
    }

    res.send(plotdata)
  } catch (e) {
    res.status(400).send()
  }
})

app.post('/plot_data', jsonParser, (req, res) => {
  if (!req.body) {
    res.status(400).send('Request must have a body')
  }

  const plotdata = new PlotData(req.body)

  plotdata.save().then( () => {
    res.send(plotdata)
  }).catch( e => {
    res.status(400).send(e)
  })
})

app.get('/plot_json/:id', jsonParser, (req, res) => {
  const _id = req.params.id

  if (!ObjectID.isValid(_id)) {
    res.status(400).send({ error: process.env.ERROR_BAD_OBJECT_ID })
  }

  PlotData.findById(_id).then(plotdata => {
    if (!plotdata) {
      return res.status(404).send()
    }

    fetch(process.env.RECURRENCE_PLOT_JSON_ENDPOINT_URL, {
      method: 'post',
      body: JSON.stringify(plotdata),
      headers: { 'Content-Type': 'application/json' }
    }).then(resp => {
      return resp.json()
    }).then(json => {
      res.type('application/json')
      .status(200)
      .send(json)
    }).catch(e => {
      res.status(500).send()
    })
  }).catch(e => {
    res.status(500).send(e)
  })
})

app.get('/plot_image/:id', (req, res) => {
  const _id = req.params.id
  if (!ObjectID.isValid(_id)) {
    res.status(400).send({ error: process.env.ERROR_BAD_OBJECT_ID })
  }

  PlotData.findById(_id).then(plotdata => {
    if (!plotdata) {
      return res.status(404).send()
    }

    fetch(process.env.RECURRENCE_PLOT_IMAGE_ENDPOINT_URL, {
      method: 'post',
      body: JSON.stringify(plotdata),
      headers: { 'Content-Type': 'application/json' }
    }).then(resp => {
      return resp.buffer()
    }).then(buff => {
      fs.writeFile('./public/' + process.env.PLOT_IMAGE_NAME, buff, () =>{
        res.type('application/json');
        res.status(200)
        .send( {'fileUrl' : process.env.PLOT_IMAGE_NAME} )
      })
    }).catch(e => {
      res.status(500).send()
    })
  }).catch(e => {
    res.status(500).send(e)
  })

})

app.listen(4000)