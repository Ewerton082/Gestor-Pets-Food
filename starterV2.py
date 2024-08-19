import customtkinter as ctk

def ImpresBanho():
    print("Tentando Imprimir Banho e Tosa")


def ImpresEntrega():
    print("Tentando Realizar Nossas Entregas")

### Definindo Configurações e Alguns Detalhes do App ###
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app =  ctk.CTk()
app.geometry("350x450")
app.resizable(False, False)
app.title("Pets Food")

### Fim de Bloco ###

### Base da Tela, onde vai ficar nosso TabView e titulo ###

title = ctk.CTkLabel(app, text="Pets Food", font=("Times", 36, "bold"), width=350, height=35)
title.grid(row=1, column=1)

tabview = ctk.CTkTabview(app, width=325, height=400, corner_radius=15, border_width=2
                         ,fg_color="#c4c2c2", segmented_button_fg_color="grey",)
tabview.grid(row=2, column=1)
tabview.add("Pet Shop")
tabview.add("Entregas")

### Fim de Bloco ###

### Tela do banho e Tosa ###

position_list = [
            '1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º',
            '11º', '12º', '13º', '14º', '15º', '16º', '17º', '18º', '19º', '20º',
            '21º', '22º', '23º', '24º', '25º'
            ]

procediment_list = [
            'Banho e Higiênica', 'Tosa Padrão 7', 'Tosa Padrão 10',
            'Tosa Completa 7', 'Tosa Completa 10', 'Tosa Bebê'
            ]

client_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=120 , font=("Times", 23, "bold"), text="Dono:")
client_text.grid(row=0, column=0, pady=3)
client_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Nome do Dono", fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
client_entry.grid(row=0, column=1, pady=3)

number_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=120 , font=("Times", 23, "bold"), text="Telefone:")
number_text.grid(row=1, column=0, pady=3)
number_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Num. telefone", fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
number_entry.grid(row=1, column=1, pady=3)

pet_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=120 , font=("Times", 23, "bold"), text="Pet:")
pet_text.grid(row=2, column=0, pady=3)
pet_entry = ctk.CTkEntry(tabview.tab("Pet Shop"), width=150, placeholder_text="Nome do Pet", fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
pet_entry.grid(row=2, column=1, pady=3)

position_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=120 , font=("Times", 23, "bold"), text="Ordem:")
position_text.grid(row=3, column=0, pady=3)
position_entry = ctk.CTkComboBox(tabview.tab("Pet Shop"), width=150, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, values= position_list,  font=("Times", 18),button_color="#44acf5",
                            button_hover_color="#318bc6", dropdown_hover_color="#7bc2f2", justify="center", dropdown_font=("Times", 10, "bold") )
position_entry.grid(row=3, column=1, pady=3)

procediment_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=120 , font=("Times", 23, "bold"), text="Processo:")
procediment_text.grid(row=4, column=0, pady=3)
procediment_entry = ctk.CTkComboBox(tabview.tab("Pet Shop"), width=150, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, values= procediment_list,  font=("Times", 15),button_color="#44acf5",
                            button_hover_color="#318bc6", dropdown_hover_color="#7bc2f2", justify="center", dropdown_font=("Times", 10, "bold") )
procediment_entry.grid(row=4, column=1, pady=3)

obs_text = ctk.CTkLabel(tabview.tab("Pet Shop"),width=270 , font=("Times", 23, "bold"), text="Observações Gerais:")
obs_text.grid(row=5, column=0, pady=7, columnspan=2)
obs_entry = ctk.CTkTextbox(tabview.tab("Pet Shop"), width=290, height=55, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 16))
obs_entry.grid(row=6, column=0, pady=3, columnspan=2)

submit_buttom = ctk.CTkButton(tabview.tab("Pet Shop"), width=290, corner_radius=10, border_width=2, font=("Times", 24, "bold"),
                              text="Imprimir Comanda", command=ImpresBanho)
submit_buttom.grid(row=7, column=0, columnspan=2, pady=15)

### Fim do Bloco ###

### Tela Entregas ###

clientdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"),width=120 , font=("Times", 23, "bold"), text="Cliente:")
clientdelivery_text.grid(row=0, column=0, pady=3)
clientdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="Cliente", fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
clientdelivery_entry.grid(row=0, column=1, pady=3)

numberdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"),width=120 , font=("Times", 23, "bold"), text="Telefone:")
numberdelivery_text.grid(row=1, column=0, pady=3)
numberdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="Num. telefone", fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
numberdelivery_entry.grid(row=1, column=1, pady=3)

adress_text = ctk.CTkLabel(tabview.tab("Entregas"),width=270 , font=("Times", 23, "bold"), text="Endereço:")
adress_text.grid(row=2, column=0, pady=4, columnspan=2)
adress_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=290, height=20, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 14, "bold"),placeholder_text="Endereço do Cliente")
adress_entry.grid(row=3, column=0, pady=3, columnspan=2)

items_text = ctk.CTkLabel(tabview.tab("Entregas"),width=270 , font=("Times", 23, "bold"), text="Produtos Comprados:")
items_text.grid(row=4, column=0, pady=4, columnspan=2)
items_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=290, height=25, fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 13, "bold"), placeholder_text="Recomendo usar / ou | para melhor visualização")
items_entry.grid(row=5, column=0, pady=7, columnspan=2)

value_text = ctk.CTkLabel(tabview.tab("Entregas"),width=120 , font=("Times", 23, "bold"), text="Valor Total:")
value_text.grid(row=6, column=0, pady=3)
value_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="R$:---,--",fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 18))
value_entry.grid(row=6, column=1, pady=3)

pag_var = ctk.StringVar(value="----")
din_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Dinheiro", variable=pag_var, value="Dinheiro", width=50)
din_radio.grid(row=7, column=0, pady=8)
Pix_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Pix", variable=pag_var, value="Pix", width=50)
Pix_radio.grid(row=7, column=0, pady=8, columnspan=2)
din_radio = ctk.CTkRadioButton(tabview.tab("Entregas"), text="Cartão", variable=pag_var, value="Cartão", width=50)
din_radio.grid(row=7, column=1, pady=8)

submitdelivery_buttom = ctk.CTkButton(tabview.tab("Entregas"), width=290, corner_radius=10, border_width=2, font=("Times", 24, "bold"),
                              text="Realizar Entrega", command=ImpresEntrega)
submitdelivery_buttom.grid(row=8, column=0, columnspan=2, pady=15)

### Fim do Bloco ###


"""
obsdelivery_text = ctk.CTkLabel(tabview.tab("Entregas"),width=120, font=("Times", 23, "bold"), text="Observações:")
obsdelivery_text.grid(row=8, column=0)
obsdelivery_entry = ctk.CTkEntry(tabview.tab("Entregas"), width=150, placeholder_text="Algo pra anotar?",fg_color="white", border_color="black",
                            border_width=2, corner_radius=8, font=("Times", 14, "bold"))
obsdelivery_entry.grid(row=8, column=1)
"""



app.mainloop()