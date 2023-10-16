import tkinter as tk
from tkinter import ttk

# Calcular os parâmetros do PID
def calcular_pid():
    theta = float(theta_var.get())
    T = float(T_var.get())
    K = float(K_var.get())
    setpoint = float(setpoint_var.get())

    # Cálculos dos parâmetros PID
    kc_chr = 0.95 * T / (K * theta)
    ti_chr = 1.357 * T
    td_chr = 0.473 * theta

    cc_kc = ((1 / K) * (T / theta)) * ((4 / 3) + ((1 / 4) * (theta / T)))
    cc_ti = theta * ((32 + (6 * (theta / T))) / (13 + (8 * (theta / T))))
    cc_td = theta * (4 / (11 + 2 * (theta / T)))

    # Limpar a tabela
    for row in resultado_tree.get_children():
        resultado_tree.delete(row)

    # Inserir os resultados na tabela
    resultado_tree.insert('', 'end', values=('PID do CHR', kc_chr, ti_chr, td_chr))
    resultado_tree.insert('', 'end', values=('PID do Cohen-Coon', cc_kc, cc_ti, cc_td))

# Cria a janela principal
root = tk.Tk()
root.title("Cáclculo PID")

root.configure(bg='navy')


style = ttk.Style()


style.configure('TButton', font=('Helvetica', 12))
style.configure('TButton', padding=6)


style.configure('TLabel', font=('Helvetica', 12))
style.configure('TLabel', padding=6)


style.configure('TEntry', font=('Helvetica', 12))
style.configure('TEntry', padding=6)


frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)


labels = ['Theta (θ):', 'T:', 'K:', 'Setpoint:']
entries = []
entry_vars = []

for i, label in enumerate(labels):
    entry_label = ttk.Label(frame, text=label)
    entry_label.grid(row=i, column=0, sticky='e')
    entry_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=entry_var)
    entry.grid(row=i, column=1)
    entries.append(entry)
    entry_vars.append(entry_var)

theta_var, T_var, K_var, setpoint_var = entry_vars

# Botão para calcular
calcular_button = ttk.Button(frame, text="Calcular", command=calcular_pid)
calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

#Tabela para exibir os resultados
resultado_tree = ttk.Treeview(root, columns=('1', '2', '3', '4'), show='headings')
resultado_tree.heading('1', text='Método')
resultado_tree.heading('2', text='Kp/Kc')
resultado_tree.heading('3', text='Ki/Ti')
resultado_tree.heading('4', text='Kd/Td')
resultado_tree.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
#codigo so mostra os valores das variaveis
#Crie uma interface que permita com que o usuário entre com os dados os parâmetros do PID e do Setpoint.
