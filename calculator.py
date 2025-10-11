import cmd
import re
import sys

class CDC(cmd.Cmd):
    intro = "Welcome to our calculator CLI!"
    prompt = "> "

    def __init__(self):
        super().__init__()
        self.stack = [] 

    def do_push(self, args):
        """push <number>"""
        num = self.parse_complex_nb(args.replace(" ", ""))
        if num == None:
            print("Invalid number format", file=sys.stderr)
        else:
            self.stack.append(num)
    
    def do_pop(self, args=None):
        """pop"""
        if len(self.stack) == 0:
            print("Error: stack underflow", file=sys.stderr)
        else:
            self.print_formatted_complex_num(self.stack.pop())
    
    def do_delete(self, args=None):
        """remove the top value on stack without printing"""
        if len(self.stack) == 0:
            print("Error: stack underflow", file=sys.stderr)
        else:
            self.stack.pop()
    
    def do_add(self, args=None):
        """add last 2 numbers on stack"""
        if len(self.stack) < 2:
            print("Error: stack underflow", file=sys.stderr)
            return
        ans = self.stack.pop() + self.stack.pop()
        self.stack.append(ans)
    
    def do_sub(self, args=None):
        """sub last 2 numbers on stack"""
        if len(self.stack) < 2:
            print("Error: stack underflow", file=sys.stderr)
            return
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        ans = num1 - num2
        self.stack.append(ans)
    
    def do_mul(self, args=None):
        """mul last 2 numbers on stack"""
        if len(self.stack) < 2:
            print("Error: stack underflow", file=sys.stderr)
            return
        ans = self.stack.pop() * self.stack.pop()
        self.stack.append(ans)
    
    def do_div(self, args=None):
        """div last 2 numbers on stack"""
        if len(self.stack) < 2:
            print("Error: stack underflow", file=sys.stderr)
            return
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        if (num2.real == 0 and num2.imag == 0):
            print("Error: division by zero", file=sys.stderr)
            return
        ans = num1 / num2
        self.stack.append(ans)

    def do_exit(self, args=None):
        """Exit CLI"""
        print("Exiting the calculator!")
        return True
    
    def parse_complex_nb(self, num):
        """Parse a number of form "0 +j0" into a complex number"""
        if num == None:
            return None
        
        # general complex
        pattern = r"^([+-]?\d*\.?\d*)?[+-]j(\d*\.?\d*)$"
        if re.fullmatch(pattern, num):
            num = num.replace("j", "",1) + "j"
            return complex(num)
    
        # real
        pattern = r"[+-]?\d*\.?\d*"
        if re.fullmatch(pattern, num):
            return complex(num)
        
        # pure imaginary
        pattern = r"-?j\d*\.?\d*"
        if re.fullmatch(pattern, num):
            num = num.replace("j", "",1) + "j"
            return complex(num)
        
        # invalid format
        return None

    def print_formatted_complex_num(self, num: complex):
        real = self.format_float(num.real)
        imaginary = self.format_float(abs(num.imag))
        if (num.imag < 0):
            print(f"{real} - j{imaginary}")
        else:
            print(f"{real} + j{imaginary}")
    
    def format_float(self, num):
        if num == int(num):
            return int(num)
        return num

if __name__ == "__main__":
    CDC().cmdloop()