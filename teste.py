import tkinter as tk 

def evaluate (event):
  result_label.config(text=str(eval(entry.pygame.event.get()))

root = tk.tk()
root.title("Calculadora simples")

entry = tk.Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()

result_label = tk.label(root, text="")
result_label.pack()

root.geometry("250x100")
root.mainloop()