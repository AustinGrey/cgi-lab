#!/usr/bin/env python3
import cgi
import cgitb

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

import json


# Question 1
# print(os.environ) # How to show all environment variables available

# Make output HTML
print("Content-Type: text/html")

# Question 2
# Show query string
# print(os.environ['QUERY_STRING'])

# Question 3
# Show user agent
# print(os.environ['HTTP_USER_AGENT'])

# Question 4
# print(login_page())
s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')

# Question 5
form_ok = username == secret.username and password == secret.password
c = SimpleCookie(os.environ['HTTP_COOKIE'])
c_username = None
c_password = None
if c.get('username'):
    c_username = c.get('username').value
if c.get('password'):
    c_password = c.get('password').value

cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password

if form_ok:
    print('Set-Cookie: username=', username)
    print('Set-Cookie: password=', password)
# Newline, headers complete
print()

# Question 6

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())