import PySimpleGUI as sg

# Obtém a lista de todos os temas disponíveis
available_themes = sg.theme_list()

# Exibe os nomes dos temas na janela
layout = [
    [sg.Text('Temas Disponíveis')],
    [sg.Listbox(values=available_themes, size=(40, 10), enable_events=True, key='-THEME LIST-')],
    [sg.Button('Selecionar Tema')]
]

window = sg.Window('Escolher Tema', layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Selecionar Tema':
        selected_theme = values['-THEME LIST-'][0]
        sg.theme(selected_theme)
        sg.popup(f'Tema selecionado: {selected_theme}')
        print(f"tema: {selected_theme}")

window.close()

