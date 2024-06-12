#Clases usadas para las excepciones de tranferencia y saldo, deposito 
class SaldoEfectivoInsuficiente(Exception):
    pass

class SaldoCuentaInsuficiente(Exception):
    pass

class Cuenta:
    def __init__(self, numero, nombre, saldo):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("No hay suficiente saldo en el cajero.")
        self.saldo -= monto

    def transferir(self, monto, cuenta_destino):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("Saldo insuficiente. No posee esa cantidad de dinerp")
        self.retirar(monto)
        cuenta_destino.depositar(monto)

    def mostrar_datos(self):
        return f"Cuenta: {self.numero}, Nombre: {self.nombre}, Saldo: {self.saldo}"

class CajeroAutomatico:
    def __init__(self, saldo_efectivo):
        self.saldo_efectivo = saldo_efectivo
        self.cuentas = {}
        self.cuenta_actual = None

    def agregar_cuenta(self, cuenta):
        self.cuentas[cuenta.numero] = cuenta

    def autenticar(self, numero_cuenta, nombre):
        if numero_cuenta in self.cuentas and self.cuentas[numero_cuenta].nombre == nombre:
            self.cuenta_actual = self.cuentas[numero_cuenta]
            return True
        return False

    def mostrar_saldo_efectivo(self):
        return self.saldo_efectivo

    def depositar_efectivo_propio(self, monto):
        if self.cuenta_actual:
            self.cuenta_actual.depositar(monto)
        else:
            print("Haga la autenticacion correspondiente por favo.")

    def depositar_efectivo_otra_cuenta(self, monto, numero_cuenta_destino):
        if numero_cuenta_destino in self.cuentas:
            self.cuentas[numero_cuenta_destino].depositar(monto)
        else:
            print("La cuenta a la que quiere enviar no existe.")

    def transferir(self, monto, numero_cuenta_destino):
        if numero_cuenta_destino in self.cuentas:
            self.cuenta_actual.transferir(monto, self.cuentas[numero_cuenta_destino])
        else:
            print("La cuenta a la que quiere enviar no existe")

    def retirar_efectivo(self, monto):
        if monto > self.saldo_efectivo:
            raise SaldoEfectivoInsuficiente("No hay el suficiente saldo en el cajero")
        self.cuenta_actual.retirar(monto)
        self.saldo_efectivo -= monto

# main del cajero
def main():
    #se define el dinero del cajero en este caso cien mil
    cajero = CajeroAutomatico(100000)
    #se registran los cuentahabientes de forma manual en el código con nombre y saldo
    cuenta1 = Cuenta(282828, "Alan Pacheco", 1000)
    cuenta2 = Cuenta(123456, "Cookie", 3000)
    
    cajero.agregar_cuenta(cuenta1)
    cajero.agregar_cuenta(cuenta2)
    
    while True:
        print("\nBienvenido al Cajero Automático de Alan")
        numero_cuenta = int(input("Ingrese su número de cuenta: "))
        nombre = input("Ingrese su nombre: ")
        
        if cajero.autenticar(numero_cuenta, nombre):
            print("Autenticación exitosa")
            while True:
                print("\nBuenas tardes, bienvenido al cajero de Alan")
                print("\nElija una operación:")
                print("1. Verifique el saldo de su cuenta")
                print("2. Deposito a su cuenta")
                print("3. Deposito a otra cuenta")
                print("4. Transferencia a otra cuenta")
                print("5. Retirar efectivo")
                print("6. Salir")
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    print(cajero.cuenta_actual.mostrar_datos())
                
                elif opcion == 2:
                    monto = float(input("Ingrese el monto a depositar: "))
                    cajero.depositar_efectivo_propio(monto)
                    print("Depósito exitoso.")
                
                elif opcion == 3:
                    monto = float(input("Ingrese el monto a deposita: "))
                    numero_cuenta_destino = int(input("Ingrese el número de cuenta a enviar: "))
                    cajero.depositar_efectivo_otra_cuenta(monto, numero_cuenta_destino)
                    print("El deposito fue correcto.")
                
                elif opcion == 4:
                    monto = float(input("Ingrese el monto a tranferir: "))
                    numero_cuenta_destino = int(input("Ingrese el numero de cuenta a la cual transferir "))
                    try:
                        cajero.transferir(monto, numero_cuenta_destino)
                        print("La transferencia exitosa.")
                    except SaldoCuentaInsuficiente as e:
                        print(e)
                
                elif opcion == 5:
                    monto = float(input("Ingrese el monto a retirar: "))
                    try:
                        cajero.retirar_efectivo(monto)
                        print("Se retiro de manera exitosa")
                    except SaldoEfectivoInsuficiente as e:
                        print(e)
                
                elif opcion == 6:
                    print("Gracias por su visita.")
                    break
                
                else:
                    print("La opcion no es valida intentelo de nuevo.")
        else:
            print("No se puedo autenticar, intentelo de nuevo porfa .")

if __name__ == "__main__":
    main()
