const { MongoClient, ObjectID } = require('mongodb');
const assert = require('assert');

// Connection URL
const url = 'mongodb://localhost:27017';
const dbName = 'plotabase';

// const id = new ObjectID()
// console.log(id.id.length)
// console.log(id.toHexString().length)
// console.log(id.getTimestamp())


// Use connect method to connect to the server
MongoClient.connect(url, { useUnifiedTopology: true }, (err, client) => {
  assert.strictEqual(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  // db.collection('users').insertOne({
  //   name:"Audrius",
  //   surname:"Baranauskas"
  // })
  // .then( res => {
  //   console.log(res.ops)
  //   client.close();
  // })
  // .catch( e => {
  //   // console.log(e)
  //   client.close();
  // })

  // db.collection('users').findOne({name: 'Audrius'})
  // .then(res => {
  //   console.log('We found:')
  //   console.log(res)
  // })
  // .catch(e => {
  //   console.log(e)
  // })

  // db.collection('users').find({ name: 'Audrius' })
  // .toArray()
  // .then(res => {
  //   console.log(res)
  // })
  // .catch (e => {
  //   console.log(e)
  // })

  // db.collection('users').find({ name: 'Audrius' })
  // .count()
  // .then(num => {
  //   console.log(num)
  // })
  // .catch(e => {
  //   console.log(e)
  // })

  db.collection('users').updateOne({
    _id: new ObjectID('5fd5f3191ecfde15ec6853db')
  }, {
    $set: {
      name: 'Baudrius'
    }
  }).then( res => {
    console.log(res.modifiedCount)
  }).catch( e => {
    console.log(e)
  })
  // client.close();
});