# Basics

## Comments / Comentários
```python
# one single line comment
# and we don't have multiple line comments ...
```

## Data types / Tipos de dados simples
```python
integer = 1
floatting_point = 3.1415
string = 'this is a string'
string2 = "this is also a string"
null = None
complex_number = 2 + 3j
true_valus = True
false_value = False
```

## Arithmetic operations
```python
1 + 2   # = 3
1 - 2   # = -1 // 1 + -2 # = -1
2 * 3   # = 6
2 / 3   # = 0.6666666666666666
2 / 2   # = 1.0
3 // 2  # = 1
3 % 2   # = 1
2 ** 3  # = 8
2 ** .5 # = 1.4142135623730951

from math import sqrt
2 ** .5 == sqrt(2) # True
```

## Boolean operations
```python
True or False   # True
True and False  # False
not False       # True

1 > 2           # False
1 < 2           # True
1 <= 2          # True
1 >= 2          # False
1 == 2          # False
1 != 2          # True

1 < 2 < 3       # True
1 < 2 < 3 < 4   # True
1 > 0 < 2       # True
```

## Decision Structures
```python
if 1 > 2:
  print('1 > 2')


if 1 > 2:
  print('1 > 2')
else:
  print('1 < 2')


print(f"1 {'<' if 1 < 2 else '>'} 2")
print('1 {} 2'.format('<' if 1 < 2 else '>'))


if 1 > 2:
  print('1 > 2')
elif 1 == 2:
  print('1 = 2')
else:
  print('1 < 2')
```

## Loops
```python
while True:
  print('Infinite loop')


for element in elements:
  print(element)
```

## Basic Data Structures / Estruturas de Dados Simples
```python
ll = []
ll = [1, 2, 3]
ll = [i for i in range(10) if i % 2]
ll = [1, 1.02, 1 + 3j, 'a', 'abc', None, True]
ll = list('Hello, world!') # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']
```


