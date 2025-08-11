print("string".capitalize())
print("esta é uma frase".title())
print("esta é uma frase".replace(' ', '*'))
print("esta é uma frase".count("a"))
print("esta é uma frase".casefold())
print("esta é uma frase".find("fra"))
print("esta é uma frase".find("fra", 12))
tupla = ['esta','é','uma','frase']
#junta todos os itens de uma tupla em uma string, separada pelo para caracter
print("*".join(tupla))
#retira os espaços no início e fim
print("    esta é uma frase      ".strip())
print("esta é uma frase".replace('frase', 'sentença'))
print('esta é uma frase'.split())
#slicing string[start:stop:step]
#o : simboliza a parte do texto que vai manter, se está do lado esquerdo, considera o lado esquerdo
print("esta é uma frase"[:4])
#se está do lado direito, corta as posições e mantem o lado direito da string
print("esta é uma frase"[4:])
#faz a contagem do fim da frase para o início, também mantendo o lado no qual o : estiver posicionado
print("esta é uma frase"[-2:])
print("esta é uma frase"[:-2])
#faz o reverse string
print("esta é uma frase"[::-1])
#o segundo parâmetro é o segundo índice de corte
print("esta é uma frase"[0:9])


#interpolation

inicio = 'esta'
print(f'{inicio} é uma frase.')
