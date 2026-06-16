import auth


username = "Raphael"
password = "password123"
password2 = "password123"

auth.login(username, password)
auth.signup(username, password, password2)