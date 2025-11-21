# Balanced Parentheses Checker

This program checks whether an expression contains properly matched brackets such as:
- ()
- {}
- []

The logic uses a stack to validate whether each opening bracket has its correct closing pair.

---

## Features
- Detects matching and mismatching brackets  
- Supports (), {}, and []  
- Works for mathematical expressions and strings  

---

## How It Works
- Push each opening bracket into a stack  
- When a closing bracket appears, check if it matches the top of the stack  
- Pop when matched  
- Expression is balanced if the stack becomes empty at the end  

---

## How to Run
```bash
python balanced_parentheses.py# Balanced_paranthesis-checker
