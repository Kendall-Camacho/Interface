from ast import While
import PySimpleGUI as sg

def show_info(nombre, codigo_acceso):
    # pregunar si es un numero y si lo es y esta en un rango de 3000 y 3999
        areaT = ''
        sueldo = 0
        if codigo_acceso.isdigit() and int(codigo_acceso) in range(3000,4000):
            areaT = 'Contabilidad'
            sueldo = 3500
            sg.popup("Saludos " + nombre, "El codigo ingresado es: " + f"""{codigo_acceso}
                Su area de trabajo es: {areaT}
                Su sueldo es: {sueldo}
                Usted trabaja 8 horas al dia
                Usted gana por dia: {sueldo*8} colones
                Usted gana Semanalmente: {((sueldo*8)*5)} colones
                Usted gana quincenalmente: {((sueldo*8)*15)} colones
                Usted gana Mensualmente: {((sueldo*8)*30)} colones
                Usted gana Anualmente: {(((sueldo*8)*30)*12)} colones
            """)
        elif codigo_acceso.isdigit() and int(codigo_acceso) in range(1000,2000):
            areaT = 'Talento Humano'
            sueldo = 2250
            sg.popup("Saludos " + nombre,  "El codigo ingresado es: " + f"""{codigo_acceso}
                Su area de trabajo es: {areaT}
                Su sueldo es: {sueldo} colones por hora 
                Usted trabaja 8 horas al dia
                Usted gana por dia: {sueldo*8} colones
                Usted gana Semanalmente:    {((sueldo*8)*5)} colones
                Usted gana quincenalmente:  {((sueldo*8)*15)} colones
                Usted gana Mensualmente:    {((sueldo*8)*30)} colones
                Usted gana Anualmente:      {(((sueldo*8)*30)*12)} colones
            """)
        elif codigo_acceso.isdigit() and int(codigo_acceso) in range(2000,3000):
            areaT = 'Producción'
            sueldo = 3000
            sg.popup("Saludos " + nombre,  "El codigo ingresado es: " + f"""{codigo_acceso}
                Su area de trabajo es: {areaT}
                Su sueldo es: {sueldo} colones por hora
                Usted trabaja 6 horas al dia
                Usted gana por dia: {sueldo*6} colones
                Usted gana Semanalmente: {((sueldo*6)*5)} colones
                Usted gana quincenalmente: {((sueldo*6)*15)} colones
                Usted gana Mensualmente: {((sueldo*6)*30)} colones
                Usted gana Anualmente: {(((sueldo*6)*30)*12)} colones 
            """)
        elif codigo_acceso.isdigit() and int(codigo_acceso) in range(9000,9999):
            areaT = 'Gerencia'
            sueldo = 3500
            sg.popup("Saludos " + nombre,  "El codigo ingresado es: " + f"""{codigo_acceso}
            su area de trabajo es: {areaT}
            su sueldo es: {sueldo} colones por hora
            Usted trabaja 6 horas al dia
            Usted gana por dia: {sueldo*6} colones colones
            Usted gana Semanalmente: {((sueldo*6)*5)} colones
            Usted gana quincenalmente: {((sueldo*6)*15)} colones
            Usted gana Mensualmente: {((sueldo*6)*30)} colones
            Usted gana Anualmente: {(((sueldo*6)*30)*12)} colones
            """)
        
        elif codigo_acceso.isdigit() and int(codigo_acceso) in range(4000,4999):
            areaT = 'Gerencia'
            sueldo = 4200
            sg.popup("Saludos " + nombre,  "El codigo ingresado es: " + f"""{codigo_acceso}
            Su area de trabajo es: {areaT}
            Su sueldo es: {sueldo} colones por hora
            Usted trabaja 8 horas al dia
            Usted gana por dia: {sueldo*8} colones
            Usted gana Semanalmente: {((sueldo*8)*5)} colones
            Usted gana quincenalmente: {((sueldo*8)*15)} colones
            Usted gana Mensualmente: {((sueldo*8)*30)} colones
            Usted gana Anualmente: {(((sueldo*8)*30)*12)} colones
            """)

        else:
            sg.popup("Informacion","El codigo ingresado no es valido")
