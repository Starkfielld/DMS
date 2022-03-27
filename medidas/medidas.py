def quantidade():
    while True:
        try:
            quantidade = float(input('Quantidade da medidas: '))
            break
        except ValueError:
            print('Valor inválido')
    return quantidade

def medida(x):
    quant = x
    print(' 1 - Milhas \n', '2 - Polegadas \n', '3 - Pés \n', '4 - Centimetros \n', '5 - Metros \n', '6 - Kilomentro')
    medida = input('Entre com o número da médida desejada: \n')
    if medida == '1':
        pol  = quant * 63360
        pes = quant * 5280
        cm = quant * 160934
        mt = quant * 1609.34
        km = quant * 1.60934
        print(f'{quant} milhas equivalem a {quant} milhas')
        print(f'{quant} milhas equivalem a {pol:.2f} polegadas')
        print(f'{quant} milhas equivalem a {pes:.2f} pés')
        print(f'{quant} milhas equivalem a {cm:.2f} centimetros')
        print(f'{quant} milhas equivalem a {mt:.2f} metros')
        print(f'{quant} milhas equivalem a {km:.2f} kilomentros')
    elif medida == '2':
        mi  = quant / 63360
        pes = quant / 12
        cm = quant * 2.54
        mt = quant / 39.37
        km = quant / 39370
        print(f'{quant} polegadas equivalem a {mi:.4f} milhas')
        print(f'{quant} polegadas equivalem a {quant} polegadas')
        print(f'{quant} polegadas equivalem a {pes:.2f} pés')
        print(f'{quant} polegadas equivalem a {cm:.2f} centimetros')
        print(f'{quant} polegadas equivalem a {mt:.2f} metros')
        print(f'{quant} polegadas equivalem a {km:.4f} kilomentros')
    elif medida == '3':
        mi  = quant / 5280
        pol = quant * 12
        cm = quant * 30.48
        mt = quant / 3.281
        km = quant / 3280.84
        print(f'{quant} pés equivalem a {mi:.4f} milhas')
        print(f'{quant} pés equivalem a {pol:.2f} polegadas')
        print(f'{quant} pés equivalem a {quant} pés')
        print(f'{quant} pés equivalem a {cm:.2f} centimetros')
        print(f'{quant} pés equivalem a {mt:.2f} metros')
        print(f'{quant} pés equivalem a {km:.4f} kilomentros')
    elif medida == '4':
        mi  = quant / 160934
        pol = quant * 0.3937
        pes = quant / 30.48
        mt = quant / 100
        km = quant / 100000
        print(f'{quant} centimetros equivalem a {mi:.4f} milhas')
        print(f'{quant} centimetros equivalem a {pol:.2f} polegadas')
        print(f'{quant} centimetros equivalem a {pes:.4f} pés')
        print(f'{quant} centimetros equivalem a {quant} centimetros')
        print(f'{quant} centimetros equivalem a {mt:.4f} metros')
        print(f'{quant} centimetros equivalem a {km:.4f} kilomentros')
    elif medida == '5':
        mi  = quant / 1609.34
        pol = quant * 39.37
        pes = quant * 3.281
        cm = quant * 100
        km = quant / 1000
        print(f'{quant} metros equivalem a {mi:.4f} milhas')
        print(f'{quant} metros equivalem a {pol:.2f} polegadas')
        print(f'{quant} metros equivalem a {pes:.2f} pés')
        print(f'{quant} metros equivalem a {cm:.2f} centimetros')
        print(f'{quant} metros equivalem a {quant} metros')
        print(f'{quant} metros equivalem a {km:.4f} kilomentros')
    elif medida == '6':
        mi  = quant / 1.60934
        pol = quant * 39370
        pes = quant * 3280.84
        cm = quant * 100000
        mt = quant * 1000
        print(f'{quant} kilomentros equivalem a {mi:.2f} milhas')
        print(f'{quant} kilomentros equivalem a {pol:.2f} polegadas')
        print(f'{quant} kilomentros equivalem a {pes:.2f} pés')
        print(f'{quant} kilomentros equivalem a {cm:.2f} centimetros')
        print(f'{quant} kilomentros equivalem a {mt:.2f} metros')
        print(f'{quant} kilomentros equivalem a {quant} kilomentros')
    else:
        print('Opção inválida')
    
        

def main():
    q = quantidade()
    medida(q)
    
main()