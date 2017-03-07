#!/usr/bin/python
# coding=utf-8

from obspy.core import read
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from matplotlib import *
from decimal import *







class App:

	def __init__(self,master):
	#============================ BOTONES Y ENTRADAS =======================================
		frame = Frame(master, background= "#BBD1DC", padx = 25, pady = 25)
		frame.pack()
		self.plotLabel = Label(frame, pady=5, font = "Verdana 10 bold italic", background= "#BBD1DC", text = "INGRESE LOS ARCHIVOS SÍSMICOS")
		self.plotLabel.grid(rowspan = 1,columnspan = 4,sticky = W+E+N+S)
		self.plotLabel.grid(row = 1, column = 1)
		#=================== ENTRADAS DE ARCHIVOS =============================
		self.fileNameText = Entry(frame, bd = 2,state = DISABLED)
		self.fileNameText.grid(columnspan = 1,sticky = W+E+N+S)
		self.fileNameText.grid(row=2, column = 2)
		
		self.fileNameText2 = Entry(frame, bd = 2,state = DISABLED)
		self.fileNameText2.grid(columnspan = 1,sticky = W+E+N+S)
		self.fileNameText2.grid(row=3, column = 2)
		
		self.fileNameText3 = Entry(frame, bd = 2,state = DISABLED)
		self.fileNameText3.grid(columnspan = 1,sticky = W+E+N+S)
		self.fileNameText3.grid(row=4, column = 2)
						#====BOTONES PARA BUSCAR ARCHIVO=======
		self.buttonFile = Button(frame, text= "Abrir", command = self.openFile)
		self.buttonFile.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonFile.grid(row = 2, column = 3)

		self.buttonFile = Button(frame, text= "Abrir", command = self.openFile2)
		self.buttonFile.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonFile.grid(row = 3, column = 3)

		self.buttonFile = Button(frame, text= "Abrir", command = self.openFile3)
		self.buttonFile.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonFile.grid(row = 4, column = 3)
						#===FIN BOTONES PARA BUSCAR ARCHIVOS ===
		#==================FIN DE ENTRADAS DE ARCHIVO ===========================

		#=========================== PLOTEAR SEÑAL ==============================

		self.plotButton = Button(frame, pady = 20, bg = "#4D794B", text = "PLOT!", command = self.botonPlot)
		self.plotButton.grid(rowspan = 1,columnspan = 4,sticky=W+E+N+S)
		self.plotButton.grid(row=5,column=1)

		#========================== FIN PLOTEAR SEÑAL ============================

		#========================= ASIGNAR PUNTO DE INICIO =====================
		self.plotLabel2 = Label(frame, font = "Verdana 10 bold italic", background= "#BBD1DC", text = "ASIGNAR PUNTO DE INICIO")
		self.plotLabel2.grid(rowspan = 1,columnspan = 3,sticky = W+E+N+S)
		self.plotLabel2.grid(row = 6, column = 1)

		self.setText = Entry(frame, bd = 2)
		self.setText.grid(columnspan = 1,sticky = W+E+N+S)
		self.setText.grid(row=7, column = 2)

		self.buttonInterval = Button(frame, bg = "#6D8C9B", text= "SETEAR", command = self.setear)
		self.buttonInterval.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonInterval.grid(row = 7, column = 3)

		# ======================= FIN ASIGNAR PUNTO DE INICIO ===================

		self.plotLabel2 = Label(frame, pady=5, font = "Verdana 10 bold italic", background= "#BBD1DC", text = "INTERVALO DE MUESTRAS")
		self.plotLabel2.grid(rowspan = 1,columnspan = 3,sticky = W+E+N+S)
		self.plotLabel2.grid(row = 8, column = 1)

		self.intervalText = Entry(frame, bd = 2)
		self.intervalText.grid(columnspan = 1,sticky = W+E+N+S)
		self.intervalText.grid(row=9, column = 2)


		self.buttonInterval = Button(frame, bg = "#6D8C9B", text= "ASIGNAR", command = self.interval)
		self.buttonInterval.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonInterval.grid(row = 9, column = 3)

		self.buttonInterval = Button(frame, pady = 5, bg = "#6D8C9B", text= "MOSTRAR MOVIMIENTO", command = self.movi)
		self.buttonInterval.grid(columnspan = 2,sticky = W+E+N+S)
		self.buttonInterval.grid(row = 10, column = 2)

		self.buttonFile = Button(frame, activebackground = "#CD3939", text= ">>", command = self.replot)
		self.buttonFile.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonFile.grid(row = 10, column = 4)

		self.buttonFile = Button(frame, activebackground = "#CD3939", text= "<<", command = self.replot2)
		self.buttonFile.grid(columnspan = 1,sticky = W+E+N+S)
		self.buttonFile.grid(row = 10, column = 1)

		self.buttonInterval = Button(frame, bg = "#6D8C9B", text= "MOSTRAR POSICIONES", command = self.mostrar)
		self.buttonInterval.grid(columnspan = 2,sticky = W+E+N+S)
		self.buttonInterval.grid(row = 11, column = 2)

	#======================== FIN BOTONES Y ENTRADAS ===============================	

	def openFile(self):
		global fileSelectString
		fileSelect = askopenfilename()
		fileSelectString = str(fileSelect)
		fileName = os.path.split(fileSelect)[1]
		self.fileNameText.config(state = NORMAL)
		self.fileNameText.insert(0,fileName)

	def openFile2(self):
		global fileSelectString1
		fileSelect2 = askopenfilename()
		fileSelectString1 = str(fileSelect2)
		fileName = os.path.split(fileSelect2)[1]
		self.fileNameText2.config(state = NORMAL)
		self.fileNameText2.insert(0,fileName)

	def openFile3(self):
		global fileSelectString2
		fileSelect = askopenfilename()
		fileSelectString2 = str(fileSelect)
		fileName = os.path.split(fileSelect)[1]
		self.fileNameText3.config(state = NORMAL)
		self.fileNameText3.insert(0,fileName)

	def botonPlot(self):
		
		if(fileSelectString == ""):
			tkMessageBox.showinfo("Problemas","Debe seleccionar un archivo e ingresar un intervalo")

		else:
			self.mostrargrafica(fileSelectString, fileSelectString1, fileSelectString2)



	def mostrargrafica(self,fname,fname2,fname3):
		canaluno = read(fname)
		canaldos = read(fname2)
		canaltres = read(fname3)

		global xx 
		xx = canaluno[0]
		global yy 
		yy = canaldos[0]
		global zz
		zz = canaltres[0]

		plt.subplot(3,2,1)
		plt.title("ESTE-OESTE")
		plt.plot(xx.data)

		plt.subplot(3,2,3)
		plt.title("NORTE-SUR")
		plt.plot(yy.data)

		plt.subplot(3,2,5)
		plt.title("VERTICAL")
		plt.plot(zz.data)


		plt.show()


	def setear(self):
		global inicio
		global fin
		numSet = int(self.setText.get())
		inicio = numSet
		fin = numSet
		print "==========================="
		print "Posicion Seteada en: "
		print inicio
		print " "
		



	def interval(self):
		global inicio
		global fin
		num1 = int(self.intervalText.get())
		inicio = inicio
		fin = inicio
		fin = fin + num1
		print "==========================="
		print "Intervalo Asignado"
		print " "

		

	def replot(self):
		global inicio
		global fin
		plt.subplot(3,2,2)
		plt.title("MOVIMIENTO X Y")
		plt.cla()
		plt.plot(xx.data[inicio:fin], yy.data[inicio:fin])
		plt.plot(xx.data[fin], yy.data[fin],'ro')
		plt.plot(xx.data[inicio], yy.data[inicio],'kx')
		plt.axis([-2000, 2000, -2000, 2000])
		plt.draw()
		inicio = inicio + 1
		fin = fin + 1
		

	def replot2(self):
		global inicio
		global fin
		plt.subplot(3,2,2)
		plt.title("MOVIMIENTO X Y")
		plt.cla()
		plt.plot(xx.data[inicio:fin], yy.data[inicio:fin])
		plt.plot(xx.data[fin], yy.data[fin],'ro')
		plt.plot(xx.data[inicio], yy.data[inicio],'kx')
		plt.axis([-2000, 2000, -2000, 2000])
		plt.draw()
		if(inicio != 0):
			inicio = inicio - 1
			fin = fin - 1
		

	def movi(self):
		global inicio
		global fin
		plt.subplot(3,2,2)
		plt.title("MOVIMIENTO X Y")
		plt.cla()
		plt.plot(xx.data[inicio:fin], yy.data[inicio:fin])
		plt.plot(xx.data[fin], yy.data[fin],'ro')
		plt.plot(xx.data[inicio], yy.data[inicio],'kx')
		plt.axis([-2000, 2000, -2000, 2000])
		plt.draw()

	def mostrar(self):
		global inicio
		global fin
		print "======================"
		print "Posicion Inicial en la muestra Nro: "
		print inicio
		print "Posicion Final en la muestra Nro: "
		print fin
		print " "
		
		

		

	


		

inicio = 0
fin = 0
xx = ""
yy = ""
zz = ""
fileSelectString = ""
fileSelectString1 = ""
fileSelectString2 = ""
intervalString = ""
covarianceArray = []
timeArray = []
root = Tk()
root.title("P. M. P.")
app=App(root)
root.mainloop()
root.destroy()