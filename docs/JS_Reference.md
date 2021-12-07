# JS Reference

## React
### useImperativeHandle

```javascript
const ChildComp = forwardRef((props, ref) => {
  const childRef = useRef(null)
  const [stuff, setStuff] = useState(null)

    useImperativeHandle(ref, () => ({
        setStuff: (x) => {
            setStuff(x)
        }
    }))
    
  return (
     <button onClick={() => childRef.current.doStuff()} />
  )
})

const ParentComp = () => {
  const childRef = useRef(null)
  const onClick = () => childRef.current.doStuff()

  return (
     <ChildComp ref={childRef} onClick={() => childRef.current.setStuff('data')} />
  )
}
```

## ES6
### Pipe operator function
```javascript
// usage: pipe(firstFn, secondFn, ...)(argument)
export const pipe =
    (...fns: any[]) =>
        (input: any) =>
            fns.reduce((acc, f) => f(acc), input)
```


## Node
### sync fs read to array
```javascript
const fs = require('fs')
const getFileContentsAsArray = (filePath) =>
  fs.readFileSync(filePath).toString().split(/\r\n|\n/g)
```
