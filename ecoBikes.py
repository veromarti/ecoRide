from datetime import date

tipos_bikes=["Infantil", "Electrica", "Deportiva", "Estandar"]
precios_bikes=[250, 500, 400, 200]

servicio=False
usuario = False
menu = False
cont = 1
total = 0

dict_usuario = {
    "Usuario ":{"Nombre": "",
    "Telefono": ""},
    "Servicio " + str(cont):{"Bicleta": "",
    "Tiempo": 0,
    "Tarifa por minuto": 0.0,
    "Costo bicicleta": 0,
    "Tiempo de uso":0,
    "Descuento": 0,
    "Multa": 0,
    "Costo Total": 0},
    "Metodo de Pago":"",
    "Valor a Pagar":0.0}

def registro_usuario():
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.\n")
            continue
        if not all(c.isalpha() or c.isspace() for c in nombre):
            print("El nombre solo puede contener letras y espacios.\n")
            continue
        break
    
    while True:
        telefono = input("Teléfono: ").strip()
        if not telefono or not telefono.isdigit():
            print("El teléfono no puede estar vacío y debe contener solo números.\n")
            continue
        break
    
    dict_usuario["Usuario "]["Nombre"] = nombre
    dict_usuario["Usuario "]["Telefono"] = telefono
    user = True
    print("\nUsuario registrado con exito.\n")
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
    
def resumen_pedido(valor):
    print("\nResumen del servicio:")
    print("Querido usuario, el valor a pagar es: $", valor)
    
def calcular_costo(bicicleta, tiempo):
    costo = precios_bikes[bicicleta-1] * tiempo
    return costo
    
def menu_principal():
    menu_texto= (
        "\n--- BIENVENIDO A EcoRide ---\n"
        "1. Alquilar bicicleta\n"
        "2. Consultar Tarifas\n"
        "3. Pagar\n"
        "4. Salir\n"
    )
    opcion = validar_entero(menu_texto, "Seleccione una opción (1-4): ", 1, 4)
    return opcion


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo or maximo is not None and valor > maximo:
                raise ValueError
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.\n")
            
            
            
def validar_entero(menu_texto, mensaje, minimo=None, maximo=None):
    while True:
        print(menu_texto)
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo or maximo is not None and valor > maximo:
                raise ValueError
            return valor
        except ValueError:
            print("Opción inválida. Ingrese un valor disponible en el menú.\n")
    
def mostrar_bikes():
    menu_texto ="\n--- Tipos de Bicicletas ---\n"
    for i in range(len(tipos_bikes)):
        menu_texto += (f"{str(i+1)}.{tipos_bikes[i]}- ${str(precios_bikes[i])} por minuto\n")
        
    opcion = validar_entero(menu_texto, "\nSeleccione el tipo de bicicleta (1-4): ", 1, len(tipos_bikes))
    return opcion

def mostrar_tarifas():
    print("\n- - - - - Tarifas EcoRides - - - - -\n")

    for i in range(len(tipos_bikes)):
        print(str(i+1)+". " + tipos_bikes[i] + " - $" + str(precios_bikes[i]) + " por minuto")
    
    opcion = (input("\nIngrese cualquier tecla para volver al Menu Principal ->"))
    return opcion

def mostrar_metodo():
    menu_texto = ("\n--- Métodos de Pago ---\n1. Efectivo\n2. Tarjeta\n3. Puntos\n4. Salir")
    while True: 
        opcion = validar_entero(menu_texto, "\n¿Cuál método de pago desea utilizar? (1-4): ", 1, 4)

        if opcion == 1:
            metodo_pago = "Efectivo"
        elif opcion == 2:
            metodo_pago = "Tarjeta"
        elif opcion == 3:
            metodo_pago = "Puntos"
        elif opcion == 4:
            print("Saliendo del sistema...")
            return None

        print(f"Método de pago seleccionado: {metodo_pago.capitalize()}") 
        dict_usuario["Metodo de Pago"] = metodo_pago
        return metodo_pago.lower()
    
def tiempo_de_uso(num_pedidos):
    for i in range(num_pedidos):
        print("\nServicio " , i+1)
        print(dict_usuario["Servicio " + str(i+1)])
        tiempo_real = pedir_entero("\nIngrese el tiempo real de uso para este servicio en minutos: ", 1)
        dict_usuario["Servicio " + str(i+1)]["Tiempo de uso"] = tiempo_real
    
def descuentos(tiempo, tiempo_uso, metodo_pago):
    fecha= date.today()
    dia = fecha.weekday() #0 = Lunes 6= Domingo  
    descuento = 0  
    multa = 0
    recargo_finde = 0 
    
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

def valor_final(valor_inicial, discount, extra_fds, multa, time, real_time,rate):
    
    if real_time > time:
        valor_inicial = rate * real_time
    else:
        pass

    valor_final = (valor_inicial * (1-discount)) * (1+extra_fds) + multa

    return valor_final

while not menu:
    opcion = menu_principal()

    if opcion == 1:

        while not usuario:
            usuario = registro_usuario()
        
        while not servicio:
            bicicleta = mostrar_bikes()
            tiempo = pedir_entero("Ingrese el tiempo de uso en minutos: ",1)
            
            crear_servicio(bicicleta, tiempo, cont)
            desea_agregar = input("\nDesea agregar otro servicio -> (y/n): ")
            print("\n")

            if desea_agregar.lower() == "y":
                cont += 1            
                servicio = False
                
            elif desea_agregar.lower() == "n":
                print("- - - Gracias por usar el servicio de alquiler - - -")
                servicio = True   

    elif opcion == 2:
        mostrar_tarifas()

    elif opcion == 3: 

        if servicio:
            
            print("\n")
            tiempo_de_uso(cont)
            pago = mostrar_metodo()
            if pago is None:
                continue
            dict_usuario["Metodo de Pago"] = pago

            for i in range(cont):
                tiempo = dict_usuario["Servicio " + str(i+1)]["Tiempo"]
                tiempo_real = dict_usuario["Servicio " + str(i+1)]["Tiempo de uso"]
                descuento, recargo_finde, multa = descuentos(tiempo, tiempo_real, pago)
                tarifa = dict_usuario["Servicio " + str(i+1)]["Tarifa por minuto"]
                valor_base = int(dict_usuario["Servicio " + str(i+1)]["Costo bicicleta"])
                valor_pago = valor_final(valor_base, descuento, recargo_finde, multa, tiempo, tiempo_real, tarifa)
                total += valor_pago

                dict_usuario["Servicio " + str(i+1)]["Descuento"] = descuento
                dict_usuario["Servicio " + str(i+1)]["Multa"] = multa
                dict_usuario["Servicio " + str(i+1)]["Costo Total"] = valor_pago
                dict_usuario["Valor a Pagar"] = total

            resumen_pedido(total)
            
            confirmacion_pago = ("\n--- Confirmación de pago ---\n"
                "1. Confirmar pago\n"
                "2. Cancelar y volver al menú\n" )
            opcion_confirmacion = validar_entero(confirmacion_pago, "Seleccione una opción (1-2): ", 1, 2)
            
            if opcion_confirmacion == 1:
                print("\nPago realizado con éxito. ¡Gracias por usar EcoRide!\n")
                servicio = False
                total = 0
                cont = 1
            else:
                print("\nPago cancelado. Puede volver a la opción de pagar cuando desee reintentar el pago.\n")
        
        else:
            print("\nNo hay ningun servicio pendiente de pago\n")
            

    elif opcion == 4:
        print ("\nGracias por usar el servicio EcoRides")
        menu = True

    else:
        ("\nIngrese una opcion valida/n")
