from tkinter import *
import time

def bt_onclick():
    if vectorA.get() and vectorB.get():
        try:
            v1 = list(map(float, vectorA.get().split()))
            v2 = list(map(float, vectorB.get().split()))

        except:
            resultado['text'] = "Erro: verifique os valores e tente novamente"
        else:
            soma = 0
            for i in range(len(v1)):
                soma += v1[i] * v2[i]
            resultado['text'] = "O produto escalar dos vetores A e B é " + str(soma)
    else:
        resultado['text'] = "Erro: Informe os dois vetores e tente novamente"


janela = Tk()

# Config
janela.title("Produto Escalar")
janela.minsize(450, 300)
janela.maxsize(450, 300)

# In
text_VA = Label(janela, text="INFORME OS VETORES SEPARADOS POR ESPAÇO", font=("Arial",11))
text_VA.place(x=50, y=40)

text_VA = Label(janela, text="Vetor A", font=("Arial",10))
text_VA.place(x=50, y=80)
vectorA = Entry(janela,bd=4,font=("Arial",11), justify=LEFT)
vectorA.place(x=50, y=100)
text_VB = Label(janela, text="Vetor B", font=("Arial",10))
text_VB.place(x=50, y=130)
vectorB = Entry(janela,bd=4,font=("Arial",11), justify=LEFT)
vectorB.place(x=50, y=150)

B_ent = Button(janela, width =10, text="Calcular", command=bt_onclick)
B_ent.place(x=50, y=200)

# Out
resultado = Label(janela, text="", font=("Arial",12))
resultado.place(x=50, y=250)

janela.mainloop()