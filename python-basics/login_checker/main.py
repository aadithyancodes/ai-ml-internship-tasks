def login(username, password):
    if username=="admin" and password==1234:
        return "Login Successfull"
    else:
        return "Invalid login"
status = login("admin", 1234)
print(status)