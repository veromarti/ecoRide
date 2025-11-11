#Importamos un modulo que nos va a ayudar con la gestion del tiempo
from datetime import date

#Creamos las listas donde tendremos el tipo de bike y la tarifa de alquiler por minuto
tipos_bikes=["Infantil", "Electrica", "Deportiva", "Estandar"]
precios_bikes=[250, 500, 400, 200]

#Inicializamos variables principales en el valor que necesitamos para ejecutar los ciclos
servicio=False
usuario = False
menu = False
cont = 1
cont_usuario = 1
total = 0

#Molde de la cuenta del usuario. Donde se almacenan los datos principales de la cuenta y posteriormente se imprimen en ese formato
dict_usuario = {
    "Usuario "+ str(cont_usuario): "",
    "Telefono "+ str(cont_usuario): ""}
    
dict_servicio ={
    "Telefono "+ str(cont_usuario): "",
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

#Esta funcion nos ayuda a registrar al usuario 
def buscar_usuario(cont_usuario, num_servicio):
    while True:
        telefono = input("Teléfono: ").strip()
        if not telefono:
            print("El teléfono no puede estar vacío\n")
            continue
        if not telefono.isdigit():
            print("Valor no valido. El campo telefono debe contener solo números")
            continue
        if len(telefono) != 10:
            print("El numero de telefono debe tener exactamente 10 digitos. Vuelva a ingresarlo")
            continue
        break
    
    if telefono in dict_usuario.values():
        print("\nYa tiene un usuario creado en el sistema\n")
        num_servicio += 1
        
    else:
        while True:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.\n")
                continue
            if not all(c.isalpha() or c.isspace() for c in nombre):
                print("El nombre solo puede contener letras y espacios.\n")
                continue
            break
        print("\nUsuario registrado con exito.\n")
        
        dict_usuario["Usuario "+ str(cont_usuario)] = nombre
        dict_usuario["Telefono "+ str(cont_usuario)] = telefono
        dict_servicio["Telefono "+ str(cont_usuario)] = telefono
        cont_usuario += 1
    
    return cont_usuario, num_servicio

#Con esta funcion creamos el servicio y añadimos eso a la cuenta del usuario
def crear_servicio(bicicleta, tiempo, num_servicio):
    bike = tipos_bikes[int(bicicleta)-1]
    rate = precios_bikes[int(bicicleta)-1]
    total_cost = calcular_costo(bicicleta, tiempo)
    time = tiempo
    
    dict_servicio["Servicio " + str(num_servicio)] = {"Bicicleta": bike,
    "Tiempo": time,
    "Tarifa por minuto": rate,
    "Costo bicicleta": total_cost}
    
    print("\nServicio agregado exitosamente.")

#aqui le mostramos al usuario el estado de su cuenta (mostramos todos los detalles del servicio)     
def resumen_pedido(valor, cant_servicio):
    print("\nResumen del servicio:")

    for k in range(cant_servicio):
        print(f"\n--Servicio {k+1}--")
        for i, j in dict_servicio["Servicio " + str(k+1)].items():
            print(f"{i}: {j}")
    print("Querido usuario, el valor a pagar es: $", valor)

#Aqui calculamos el costo del alquiler de la bicicleta utilizada por el usuario, se calcula costo por bicicleta, no por el total de las bicicletas alquiladas    
def calcular_costo(bicicleta, tiempo):
    costo = precios_bikes[bicicleta-1] * tiempo
    return costo

#Esta funcion nos muestra el menu principal
def menu_principal():
    menu_texto= (
        "\n--- BIENVENIDO A EcoRide ---\n"
        "1. Alquilar bicicleta\n"
        "2. Consultar Tarifas\n"
        "3. Pagar\n"
        "4. Salir\n"
    )
    opcion = validar_entero_menu(menu_texto, "Seleccione una opción (1-4): ", 1, 4)
    return opcion

#Aqui le pedimos al usuario que ingrese un numero ya que lo anteriormente ingresado no correspondia con lo solicitado
def validar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo or maximo is not None and valor > maximo:
                raise ValueError
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.\n")
            
#con este estamos validando que la opcion que escoja del menu sea un numero entero y si no le notificamos al usuario            
def validar_entero_menu(menu_texto, mensaje, minimo=None, maximo=None):
    while True:
        print(menu_texto)
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo or maximo is not None and valor > maximo:
                raise ValueError
            return valor
        except ValueError:
            print("Opción inválida. Ingrese un valor disponible en el menú.\n")

#Con esta funcion imprimimos las opciones de bicicletas disponibles para alquilar    
def mostrar_bikes():
    menu_texto ="\n--- Tipos de Bicicletas ---\n"
    for i in range(len(tipos_bikes)):
        menu_texto += (f"{str(i+1)}.{tipos_bikes[i]}- ${str(precios_bikes[i])} por minuto\n")
        
    opcion = validar_entero_menu(menu_texto, "\nSeleccione el tipo de bicicleta (1-4): ", 1, len(tipos_bikes))
    return opcion

#Con esta funcion imprimimos la tarifa de las bicicletas, tarifa x minuto
def mostrar_tarifas():
    print("\n- - - - - Tarifas EcoRides - - - - -\n")

    for i in range(len(tipos_bikes)):
        print(str(i+1)+". " + tipos_bikes[i] + " - $" + str(precios_bikes[i]) + " por minuto")
    
    opcion = (input("\nIngrese cualquier tecla para volver al Menu Principal ->"))
    return opcion

#Aqui le pasamos al usuario una lista de opciones para el método de pago, y el escogerá una

def obtener_servicios(diccionario, telefono_buscado):
    valores = list(diccionario.values())
    
    if telefono_buscado not in valores:
        return None  # Teléfono no encontrado
        
    # Buscar todos los servicios con el mismo número
    servicios = {
        k: v
        for k, v in diccionario.items()
        if k.startswith('Servicio')
    }
    
    return servicios

def mostrar_metodo():
    menu_texto = ("\n--- Métodos de Pago ---\n1. Efectivo\n2. Tarjeta\n3. Puntos\n4. Salir")
    while True: 
        opcion = validar_entero_menu(menu_texto, "\n¿Cuál método de pago desea utilizar? (1-4): ", 1, 4)

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
        dict_servicio["Metodo de Pago"] = metodo_pago
        return metodo_pago.lower()

#En esta funcion estamos verificando que el tiempo de uso sea meno o igual al tiempo solicitado al alquilar    
def tiempo_de_uso(num_pedidos):

    for k in range(num_pedidos):
        print(f"\n--Servicio {k+1}--")
        for i, j in dict_servicio["Servicio " + str(k+1)].items():
            print(f"{i}: {j}")
        tiempo_real = validar_entero("\nIngrese el tiempo real de uso para este servicio en minutos: ", 1)
        dict_servicio["Servicio " + str(k+1)]["Tiempo de uso"] = tiempo_real

#Con esta funcion validamos los descuentos, recargos y multas que aplican a cada servicio 
def descuentos(tiempo, tiempo_uso, metodo_pago):
    fecha= date.today()
    dia = fecha.weekday()
    descuento = 0  
    multa = 0
    recargo_finde = 0 

    if metodo_pago == "tarjeta":
        if tiempo_uso > 60:
            descuento = 0.10

    if metodo_pago == "puntos":
        if tiempo_uso < 10:
            descuento 

    if dia in (5, 6):
        recargo_finde = 0.05

    if tiempo_uso > tiempo:
        multa = 10000

    return descuento, recargo_finde, multa

#Esta funcion nos ayuda a calcular el valor final del alquiler, incluyendo cantidad de bicicletas alquiladas, el tiempo y estos datos son traidos desde la cuenta del usuario
def valor_final(valor_inicial, discount, extra_fds, multa, time, real_time,rate):
    
    if real_time > time:
        valor_inicial = rate * real_time
    else:
        pass

    valor_final = (valor_inicial * (1-discount)) * (1+extra_fds) + multa

    return valor_final

#Con esta funcion limpiamos la cuenta del usuario una vez ya haya pagado
def limpiar_servicios():
    

    dict_usuario["Metodo de Pago"] = ""
    dict_usuario["Valor a Pagar"] = 0.0

#Iniciamos la ejecucion del codigo principal, usamos un while para controlar el ingreso y la salida del usuario
while not menu:
    #pedimos una opcion a escojer y ejecutamos
    opcion = menu_principal()


    #si la opcion es 1, vamos a registrar al usuario para posteriormente proceder con el alquiler de las unidades que se escojan
    if opcion == 1:

        cont_usuario, cont = buscar_usuario(cont_usuario,cont)
        servicio = False
        
        while not servicio:
            bicicleta = mostrar_bikes()
            tiempo = validar_entero("Ingrese el tiempo de uso en minutos (máximo 180): ",1, 180)
            
            crear_servicio(bicicleta, tiempo, cont)
            print("\n")
             
            while True: 
                desea_agregar = input("\nDesea agregar otro servicio -> (y/n): ")
            
                if desea_agregar.lower() == "y":
                    cont += 1            
                    break
                    
                elif desea_agregar.lower() == "n":
                    print("- - - Gracias por usar el servicio de alquiler - - -")
                    servicio = True  
                    break   
                else: 
                    print("Error. Ingrese una opción valida -> (y: si / n: no):")
                
    #si la opcion es 2 procederiamos a mostrar exclusivamente las tarifas de las bicicletas para alquilar
    elif opcion == 2:
        mostrar_tarifas()

    #si la opcion es 3, dirigimos al usuario a la seccion de pagos, donde se le mostrará el total acomulado en su cuenta, y los metodos por los cuales podrá realizar el pago
    elif opcion == 3: 

        while True:
            telefono = input("Teléfono: ").strip()
            if not telefono:
                print("El teléfono no puede estar vacío\n")
                continue
            if not telefono.isdigit():
                print("Valor no valido. El campo telefono debe contener solo números")
                continue
            if len(telefono) != 10:
                print("El numero de telefono debe tener exactamente 10 digitos. Vuelva a ingresarlo")
                continue
            break
        
        
    
        dict_pago = obtener_servicios(dict_servicio,telefono)
                
        if servicio and dict_pago != None:
            
            print("\n")
            tiempo_de_uso(cont)
            pago = mostrar_metodo()
            if pago is None:
                continue
            dict_servicio["Metodo de Pago"] = pago

            for i in range(cont):
                tiempo = dict_pago["Servicio " + str(i+1)]["Tiempo"]
                tiempo_real = dict_pago["Servicio " + str(i+1)]["Tiempo de uso"]
                descuento, recargo_finde, multa = descuentos(tiempo, tiempo_real, pago)
                tarifa = dict_pago["Servicio " + str(i+1)]["Tarifa por minuto"]
                valor_base = int(dict_pago["Servicio " + str(i+1)]["Costo bicicleta"])
                valor_pago = valor_final(valor_base, descuento, recargo_finde, multa, tiempo, tiempo_real, tarifa)
                total += valor_pago
                
                
                
                valor_descuento = valor_base * descuento
                valor_recargo_fds =  valor_base * recargo_finde

                dict_pago["Servicio " + str(i+1)]["Descuento"] = valor_descuento
                dict_pago["Servicio " + str(i+1)]["Multa"] = multa
                dict_pago["Servicio " + str(i+1)]["Recargo finde"] = valor_recargo_fds
                dict_pago["Servicio " + str(i+1)]["Costo Total"] = valor_pago
                dict_pago["Valor a Pagar"] = total

            resumen_pedido(total, cont)
            
            confirmacion_pago = ("\n--- Confirmación de pago ---\n"
                "1. Confirmar pago\n"
                "2. Cancelar y volver al menú\n" )
            opcion_confirmacion = validar_entero_menu(confirmacion_pago, "Seleccione una opción (1-2): ", 1, 2)
            
            if opcion_confirmacion == 1:
                print("\nPago realizado con éxito. ¡Gracias por usar EcoRide!\n")
                
                servicio = False
                total = 0
                cont = 1
                
                limpiar_servicios()
                
            else:
                print("\nPago cancelado. Puede volver a la opción de pagar cuando desee reintentar el pago.\n")
        
        #Si en la cuenta no hay saldo pendiente, le decimos al usuario que no hay servicio pendiente
        else:
            print("\nNo hay ningun servicio pendiente de pago\n")
            

    elif opcion == 4:
        print ("\nGracias por usar el servicio EcoRides")
        menu = True

    #Si lo ingresado es invalido, se notifica
    else:
        print("\nIngrese una opcion valida/n")

