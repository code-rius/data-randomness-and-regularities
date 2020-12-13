const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost:27017/plotter', {
  useCreateIndex: true
})

const