```bash
mypy square.py  # echo $? 1
                #square.py:5: error: Argument 1 to "square" has incompatible type "str"; expected "int"
                #square.py:6: error: Unsupported operand types for + ("int" and "str")
```
