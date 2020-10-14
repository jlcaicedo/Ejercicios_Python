def selector(pais, dolar):
    valor = input('ingrese el valor en moneda de ' + pais + ' aqui: ')

    valor = float(valor)

    resultado = valor / dolar
    resultado = round(resultado, 2)
    resultado = str(resultado)

    print('ud tiene en dolares USD$' + resultado)


menu = """
Bienvenido al Conversor de monedas 

1- Pesos mexicanos
2- Pesos Argentinos
3- Pesos Colombianos

Elige una opcion: 
"""

option = int(input(menu))

if option == 1:
    selector('mexico', 21.31)
    
elif option == 2:
    selector('Argentina', 77.15)

elif option == 3:
    selector('Colombia', 3828.00)
    
else:
    print('elige una opcion correcta')