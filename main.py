'''
Um trabalhador trabalha 40 horas por semana.
Escreva um algoritmo que leia o número de horas trabalhadas em cada semana de um mês,
o salário por hora e escreva o salário total do mês do funcionário (considere que o mês possua 4 semanas exatas).
Considere que o trabalhador que trabalhar mais de 40 horas em uma semana,
recebe hora extra de 50% nas horas que foram trabalhadas a mais.
O número de horas por semana não pode ser negativo e não pode ultrapassar 50 horas por semana.
'''


class Salario:
    def __init__(self, ):
        self.horas_trabalhadas = []
        self.salario_hora = -1
        self.salario_mes = -1
        self.hora_extra_50 = 1.5
    def set_salario_hora(self):
        while True:
            self.salario_hora = float(input('Insira o valor do salario por hora : \n'))
            if self.salario_hora <=0:
                print('Salario não pode ser negativo ou zero')
            else:
                return self.salario_hora

    def set_horas_trabalhadas(self):
        for n in range(4):
            while True:
                hora = int(input(f'Insira o valor de horas trablhadas na semana {n+1}: \n'))
                if hora < 0 or hora > 50:
                    print('O número de horas por semana não pode ser negativo e '
                          'não pode ultrapassar 50 horas por semana.')
                else:
                    self.horas_trabalhadas.append(hora)
                    break

        return self.horas_trabalhadas

    def calcular_salario(self):
        salario_total = 0
        for i in range(len(self.horas_trabalhadas)):
            if self.horas_trabalhadas[i] <= 40:
                salario_total += self.salario_hora * 40
            else:
                salario_total += ((self.horas_trabalhadas[i] - 40) * self.salario_hora) * self.hora_extra_50
                salario_total += self.salario_hora * 40

        self.salario_mes = salario_total
        return self.salario_mes


t = Salario()
t.set_salario_hora()
t.set_horas_trabalhadas()
print(f'O salario total do mes do funcionario é R$ : {t.calcular_salario():.2f}')
