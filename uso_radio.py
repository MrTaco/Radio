from radio import Radio
t_radio= Radio("Toshiba")
desea_continuar = True
opcion = 0
while desea_continuar:
	if not t_radio.encendido:
		print("1. Encender \n 2. Salir")
		resp = int(input("que opcion desea: "))

		if resp == 1:
			t_radio.encender()
		elif resp == 2:
			desea_continuar = False
	else:
		print("""
			1. Subir volumen
			2. Subir emisora
			3. Bajar volumen
			4. Bajar emisora
			5. Cambiar de Frecuencia
			6. Salir
			""")
		resp = int(input("que opcion desea: "))

		if resp == 1:
			t_radio.subir_volumen()
		elif resp == 2:
			t_radio.subir_emisora()
		elif resp == 3:
			t_radio.bajar_volumen()
		elif resp == 4:
			t_radio.bajar_emisora()
		elif resp == 5:
			t_radio.cambiar_frecuencia()
		elif resp == 6:
			t_radio.apagar()
			desea_continuar = False
		print(t_radio)
