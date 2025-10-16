import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from calculator import CDC

# T-PUSH-REAL1
def test_push_real1(capsys):
    # operation: push/pop (real)
    cdc = CDC()
    cmd_List = ["push 5", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "5 + j0"

# T-PUSH-CPLX1
def test_push_cplx1(capsys):
    # operation: push/pop (complex, compact)
    cdc = CDC()
    cmd_List = ["push -2.5-j0.25", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "-2.5 - j0.25"

# T-PUSH-CPLX2
def test_push_cplx2(capsys):
    # operation: push/pop (complex, spaced)
    cdc = CDC()
    cmd_List = ["push 3 + j 4", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
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
    cmd_List = ["push 2", "push 5", "add", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "7 + j0"

# T-ADD-CPLX1
def test_add_cplx1(capsys):
    # operation: add (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "add", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "4 + j2"

# T-ADD-ERR1
def test_add_err1(capsys):
    # operation: add (error)
    cdc = CDC()
    cmd_List = ["push 3", "add"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-SUB-REAL1
def test_sub_real1(capsys):
    # operation: sub (real)
    cdc = CDC()
    cmd_List = ["push 5", "push 2", "sub", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + j0"


 # T-SUB-CPLX1
def test_sub_cplx1(capsys):
    # operation: sub (complex)
    cdc = CDC()
    cmd_List = ["push 3+j4", "push 1-j2", "sub", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
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
    cmd_List = ["push 3", "push -2", "mul", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "-6 + j0"

# T-MUL-CPLX1
def test_mul_cplx1(capsys):
    # operation: mul (complex)
    cdc = CDC()
    cmd_List = ["push 1+j2", "push 3-j4", "mul", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
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
    cmd_List = ["push 8", "push 2", "div", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "4 + j0"

# T-DIV-CPLX1
def test_div_cplx1(capsys):
    # operation: div (complex)
    cdc = CDC()
    cmd_List = ["push 4+j2", "push 1+j1", "div", "pop"]
    for cmd in cmd_List:
        cdc.onecmd(cmd)
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

# T-DIV-ERR3
def test_div_err3(capsys):
    # operation: div (error)
    cdc = CDC()
    cdc.onecmd("div")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-DEL-REAL1
def test_del_real1(capsys):
    # operation: delete (real stack)
    cdc = CDC()
    cmd_list = ["push 1", "push 2", "delete", "pop"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 + j0"

# T-DEL-CPLX1
def test_del_cplx1(capsys):
    # operation: delete (complex stack)
    cdc = CDC()
    cmd_list = ["push 1+j1", "push 2+j3", "delete", "pop"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 + j1"

# T-DEL-ERR1
def test_del_err1(capsys):
    # operation: delete (error)
    cdc = CDC()
    cdc.onecmd("delete")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-ABS-REAL1
def test_abs_real1(capsys):
    # operation: ABS (real)
    cdc = CDC()
    cmd_list = ["push 3", "ABS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + j0"

# T-ABS-CPLX1
def test_abs_cplx1(capsys):
    # operation: ABS (complex)
    cdc = CDC()
    cmd_list = ["push 3+j4", "ABS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "5 + j0"

# T-ABS-ERR1
def test_abs_err1(capsys):
    # operation: ABS (error)
    cdc = CDC()
    cdc.onecmd("ABS")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-SIN-REAL1
def test_sin_real1(capsys):
    # operation: SIN (real)
    cdc = CDC()
    cmd_list = ["push 0", "SIN"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 + j0"

# T-SIN-CPLX1
def test_sin_cplx1(capsys):
    # operation: SIN (complex)
    cdc = CDC()
    cmd_list = ["push 1+j1", "SIN"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "1.298457581 + j0.634963915"

# T-SIN-ERR1
def test_sin_err1(capsys):
    # operation: SIN (error)
    cdc = CDC()
    cdc.onecmd("SIN")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-ASIN-REAL1
def test_asin_real1(capsys):
    # operation: ASIN (real)
    cdc = CDC()
    cmd_list = ["push 0", "ASIN"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 + j0"

# T-ASIN-CPLX1
def test_asin_cplx1(capsys):
    # operation: ASIN (complex)
    cdc = CDC()
    cmd_list = ["push 1+j1", "ASIN"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.666239432 + j1.061275061"

# T-ASIN-ERR1
def test_asin_err1(capsys):
    # operation: ASIN (error)
    cdc = CDC()
    cdc.onecmd("ASIN")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-COS-REAL1
def test_cos_real1(capsys):
    # operation: COS (real)
    cdc = CDC()
    cmd_list = ["push 0", "COS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 + j0"

# T-COS-CPLX1
def test_cos_cplx1(capsys):
    # operation: COS (complex)
    cdc = CDC()
    cmd_list = ["push 1+j1", "COS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.833730025 - j0.988897706"

# T-COS-ERR1
def test_cos_err1(capsys):
    # operation: COS (error)
    cdc = CDC()
    cdc.onecmd("COS")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-ACOS-REAL1
def test_acos_real1(capsys):
    # operation: ACOS (real)
    cdc = CDC()
    cmd_list = ["push 1", "ACOS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 + j0"

# T-ACOS-CPLX1
def test_acos_cplx1(capsys):
    # operation: ACOS (complex)
    cdc = CDC()
    cmd_list = ["push 1+j1", "ACOS"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.904556894 - j1.061275061"

# T-ACOS-ERR1
def test_acos_err1(capsys):
    # operation: ACOS (error)
    cdc = CDC()
    cdc.onecmd("ACOS")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-SQR-REAL1
def test_sqr_real1(capsys):
    # operation: SQR (real)
    cdc = CDC()
    cmd_list = ["push 5", "SQR"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "25 + j0"

# T-SQR-CPLX1
def test_sqr_cplx1(capsys):
    # operation: SQR (complex)
    cdc = CDC()
    cmd_list = ["push 1+j2", "SQR"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "-3 + j4"

# T-SQR-ERR1
def test_sqr_err1(capsys):
    # operation: SQR (error)
    cdc = CDC()
    cdc.onecmd("SQR")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"

# T-SQRT-REAL1
def test_sqrt_real1(capsys):
    # operation: SQRT (real)
    cdc = CDC()
    cmd_list = ["push 4", "SQRT"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 + j0"

# T-SQRT-CPLX1
def test_sqrt_cplx1(capsys):
    # operation: SQRT (complex)
    cdc = CDC()
    cmd_list = ["push -1", "SQRT"]
    for cmd in cmd_list:
        cdc.onecmd(cmd)
    cdc.onecmd("pop")
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 + j1"

# T-SQRT-ERR1
def test_sqrt_err1(capsys):
    # operation: SQRT (error)
    cdc = CDC()
    cdc.onecmd("SQRT")
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: stack underflow"
