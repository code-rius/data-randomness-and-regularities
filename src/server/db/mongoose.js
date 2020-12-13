const mongoose = require('mongoose')
require('dotenv').config()

mongoose.connect(process.env.MONGO_DB_URL, {
  useCreateIndex: true,
  useNewUrlParser: true,
  useUnifiedTopology: true
})

// const dji = new PlotData({
//   name: "S&P 500",
//   M: 1,
//   data: [1, 2, 3, 4, 5, 6, 8 , 9]
// })

// dji.save().then( () => {
//   console.log(dji)
// }).catch( e => {
//   console.log('Error:', e)
// })