from radio import Radio 
var_radio=Radio("TDs")
desea_continuar=True
while desea_continuar:
	print("1-Subir Volumen \n2-Bajar Volumen \n3-Subir Estacion \n4-Bajar Estacion \n5-Cambiar Frecuencia \n6-Apagar \n7-Encender "
	if opc==1:
		var_radio.subir_volumen()
	elif opc==2:
		var_radio.bajar_volumen()
	elif opc==3:
		var_radio.subir_emisora()
	elif opc==4:
		var_radio.bajar_emisora()
	elif opc==5:
		var_radio.