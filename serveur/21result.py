#coding:utf-8
import cgi 
import cgitb

#debug
cgitb.enable()
#cree le fiel recupere les info du formulaire 
form = cgi.FieldStorage()

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

#ont recuper le usermane du form
try:
  if form.getvalue("username"):
    username = form.getvalue("username")
    print(f"<p>bonjour {username} !</p>")  
    print("oui")
  else:
    raise Exception("pseaud non tra")
except:
  print("<p>pseudo non transmis</p>")
html = """
</body>
</html>
"""
print(html)



