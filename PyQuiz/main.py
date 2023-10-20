import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random


df = pd.read_excel('questions.xlsx')
questoes = df.sample(n=3).values.tolist()

print(questoes)

janela = tk.Tk()
janela.title('PyQuiz')
janela.geometry("400x450")
#DEFININDO CORES
background_color = "#ECECEC"
text_color= "#333333"
button_color = "#4CAF50"
janela.config(bg=background_color)
janela.option_add('#Font','Arial')

janela.mainloop()