import tkinter as tk
# Definición de constantes
g = 9.8  # Aceleración debido a la gravedad en la Tierra, en m/s^2


# Función para calcular la energía potencial gravitacional
def calcular_energia_potencial():
    masa = float(masa_entry.get())
    altura = float(altura_entry.get())
    energia_potencial = masa * g * altura
    resultado_label.config(text="La energía potencial gravitacional es: {:.2f} Joules".format(energia_potencial))

# Configuración de la ventana
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.configure(bg="cyan")
ventana.title("Cálculo de Energía Potencial Gravitacional")

# Etiqueta y entrada para la masa del objeto
masa_label = tk.Label(ventana, bg="cyan", text="Masa del objeto (kg):")
masa_label.pack()
masa_entry = tk.Entry(ventana)
masa_entry.pack()

# Etiqueta y entrada para la altura del objeto
altura_label = tk.Label(ventana, bg="cyan", text="Altura del objeto (metros):")
altura_label.pack()
altura_entry = tk.Entry(ventana)
altura_entry.pack()

# Botón para calcular la energía potencial gravitacional
calcular_button = tk.Button(ventana, text="Calcular", command=calcular_energia_potencial)
calcular_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.configure(bg="cyan")
resultado_label.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()