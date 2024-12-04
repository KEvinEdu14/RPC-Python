# app.py
from flask import Flask, render_template, request
import xmlrpc.client

# Conectar al servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Llamar al servidor RPC según la operación seleccionada
        if operation == 'add':
            result = server.add(num1, num2)
        elif operation == 'subtract':
            result = server.subtract(num1, num2)
        elif operation == 'multiply':
            result = server.multiply(num1, num2)
        elif operation == 'divide':
            result = server.divide(num1, num2)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
