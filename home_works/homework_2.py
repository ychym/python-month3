import flet as ft

def main(page: ft.Page):
   
   def age(e):    
    if age_input.value.isdigit():#on butun sandar gana->TRUE
      
      if int(age_input.value) >= 18:
        text_hello.value = f"Доступ разрешен!"
        text_hello.color = ft.Colors.GREEN
      else:   
        text_hello.value = f"Доступ запрещен!"
        text_hello.color = ft.Colors.RED  

    else:
      text_hello.value = f"Введите корректный возраст!"
      text_hello.color = ft.Colors.YELLOW     
    
    age_input.value = ""  

   text_hello = ft.Text("Hi")
   age_input = ft.TextField(label = "Enter your age")
   btn = ft.FilledButton("SEND", on_click = age)

   page.add(text_hello, age_input, btn)

ft.app(target = main, view = ft.AppView.WEB_BROWSER)