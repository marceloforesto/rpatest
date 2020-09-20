import glob
import csv
import os.path
from os import path
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import tkinter as tk  
from tkinter import *
from functools import partial  
from csv import writer
from csv import reader


totalMatrix = []
cvsPath = ""
outPath = ""
nameOut = ""

def setDirCSV():
    global cvsPath
    cvsPath = askdirectory()

def setDirOut():
    global outPath
    outPath = askdirectory()

def verifyValues(name):
    global nameOut
    nameOut = name.get()        #get the file name from UI
    if (path.exists(cvsPath) == False or path.exists(outPath)  == False):       #verify the paths 
        messagebox.showerror("Erro", "Selecione os diretórios.")
        return
    else:
        try:
            open(outPath +'/'+nameOut, 'w')                 #verify if filename is valid
        except OSError:
            messagebox.showerror("Erro", "Nome de arquivo CSV inválido")
            return

    os.remove(outPath +'/'+nameOut)         #just remove the file test created 

    for file in glob.glob(cvsPath +'/'+"*.csv"):
        init()
        return

    messagebox.showerror("Erro", "Sem arquivos CSV no diretório selecionado.")

def init():
    global nameOut
    global outPath
    global cvsPath

    msgWait = waitMessage()
    with open(outPath+'/'+nameOut+'.csv', 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for file in glob.glob(cvsPath +'/'+ "*.csv"):
            supller = os.path.basename(file)
            supller = supller[:-4]
            if (supller != nameOut):
                with open(file,'r') as f:
                    csv_reader = reader(f)      
                    next(f)         #skip header
                    for line in csv_reader:
                        line.append(supller)       #add supller name colum
                        csv_writer.writerow(line)   #write the line on out csv file
                        line.pop()
                        addToMatrix(line)       #add product to matrix 

    insetMatrix()
    msgWait.destroy()           #close dialog
    messagebox.showinfo("Alerta","Processo finalizado com sucesso.")


def waitMessage():      #a dialog to wait the process
    win = Toplevel(root)
    win.transient()
    win.title('Operando')
    Label(win, text='Por favor, aguarde.').pack()
    return win
    
def addToMatrix(product):
    global totalMatrix
    for line in totalMatrix:
        if (product[0] == line[0]):     #if the product is already in the matrix, add the values of quantity and value
            line[1] = int(line[1]) + int(product[1])
            line[2] = int(line[2]) + int(product[2])
            return
    totalMatrix.append(product)       # if the product is not on matrix, add it

def insetMatrix():      #insert the matrix of all products in the end of csv file
    global totalMatrix
    header = ["Produto", "Quantidade", "Valor"]

    with open(outPath+'/'+nameOut+'.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow('')
        csv_writer.writerow('')
        csv_writer.writerow('')
        csv_writer.writerow(header)
        for line in totalMatrix:
            csv_writer.writerow(line)

if __name__ == "__main__":    
    root = tk.Tk()  
    root.geometry('210x140')  
    root.title('PSel')  

    nameEntry = tk.StringVar()
    label = tk.Label(root, text="Nome de arquivo CSV de saída").grid(row=3, column=3)  
    entry = tk.Entry(root, textvariable=nameEntry).grid(row=4, column=3)
    verifyValues = partial(verifyValues, nameEntry)

    buttonCal = tk.Button(root, text="Local dos arquivos CSVs", command=setDirCSV).grid(row=1, column=3)  
    buttonCal = tk.Button(root, text="Local do arquivo de saída", command=setDirOut).grid(row=2, column=3)  
    buttonCal = tk.Button(root, text="Iniciar", command=verifyValues).grid(row=5, column=3)  

    root.mainloop()