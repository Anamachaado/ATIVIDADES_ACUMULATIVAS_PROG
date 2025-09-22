#Alunos(as): Jéssica Martins, Ana Luíza Ferreira e Guilherme Moreira

print('1. Saudação Personalizada: \n');
nome = input('Digite seu nome: ');
frase = F"Olá {nome}! Bem-vindo(a)!";
print(frase);

print('\n');

print('2. Cadastro Simples: \n')
nome2 = input('Nome: ');
idade = input('Idade: ');
cidade = input('Cidade: ');
frase2 = (F'Seu nome é {nome2}, você tem {idade} anos e mora em {cidade}.');
print(frase2);

print('\n');

print('3. Etiqueta de Endereço: \n');
nome3 = input('Nome: ');
endereco = input ('Endereço: ');
tel = input ('Telefone: ');
print('\n');
print(nome3);
print(endereco);
print(tel);

print('\n');

print('4. União de Palavras: \n');
print('Vamos fazer uma frase!');
pal1 = input('Digite uma palavra: ');
pal2 = input('Digite a segunda palavra: ');
frase4 = (F'{pal1}{pal2}');
print(frase4.upper());

print('\n');

print('5. Conversor de Medidas: \n');
metro = float(input('Valor em metro: '));
cm = (metro * 100);
mm = (metro * 1000);
print(F'{metro} em centimetros é: {cm} \n {metro} em milímetros é: {mm}')

print('\n');

print('6. Cálculos Simples: \n');
num = float(input('Digite seu numero: '));
dobro = num * 2;
terça = num / 3;
print(F'O dobro de {num} é {dobro} e a terça parte é {terça}');
print('\n');

print('7. Calculadora de Quatro Operações: \n');
fav = int(input('Digite seu numero favorito: '));
nao = int(input('Digite seu numero menos favorito: '));
print('\n');
soma = fav + nao;
sub = fav - nao;
mult = fav * nao;
div = fav / nao;
print(F' Calculando...\n  Soma: {soma}\n  Subtração: {sub}\n  Multiplicação: {mult}\n  Divisão: {div}');

print('\n');

print('8. Cálculo de Média Escolar:\n');

print('Alunos:');
nota1 = float(input('Nota 1: '));
nota2 = float(input('Nota 2: '));
nota3 = float(input('Nota 3: '));
media = (nota1 + nota2 + nota3) / 3;
print(F'Média da nota: {media}' );

print('\n');

print('9. Cálculo de Área:\n');

print('Retangulo: ');
base = int(input('Base: '));
alt = int(input('Altura: '));
a = base * alt;
print(F'Area: {a}');

print('\n');

print('10. Calculadora de Números Decimais:\n');
num1 = float(input('Digite seu numero: '));
num2 = float(input('Digite seu outro numero  : '));
calc = input('Qual a conta: ');
print('\n');
if calc == '+':
    conta = num1 + num2;
if calc == '-':
    conta = num1 - num2;
if calc == '*':
    conta = num1 * num2;
if calc == '/':
    conta = num1 / num2;
print(conta);

print('\n');

print('11. Reajuste Salarial:\n');
sal = float(input('Salário: '));
por = float(input('Porcentagem: '));
reaj = sal / por;
print(reaj);
print('\n');

print('12. Índice de Massa Corporal (IMC):\n');
print ('IMC:');
peso = float(input('Peso: '));
altura = float(input('Altura: '))
imc = peso / altura ** 2;
print(F'Seu IMC é: {imc}');