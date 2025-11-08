from datetime import date

tipos_bikes=["Infantil", "Electrica", "Deportiva", "Estandar"]
precios_bikes=[250, 500, 400, 200]

servicio=False
usuario = False
cont = 1

dict_usuario = {
    "Usuario ":{"Nombre": "",
    "Telefono": ""},
    "Servicio " + str(cont):{"Bicleta": "",
    "Tiempo": 0,
    "Tarifa por minuto": 0.0,
    "Costo bicicleta": 0},
    "Metodo de Pago":"",
    "Costo Total": 0,
    "Descuentos": 0,
    "Multas": 0
}

def registro_usuario():
    print("Ingrese su información de usuario:\n")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    dict_usuario["Usuario "]["Nombre"] = nombre
    dict_usuario["Usuario "]["Telefono"] = telefono
    user = True
    print("\nUsuario registrado con exito.")
    return user

def crear_servicio(bicicleta, tiempo, num_servicio):
    bike = tipos_bikes[int(bicicleta)-1]
    rate = precios_bikes[int(bicicleta)-1]
    total_cost = calcular_costo(bicicleta, tiempo)
    time = tiempo
    
    dict_usuario["Servicio " + str(num_servicio)] = {"Bicicleta": bike,
    "Tiempo": time,
    "Tarifa por minuto": rate,
    "Costo bicicleta": total_cost}
    
    print("\nServicio agregado exitosamente.")
    
def resumen_pedido():
    print("\nResumen del servicio:")
    for i, j in dict_usuario.items():
        print(f"{i}: {j}")
    print("\nGracias por usar ecoBikes.")
    
def calcular_costo(bicicleta, tiempo):
    costo = precios_bikes[bicicleta-1] * tiempo
    return costo
    
def menu_principal():
    print("\n--- BIENVENIDO A EcoRide ---\n")
    print("1. Alquilar bicicleta\n2. Consultar Tarifas\n3. Pagar\n4. Salir")
    opcion = int(input("\nSeleccione una opción (1-4): "))  
    return opcion 
    
def mostrar_bikes():    
    for i in range(len(tipos_bikes)):
        print(str(i+1)+". " + tipos_bikes[i] + " - $" + str(precios_bikes[i]) + " por minuto")
        
    opcion = int(input("\nSeleccione el tipo de bicicleta (1-4): "))
    return opcion

def mostrar_tarifas():
    for i in range(len(tipos_bikes)):
        print(str(i+1)+". " + tipos_bikes[i] + " - $" + str(precios_bikes[i]) + " por minuto")
        

def mostrar_metodo():
    print("1. Efectivo\n2. Tarjeta \n3. Puntos\n4. Salir")

    metodo_pago = input("\n¿Cuál método de pago deseas utilizar?: \n").strip()

    if metodo_pago == "1":
        metodo_pago = "Efectivo"
    elif metodo_pago == "2":
        metodo_pago = "Tarjeta"
    elif metodo_pago == "3":
        metodo_pago = "Puntos"
    elif metodo_pago == "4":
        print("Saliendo del sistema...")
    else:
        print("Opción no válida.")
        metodo_pago = None

    if metodo_pago:
        print(f"Método de pago seleccionado: {metodo_pago}") 
        return metodo_pago
    
def descuentos(tiempo, tiempo_uso,metodo_pago):
    
    #tarifa = dict_usuario["Servicio " + str(cont)]["Costo bicicleta"] 
    fecha= date.today()
    dia = fecha.weekday() #0 = Lunes 6= Domingo    
    
    if tiempo > 60 and metodo_pago == "tarjeta":
        descuento = 0.10
    if tiempo_uso < 10 and metodo_pago == "puntos":
        descuento = 0
        pass
    if dia in (5,6):
        recargo_finde = 0.05
    if tiempo_uso > tiempo:
        multa = 10000

    return descuento, recargo_finde, multa

opcion = menu_principal()

while not servicio:
    
    
    if opcion == 1:
        while not usuario:
            usuario = registro_usuario()
        
        bicicleta = mostrar_bikes()
        tiempo = int(input("Ingrese el tiempo de uso en minutos: "))
        
        crear_servicio(bicicleta, tiempo, cont)
        
        desea_agregar = input("\nDesea agregar otro servicio -> (y/n): ")
        if desea_agregar.lower() == "y":
            cont += 1            
            servicio = False
            
        elif desea_agregar.lower() == "n":
            print("\n - - - Gracias por usar el sericio de alquiler - - -")
            servicio = True   
        
    elif opcion == 2:
        mostrar_tarifas()
        
    elif opcion == 3: 
        tiempo_real = int(input("Ingrese el tiempo real de uso en minutos: "))  
        pago=mostrar_metodo()
        dict_usuario["Metodo de Pago"] = pago
        descuento, recargo_finde, multa = descuentos(tiempo, tiempo_real, pago)
        
        valor_pago = (dict_usuario["Servicio " + str(cont)]["Costo bicicleta"] * (1-descuento))(1+recargo_finde) + multa
        dict_usuario["Costo Total"] = valor_pago
        resumen_pedido()
    
    print(dict_usuario)
    
    #pago = dicti(s1)llave(tarifa)*