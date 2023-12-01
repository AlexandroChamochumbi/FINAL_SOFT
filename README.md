# FINAL_SOFT

Pregunta3:
Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir
por día.
¿Qué cambiaría en el código (Clases / Métodos)?
Tendría que limitar la cantidad de soles máxima que puede transferir con su cuenta por 24 horas
Para verificar el correcto funcionamiento de este nuevo requirimiento tendría que crear un test que intente transferir en un solo pago una cantidad mayor a 200, también otro posible test que nos ayudaría con esto sería realizar un gran número de transferencias que juntas sumen más de 200, si se ha logrado implementar esta nueva funcionalidad correctamente debería de impedir o retornar error sin importar si fue hecha en partes las transferencias y por último un test que retorne exito al realizarse transferencias menores de 200 durante el día
 ¿Cuánto riesgo hay de romper lo que ya funciona?
 Al ser solo un limitante en la cantidad de movimientos de dinero , si se acompaña con una buena integración de tests para comprobar su correcta funcionalidad , los programadores podrían verificar rapidamente si se cometió algún error de lógica por las condiciones. Con esto se aseguraría que se implemente correctamente y sin romper el resto de funcionalidades anteriores.
