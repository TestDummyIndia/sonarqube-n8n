# bad_code.py

# Hardcoded credentials (Security Hotspot)
USERNAME = "admin"
PASSWORD = "123456"

# Duplicate code (will trigger duplication detection)
def connect_db():
    print("Connecting to DB with", USERNAME, PASSWORD)

def connect_db2():
    print("Connecting to DB with", USERNAME, PASSWORD)

# Unused variable (Code Smell)
unused_variable = 42

# Complex method with poor naming and logic
def a(x, y):
    if x > 10:
        if y > 10:
            if x + y > 30:
                print("Too big")
            else:
                print("Still big")
        else:
            print("Y is small")
    else:
        print("X is small")

# Using break outside loop (SyntaxError + SonarQube issue)
def bad_break():
    print("This is wrong")
    break  # ❌ Not inside a loop

# Using continue outside loop (SyntaxError + SonarQube issue)
def bad_continue():
    print("Wrong use of continue")
    continue  # ❌ Not inside a loop

# Empty function (Code Smell)
def do_nothing():
    pass

# Function with same name as built-in
def list():
    return [1, 2, 3]
