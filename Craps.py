import random

din=100
while din>0:
    print('seu dinheiro é: ',din)
    aposta=int(input('Quanto você deseja apostar? '))
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    while aposta>0:
        print('Fase: Come Out')
        comeout=input('Qual aposta deseja fazer?(PLB,F,AC,T) ')
        if comeout=='PLB':
            if (d1+d2==7 or d1+d2==11):
                print('Resultado dos dados: ',d1+d2)
                din=din+aposta
            elif (d1+d2==2 or d1+d2==3 or d1+d2==12):
                din=din-aposta
                print('Resultado dos dados: ',d1+d2)
            else:
                print('Fase:Point')
                print('Resultado dos dados: ',d1+d2)
                d3=random.randint(1,6)
                d4=random.randint(1,6)
                while (d3+d4!=d1+d2 or d3+d4!=7):
                    d3=random.randint(1,6)
                    d4=random.randint(1,6)
                if d3+d4==d1+d2:
                    print('Comeout= Point')
                    din=din+aposta
                else:
                    print('Point = 7')
                    din=din-aposta
        elif comeout=='F':
            if (d1+d2==5 or d1+d2==6 or d1+d2==7 or d1+d2==8):
                din=0
                print('Resultado dos dados, perdeu: ',d1+d2)
            elif (d1+d2==3 or d1+d2==4 or d1+d2==9 or d1+d2==10 or d1+d2==11):
                din=din+aposta
                print('Resultado dos dados, ganhou: ',d1+d2)
            elif d1+d2==2:
                din=din+2*aposta
                print('Resultado dos dados, ganhou: ',d1+d2)
            else:
                din=din+3*aposta
                print('Resultado dos dados, ganhou: ',d1+d2)
