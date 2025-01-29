import customtkinter as ctk
from datetime import datetime
import os
import win32print
import win32api
from tkcalendar import DateEntry
from tkinter.ttk import Treeview
import sqlite3
import pyperclip

# Conectar Banco de Dados
banco = sqlite3.connect("Clientes_Pet.db")
Cursor = banco.cursor()
BD_COMMAND = "SELECT * FROM Clientes_Pet WHERE Data = ?"

banco.execute('''CREATE TABLE IF NOT EXISTS Clientes_PET(
                  Data TEXT,
                  Posicao TEXT,
                  Dono TEXT,
                  Número TEXT,
                  Pet TEXT,
                  Procedimento TEXT
                  )''')


def imprimir(QTD):
    lista = win32print.EnumPrinters(2)
    impr = lista[6]
    win32print.SetDefaultPrinter(impr[2])

    diretorio = "C:/Users/waldo/ComandasPet/Comandas"
    lista_arquivos = os.listdir(diretorio)

    for i in range(0, QTD, 1):
        for arquivo in lista_arquivos:
            win32api.ShellExecute(0, "print", arquivo, None, diretorio, 0)


def ImpresBanho():
    data_ban = {"client": client_entry.get(), "number": number_entry.get(), "pet": pet_entry.get(),
                "position": position_entry.get(), "process": procediment_entry.get(),
                "obs": obs_entry.get('0.0', 'end'),
                "date": datetime.now().strftime("%d/%m/%Y"), "hour": datetime.now().strftime("%H:%M")}
    text_imp_ban = f"""
____________[ {data_ban["date"]} ]___________
=====================================
    PetsFood [ {data_ban["position"]} ]        {data_ban["hour"]}
=====================================

        Dono: {data_ban["client"]}                      

        Pet: {data_ban["pet"]}

        Telefone: {data_ban["number"]}

        Procedimeno: {data_ban["process"]}        

        Observações:

    {data_ban["obs"]}
=====================================    
    """

    Cursor.execute(f"""INSERT INTO Clientes_PET VALUES('{datetime.now().strftime("%Y-%m-%d")}',
                    '{data_ban["position"]}', '{data_ban["client"]}', '{data_ban["number"]}',
                '{data_ban["pet"]}', '{data_ban["process"]}') """)
    banco.commit()


    try:
        os.makedirs("Comandas")

    except:

        arquivo = open("Comandas/text_copy.txt", 'w')
        arquivo.write(text_imp_ban)
        arquivo.close()

        try:
            imprimir(1)

        finally:

            client_entry.delete(0, 50)
            client_entry.focus()
            number_entry.delete(0, 50)
            pet_entry.delete(0, 50)
            obs_entry.delete("0.0", 'end')


def ImpresEntrega():
    try:
        data_entr = {"client": clientdelivery_entry.get(), "number": numberdelivery_entry.get(),
                     "adress": adress_entry.get(),
                     "items": items_entry.get(), "value": round(int(value_entry.get()), 2), "payment": pag_var.get(),
                     "obs": obsdelivery_entry.get()}

    except:
        data_entr = {"client": clientdelivery_entry.get(), "number": numberdelivery_entry.get(),
                     "adress": adress_entry.get(),
                     "items": items_entry.get(), "value": value_entry.get(), "payment": pag_var.get(),
                     "obs": obsdelivery_entry.get()}
    finally:

        data_entr["items"] = data_entr["items"].replace('|', "\n")
        """if data_entr["items"].count("|") >= 1:
            sep_item_list = data_entr["items"].split("|")
            printed_text = ""

            for item in sep_item_list:
                printed_text =  printed_text + item + "     \n"

            data_entr["items"] = printed_text"""


    text_imp_ent = f"""
_______Pet's Food - Graciliano
=====================================
                Dados
                
    Nome: {data_entr['client']}
    Número: {data_entr['number']}
    Endereço: {data_entr['adress']}
=====================================
                Pedido
            
 {data_entr["items"]}
    
=====================================
    Valor: R$ {data_entr["value"]}  Status: {data_entr["payment"]}
=====================================
    OBSERVAÇÔES:

    {data_entr["obs"]}
                            
    """

    try:
        os.makedirs("Comandas")

    except:
        pyperclip.copy(text_imp_ent)
        arquivo = open("Comandas/text_copy.txt", 'w')
        arquivo.write(text_imp_ent)
        arquivo.close()

        try:
            imprimir(2)

        finally:

            clientdelivery_entry.delete(0, 50)
            clientdelivery_entry.focus()
            numberdelivery_entry.delete(0, 50)
            adress_entry.delete(0, 50)
            items_entry.delete(0, 500)
            value_entry.delete(0, 50)
            obsdelivery_entry.delete(0, 100)


def datefilter():

    for item in pets_table.get_children():
        pets_table.delete(item)

    date_today = date_filter_entry.get_date()
    for data in Cursor.execute(BD_COMMAND, (date_today,)):
        pets_table.delete()
        real_data = [data[1], data[2], data[3], data[4], data[5], ]
        pets_table.insert(parent="", index=0, values=real_data)


# Definindo Configurações e Alguns Detalhes do Aplicativo

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("370x515")
app.resizable(False, False)
app.title(f"Pets Food  |  {datetime.now().strftime('%d/%m/%Y')}")
app.iconbitmap("icon.ico")

# Fim de Bloco

# Base da Tela, onde vai ficar nosso TabView e titulo

title = ctk.CTkLabel(app, text="Pets Food", font=("Times", 36, "bold"), width=350, height=35)
title.grid(row=1, column=1)

tabview = ctk.CTkTabview(app, width=365, height=400, corner_radius=15, border_width=2
                         , fg_color="#c4c2c2", segmented_button_fg_color="grey", )
tabview.grid(row=2, column=1, padx=2)
tabview.add("Pet Shop")
tabview.add("Diario")
tabview.add("Entregas")

# Fim de Bloco

# Tela do banho e Tosa

position_list = [
    '1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º',
    '11º', '12º', '13º', '14º', '15º', '16º', '17º', '18º', '19º', '20º',
    '21º', '22º', '23º', '24º', '25º'
]

procediment_list = [
    'Banho e Higiênica', 'Tosa Padrão 7', 'Tosa Padrão 10',
    'Tosa Completa 7', 'Tosa Completa 10', 'Tosa Bebê'
]

client_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=120, font=("Times", 23, "bold"), text="Dono:")
client_text.grid(row=0, column=0, pady=3)
client_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Nome do Dono", fg_color="white",
                            border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
client_entry.grid(row=0, column=1, pady=3)

number_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=120, font=("Times", 23, "bold"), text="Telefone:")
number_text.grid(row=1, column=0, pady=3)
number_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Num. telefone", fg_color="white",
                            border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
number_entry.grid(row=1, column=1, pady=3)

pet_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=120, font=("Times", 23, "bold"), text="Pet:")
pet_text.grid(row=2, column=0, pady=3)
pet_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Nome do Pet", fg_color="white",
                         border_color="black",
                         border_width=2, corner_radius=8, font=("Times", 18))
pet_entry.grid(row=2, column=1, pady=3)

position_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=120, font=("Times", 23, "bold"), text="Ordem:")
position_text.grid(row=3, column=0, pady=3)
position_entry = ctk.CTkComboBox(tabview.tab("Pet Shop"), width=150, fg_color="white", border_color="black",
                                 border_width=2, corner_radius=8, values=position_list, font=("Times", 18),
                                 button_color="#44acf5",
                                 button_hover_color="#318bc6", dropdown_hover_color="#7bc2f2", justify="center",
                                 dropdown_font=("Times", 10, "bold"))
position_entry.grid(row=3, column=1, pady=3)

procediment_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=120, font=("Times", 23, "bold"), text="Processo:")
procediment_text.grid(row=4, column=0, pady=3)
procediment_entry = ctk.CTkComboBox(tabview.tab("Pet Shop"), width=150, fg_color="white", border_color="black",
                                    border_width=2, corner_radius=8, values=procediment_list, font=("Times", 15),
                                    button_color="#44acf5",
                                    button_hover_color="#318bc6", dropdown_hover_color="#7bc2f2", justify="center",
                                    dropdown_font=("Times", 10, "bold"))
procediment_entry.grid(row=4, column=1, pady=3)

obs_text = ctk.CTkLabel(tabview.tab("Pet Shop"), width=270, font=("Times", 23, "bold"), text="Observações Gerais:")
obs_text.grid(row=5, column=0, pady=7, columnspan=2, padx=25)
obs_entry = ctk.CTkTextbox(tabview.tab("Pet Shop"), width=290, height=55, fg_color="white", border_color="black",
                           border_width=2, corner_radius=8, font=("Times", 16))
obs_entry.grid(row=6, column=0, pady=3, columnspan=2)

submit_buttom = ctk.CTkButton(tabview.tab("Pet Shop"), width=290, corner_radius=10, border_width=2,
                              font=("Times", 24, "bold"),
                              text="Imprimir Comanda", command=ImpresBanho)
submit_buttom.grid(row=7, column=0, columnspan=2, pady=7)

# Fim do Bloco

# Tela Entregas

clientdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"), width=120, font=("Times", 23, "bold"), text="Cliente:")
clientdelivery_text.grid(row=0, column=0, pady=3)
clientdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="Cliente", fg_color="white",
                                    border_color="black",
                                    border_width=2, corner_radius=8, font=("Times", 18))
clientdelivery_entry.grid(row=0, column=1, pady=3)

numberdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"), width=120, font=("Times", 23, "bold"), text="Telefone:")
numberdelivery_text.grid(row=1, column=0, pady=3)
numberdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="Num. telefone",
                                    fg_color="white", border_color="black",
                                    border_width=2, corner_radius=8, font=("Times", 18))
numberdelivery_entry.grid(row=1, column=1, pady=3)

adress_text = ctk.CTkLabel(tabview.tab("Entregas"), width=270, font=("Times", 23, "bold"), text="Endereço:")
adress_text.grid(row=2, column=0, pady=4, columnspan=2)
adress_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=290, height=20, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 14, "bold"),
                            placeholder_text="Endereço do Cliente")
adress_entry.grid(row=3, column=0, pady=3, columnspan=2)

items_text = ctk.CTkLabel(tabview.tab("Entregas"), width=270, font=("Times", 23, "bold"), text="Produtos Comprados:")
items_text.grid(row=4, column=0, pady=4, columnspan=2)
items_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=290, height=25, fg_color="white", border_color="black",
                           border_width=2, corner_radius=8, font=("Times", 13, "bold"),
                           placeholder_text="Recomendo usar / ou | para melhor visualização")
items_entry.grid(row=5, column=0, pady=7, columnspan=2)

value_text = ctk.CTkLabel(tabview.tab("Entregas"), width=120, font=("Times", 23, "bold"), text="Valor Total:")
value_text.grid(row=6, column=0, pady=3)
value_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="R$:---,--", fg_color="white",
                           border_color="black",
                           border_width=2, corner_radius=8, font=("Times", 18))
value_entry.grid(row=6, column=1, pady=3)

pag_var = ctk.StringVar(value="----")
din_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Dinheiro", variable=pag_var, value="Dinheiro", width=50)
din_radio.grid(row=7, column=0, pady=8)
Pix_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Pix", variable=pag_var, value="Pix", width=50)
Pix_radio.grid(row=7, column=0, pady=8, columnspan=2)
din_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Cartão", variable=pag_var, value="Cartão", width=50)
din_radio.grid(row=7, column=1, pady=8)

obsdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"), width=120, font=("Times", 23, "bold"), text="Observações:")
obsdelivery_text.grid(row=8, column=0, columnspan=2)
obsdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=290, placeholder_text="Tem alguma informação a mais?",
                                 fg_color="white", border_color="black", border_width=2, corner_radius=8,
                                 font=("Times", 14, "bold"))
obsdelivery_entry.grid(row=9, column=0, columnspan=2)

submitdelivery_buttom = ctk.CTkButton(tabview.tab("Entregas"), width=290, corner_radius=10, border_width=2,
                                      font=("Times", 24, "bold"),
                                      text="Realizar Entrega", command=ImpresEntrega)
submitdelivery_buttom.grid(row=10, column=0, columnspan=2, pady=15)

# Tela Pets Diarios

date_filter_entry = DateEntry(tabview.tab("Diario"), date_pattern="d-m-y", cursor="hand2", fg_color="white",
                              border_color="black", border_width=2, corner_radius=8, font=("Times", 13, "bold"), )
date_filter_entry.grid(row=0, column=0, padx=4, pady=6)

date_filter_submit = ctk.CTkButton(tabview.tab("Diario"), width=120, corner_radius=10, border_width=2,
                                   font=("Times", 17, "bold"), text="Filtrar por data", command=datefilter)
date_filter_submit.grid(row=0, column=1, padx=10, pady=6)

pets_table = Treeview(tabview.tab("Diario"), columns=["Posição", "Dono", "Telefone", "Pet", "Procedimento"],
                      show="headings",)
pets_table.grid(row=1, column=0, columnspan=2, pady=4)

pets_table.column("Posição", width=20)
pets_table.heading("Posição", text="nº")

pets_table.column("Dono", width=60)
pets_table.heading("Dono", text="Dono")

pets_table.column("Telefone", width=75)
pets_table.heading("Telefone", text="Celular")

pets_table.column("Pet", width=70)
pets_table.heading("Pet", text="Pet")

pets_table.column("Procedimento", width=110)
pets_table.heading("Procedimento", text="Procedimento")

date_today = datetime.now().strftime("%Y-%m-%d")
for data in Cursor.execute(BD_COMMAND, (date_today,)):
    real_data = [data[1], data[2], data[3], data[4], data[5],]
    pets_table.insert(parent="", index=0, values=real_data)

app.mainloop()
