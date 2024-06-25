from tkinter.ttk import *
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox

from app import ShowDoMilhao
jogo = ShowDoMilhao()

janela = tk.Tk()
janela.geometry('825x600')
janela.resizable(False, False)
janela.title('Projeto Cvti')

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


def exibir_entry():
    
    global entry, button_entry_confirmar, label_nome_entry, button_ajuda, frame_entry, radio_1, radio_2, radio_3, radio_4, radio, label_pergunta, button_ajuda, button_proxima, button_eliminar
    
    perguntas = [radio_1, radio_2, radio_3, radio_4, radio, label_pergunta, button_ajuda, button_proxima, button_eliminar]
    
    for i in perguntas:
        i.destroy()
    
    image_label.destroy()
    
    if button_ajuda:
        button_ajuda.destroy() 
        
    label_nome_entry = Label(janela, width=10, height=2, text='Nome: ')
    label_nome_entry.place(relx=0.4, rely=0.4, anchor='center')
    
    entry = Entry(janela, width=20) 
    entry.place(relx=0.5, rely=0.4, anchor='center')
    
    button_entry_confirmar = Button(janela, text="Confirmar", relief='ridge' ,command=validar_entry)
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
    global radio_value, entry, pontuacao, button_ajuda
    
    resposta_usuario = radio_value.get()
    nome = entry.get()
    
    if jogo.get_user_answer(resposta_usuario):
        pontuacao += 10
        exibir_perguntas()
        
    else:
        messagebox.showinfo('Resultado', f'Você perdeu! Sua pontuação foi: {pontuacao}')
        
        with open('respostas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Nome: {nome}, Opção escolhida: {resposta_usuario}, Pontuação: {pontuacao}\n')
            exibir_entry()
    
    entry.delete(0, END)
    radio_value.set(0)  
    

def exibir_perguntas():
    global label_pergunta, radio_value, button_confirma, entry, button_ajuda, label_numero_1, button_eliminar, button_proxima, radio_1, radio_2, radio_3, radio_4, radio, label_pergunta
    
    perguntas = [radio_1, radio_2, radio_3, radio_4, radio, label_pergunta]
    
    for i in perguntas:
        i.destroy()
    
    image_label.destroy()
    label_nome_entry.destroy()
    
    entry.place_forget()
    button_entry_confirmar.place_forget()
    
    question = jogo.display_question()

    label_pergunta = Label(janela, text=question["question"], font=('Helvetica', 20))
    label_pergunta.place(relx=0.3, rely=0.2, anchor='center')
    
    button_ajuda = Button(janela, width=20, height=3, text='Ajuda do professor', relief='ridge',command=lambda: exibir_ajuda('Aqui vai a mensagem de ajuda do professor.'))
    button_ajuda.place(relx=0.2, rely=0.8)
    
    button_proxima = Button(janela, width=20, height=3, text='Próxima pergunta', relief='ridge' ,command=proxima_funcao)
    button_proxima.place(relx=0.4, rely=0.8)
    
    button_eliminar = Button(janela, width=20, height=3, text='Ajuda dos universitários', relief='ridge' ,command=ajuda_universitarios)
    button_eliminar.place(relx=0.6, rely=0.8)
    
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
    
    global label_numero_1
    label_numero_1 = Label(janela, text=f'Número de Próxima: {contador}')
    label_numero_1.place(relx=0.7, rely=0.2)
    
    button_confirma = Button(janela, text="Confirmar", relief='ridge' ,command=salvar_resposta)
    button_confirma.place(relx=0.5, rely=0.8, anchor='center')

def proxima_funcao(): 
    global contador, button_proxima, label_numero_1, button_eliminar
    
    contador += 1
    
    if label_numero_1:
        label_numero_1.config(text=f'Número atual: {contador}')
    else:
        label_numero_1 = Label(janela, text=f'Número atual: {contador}')
        label_numero_1.place(relx=0.7, rely=0.2)
    
    if contador >= 1:
        button_proxima.config(state=tk.DISABLED)

def exibir_ajuda(mensagem):
    messagebox.showinfo('Ajuda do Professor', mensagem)

def ajuda_universitarios():
    messagebox.showinfo('Ajuda dos Universitários', 'Os universitários estão em dúvida entre A, B, C ou D.')

button_iniciar = Button(janela, width=20, height=3, text='Iniciar', relief='ridge' ,command=exibir_entry)
button_iniciar.place(relx=0.5, rely=0.8, anchor='center')

janela.mainloop()
