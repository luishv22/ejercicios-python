# Programa de cuenta regresiva que incia contando en 10 
# y al llegar a 0 muestra despegue

def cuenta_regresiva():
    contador = 10
    # ciclo while
    while contador >= 0:
        print(contador)
        contador -= 1 # resta 1 cada vez
        
    print("Despegue 🚀")

cuenta_regresiva()
