import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT

    
    def text_name(e): #e - event
        name = text_input.value.strip()#strip() used to remove spaces
        
        if name:
            text_hello.value = f"Hello, {text_input.value}"
            text_hello.color = ft.Colors.GREEN_100
            text_input.value = ""
        else:
            text_hello.value = f"Enter your name !"
            text_hello.color = ft.Colors.RED


    def change_theme_mode(e):
        if page.theme_mode  == ft.ThemeMode.LIGHT:
           page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text('Hello', color = ft.Colors.RED)
    text_input = ft.TextField(label = "Enter your name", on_submit = text_name)
    btn = ft.ElevatedButton('send', on_click = text_name)

    theme_btn = ft.ElevatedButton(icon = ft.Icons.BRIGHTNESS_7, on_click = change_theme_mode)

    page.add(text_hello, text_input, btn, theme_btn)

ft.app(target = main)
#ft.app(target = main, view = ft.AppView.WEB_BROWSER)


#2nd lesson
# import flet as ft

# def main(page: ft.Page):
#     page.title = 'My first app'
#     page.theme_mode = ft.ThemeMode.LIGHT
    
#     text_hello = ft.Text('Hello, group 65-1')

#     text_button = ft.TextButton('SEND')
#     elevated_button = ft.ElevatedButton('send')
#     icon_button = ft.IconButton(icon = ft.Icons.SEARCH) 

#     name_input = ft.TextField(label = "Enter your name")

#     page.add(text_hello, text_button, elevated_button, icon_button, name_input)

# ft.app(target = main, view = ft.AppView.WEB_BROWSER)