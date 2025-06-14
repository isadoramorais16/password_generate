import customtkinter as ctk
import string
import random


#configuração padrão fixa da janela
E = ctk.CTk(fg_color="#006A71")
E.title("Password Generate")
E.geometry("400x400")
E.resizable(False,False)

icon = PhotoImage(file="C:\\Users\\jvbmo\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-06-04 110203.png")
E.iconphoto(True, icon)


#funções que geram a senha
def gerar_senha():
    tamanho = int(entry_tamanho.get()) #aqui ele vai ler o número digitado
    chars = string.digits #usa apenas múmeros para gerar senha
    senha = ''.join(random.choice(chars) for _ in range(tamanho)) 
    label_resultado.configure(state="normal") #impede que o resultado da senha gerada seja alterado
    label_resultado.configure(text=senha)


def senha_letras():
    tamanho = int(entry_tamanho.get()) #aqui ele vai ler o número digitado
    chars = string.digits + string.ascii_letters #junta letras e dígitos para geração da senha
    senha = ''.join(random.choice(chars) for _ in range(tamanho))
    label_resultado.configure(state="normal")  #impede que o resultado da senha gerada seja alterado
    label_resultado.configure(text=senha)

def copiar_senha():
    senha = label_resultado.cget("text")
    if senha:
        E.clipboard_clear() #limpa a área de transferência
        E.clipboard_append(senha) #copia a senha
        botao_copiar.configure(text="Copied!")
        E.after(1500, lambda: botao_copiar.configure(text="Copiar Senha"))
    

#------------------------ widgets da janela -------------------------------------------

#1.Label de instrução
label_instrucao = ctk.CTkLabel(E, text="Welcome to Password Generate ", font=("Rubik", 18),text_color="#edeff2")
label_instrucao.pack(pady=30)


#2.Campo de entrada
entry_tamanho = ctk.CTkEntry(E, fg_color="#48A6A7",border_color="#48A6A7", border_width=1, text_color="white", placeholder_text="Enter the number of digits",placeholder_text_color="white", width=250)
entry_tamanho.pack(pady=10)

#3.Botões
#3.1 Frame onde os botões vão ficar
botoes_frame = ctk.CTkFrame(E, fg_color="transparent")
botoes_frame.pack(pady=50)

#3.2 Botões de opções 
botao_opcaoletras = ctk.CTkButton(botoes_frame , text="With Leters", command= senha_letras ,fg_color="#A53860",
hover_color="#48A6A7", text_color="white")
botao_opcaoletras.pack(padx=10, side="left")

botao_gerar = ctk.CTkButton(botoes_frame , text="Only Numbers", command=gerar_senha,fg_color="#A53860",
hover_color="#48A6A7", text_color="white")
botao_gerar.pack(side="left", padx=10)


label_resultado = ctk.CTkLabel(E, text="", font=("Arial", 20), text_color="white")
label_resultado.pack(pady=5)

#3.3 Botão de Copiar resultado
botao_copiar = ctk.CTkButton(E, text="Copy Password",fg_color="#48A6A7",
hover_color="#A53860", text_color="white", command=copiar_senha)
botao_copiar.pack(pady=10)



E.mainloop()