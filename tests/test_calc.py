import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from calculator import CDC
# T-PUSH-REAL1
def test_push_real1():
    # operation: push/pop (real)
    cdc = CDC()
    cdc.execute("push 5")
    pop_res = cdc.execute("pop")
    assert pop_res == "5 + j0"

# T-PUSH-CPLX1
def test_push_cplx1():
    # operation: push/pop (complex, compact)
    cdc = CDC()
    cdc.execute("push -2.5-j0.25")
    pop_res = cdc.execute("pop")
    assert pop_res == "-2.5 - j0.25"

# T-PUSH-CPLX2
def test_push_cplx2():
    # operation: push/pop (complex, spaced)
    cdc = CDC()
    cdc.execute("push 3 + j 4")
    pop_res = cdc.execute("pop")
    assert pop_res == "3 + j4"

# T-POP-ERR1
def test_pop_err1():
    # operation: pop (error)
    cdc = CDC()
    pop_res = cdc.execute("pop")
    assert pop_res == "Error: stack underflow"

# T-ADD-REAL1
def test_add_real1():
    # operation: add (real)
    cdc = CDC()
    cmd_List = ["push 2", "push 5", "add"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "7 + j0"

# T-ADD-CPLX1
def test_add_cplx1():
    # operation: add (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "add"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "4 + j2"

# T-ADD-ERR1
def test_add_err1():
    # operation: add (error)
    cdc = CDC()
    cdc.execute("push 3")
    add_res = cdc.execute("add")
    assert add_res == "Error: stack underflow"

# T-SUB-REAL1
def test_sub_real1():
    # operation: sub (real)
    cdc = CDC()
    cmd_List = ["push 5", "push 2", "sub"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "3 + j0"


 # T-SUB-CPLX1
def test_sub_cplx1():
    # operation: sub (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "sub"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "2 + j6"
       
 # T-SUB-ERR1
def test_sub_err1():
    # operation: sub (error)
    cdc = CDC()
    sub_res = cdc.execute("sub")
    assert sub_res == "Error: stack underflow"

# T-MUL-REAL1
def test_mul_real1():
    # operation: mul (real)
    cdc = CDC()
    cmd_List = ["push 3", "push -2", "mul"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "-6 + j0"

# T-MUL-CPLX1
def test_mul_cplx1():
    # operation: mul (complex)
    cdc = CDC()
    cmd_List = ["push 1+j2", "push 3-j4", "mul"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "2 + j6"

# T-MUL-ERR1
def test_mul_err1():
    # operation: mul (error)
    cdc = CDC()
    mul_res = cdc.execute("mul")
    assert mul_res == "Error: stack underflow"

# T-DIV-REAL1
def test_div_real1():
    # operation: div (real)
    cdc = CDC()
    cmd_List = ["push 8", "push 2", "div"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "4 + j0"

# T-DIV-CPLX1
def test_div_cplx1():
    # operation: div (complex)
    cdc = CDC()
    cmd_List = ["push 4+j2", "push 1+j1", "div"]
    for cmd in cmd_List:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "3 - j1"

# T-DIV-ERR1
def test_div_err1():
    # operation: div (error: /0 real)
    cdc = CDC()
    cmd_List = ["push 1", "push 0", "div"]
    for cmd in cmd_List:
        result = cdc.execute(cmd)
    assert result == "Error: division by zero"

# T-DIV-ERR2
def test_div_err2():
    # operation: div (error: /0 complex)
    cdc = CDC()
    cmd_List = ["push 1+j0", "push 0+j0", "div"]
    for cmd in cmd_List:
        result = cdc.execute(cmd)
    assert result == "Error: division by zero"

# T-DEL-REAL1
def test_del_real1():
    # operation: delete (real stack)
    cdc = CDC()
    cmd_list = ["push 1", "push 2", "delete"]
    for cmd in cmd_list:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "1 + j0"

# T-DEL-CPLX1
def test_del_cplx1():
    # operation: delete (complex stack)
    cdc = CDC()
    cmd_list = ["push 1+j1", "push 2+j3", "delete"]
    for cmd in cmd_list:
        cdc.execute(cmd)
    pop_res = cdc.execute("pop")
    assert pop_res == "1 + j1"

# T-DEL-ERR1
def test_del_err1():
    # operation: delete (error)
    cdc = CDC()
    del_res = cdc.execute("delete")
    assert del_res == "Error: stack underflow"
