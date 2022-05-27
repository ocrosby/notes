# Express

## Overview

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

### Installing Express

```bash
> npm install express --save
```

### Hello World

```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening on ${port}`)
})
```

This app starts a server and listens on port 3000 for connections.  