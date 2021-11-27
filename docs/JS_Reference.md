# JS Reference


### Pipe operator function
```javascript
// usage: pipe(firstFn, secondFn, ...)(argument)
export const pipe =
    (...fns: any[]) =>
        (input: any) =>
            fns.reduce((acc, f) => f(acc), input)
```
