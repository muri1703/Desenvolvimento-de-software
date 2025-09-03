import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------
# CLASSES
# -----------------------

class Pessoa:
    def __init__(self, nome, idade, cpf, email, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, email, telefone, plano_saude=None):
        super().__init__(nome, idade, cpf, email, telefone)
        self.plano_saude = plano_saude

class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, email, telefone, crm, especialidade):
        super().__init__(nome, idade, cpf, email, telefone)
        self.crm = crm
        self.especialidade = especialidade

class Consulta:
    def __init__(self, paciente, medico, data, hora):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.hora = hora

# -----------------------
# LISTAS (banco em memória)
# -----------------------
pacientes = []
medicos = []
consultas = []

# -----------------------
# FUNÇÕES
# -----------------------

def cadastrar_paciente():
    nome = entry_nome_p.get()
    idade = entry_idade_p.get()
    cpf = entry_cpf_p.get()
    email = entry_email_p.get()
    tel = entry_tel_p.get()
    plano = entry_plano_p.get()

    if not nome or not idade or not cpf:
        messagebox.showwarning("Aviso", "Preencha os campos obrigatórios!")
        return

    p = Paciente(nome, idade, cpf, email, tel, plano)
    pacientes.append(p)
    lista_pacientes.insert("", "end", values=(p.nome, p.idade, p.cpf, p.email, p.telefone, p.plano_saude))

    # atualiza combobox paciente da aba consultas
    combo_paciente['values'] = [pac.nome for pac in pacientes]

    # limpa campos
    entry_nome_p.delete(0, tk.END)
    entry_idade_p.delete(0, tk.END)
    entry_cpf_p.delete(0, tk.END)
    entry_email_p.delete(0, tk.END)
    entry_tel_p.delete(0, tk.END)
    entry_plano_p.delete(0, tk.END)

def cadastrar_medico():
    nome = entry_nome_m.get()
    idade = entry_idade_m.get()
    cpf = entry_cpf_m.get()
    email = entry_email_m.get()
    tel = entry_tel_m.get()
    crm = entry_crm_m.get()
    esp = entry_esp_m.get()

    if not nome or not idade or not cpf or not crm:
        messagebox.showwarning("Aviso", "Preencha os campos obrigatórios!")
        return

    m = Medico(nome, idade, cpf, email, tel, crm, esp)
    medicos.append(m)
    lista_medicos.insert("", "end", values=(m.nome, m.idade, m.cpf, m.email, m.telefone, m.crm, m.especialidade))

    # atualiza combobox medico da aba consultas
    combo_medico['values'] = [med.nome for med in medicos]

    # limpa campos
    entry_nome_m.delete(0, tk.END)
    entry_idade_m.delete(0, tk.END)
    entry_cpf_m.delete(0, tk.END)
    entry_email_m.delete(0, tk.END)
    entry_tel_m.delete(0, tk.END)
    entry_crm_m.delete(0, tk.END)
    entry_esp_m.delete(0, tk.END)

def agendar_consulta():
    paciente_nome = combo_paciente.get()
    medico_nome = combo_medico.get()
    data = entry_data.get()
    hora = entry_hora.get()

    if not paciente_nome or not medico_nome or not data or not hora:
        messagebox.showwarning("Aviso", "Preencha todos os campos da consulta!")
        return

    # encontra objetos
    paciente = next((p for p in pacientes if p.nome == paciente_nome), None)
    medico = next((m for m in medicos if m.nome == medico_nome), None)

    if not paciente or not medico:
        messagebox.showerror("Erro", "Paciente ou Médico inválido!")
        return

    c = Consulta(paciente, medico, data, hora)
    consultas.append(c)
    lista_consultas.insert("", "end", values=(c.paciente.nome, c.medico.nome, c.data, c.hora))

    # limpa campos
    combo_paciente.set("")
    combo_medico.set("")
    entry_data.delete(0, tk.END)
    entry_hora.delete(0, tk.END)

# -----------------------
# INTERFACE
# -----------------------

root = tk.Tk()
root.title("Sistema de Clínica")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# -----------------------
# ABA PACIENTES
# -----------------------
aba1 = ttk.Frame(notebook)
notebook.add(aba1, text="Pacientes")

ttk.Label(aba1, text="Nome:").grid(row=0, column=0)
entry_nome_p = ttk.Entry(aba1); entry_nome_p.grid(row=0, column=1)

ttk.Label(aba1, text="Idade:").grid(row=1, column=0)
entry_idade_p = ttk.Entry(aba1); entry_idade_p.grid(row=1, column=1)

ttk.Label(aba1, text="CPF:").grid(row=2, column=0)
entry_cpf_p = ttk.Entry(aba1); entry_cpf_p.grid(row=2, column=1)

ttk.Label(aba1, text="Email:").grid(row=3, column=0)
entry_email_p = ttk.Entry(aba1); entry_email_p.grid(row=3, column=1)

ttk.Label(aba1, text="Telefone:").grid(row=4, column=0)
entry_tel_p = ttk.Entry(aba1); entry_tel_p.grid(row=4, column=1)

ttk.Label(aba1, text="Plano de Saúde:").grid(row=5, column=0)
entry_plano_p = ttk.Entry(aba1); entry_plano_p.grid(row=5, column=1)

btn_add_p = ttk.Button(aba1, text="Cadastrar Paciente", command=cadastrar_paciente)
btn_add_p.grid(row=6, column=0, columnspan=2, pady=5)

lista_pacientes = ttk.Treeview(aba1, columns=("Nome","Idade","CPF","Email","Telefone","Plano"), show="headings")
for col in ("Nome","Idade","CPF","Email","Telefone","Plano"):
    lista_pacientes.heading(col, text=col)
lista_pacientes.grid(row=7, column=0, columnspan=2)

# -----------------------
# ABA MÉDICOS
# -----------------------
aba2 = ttk.Frame(notebook)
notebook.add(aba2, text="Médicos")

ttk.Label(aba2, text="Nome:").grid(row=0, column=0)
entry_nome_m = ttk.Entry(aba2); entry_nome_m.grid(row=0, column=1)

ttk.Label(aba2, text="Idade:").grid(row=1, column=0)
entry_idade_m = ttk.Entry(aba2); entry_idade_m.grid(row=1, column=1)

ttk.Label(aba2, text="CPF:").grid(row=2, column=0)
entry_cpf_m = ttk.Entry(aba2); entry_cpf_m.grid(row=2, column=1)

ttk.Label(aba2, text="Email:").grid(row=3, column=0)
entry_email_m = ttk.Entry(aba2); entry_email_m.grid(row=3, column=1)

ttk.Label(aba2, text="Telefone:").grid(row=4, column=0)
entry_tel_m = ttk.Entry(aba2); entry_tel_m.grid(row=4, column=1)

ttk.Label(aba2, text="CRM:").grid(row=5, column=0)
entry_crm_m = ttk.Entry(aba2); entry_crm_m.grid(row=5, column=1)

ttk.Label(aba2, text="Especialidade:").grid(row=6, column=0)
entry_esp_m = ttk.Entry(aba2); entry_esp_m.grid(row=6, column=1)

btn_add_m = ttk.Button(aba2, text="Cadastrar Médico", command=cadastrar_medico)
btn_add_m.grid(row=7, column=0, columnspan=2, pady=5)

lista_medicos = ttk.Treeview(aba2, columns=("Nome","Idade","CPF","Email","Telefone","CRM","Especialidade"), show="headings")
for col in ("Nome","Idade","CPF","Email","Telefone","CRM","Especialidade"):
    lista_medicos.heading(col, text=col)
lista_medicos.grid(row=8, column=0, columnspan=2)

# -----------------------
# ABA CONSULTAS
# -----------------------
aba3 = ttk.Frame(notebook)
notebook.add(aba3, text="Consultas")

ttk.Label(aba3, text="Paciente:").grid(row=0, column=0)
combo_paciente = ttk.Combobox(aba3, values=[p.nome for p in pacientes])
combo_paciente.grid(row=0, column=1)

ttk.Label(aba3, text="Médico:").grid(row=1, column=0)
combo_medico = ttk.Combobox(aba3, values=[m.nome for m in medicos])
combo_medico.grid(row=1, column=1)

ttk.Label(aba3, text="Data:").grid(row=2, column=0)
entry_data = ttk.Entry(aba3); entry_data.grid(row=2, column=1)

ttk.Label(aba3, text="Hora:").grid(row=3, column=0)
entry_hora = ttk.Entry(aba3); entry_hora.grid(row=3, column=1)

btn_agendar = ttk.Button(aba3, text="Agendar Consulta", command=agendar_consulta)
btn_agendar.grid(row=4, column=0, columnspan=2, pady=5)

lista_consultas = ttk.Treeview(aba3, columns=("Paciente","Médico","Data","Hora"), show="headings")
for col in ("Paciente","Médico","Data","Hora"):
    lista_consultas.heading(col, text=col)
lista_consultas.grid(row=5, column=0, columnspan=2)

# -----------------------
root.mainloop()
