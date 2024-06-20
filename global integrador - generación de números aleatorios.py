import random
import math

def MetodoConguencialLineal(x, a, b, mod):

    sucesion = []
    periodo = 0
    bandera = 0

    while(bandera != x):
        if (periodo == 0):
            bandera = x
        x = ((a * x) + b) % mod
        periodo = periodo + 1
        if (bandera == x): break
        print(x)
        sucesion.append(x/mod)

    if(periodo == mod):
        print("El generador es de ciclo completo")
    else:
        print("El generador es de ciclo incompleto")

    return sucesion, periodo

def metodoKS(sucesion, n, ks):
    sucesion.sort()
    i_dividido_n = []
    valorAbs_Yin= []
    num = 0

    for i in range(1, n+1):
        i_n = i/n
        i_dividido_n.append(i_n)
        if i < len(sucesion):
            num = abs(sucesion[i] - i_n)
            valorAbs_Yin.append(num)

    max_valorAbs_Yin = max(valorAbs_Yin)

    if(max_valorAbs_Yin < ks):
      print("La prueba está aceptada! Los valores son aleatorios. ")
      print("El número máximo de la diferencia Y/(i-n) es menor al número de Kolmogorov-Smirnov: ")
      print(round(max_valorAbs_Yin,4)," <", round(ks,4))
    else:
      print("No se pasó la prueba. Los valores no son aleatorios. ")
      print("El número máximo de la diferencia Y/(i-n) es mayor al número de Kolmogorov-Smirnov: ")
      print(round(max_valorAbs_Yin,4)," >", round(ks,4))

def verificar_alfa(n):

    alfa = float(input("Ingrese el nivel de significancia (alfa): "))
    ks = 0

    if alfa == 0.2:
        ks = 1.07/math.sqrt(n)
    elif alfa == 0.1:
        ks = 1.22/math.sqrt(n)
    elif alfa == 0.05:
        ks = 1.36/math.sqrt(n)
    elif alfa == 0.02:
        ks = 1.52/math.sqrt(n)
    elif alfa == 0.01:
        ks = 1.63/math.sqrt(n)
    elif alfa == 0.005:
        ks = 1.73/math.sqrt(n)
    elif alfa == 0.002:
        ks = 1.85/math.sqrt(n)
    elif alfa == 0.001:
        ks = 1.95/math.sqrt(n)
    else:
        print("El nivel de significancia no es válido, inténtelo nuevamente ")
        print("Niveles de significancia válidos: 0.2 - 0.1 - 0.05 - 0.02 - 0.01 - 0.005 - 0.002 - 0.001 ")
        ks = verificar_alfa(n)
    return ks

def main():

    print("Generación de números pseudosaleatorios con un generador congruencial mixto: \n")

    m = int(input("Ingrese el valor del módulo: "))
    x = int(input("Ingrese  el valor de la semilla: "))
    a = int(input("Ingrese el valor del multiplicador: "))
    b = int(input("Ingrese el valor de la constante aditiva: "))

    sucesionGenerada, periodo_n = MetodoConguencialLineal(x,a,b,m)

    print("Comprobar que la sucesión generada sea válida: \n")

    ks = verificar_alfa(periodo_n)

    metodoKS(sucesionGenerada, periodo_n, ks)


if __name__ == "__main__":
    main()


