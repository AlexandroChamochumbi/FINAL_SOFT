import unittest
import requests  
from app import app, BD, buscar_nombre, realizar_pago, obtener_historial, obtener_contactos
from flask import json

class TestApp(unittest.TestCase):

 def test_realizar_pago_sin_saldo_suficiente(self):
        #Cuenta("123", "Luisa", 400, ["456"]), PAGA A Cuenta("456", "Andrea", 300, ["21345"]) monto de 9999.... qye no posee
        tester = app.test_client(self)
        response = tester.post('/billetera/pagar?minumero=123&numerodestino=456&valor=999999999999999999999909')
        self.assertEqual(response.status_code, 400)
        #error que devuelve si saldo insuficiente
        #if cuenta_origen.saldo < valor:
        #return "Saldo insuficiente", 400

 def test_obtener_contactos_no_existente(self):#da error 404 al buscar contactos de un no existente
    #Cuenta("21345", "Arnaldo", 200, ["123", "456"])
    tester = app.test_client(self)
    response = tester.get('/billetera/contactos?minumero=666')
    self.assertEqual(response.status_code, 404)

 def test_obtener_historial_existente(self):#historial de la cuenta 123
    # Cuenta("123", "Luisa", 400, ["456"]),
    tester = app.test_client(self)
    response = tester.get('/billetera/historial?minumero=123')
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(response.status_code, 200)#fine
    self.assertIn("Saldo de Luisa", data)
    self.assertEqual(data["Saldo de Luisa"], 400)#su saldo inicial es de 400
    self.assertIn("Operaciones de Luisa", data)
    self.assertEqual(data["Operaciones de Luisa"], [])#no ha realizado operaciones aun


 def test_obtener_historial_no_existente(self): #obtener historial de numero no existente
    tester = app.test_client(self)
    response = tester.get('/billetera/historial?minumero=99999')
    self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()