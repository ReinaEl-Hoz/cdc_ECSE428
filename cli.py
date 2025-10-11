import sys
from calculator import CDC

def print_welcome_message():
    print("=" * 60)
    print("Welcome to Our Complex Desk Calculator (CDC)")
    print("=" * 60)
    print("\nAvailable commands:")
    print("  PUSH <number>    - Push a real or complex number onto stack")
    print("  POP              - Pop and display top of stack")
    print("  ADD              - Add top two stack values")
    print("  SUB              - Subtract top two stack values")
    print("  MUL              - Multiply top two stack values")
    print("  DIV              - Divide top two stack values")
    print("  DELETE           - Remove top stack value without printing")
    print("\nNumber formats:")
    print("  Real:    5, -2.5, 3.14")
    print("  Complex: 3+j4, -2.5-j0.25, j5, 1+j1")
    print("\n" + "=" * 60 + "\n")

# 2 modes for CLI interactive and batch mode
def interactive_mode():
    cdc = CDC()
    print_welcome_message()
    while True:
        try:
            user_cmd = input("cdc> ").strip()
            if not user_cmd:
                continue
            
            res = cdc.execute(user_cmd)
            if res:
                print(res)
        except Exception as e:
            print(f"Error: {e}")

def batch_mode(cmds):
    cdc = CDC()
    print_welcome_message()
    for cmd in cmds:
        res = cdc.execute(cmd)
        if res:
            print(res)

def main():
    if len(sys.argv) > 1:
        # then we execute in batch mode
        cmds = sys.argv[1:]
        batch_mode(cmds)
    else:
        # then we execute in interactive mode
        interactive_mode()

