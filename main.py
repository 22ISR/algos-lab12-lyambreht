# from tkinter import *
# from random import *


# root = Tk()
# root.title("Генератор паролей")
# root.geometry("350x300")



# symbols = [
#     "@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "№", "`", "/", "[", "]", "?", ",", ">", "<", "-", "+", "="
# ]

# letters = [
#     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

#     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
# ]

# numbers = [
#     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
# ]

# space = [
#     # Пробел
#     ' '
# ]




# def generate_password():
#     length = int(spinbox.get())
#     selected_chars = []

#     # amount_of_letters = length // 2
#     # amount_of_symbols = randint(1, amount_of_letters - 2)
#     # amount_of_numbers = length - amount_of_letters - amount_of_symbols
#     if symbols.get():
#         selected_chars.extend(symbols)
#     if letters.get():
#         selected_chars.extend(letters)
#     if numbers.get():
#         selected_chars.extend(numbers)
#     if space.get():
#         selected_chars.extend(space)

#     if not selected_chars:
#         textbox.delete(0, END)
#         textbox.insert(0, "Выберите хотя бы один выриант")
#         return
    
#     password = ''.join(choice(selected_chars) for _ in range(length))
#     textbox.delete(0, END)
#     textbox.insert(0, password)



# spinbox = Spinbox(root, from_=1, to=100, width=5)
# spinbox.pack(anchor=NW)

# symbols = IntVar()

# symbols_checkbutton = Checkbutton(text="Включить символы", variable=symbols)
# symbols_checkbutton.pack(padx=6, pady=6, anchor=NW)

# letters = IntVar()
  
# letters_checkbutton = Checkbutton(text="Включить буквы", variable=letters)
# letters_checkbutton.pack(padx=6, pady=6, anchor=NW)

# numbers = IntVar()
  
# numbers_checkbutton = Checkbutton(text="Включить цифры", variable=numbers)
# numbers_checkbutton.pack(padx=6, pady=6, anchor=NW)

# space = IntVar()
  
# space_checkbutton = Checkbutton(text="Включить пробел", variable=space)
# space_checkbutton.pack(padx=6, pady=6, anchor=NW)



# textbox = Entry(root, font=("Arial", 16))
# textbox.pack(pady=10)
# btn = Button(text="Сгенерировать", command=generate_password)
# btn.pack()




# root.mainloop()

from tkinter import *
from random import *

root = Tk()
root.title("Генератор паролей")
root.geometry("350x300")

# Списки символов
symbols_list = [
    "@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "№", "`", "/", "[", "]", "?", ",", ">", "<", "-", "+", "="
]

letters_list = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers_list = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

space_list = [' ']

def generate_password():
    length = int(spinbox.get())
    selected_chars = []
    
    # Добавляем выбранные символы в общий список
    if symbols_var.get():
        selected_chars.extend(symbols_list)
    if letters_var.get():
        selected_chars.extend(letters_list)
    if numbers_var.get():
        selected_chars.extend(numbers_list)
    if space_var.get():
        selected_chars.extend(space_list)
    
    # Проверяем, что хотя бы один вариант выбран
    if not selected_chars:
        textbox.delete(0, END)
        textbox.insert(0, "Выберите хотя бы один вариант")
        return
    
    # Генерируем пароль
    password = ''.join(choice(selected_chars) for _ in range(length))
    textbox.delete(0, END)
    textbox.insert(0, password)

# Элементы интерфейса
spinbox = Spinbox(root, from_=1, to=100, width=5)
spinbox.pack(anchor=NW)

# Переменные для чекбоксов
symbols_var = IntVar()
symbols_checkbutton = Checkbutton(text="Включить символы", variable=symbols_var)
symbols_checkbutton.pack(padx=6, pady=6, anchor=NW)

letters_var = IntVar()
letters_checkbutton = Checkbutton(text="Включить буквы", variable=letters_var)
letters_checkbutton.pack(padx=6, pady=6, anchor=NW)

numbers_var = IntVar()
numbers_checkbutton = Checkbutton(text="Включить цифры", variable=numbers_var)
numbers_checkbutton.pack(padx=6, pady=6, anchor=NW)

space_var = IntVar()
space_checkbutton = Checkbutton(text="Включить пробел", variable=space_var)
space_checkbutton.pack(padx=6, pady=6, anchor=NW)

# Поле для вывода пароля
textbox = Entry(root, font=("Arial", 16))
textbox.pack(pady=10)

# Кнопка генерации
btn = Button(text="Сгенерировать", command=generate_password)
btn.pack()

root.mainloop()




root.mainloop()
