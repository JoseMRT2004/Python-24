
cliente = str(input("Introduce tu nombre: ")).strip().lower()
total = float(input("Ingrese el total de la compra (RD$): ")) 
tipo_producto = input("Ingrese el tipo de producto (navideños, supermercado, limpieza): ").strip().lower()

descuento = 0
puntos = total

# Calcular los descuestos en cada caso 
if tipo_producto == 'navideños' and total >= 10000:
    descuento = total * 0.25
    puntos = total * 2
elif tipo_producto == 'supermercado' and total >= 5000:
    descuento = total * 0.10
    puntos = total * 2

elif tipo_producto == 'limpieza' and total >= 3000:
    descuento = total * 0.05
    puntos = total * 2
total_con_descuento = total - descuento 

print(f"\nTipo de producto: {tipo_producto.capitalize()}")
print(f"Total inicial: RD${total:.2f}")
print(f"Descuento: RD${descuento:.2f}")
print(f"Total a pagar: RD${total_con_descuento:.2f}")
print(f"Puntos acumulados: {puntos:.2f}")
print (f"\n\t\tGracias por preferirnos {cliente} 💕")

