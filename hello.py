from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def query_example():
    name = request.args.get('name')
    message = request.args.get('message')
    return	'''
			<body style = "background-color:#1A1B1E">
				<h1 style = "color:rgb(255, 255, 255);">
					<center>Hello {}! {}</center>
   				</h1>
      		</body>'''.format(name, message)

if __name__ == '__main__':
    app.run(host='192.168.1.1')
