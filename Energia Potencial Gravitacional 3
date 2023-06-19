import tkinter as tk
# Definición de constantes
g = 9.8; xm = 0 ;xm2 = 100; ym = 0; ym2 = 100; xh = 50; yh = 40; xh2 = 120; yh2 = 45 

# Función para calcular la energía potencial gravitacional
def calcular_energia_potencial():
    masa = float(masa_entry.get())
    altura = float(altura_entry.get())
    energia_potencial = masa * g * altura
    resultado_label.config(text="La energía potencial gravitacional es: {:.2f} Joules".format(energia_potencial))

# Funcion para poder actualizar la masa en el grafico
def actualizarM():
    Mas = masa_entry.get()
    mostrarM = "Masa = {0} Kg".format(Mas)
    canv_cuad.itemconfig(text1, text=mostrarM)

def actualizarH():
    H = altura_entry.get()
    mostrarH = "Altura = {0} M".format(H)
    canv_H.itemconfig(text1, text=mostrarH)

# Configuración de la ventana
ventana = tk.Tk()
ventana.geometry("450x350")
ventana.configure(bg="#06B6AE")
ventana.title("Cálculo de Energía Potencial Gravitacional")

# Etiqueta y entrada para la masa del objeto
masa_label = tk.Label(ventana, bg="#06B6AE", text="Masa del objeto (kg):")
masa_label.place(x=10, y=20)
masa_entry = tk.Entry(ventana)
masa_entry.place(x=10 , y=42)

# Etiqueta y entrada para la altura del objeto
altura_label = tk.Label(ventana, bg="#06B6AE", text="Altura del objeto (metros):")
altura_label.place(x=6, y=65)
altura_entry = tk.Entry(ventana)
altura_entry.place(x=10, y=87)

# Botón para calcular la energía potencial gravitacional
calcular_button = tk.Button(ventana, text="Calcular", font=("Arial", 11), command=calcular_energia_potencial)
calcular_button.place(x=40 , y= 115)

# Creacion de grafico que simula la masa
canv_cuad = tk.Canvas(ventana, width=100, height=100, bg="#06B6AE", background="#06B6AE", highlightbackground="#06B6AE")
canv_cuad.place(x= 230, y= 20)
cuadrado = canv_cuad.create_rectangle(xm,ym,xm2,ym2, fill="#00FFC1", outline="black")
 
# Texto que representa la Masa 
x_centro = (xm + xm2) // 2
y_centro = (ym + ym2) // 2
inicial = "Masa = ?"
text1 = canv_cuad.create_text(x_centro, y_centro, text=inicial, font=("Arial", 10))

#Botón que actualiza la masa en el grafico
boton_actualizar = tk.Button(ventana, text="Actualizar Masa", command=actualizarM)
boton_actualizar.place(x=25, y=160)

# Creacion de grafico que simula la altura
canv_H = tk.Canvas(ventana, width=200, height=100, bg="#06B6AE", highlightbackground="#06B6AE")
canv_H.place(x = 230, y =123 )
canv_H.create_text(xh, yh, text="}",fill="#007458", font=("Arial", 70))
inicial2 = "Altura = ?"
text2 = canv_H.create_text(xh2, yh2,text=inicial2, font=("Arial", 10))

#Botón que actualiza la altura en el grafico
boton_actualizar = tk.Button(ventana, text="Actualizar altura", command=actualizarH)
boton_actualizar.place(x=25, y=200)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="",bg="#06B6AE")
resultado_label.place(x=150, y=250)

# Ejecutar la interfaz gráfica
ventana.mainloop()                        
