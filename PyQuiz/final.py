import tkinter as tk

# Função chamada quando uma opção é selecionada
def check_answer(user_answer):
    global question_index
    correct_answer = questions[question_index][1]
    if user_answer == correct_answer:
        result_label.config(text="Resposta correta!")
    else:
        result_label.config(text="Resposta incorreta!")

    # Avança para a próxima pergunta
    question_index += 1
    if question_index < len(questions):
        show_question()
    else:
        result_label.config(text="Quiz concluído!")

# Função para exibir a pergunta atual
def show_question():
    question_label.config(text=questions[question_index][0])
    for i, option in enumerate(questions[question_index][2]):
        options_buttons[i].config(text=option)

# Perguntas e respostas (formato: [pergunta, resposta_correta, [opção_1, opção_2, ...]])
questions = [
    ["Qual é a capital da França?", 2, ["Berlim", "Londres", "Paris", "Madrid"]],
    ["Qual é o maior planeta do sistema solar?", 3, ["Vênus", "Júpiter", "Marte", "Saturno"]],
    ["Quem pintou a Mona Lisa?", 0, ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"]]
]

question_index = 0

# Criando a janela
root = tk.Tk()
root.title("PyQuiz")
root.geometry("600x400")

# Rótulo para a pergunta
question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.pack(pady=10)

# Botões para as opções
options_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Arial", 10), width=40, command=lambda i=i: check_answer(i))
    button.pack(pady=10)
    options_buttons.append(button)

# Rótulo para mostrar se a resposta está correta ou não
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Exibindo a primeira pergunta
show_question()

root.mainloop()
