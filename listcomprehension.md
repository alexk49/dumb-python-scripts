```python
mystring = 'hello'
```


```python
mylist = []

for letter in mystring:
    mylist.append(letter)
```


```python
mylist
```




    ['h', 'e', 'l', 'l', 'o']




```python
mylist = [letter for letter in mystring]
```


```python
mylist
```




    ['h', 'e', 'l', 'l', 'o']




```python
mylist = [x for x in 'word']
```


```python
mylist
```




    ['w', 'o', 'r', 'd']




```python
mylist = [x for x in range(0,11)]
```


```python
mylist
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
mylist = [num**2 for num in range(0,10)]
```


```python
mylist
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




```python
mylist = [x for x in range(0,11) if x%2==0]
```


```python
mylist
```




    [0, 2, 4, 6, 8, 10]




```python
celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
```


```python
fahrenheit
```




    [32.0, 50.0, 68.0, 94.1]




```python
fahrenheit = [] 

for temp in celcius:
    fahrenheit.append(( (9/5)*temp + 32))
```


```python
fahrenheit
```




    [32.0, 50.0, 68.0, 94.1]




```python
mylist = 'Hello world'
```


```python
newlist = []

for letter in mylist:
    newlist.append(letter)
```


```python
newlist
```




    ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']




```python
newlist = [letter for letter in mylist]
```


```python
newlist
```




    ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']




```python
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
```


```python
results
```




    [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]




```python
mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
```


```python
mylist
```




    [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]




```python
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
```


```python
mylist
```




    [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]




```python

```
