const express = require('express');
const path = require('path');


const app = express();
const port = 8080;

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/web/'));
});

app.listen(port);
console.log(`Server started at ${port}`);

