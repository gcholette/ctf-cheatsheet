# JS Reference


### Pipe operator function
```javascript
// usage: pipe(firstFn, secondFn, ...)(argument)
export const pipe =
    (...fns: any[]) =>
        (input: any) =>
            fns.reduce((acc, f) => f(acc), input)
```

### Node sync fs read to array
```javascript
const fs = require('fs')
const getFileContentsAsArray = (filePath) =>
  fs.readFileSync(filePath).toString().split(/\r\n|\n/g)
```
