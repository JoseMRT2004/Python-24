# Convierte los valores de una lista a kelvin: 

list_item = [9.1, 8.8, -270.15]

def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in list_item:
    print(celsius_to_kelvin(temperature))
