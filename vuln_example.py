# vuln_example.py
def insecure():
    user_input = input("Enter something: ")
    eval(user_input)  # This should trigger our custom rule
