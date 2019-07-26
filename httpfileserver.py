import http.server
import socketserver

PORT = 8000######change the port
Handler = http.server.SimpleHTTPRequestHandler
httpServ = socketserver.TCPServer(("",PORT), Handler)

print("File server started at port ",PORT)
print("enter to your browser localhost:",PORT)

httpServ.serve_forever()
