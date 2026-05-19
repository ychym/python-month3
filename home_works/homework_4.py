import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'

    greeting_history = []

    greeting_text = ft.Text("List of the name:")

    def text_name(e): 
        name = text_input.value.strip()
        
        if name and len(name) >= 2:
            if text_input.value not in greeting_history:
                if not text_input.value.isdigit():
                    text_hello.value = f"Hello, {text_input.value}"
                    text_hello.color = ft.Colors.GREEN_600
                    greeting_history.append(name)
                    greeting_text.value = f'List:\n' + "\n".join(greeting_history[-5:][::-1])#[::-1]-> string[start:stop:step] [-1] list akyrky maani
                    text_input.value = ""                   
                else:
                    text_hello.value = f"Имя не может состоять из цифр!"
                
            else:
                text_hello.value = f"Это имя уже в истории!"
                text_hello.color = ft.Colors.RED
        else:
            text_hello.value = f"Enter your name !"
            text_hello.color = ft.Colors.RED
    

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = f"New list:"  
    
    def change_theme_mode(e):
        if page.theme_mode  == ft.ThemeMode.LIGHT:
           page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text('Hello', size = 20)
    text_input = ft.TextField(label = "Enter your name", on_submit = text_name, expand = True)
    btn = ft.Button('send', on_click = text_name)

    clear_btn = ft.IconButton(icon = ft.Icons.DELETE, on_click = clear_history)
    theme_btn = ft.IconButton(icon = ft.Icons.SETTINGS, on_click = change_theme_mode)

    main_object = ft.Column([ft.Row([theme_btn, clear_btn]),
                             ft.Row([text_hello]),
                             ft.Row([text_input, btn]),
                             ft.Row([greeting_text])
                            ])

    page.add(main_object) 
ft.app(target = main)
#ft.app(target = main, view = ft.AppView.WEB_BROWSER)

