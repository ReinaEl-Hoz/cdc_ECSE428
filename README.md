# cdc_ECSE428

A CLI based complex number calculator, a simple extension to the ["dc" calculator](https://en.wikipedia.org/wiki/Dc_%28computer_program%29)

**Implemented by**

- Mathis Bélanger - 261049961
- Marianne Romero - 261176930
- Reina El-Hoz - 261176008

**Requirements**

- python 3.14.0
- pytest 8.4.2

**How to run**

In root of the project:

```
python3 calculator.py
> push 3+j4
> push 1-j2
> add pop
4 + j2
```

**How to test**

In root of the project:

```
pytest -v
```

**Specifications**
- Supports: PUSH, POP, ADD, SUB, MUL, DIV, DELETE, ABS, SIN, ASIN, COS, ACOS, SQR, SQRT.
- Numbers may be real (e.g., 3, -2.5) or complex (e.g., 3+j4, -1.5-j2, j5).
- Outputs follow canonical form: RVAL ± jIMAG. 
- Errors: stack underflow, division by zero, invalid token.


