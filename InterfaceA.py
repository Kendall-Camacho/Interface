import PySimpleGUI as sg
from funci import show_info
sg.theme('DarkPurple1')

#Funcion que valida el inicio de sesion
def iniciar_sesion(usuario, codigo_acceso):
    if (usuario == "" and codigo_acceso == ""):
        sg.popup("Ingrese su nombre de usuario")
pass

layout = [
    [sg.Text('Usuario:', size=(100, 1), justification='center')],
    [sg.InputText('', pad=((0,0),(0,10)), key='user')],
    [sg.Text('Codigo de acceso:', size=(100, 1), justification='center')],
    [sg.InputText('', password_char='•', key='codigo_acceso')],
    [sg.Button('iniciar Sesion', key='login', ), sg.Button('cancelar', key='close')]
]

Window = sg.Window('login', layout, size=(300, 200))

while True:
    event, values = Window.read()

    if event ==sg.WIN_CLOSED or event =='close':
        break

    elif( event == 'login'):
        iniciar_sesion(show_info(values['user'], values['codigo_acceso']))
        # Nos parece que la interfaz ya cumple con el requisito, resulta redundante que
        # se agregen mas elementos, ya es elegante, simple, atractiva, y funcional.
        