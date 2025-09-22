#Alunos(as): Jéssica Martins, Ana Luíza Ferreira e Guilherme Moreira

class Retangulo:
   def __init__(self, base, altura):
       self.base = base
       self.altura = altura
   
   def areaRetangulo(self):
       return self.base * self.altura


class Esfera:
   def __init__(self, raio):
       self.raio = raio

   def volumeEsfera(self):
       return 4/3 * 3.14 * self.raio**3


while True:
   opcao = int(input("Pressione:\n(1) para calcular ÁREA\n(2) para calcular VOLUME\n(3) para SAIR\n"))


   if opcao == 1:
       base = float(input("Informe a base: "))
       altura = float(input("Informe a altura: "))
       area = Retangulo(base, altura)
       print("Área do retângulo:", area.areaRetangulo())


   elif opcao == 2:
       raio = float(input("Informe o raio: "))
       volume = Esfera(raio)
       print("Volume da esfera:", volume.volumeEsfera())


   elif opcao == 3:
       break
  
   else:
       print("Dígito Inválido")
