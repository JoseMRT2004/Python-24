from key_word import MORSE_DICT

PALABRA = input('\nIntroduce (Palabra - Oracion): ')

PALABRA_MORSE = ""
for i in PALABRA.upper():
    for key, value in MORSE_DICT.items():
        if i == key:
            PALABRA_MORSE += value + " "

print(f'''
================================================================
 - Palabra original: {PALABRA}                  
 - Palabra en Morse: {PALABRA_MORSE.strip()}    
================================================================''')
