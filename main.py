from tkinter import *
from random import *

root = Tk()
root.title("Генератор паролей")
root.geometry("350x300")



all_symbols = [
    "@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "№", "`", "/", "[", "]", "?", ",", ">", "<", "-", "+", "="
]

all_bykv1 = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

all_bykv2 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

all_numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

all_space = [
    # Пробел
    ' '
]


# def number_in_password():
#     print("Hello")





spinbox = Spinbox(from_=1.0, to=100.0)
spinbox.pack(anchor=NW)


all_symbols = IntVar()
  
all_symbols_checkbutton = Checkbutton(text="Включить символы", variable=all_symbols)
all_symbols_checkbutton.pack(padx=6, pady=6, anchor=NW)

all_bykv1 = IntVar()
  
all_bykv1_checkbutton = Checkbutton(text="Включить заглавные буквы", variable=all_bykv1)
all_bykv1_checkbutton.pack(padx=6, pady=6, anchor=NW)

all_bykv2 = IntVar()
  
all_bykv2_checkbutton = Checkbutton(text="Включить строчные буквы", variable=all_bykv2)
all_bykv2_checkbutton.pack(padx=6, pady=6, anchor=NW)

all_numbers = IntVar()
  
all_numbers_checkbutton = Checkbutton(text="Включить цифры", variable=all_numbers)
all_numbers_checkbutton.pack(padx=6, pady=6, anchor=NW)

all_space = IntVar()
  
all_space_checkbutton = Checkbutton(text="Включить пробел", variable=all_space)
all_space_checkbutton.pack(padx=6, pady=6, anchor=NW)









textbox = Entry(root, font=("Arial", 16))
textbox.pack()
# buttonFrame = Frame(root)
# textbox.delete("1.0", END)
btn = Button(text="Сгенерировать")
btn.pack()




root.mainloop()
