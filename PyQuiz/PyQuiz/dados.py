import pandas as pd 
import openpyxl

# lista de perguntas 
questions = [
    ["Qual a capital do Amazonas? ", "Amazonas","Manaus","Belgica","Paris", 2],[],
    ["Qual a idade de Manaus? ", "1","340","200","353", 4],[],
    ["Qual a capital do Pará? ", "Teresina","São Paulo","Londres","Paris", 1],[],
]

# criando dataframe do pandas

df = pd.DataFrame(questions,columns=["Perguntas","Opção 1","Opção 2","Opção 3","Opção 4", "Resposta" ])

# salvar no arquivo do excel

df.to_excel("questions.xlsx",index=False)

print("Perguntas inseridas com sucesso!")


