def mesaXadrez(tamanho):
    
    contator = 0
           
           #0         #5
    while contator < tamanho : #Enquanto for verdadeiro vai execultar
        contator2 = 0
        while contator2 < tamanho:
            if(contator + contator2) % 2 == 0:
                print('1', end=' ') #end= printa 1 e o outro tmb
            else:
                print('0', end= ' ')
            contator2 += 1
        print()    
        contator += 1
        
mesaXadrez(5)
