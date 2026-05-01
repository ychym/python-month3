import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    text_hello = ft.Text('Hello, group 65-1')

    text_button = ft.TextButton('SEND')
    elevated_button = ft.ElevatedButton('send')
    icon_button = ft.IconButton(icon = ft.Icons.SEARCH) 

    name_input = ft.TextField(label = "Enter your name")

    page.add(text_hello, text_button, elevated_button, icon_button, name_input)

ft.app(target = main, view = ft.AppView.WEB_BROWSER)
