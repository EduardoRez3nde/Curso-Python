frase = str(input('Digite sua Frase: ').upper().strip())
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A primeira vez que ela aparece é na posição {frase.find("A")+1}')
print(f'A ultima vez que ela parece e na posição {frase.rfind("A")+1}')
