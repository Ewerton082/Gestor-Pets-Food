import customtkinter as ctk
from datetime import datetime
import win32print
import win32api
import os


class FirstScreen(ctk.CTk):

    def __init__(self):
        super().__init__()

        def imprimir_com():
            val = {"dono": self.dono_inp.get(), "telefone": self.telefone_inp.get(), "pet": self.pet_inp.get(),
                   "posição": self.pos_inp.get(), "procedimento": self.procedimento_inp.get(),
                   "obs": self.obser_inp.get(), "hora": datetime.now().strftime("%H:%M"),
                   "data": datetime.now().strftime("%d/%m/%Y")
                   }

            text_imp = f"""
______________[ {val["data"]} ]______________
=====================================
        PetsFood [ {val["posição"]} ]         {val["hora"]}
=====================================
                                    
      Dono: {val["dono"]}                      
                                            
      Pet: {val["pet"]}
                                             
      Telefone: {val["telefone"]}
                                        
      Procedimeno: {val["procedimento"]}        
                                     
      Observações:
                                                
{val["obs"]}
=====================================    
"""
            try:
                os.makedirs('Impr_Com')

            finally:
                print(os.listdir())
                arquivo = open("Impr_com/Texto_Impresso.txt", 'w')
                arquivo.write(text_imp)
                arquivo.close()

                try:
                    lista = win32print.EnumPrinters(2)
                    impr = lista[6]
                    win32print.SetDefaultPrinter(impr[2])

                    diretorio = "C:/Users/waldo/python_projeto/Comandas/Impr_Com"
                    lista_arquivos = os.listdir(diretorio)

                    for arquivo in lista_arquivos:
                        win32api.ShellExecute(0, "print", arquivo, None, diretorio, 0)
                    print('tou na impressao')

                finally:

                    self.dono_inp.delete(0, 50)
                    self.dono_inp.focus()
                    self.telefone_inp.delete(0, 50)
                    self.pet_inp.delete(0, 50)
                    self.obser_inp.delete(0, 500)

        # Definições da tela

        self.title("Teste tela 1")
        self.geometry("530x500")
        self.resizable(height=False, width=False)

        # Parte do Header da página

        self.comanda = ctk.CTkButton(self, text="Comandas", font=('sans', 20), width=170)
        self.comanda.grid(row=0, column=0, padx=3, pady=(10, 0))

        self.planos = ctk.CTkButton(self, text="Funções futuras", font=('sans', 20), width=170)
        self.planos.grid(row=0, column=1, padx=3, pady=(10, 0))

        self.devedores = ctk.CTkButton(self, text="Funções futuras", font=('sans', 20), width=170)
        self.devedores.grid(row=0, column=2, padx=3, pady=(10, 0))

        # Labels do Formulario comandas

        self.form_frame = ctk.CTkFrame(self, height=480, corner_radius=25, border_width=2)
        self.form_frame.grid(row=1, column=0, columnspan=3, padx=25, pady=(30, 0), sticky='we')

        self.title = ctk.CTkLabel(self.form_frame, text="Imprimir comandas", font=('times', 33))
        self.title.grid(row=0, column=0, columnspan=3, sticky='we', padx=10, pady=(20, 0))

        self.dono_label = ctk.CTkLabel(self.form_frame, text="Tutor:", font=('times', 25, 'bold'))
        self.dono_label.grid(row=1, column=0, pady=(10, 0), padx=10)

        self.telefone_label = ctk.CTkLabel(self.form_frame, text="Telefone:", font=('times', 25, 'bold'))
        self.telefone_label.grid(row=2, column=0, pady=(10, 0), padx=10)

        self.pet_label = ctk.CTkLabel(self.form_frame, text="Pet:", font=('times', 25, 'bold'))
        self.pet_label.grid(row=3, column=0, pady=(10, 0), padx=10)

        self.pos_label = ctk.CTkLabel(self.form_frame, text="Posição:", font=('times', 25, 'bold'))
        self.pos_label.grid(row=4, column=0, pady=(10, 0), padx=10)

        self.procedimento_label = ctk.CTkLabel(self.form_frame, text="Serviço:", font=('times', 25, 'bold'))
        self.procedimento_label.grid(row=5, column=0, pady=(10, 0))

        self.obser_label = ctk.CTkLabel(self.form_frame, text="↡ Observações ↡", font=('times', 25, 'bold'))
        self.obser_label.grid(row=6, column=0, columnspan=2, pady=(10, 0), padx=10, sticky='we')

        # inputs do form comandas

        self.dono_inp = ctk.CTkEntry(self.form_frame, placeholder_text='Nome do dono', font=('sans', 20), width=200,
                                     border_width=1, border_color='black', corner_radius=5, )
        self.dono_inp.grid(row=1, column=1, pady=(10, 0))

        self.telefone_inp = ctk.CTkEntry(self.form_frame, placeholder_text='Número de telefone', font=('sans', 20),
                                         width=200, border_width=1, border_color='black', corner_radius=5, )
        self.telefone_inp.grid(row=2, column=1, pady=(10, 0))

        self.pet_inp = ctk.CTkEntry(self.form_frame, placeholder_text='Nome do pet', font=('sans', 20),
                                    width=200, border_width=1, border_color='black', corner_radius=5, )
        self.pet_inp.grid(row=3, column=1, pady=(10, 0))

        pos_list = ['1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º', '11º', '12º', '13º', '14º', '15º',
                    '16º', '17º', '18º', '19º', '20º', '21º', '22º', '23º', '24º', '25º']
        self.pos_inp = ctk.CTkComboBox(self.form_frame, font=('sans', 20), width=200, button_color='light blue',
                                       border_color='light blue', border_width=2, values=pos_list,
                                       justify='center', dropdown_font=('sans', 10, 'bold'),
                                       dropdown_hover_color='light blue')
        self.pos_inp.grid(row=4, column=1, pady=(10, 0), padx=5)

        proc_list = ['Banho e Higiênica', 'Tosa Padrão 7', 'Tosa Padrão 10',
                     'Tosa Completa 7', 'Tosa Completa 10', 'Tosa Bebê']

        self.procedimento_inp = ctk.CTkComboBox(self.form_frame, font=('sans', 14), width=200,
                                                button_color='light blue', border_color='light blue',
                                                border_width=2, values=proc_list,
                                                justify='center', dropdown_font=('sans', 10, 'bold'),
                                                dropdown_hover_color='light blue')
        self.procedimento_inp.grid(row=5, column=1, pady=(10, 0))

        self.obser_inp = ctk.CTkEntry(self.form_frame, font=('sans', 20), border_width=1, border_color='black',
                                      corner_radius=10, placeholder_text="Mais Alguma Informação?", width=450,
                                      height=35,
                                      justify='center')
        self.obser_inp.grid(row=7, column=0, columnspan=2, sticky='we', padx=10, pady=(5, 10))

        # botão imprimir

        self.imprimir = ctk.CTkButton(self.form_frame, text="Imprimir Comanda", font=('sans', 20, 'bold'), width=200,
                                      height=35, command=imprimir_com)
        self.imprimir.grid(row=8, column=0, columnspan=2, pady=(5, 15))


app = FirstScreen()

app.mainloop()
