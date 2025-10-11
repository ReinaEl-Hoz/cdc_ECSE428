import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from calculator import CDC

# T-PUSH-REAL1
def test_push_real1(capsys):
    # operation: push/pop (real)
    cdc = CDC()
    cdc.onecmd("push 5")
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "5 + j0"

# T-PUSH-CPLX1
def test_push_cplx1(capsys):
    # operation: push/pop (complex, compact)
    cdc = CDC()
    cdc.onecmd("push -2.5-j0.25")
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "-2.5 - j0.25"

# T-PUSH-CPLX2
def test_push_cplx2(capsys):
    # operation: push/pop (complex, spaced)
    cdc = CDC()
    cdc.onecmd("push 3 + j 4")
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + j4"

# T-POP-ERR1
def test_pop_err1(capsys):
    # operation: pop (error)
    cdc = CDC()
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-ADD-REAL1
def test_add_real1(capsys):
    # operation: add (real)
    cdc = CDC()
    cmd_List = ["push 2", "push 5", "add"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "7 + j0"

# T-ADD-CPLX1
def test_add_cplx1(capsys):
    # operation: add (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "add"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "4 + j2"

# T-ADD-ERR1
def test_add_err1(capsys):
    # operation: add (error)
    cdc = CDC()
    cdc.onecmd("push 3")
    cdc.onecmd("add")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-SUB-REAL1
def test_sub_real1(capsys):
    # operation: sub (real)
    cdc = CDC()
    cmd_List = ["push 5", "push 2", "sub"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + j0"


 # T-SUB-CPLX1
def test_sub_cplx1(capsys):
    # operation: sub (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "sub"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 + j6"
       
 # T-SUB-ERR1
def test_sub_err1(capsys):
    # operation: sub (error)
    cdc = CDC()
    cdc.onecmd("sub")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-MUL-REAL1
def test_mul_real1(capsys):
    # operation: mul (real)
    cdc = CDC()
    cmd_List = ["push 3", "push -2", "mul"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "-6 + j0"

# T-MUL-CPLX1
def test_mul_cplx1(capsys):
    # operation: mul (complex)
    cdc = CDC()
    cmd_List = ["push 1+j2", "push 3-j4", "mul"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "11 + j2"

# T-MUL-ERR1
def test_mul_err1(capsys):
    # operation: mul (error)
    cdc = CDC()
    cdc.onecmd("mul")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-DIV-REAL1
def test_div_real1(capsys):
    # operation: div (real)
    cdc = CDC()
    cmd_List = ["push 8", "push 2", "div"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "4 + j0"

# T-DIV-CPLX1
def test_div_cplx1(capsys):
    # operation: div (complex)
    cdc = CDC()
    cmd_List = ["push 4+j2", "push 1+j1", "div"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 - j1"

# T-DIV-ERR1
def test_div_err1(capsys):
    # operation: div (error: /0 real)
    cdc = CDC()
    cmd_List = ["push 1", "push 0", "div"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: division by zero"

# T-DIV-ERR2
def test_div_err2(capsys):
    # operation: div (error: /0 complex)
    cdc = CDC()
    cmd_List = ["push 1+j0", "push 0+j0", "div"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: division by zero"

# T-DEL-REAL1
def test_del_real1(capsys):
    # operation: delete (real stack)
    cdc = CDC()
    cmd_list = ["push 1", "push 2", "delete"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 + j0"

# T-DEL-CPLX1
def test_del_cplx1(capsys):
    # operation: delete (complex stack)
    cdc = CDC()
    cmd_list = ["push 1+j1", "push 2+j3", "delete"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 + j1"

# T-DEL-ERR1
def test_del_err1(capsys):
    # operation: delete (error)
    cdc = CDC()
    cdc.onecmd("delete")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"
