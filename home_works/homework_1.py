import flet as ft

def main(page: ft.Page):
    c = 0
    def count(e): 
      nonlocal c #nonlocal - main negizgi function+(syrtky func) ozgormosun koldonuuga uruksat beret  
      c += 1
      text_hello.value = f"Basyldy:{c} jolu."
      
    text_hello = ft.Text("Hello, group 65-1!")    
    btn = ft.ElevatedButton('Enter', on_click = count)
    

    page.add(text_hello, btn)

ft.app(target = main)
#ft.app(target = main, view = ft.AppView.WEB_BROWSER)