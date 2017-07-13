#Projectname : webapp
#File name : callserver.py
#Author: Chinatsu  Kawakami
#Date: 13th July 2017
#version : 1.1.1

import http.server

server_address=("",8000)
set_handler = http.server.SimpleHTTPRequestHandler #set handler
add_server = http.server.HTTPServer(server_address,set_handler)
add_server.serve_forever()