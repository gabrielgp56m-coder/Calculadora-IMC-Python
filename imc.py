try:
    peso = float(input('Qual o seu peso em kg?: ').strip())
    altura = float(input('Qual a sua altura em cm?: ').strip())
    sexo = input('Você é homem ou mulher?: ').strip().lower()
    idade = int(input('Qual a sua idade?: '))

    imc = peso / (altura / 100) ** 2

    if imc >= 30:
        categoria = 'obeso'
    elif imc >= 25:
        categoria = 'sobrepeso'
    elif imc >= 18.5:
        categoria = 'normal'
    else:
        categoria = 'abaixo do peso'

    print(f'\nSeu IMC é: {imc:.2f}')
    print(f'Categoria: {categoria}')

    if sexo == 'homem':
        peso_ideal = (altura - 100) - (altura - 150) / 4
    elif sexo == 'mulher':
        peso_ideal = (altura - 100) - (altura - 150) / 2
    else:
        print('Sexo inválido.')
        peso_ideal = None

    if peso_ideal:
        peso_ideal += (idade - 20) * 0.1
        print(f'Peso ideal aproximado: {peso_ideal:.2f} kg')

except ValueError:
    print('Erro: digite valores válidos.')
