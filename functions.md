```python
def say_hello():
    print('hello')
    print('how are you')
```


```python
say_hello()
```

    hello
    how are you
    


```python
say_hello
```




    <function __main__.say_hello()>




```python
def say_hello(name='Whatever'):
    print(f'hello {name}')
```


```python
say_hello('bear')
```

    hello bear
    


```python
say_hello()
```

    hello Whatever
    


```python
def add_num(num1,num2):
    return num1+num2
```


```python
add_num(10,20)
```




    30




```python
result = add_num(1,20)
```


```python
result
```




    21




```python
def print_result(a,b):
    print(a+b)
```


```python
def return_result(a,b):
    return a+b
```


```python
print_result(10,20)
```

    30
    


```python
result = print_result(10,20)
```

    30
    


```python
result
```


```python
return_result(10,20)
```




    30




```python
result = return_result(10,20)
```


```python
result
```




    30




```python
def myfunc(a,b):
    print(a+b)
    return a+b
```


```python
result = myfunc(10,20)
```

    30
    


```python
result
```




    30




```python
def sum_numbers(num1,num2):
    return num1+num2
```


```python
sum_numbers(10,20)
```




    30




```python
sum_numbers('10','20')
```




    '1020'




```python
sum_numbers('a','b')
```




    'ab'




```python

```
