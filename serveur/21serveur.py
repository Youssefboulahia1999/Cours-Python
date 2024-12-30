#coding:utf-8

import http.server


server = http.server.HTTPServer
#le port permet la communication en 80
port = 80
#tuplie pour savoir ou en va se connecter
address = ("",port)

#gestionnaire de requet http
handler = http.server.CGIHTTPRequestHandler
#donne la racine du html
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"server demarre sur le PORT {port}")
#une sort de boucle pour faire tourner le server
httpd.serve_forever()