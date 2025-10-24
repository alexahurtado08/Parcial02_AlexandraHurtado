from flask import Flask, jsonify

#Crear app 
app = Flask(__name__)

#  calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recibir el numero por url
@app.route('/factorial/<int:num>', methods=['GET'])
def calcular(num):
    resultado_factorial = factorial(num)
    etiqueta = "par" if num % 2 == 0 else "impar"

    respuesta = {
        "numero_recibido": num,
        "factorial": resultado_factorial,
        "etiqueta": etiqueta
    }
    return jsonify(respuesta)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
