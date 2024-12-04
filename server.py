# calculator_server.py
from xmlrpc.server import SimpleXMLRPCServer

# Definir las funciones de la calculadora
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Error: División por cero"

# Crear un servidor RPC
server = SimpleXMLRPCServer(('localhost', 8000))
print("Calculadora RPC corriendo en http://localhost:8000")

# Registrar las funciones de la calculadora
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')

# Iniciar el servidor
server.serve_forever()
