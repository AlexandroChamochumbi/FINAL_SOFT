from flask import Flask, request, jsonify

app = Flask(__name__)

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

#cuentas
BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]

@app.route('/billetera/contactos', methods=['GET'])
def obtener_contactos():
    minumero = request.args.get('minumero')
    for cuenta in BD:
        if cuenta.numero == minumero:
            contactos = {contacto: buscar_nombre(contacto) for contacto in cuenta.contactos}
            return jsonify(contactos)
    return "Cuenta no encontrada", 404

def buscar_nombre(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta.nombre
    return "Contacto no encontrado"

@app.route('/billetera/pagar', methods=['POST'])
def realizar_pago():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))

    cuenta_origen = None
    cuenta_destino = None

    for cuenta in BD:
        if cuenta.numero == minumero:
            cuenta_origen = cuenta
        if cuenta.numero == numerodestino:
            cuenta_destino = cuenta

    if cuenta_origen is None or cuenta_destino is None:
        return "Cuenta no encontrada", 404

    if cuenta_origen.saldo < valor:
        return "Saldo insuficiente", 400

    cuenta_origen.saldo -= valor
    cuenta_destino.saldo += valor

    cuenta_origen.operaciones.append(f"Pago realizado de {valor} a {cuenta_destino.nombre}")
    cuenta_destino.operaciones.append(f"Pago recibido de {valor} de {cuenta_origen.nombre}")

    return f"Pago realizado de {valor} a {cuenta_destino.nombre}", 200

@app.route('/billetera/historial', methods=['GET'])
def obtener_historial():
    minumero = request.args.get('minumero')
    for cuenta in BD:
        if cuenta.numero == minumero:
            historial = {
                "Saldo de " + cuenta.nombre: cuenta.saldo,
                "Operaciones de " + cuenta.nombre: cuenta.operaciones
            }
            return jsonify(historial)
    return "Cuenta no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
