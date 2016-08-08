class Radio():
	def __init__(self,marca):
		self.marca = marca
		self.encendido = False
		self.en_fm = True
		self.emisora_am = 300
		self.emisora_fm = 87.0
		self.volumen = 0

	def encender(self):
		self.encendido = True 
	def apagar(self):
		self.encendido = False
	def subir_volumen(self):
		if self.volumen >= 100:
			self.volumen = 100
		else:
			self.volumen += 5
	def bajar_volumen(self):
		if self.volumen <= 0:
			self.volumen = 0
		else: 
			self.volumen -= 5
	def subir_emisora(self):
		if self.en_fm == True:
			if self.emisora_fm > 107.0:
				self.emisora_fm = 87.0
			elif self.emisora_fm < 87.0:
				self.emisora_fm = 107.0
			else:
				self.emisora_fm += 0.5
		else:
			if self.emisora_am > 1300:
				self.emisora_am = 300
			elif self.emisora_am < 300:
				self.emisora_am = 1300
			else: 
				self.emisora_am += 40
	def bajar_emisora(self):
		if self.en_fm == True:
			if self.emisora_fm > 107.0:
				self.emisora_fm = 87.0
			elif self.emisora_fm < 87.0:
				self.emisora_fm = 107.0
			else:
				self.emisora_fm -= 0.5
		else:
			if self.emisora_am > 1300:
				self.emisora_am = 300
			elif self.emisora_am < 300:
				self.emisora_am = 1300
			else: 
				self. emisora_am -= 40
	def cambiar_frecuencia(self):
		self.en_fm = not self.en_fm

	def __str__(self):
		resultado = ""
		resultado += "encendido: " + str(self.encendido)
		resultado += "am/fm: " + str(self.en_fm)
		resultado += "emisora am: " + str(self.emisora_am)
		resultado += "emisora fm: " + str(self.emisora_fm)
		resultado += "volumen: " + str(self.volumen)
		return resultado
