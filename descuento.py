"""Calcula el descuento aplicado a una compra"""
importe = float(input("Introduce el importe de la compra: "))
# Determina el porcentaje de descuento según el importe
if importe < 100:
    descuento = 0
elif importe < 300:
    descuento = 10
else:
    descuento = 15

importe_descuento = importe * descuento / 100
importe_final = importe - importe_descuento

print("Descuento:", descuento, "%")
print("Importe final:", importe_final, "€")