import turtle

orientacao = ['N', 'L', 'S', 'O']
i = 0  #indice que determina a orientação atual do robô

x_y = input('Largura e comprimento da sala: ') #valores devem ser separados por espaço
movimentos = input('Movimentos: ') #caminho que o robô irá percorrer
movimentos = movimentos.upper()


robo = turtle.Turtle()
turtle.setup(width=50, height=50, startx=0, starty=0)

x_y = x_y.split()
x_entrada = int(x_y[0])
y_entrada = int(x_y[1])

for movimento in movimentos:
    if movimento == 'F':
        if orientacao[i] == 'N' and int(robo.xcor()) < (x_entrada-1):
            robo.forward(1)

        elif orientacao[i] == 'S' and int(robo.xcor()) > 0:
            robo.forward(1)

        elif orientacao[i] == 'L' and int(robo.ycor()) < (y_entrada-1):
            robo.forward(1)

        elif orientacao[i] == 'O' and int(robo.ycor()) > 0:
            robo.forward(1)
        else:
            pass

    elif movimento == 'T':
        if orientacao[i] == 'N' and int(robo.xcor()) > 0:
            robo.backward(1)

        elif (orientacao[i] == 'S') and int(robo.xcor()) < (x_entrada-1):
            robo.backward(1)

        elif orientacao[i] == 'L' and int(robo.ycor()) > 0:
            robo.backward(1)

        elif orientacao[i] == 'O' and int(robo.ycor()) < (y_entrada-1):
            robo.backward(1)
        else:
            pass

    elif movimento == 'E':
        robo.left(-90)
        if i > -3:
            i = i - 1
        else:
            i = 0

    elif movimento == 'D':
        robo.left(90)
        if i < 3:
            i = i + 1
        else:
            i = 0

    else:
        pass


x_saida = int(robo.ycor())
y_saida = int(robo.xcor())

print('{} {} {}'.format(orientacao[i], x_saida, y_saida))
