import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

#CARREGAR O ARQUVO EXCEL COM AS QUESTÕES
df = pd.read_excel('questions.xlsx')
#PEGAR AS PERGUNTAS ALEATÓRIAMENTE
questions = df.sample(n=3).values.tolist()

#VARIAVEIS

score = 0
current_questions = 0

#funcao para exibir a prómixa pergunta
def display_questions():
    question, option1, option2, option3, option4, answe = questions[current_questions]
    questoes_label.config(text=question)
    opcao1_btn.config(text=option1,state=tk.NORMAL)
    opcao2_btn.config(text=option2,state=tk.NORMAL)
    opcao3_btn.config(text=option3,state=tk.NORMAL)
    opcao4_btn.config(text=option4,state=tk.NORMAL)


#CRIANDO A INTERFACE
janela = tk.Tk()
janela.title('PyQuiz')
janela.geometry("400x450")

#DEFININDO CORES DA INTERFACE
background_color = "#ECECEC"
text_color= "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('*Font','Arial')
#ICONE NA TELA
app_icon = PhotoImage(file="logo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

#COMOPENENTES DA INTERFACE
questoes_label = tk.Label(janela, text="",wraplength=380, bg=background_color, fg=text_color, font=("Arial",12,"bold"))
questoes_label.pack(pady=20)

resposta_Correta = tk.IntVar()

opcao1_btn = tk.Button(janela,text="",width=30,bg=button_color,fg=button_text_color, state=tk.DISABLED, font=("Arial",10,"bold"))
opcao1_btn.pack(pady=10)

opcao2_btn = tk.Button(janela,text="",width=30,bg=button_color,fg=button_text_color, state=tk.DISABLED, font=("Arial",10,"bold"))
opcao2_btn.pack(pady=10)

opcao3_btn = tk.Button(janela,text="",width=30,bg=button_color,fg=button_text_color, state=tk.DISABLED, font=("Arial",10,"bold"))
opcao3_btn.pack(pady=10)

opcao4_btn = tk.Button(janela,text="",width=30,bg=button_color,fg=button_text_color, state=tk.DISABLED, font=("Arial",10,"bold"))
opcao4_btn.pack(pady=10)

jogar_dnv_btn = tk.Button(janela,text="Jogar Novamente",width=30,bg=button_color,fg=button_text_color, font=("Arial",10,"bold"))


display_questions()

janela.mainloop()