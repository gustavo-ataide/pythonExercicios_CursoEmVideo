nome = str(input('Qual seu nome?'))
mai = nome.upper()
min = nome.lower()
strip = nome.strip()
replace = nome.replace(' ', '')
space = len(replace)
split = nome.split()
len = len(split [0])
print('Seu nome é: {} \nAqui está seu nome em maiúsculo: {} \nAqui está seu nome em minúsculo: {} \nSeu nome tem {} letras \nSeu primeiro nome tem {} letras'.format(nome, mai, min, space, len))
