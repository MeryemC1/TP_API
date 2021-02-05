import platform
import os
import sys
 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/resultat',methods = ['GET'])
def resultat():
  result=request.args
  x = result['a']
  y = result['nombre']
  return render_template("resultat.html", x=a, y=nombre)

app.run(debug=True)


print sys.platform()
print os.name
print platform.platform()
print platform.uname()

def get_dns_domain():
    return socket.getfqdn().split('.', 1)[1]
 
print get_dns_domain()

url_for('x')               
url_for('y')

