Hemoglobina = float(input())
genero = int(input())  # 1 = Masculino, 2 = Femenino


if genero == 1:  # Masculino
    if hemoglobina < 12.2:
        print("Baja")
    elif hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")
elif genero == 2:  # Femenino
    if hemoglobina < 12.6:
        print("Baja")
    elif hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")
else:
    print("No es posible generar la alerta")

   

      
