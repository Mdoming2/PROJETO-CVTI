import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
import  random
import pygame

pygame.mixer.init()

from app import ShowDoMilhao
jogo = ShowDoMilhao()

janela = tk.Tk()
janela.geometry('825x600')
janela.resizable(False, False)
janela.title('Projeto Cvti')

som =pygame.mixer.music.load("abertura.mp3")
pygame.mixer.music.play(-1)
volume = 0.2
pygame.mixer.music.set_volume(volume)


photo = PhotoImage(file='show_do_miao.png')
image_label = Label(janela, image=photo)
image_label.place(relx=0.5, rely=0.4, anchor='center')

entry = None
label_nome_entry = None
button_ajuda = None
pontuacao = 0
resposta_correta = 1  
contador = 0

label_pergunta = Label()
radio = Radiobutton()
radio_1 = Radiobutton()
radio_2 = Radiobutton()
radio_3 = Radiobutton()
radio_4 = Radiobutton()
button_ajuda = Button()
button_proxima = Button()
button_eliminar = Button()
button_ajuda_professor = None
button_ajuda_universitarios = None
button_confirma = None  

def exibir_entry():
    global entry, button_entry_confirmar, label_nome_entry, button_ajuda_professor, button_proxima, button_ajuda_universitarios, button_confirma
    
    perguntas = [radio_1, radio_2, radio_3, radio_4, radio, label_pergunta]
    
    for i in perguntas:
        i.destroy()

    if button_confirma:    
        button_confirma.destroy() 

    if button_proxima:
        button_proxima.destroy()
    
    if button_ajuda_universitarios:
        button_ajuda_universitarios.destroy()

    image_label.destroy()
    
    label_nome_entry = Label(janela, width=10, height=2, text='Nome: ')
    label_nome_entry.place(relx=0.4, rely=0.4, anchor='center')
    
    entry = Entry(janela, width=20) 
    entry.place(relx=0.5, rely=0.4, anchor='center')
    
    button_entry_confirmar = Button(janela, text="Confirmar", relief='ridge', command=validar_entry)
    button_entry_confirmar.place(relx=0.5, rely=0.5, anchor='center')
    button_iniciar.place_forget()

def validar_entry():
    global entry
    nome = entry.get().strip()
    if nome == '':
        messagebox.showerror('Erro', 'Por favor, digite um nome.')
    else:
        exibir_perguntas()

def salvar_resposta():
    global radio_value, entry, pontuacao, button_ajuda,button_confirma,button_ajuda_professor,button_ajuda_universitarios
    
    if button_confirma:
        button_confirma.destroy()

    if button_ajuda_professor:
        button_ajuda_professor.destroy()

    if button_proxima:
        button_proxima.destroy()

    if button_ajuda_universitarios:
        button_ajuda_universitarios.destroy()


    resposta_usuario = radio_value.get()
    nome = entry.get()
    
    if jogo.get_user_answer(resposta_usuario):
        pontuacao += 1000
        exibir_perguntas()
        
    else:
        som_erro = pygame.mixer.Sound("errou.wav")
        som_erro.play()
        messagebox.showinfo('Resultado', f'Você perdeu! Sua pontuação foi: {pontuacao}')
        
        
        with open('respostas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Nome: {nome}, Opção escolhida: {resposta_usuario}, Pontuação: {pontuacao}\n')

            exibir_entry()

            

    entry.delete(0, END)
    radio_value.set(0)  

def exibir_perguntas():
    global label_pergunta, radio_value, button_confirma, entry,label_1, button_proxima, radio_1, radio_2, radio_3, radio_4, radio, label_pergunta, button_ajuda_professor, button_ajuda_universitarios
    
    perguntas = [radio_1, radio_2, radio_3, radio_4, radio, label_pergunta]

    if button_confirma:
        button_confirma.destroy()

    if button_ajuda_professor:
        button_ajuda_professor.destroy()

    if button_proxima:
        button_proxima.destroy()

    if button_ajuda_universitarios:
        button_ajuda_universitarios.destroy()


    for i in perguntas:
        i.destroy()
    
    image_label.destroy()
    label_nome_entry.destroy()
    
    entry.place_forget()
    button_entry_confirmar.place_forget()
    
    question = jogo.display_question()

    label_pergunta = Label(janela, text=question["question"], font=('Helvetica', 20))
    label_pergunta.place(relx=0.5, rely=0.2, anchor='center')
    
    button_ajuda_professor = Button(janela, width=20, height=3, text='Ajuda do professor', relief='ridge', command=lambda: exibir_ajuda('Aqui vai a mensagem de ajuda do professor.', question))
    button_ajuda_professor.place(relx=0.7, rely=0.3)
    
    button_proxima = Button(janela, width=20, height=3, text='Próxima pergunta', relief='ridge', command=lambda: proxima_funcao(question))
    button_proxima.place(relx=0.7, rely=0.5)
    
    button_ajuda_universitarios = Button(janela, width=20, height=3, text='Ajuda dos universitários', relief='ridge', command=lambda: ajuda_universitarios(question))
    button_ajuda_universitarios.place(relx=0.7, rely=0.7)
    
    radio_value = StringVar()
    radio = Radiobutton(janela, text=question["options"][0], value='a', variable=radio_value)
    radio.place(relx=0.5, rely=0.3, anchor='center')
    
    radio_1 = Radiobutton(janela, text=question["options"][1], value='b', variable=radio_value)
    radio_1.place(relx=0.5, rely=0.4, anchor='center')
    
    radio_2 = Radiobutton(janela, text=question["options"][2], value='c', variable=radio_value)
    radio_2.place(relx=0.5, rely=0.5, anchor='center')
    
    radio_3 = Radiobutton(janela, text=question["options"][3], value='d', variable=radio_value)
    radio_3.place(relx=0.5, rely=0.6, anchor='center')
    
    radio_4 = Radiobutton(janela, text=question["options"][4], value='e', variable=radio_value)
    radio_4.place(relx=0.5, rely=0.7, anchor='center')
    
    button_confirma = Button(janela, text="Confirmar", relief='ridge', command=salvar_resposta)
    button_confirma.place(relx=0.5, rely=0.8, anchor='center')

def proxima_funcao(question): 
    global button_proxima, button_ajuda_universitarios, button_ajuda_professor
    
    if button_proxima:
        button_proxima.config(state=tk.DISABLED)
    
    if button_ajuda_universitarios:
        button_ajuda_universitarios.config(state=tk.DISABLED)
    
    if button_ajuda_professor:
        button_ajuda_professor.config(state=tk.DISABLED)
    
    exibir_perguntas()

def exibir_ajuda(mensagem, question):
   
    opcao_ajuda = random.choice(question["options"])
    resposta_ajuda = question["options"].index(opcao_ajuda) + 1
    
    messagebox.showinfo('Ajuda do Professor', f'{mensagem}\n\nPergunta: {question["question"]}\nResposta: {resposta_ajuda}')
    desativar_botoes_ajuda()

def ajuda_universitarios(question):

    opcoes_eliminar = random.sample(question["options"], 2)
    
    mensagem = f'Os universitários estão em dúvida entre:'
    for opcao in question["options"]:
        if opcao not in opcoes_eliminar:
            mensagem += f' {opcao},'
    mensagem = mensagem.rstrip(',')  
    
    messagebox.showinfo('Ajuda dos Universitários', mensagem)
    desativar_botoes_ajuda()

def desativar_botoes_ajuda():
    global button_proxima, button_ajuda_professor, button_proxima, button_ajuda_universitarios
    
    if button_ajuda_professor:
        button_ajuda_professor.config(state=tk.DISABLED)
    
    if button_proxima:
        button_proxima.config(state=tk.DISABLED)
    
    if button_ajuda_universitarios:
        button_ajuda_universitarios.config(state=tk.DISABLED)

button_iniciar = Button(janela, width=20, height=3, text='Iniciar', relief='ridge', command=exibir_entry)
button_iniciar.place(relx=0.5, rely=0.8, anchor='center')

janela.mainloop()
