#coding:utf-8
#coding:utf-8
import cgi 
import cgitb
import http.cookies
import datetime
import os 

expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")

my_cookie = http.cookies.SimpleCookie()
my_cookie ["pref_lang"] = "fr"
my_cookie ["pref_lang"] ["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
"""
Set-Cookies: pref-lang = fr;
expires # date d'expiration
path # lien pour l'utiliser 
comment #faire des commanter du cookies*
domain # racine ou domaine du site
secure # cookies marche que sur une connection https
version # version du cookies
httponly # pour qu'il ne soit pas modifier en cour
print("Set-Cookies: pref-lang = fr; httponly")
"""

#les cookies avant le html
print(my_cookie.output())
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
  <h1>page de resulta</h1>
"""
print(html)
    
if "HTTP_COOKIE" in os.environ:
    os.environ["HTTP_COOKIE"]
    print("le cookie existe est c'est")
else:
    print("HTTP_Cookie n'existe pas ")

try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(user_lang["pref_lang"].value)
except(http.cookies.CookiesError,KeyError):
    print("non trouver")
 


html = """
</body>
</html>
"""
print(html)
