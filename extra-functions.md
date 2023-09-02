```python
for num in range(0,5):
    print(num)
```

    0
    1
    2
    3
    4
    


```python
index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
```

    At index 0 the letter is a
    At index 1 the letter is b
    At index 2 the letter is c
    At index 3 the letter is d
    At index 4 the letter is e
    


```python
index_count = 0
word = 'abcde'
for item in enumerate(word):
    print(item)
```

    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    (4, 'e')
    


```python
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
```

    0
    a
    
    
    1
    b
    
    
    2
    c
    
    
    3
    d
    
    
    4
    e
    
    
    


```python
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3= [100,200,300]
mylist4= [1,2,3,4,5,6,7,8,9]
```


```python
for item in zip(mylist1,mylist2,mylist3,mylist4):
    print(item)
```

    (1, 'a', 100, 1)
    (2, 'b', 200, 2)
    (3, 'c', 300, 3)
    


```python
list(zip(mylist1,mylist2))
```




    [(1, 'a'), (2, 'b'), (3, 'c')]




```python
'x' in [1,2,3]
```




    False




```python
'x' in ['x','y','z']
```




    True




```python
mylist = [10,20,30,40,100]
```


```python
min(mylist)
```




    10




```python
max(mylist)
```




    100




```python
from random import shuffle
```


```python
mylist = [1,2,3,4,5,6,7,8,9,10]
```


```python
shuffle(mylist)
```


```python
mylist
```




    [5, 4, 7, 6, 2, 10, 8, 1, 3, 9]




```python
from random import randint
```


```python
randint(0,100)
```




    18




```python
input('Enter a number here: ')
```

    Enter a number here: 50
    




    '50'




```python
result = input('Enter a number here: ')
```

    Enter a number here: 35353
    


```python
result
```




    '35353'




```python
int(result)
```




    35353




```python

```
