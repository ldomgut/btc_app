import funciones
from tkinter import *
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = funciones.get_btc_historical_data()
max_price = max(df.price)
max_year = max(df.price.loc[df.time.dt.year == datetime.now().year])
min_year = min(df.price.loc[df.time.dt.year == datetime.now().year])
precio_btc = funciones.btc_price()
capitalization = df.market_cap.iloc[df.shape[0]-1]

# Iniciando gui
window = Tk()
window.geometry('350x250')
window.title("Bitcoin")
window.config()

# Menu de GUI
menu = Menu(window)
menu.add_command(label='Inicio')
window.config(menu=menu)

# funciones
def calculate():
    lbl = Label(window, text='{0:,}'.format(round(float(precio_btc)*float(txt.get()),2)), width=20, fg = "red")
    lbl.grid(column=4, row=1)
def show_price_chart():
    sns.lineplot(x="time", y="price",
                 data=df)


# ----------------LABELS Y BOTONES-------------------------
# Imagen
btc_image = PhotoImage(file="D:/luis/Desktop/Python/btc.png")
background_label = Label(window, image=btc_image)
background_label.grid(column=1, row=0)


# Tipo de cambio
lbl = Label(window, text="BTC/EUR" )
lbl.grid(column=0, row=0)
lbl = Label(window, text=precio_btc )
lbl.grid(column=0, row=1)

# Entrada de dato
txt = Entry(window, width = 10 )
txt.grid(column=1, row=1)

#Botones
btn = Button(window, text="Click Me", bg="black", fg="white", command=calculate)
btn.grid(column=3, row=1)
btn = Button(window, text="Price Chart", bg="black", fg="white", command=show_price_chart)
btn.grid(column=3, row=2)

#Datos
lbl = Label(window, text="Max" )
lbl.grid(column=0, row=3)
lbl = Label(window, text='{0:,}'.format(round(max_price,2)))
lbl.grid(column=1, row=3)
lbl = Label(window, text="Capitalization" )
lbl.grid(column=0, row=4)
lbl = Label(window, text='{0:,}'.format(int(capitalization/1000000))+ " Millions")
lbl.grid(column=1, row=4)
lbl = Label(window, text="Max " +str(datetime.now().year))
lbl.grid(column=0, row=5)
lbl = Label(window, text='{0:,}'.format(round(max_year,2)))
lbl.grid(column=1, row=5)
lbl = Label(window, text="Min " +str(datetime.now().year))
lbl.grid(column=0, row=6)
lbl = Label(window, text='{0:,}'.format(round(min_year,2)))
lbl.grid(column=1, row=6)

#hola

window.mainloop()