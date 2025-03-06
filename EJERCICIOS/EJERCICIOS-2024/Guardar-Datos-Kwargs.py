def registroEstudiates(**datosEstudiante):
    for key,values in datosEstudiante.items():
        print(f"{key} - {values}")
    
    
registroEstudiates(Nombre="jose",Edad=23,Carrera="Desarrollo de Software")