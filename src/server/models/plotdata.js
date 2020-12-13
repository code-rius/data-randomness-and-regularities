const mongoose = require('mongoose')

const PlotData = mongoose.model('PlotData', {
  name: {
    type: String,
    required: true
  },
  shortName: {
    type: String
  },
  M: {
    type: Number,
    default: 3,
    validate(value) {
      if (value < 2) {
        throw new Error('M must be an integer 2 or higher')
      }
    }
  },
  N: {
    type: Number,
    default: 2
  },
  deviation: {
    type: Number,
    default: 1
  },
  data: {
    type: Array,
    required: true
  }
})

module.exports = PlotData