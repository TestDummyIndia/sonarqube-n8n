def badFunction():
    break  # ❌ 'break' outside loop
    continue  # ❌ 'continue' outside loop

def getToken():
    token = "ghp_1234567890abcdef1234567890abcdef1234"  # ❌ Hardcoded token (security vulnerability)
    print("Token:", token)

def empty_function():
    pass  # ❌ Empty function without explanation

def duplicate_code():
    x = 5
    y = 10
    z = x + y
    print(z)

def duplicate_code_again():
    x = 5
    y = 10
    z = x + y
    print(z)  # ❌ Duplicated logic (code duplication)

badFunction()
getToken()
duplicate_code()
duplicate_code_again()
