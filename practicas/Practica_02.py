#PRACTICA 02:

# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados




class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def asignar_horario(self, horarios):
        self.horarios.extend(horarios)

class Autobus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []

    def registrar_horario(self, hora):
        if hora in self.horarios:
            raise ValueError(f"El horario {hora} ya está registrado para este autobús.")
        self.horarios.append(hora)

    def asignar_ruta(self, ruta):
        self.ruta = ruta

class Administracion:
    def __init__(self):
        self.autobuses = []
        self.conductores = []

    def agregar_bus(self, id_bus):
        if self.buscar_bus(id_bus):
            print(f"El autobús con ID {id_bus} ya existe.")
        else:
            self.autobuses.append(Autobus(id_bus))
            print(f"Autobús con ID: {id_bus} agregado exitosamente.")

    def buscar_bus(self, id_bus):
        for bus in self.autobuses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def asignar_ruta_a_bus(self, id_bus, ruta):
        bus = self.buscar_bus(id_bus)
        if bus:
            bus.asignar_ruta(ruta)
            print(f"Ruta {ruta} asignada al autobús con ID: {id_bus}.")
        else:
            print(f"No se encontró el autobús con ID: {id_bus}.")

    def agregar_conductor(self, nombre):
        if self.buscar_conductor(nombre):
            print(f"El conductor {nombre} ya existe.")
        else:
            self.conductores.append(Conductor(nombre))
            print(f"Conductor {nombre} agregado exitosamente.")

    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

    def asignar_horario_a_conductor(self, nombre_conductor, hora):
        conductor = self.buscar_conductor(nombre_conductor)
        if conductor:
            if hora in conductor.horarios:
                print(f"El conductor {nombre_conductor} ya tiene asignado el horario {hora}.")
            else:
                conductor.asignar_horario([hora])
                print(f"Horario {hora} asignado al conductor {nombre_conductor}.")
        else:
            print(f"No se encontró al conductor {nombre_conductor}.")

    def asignar_bus_a_conductor(self, nombre_conductor, id_bus):
        conductor = self.buscar_conductor(nombre_conductor)
        bus = self.buscar_bus(id_bus)

        if conductor and bus:
            for otro_conductor in self.conductores:
                if otro_conductor != conductor:  # ponemos esto para que no lo compare con el mismo conductor
                    conflicto = any(hora in otro_conductor.horarios for hora in bus.horarios)
                    if conflicto:
                        print(f"No se puede asignar el autobús con ID: {id_bus} al conductor {nombre_conductor}.")
                        print(f"El horario {bus.horarios} ya está asignado a otro conductor: {otro_conductor.nombre}.")
                        return

            conductor.asignar_horario(bus.horarios)
            print(f"Autobús con ID: {id_bus} asignado exitosamente al conductor {nombre_conductor}.")
        elif not conductor:
            print(f"No se encontró al conductor {nombre_conductor}.")
        elif not bus:
            print(f"No se encontró el autobús con ID: {id_bus}.")

if __name__ == "__main__":
    admin = Administracion()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar autobús")
        print("2. Asignar ruta a autobús")
        print("3. Registrar horario a autobús")
        print("4. Agregar conductor")
        print("5. Asignar horario a conductor")
        print("6. Asignar autobús a conductor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_bus = input("Ingrese el ID del autobús: ")
            admin.agregar_bus(id_bus)
        elif opcion == "2":
            id_bus = input("Ingrese el ID del autobús: ")
            ruta = input("Ingrese la ruta: ")
            admin.asignar_ruta_a_bus(id_bus, ruta)
        elif opcion == "3":
            id_bus = input("Ingrese el ID del autobús: ")
            hora = input("Ingrese el horario (formato HH:MM): ")
            bus = admin.buscar_bus(id_bus)
            if bus:
                try:
                    bus.registrar_horario(hora)
                    print(f"Horario {hora} registrado para el autobús {id_bus}.")
                except ValueError as e:
                    print(e)
            else:
                print(f"No se encontró el autobús con ID {id_bus}.")
        elif opcion == "4":
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            admin.agregar_conductor(nombre_conductor)
        elif opcion == "5":
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            hora = input("Ingrese el horario (formato HH:MM): ")
            admin.asignar_horario_a_conductor(nombre_conductor, hora)
        elif opcion == "6":
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            id_bus = input("Ingrese el ID del autobús: ")
            admin.asignar_bus_a_conductor(nombre_conductor, id_bus)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


#ESO ES ToDO POR EL EJERCICIO QUE NOS ASIGNÓ