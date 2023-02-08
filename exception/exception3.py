try:
    password = input("Enter password: ")
    if len(password)<5:
        raise ValueError("Password must be at least 5 characters")
except ValueError as e:
    print(e)

