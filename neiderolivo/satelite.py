print("programa para calcular la altura a la que se encuentra un satelite desde la superficie de la tierra ingresando un valor de periodo T")
mt=5.97e24;
rt=6371000;
G=6.67e-11;
T=float(input("ingrese un valor del periodo:"))
R=((G*mt*T**2)/(4*3.1416**2))**(1/3);
H=R-rt;
print("la altura a la que se encuentra el satelite es:",H)


