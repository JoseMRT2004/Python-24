''''1. DEFINIR MORSE_DICT COMO {
   "A": ".-", "B": "-...", "C": "-.-.", ..., "Z": "--..",
   "0": "-----", ..., "9": "----."
    }
    2. LEER palabra
    3. CONVERTIR palabra A MAYÚSCULAS
    4. DEFINIR palabra_morse COMO ""
    5. PARA key EN MORSE_DICT HACER
    6. PARA i EN palabra HACER
    7. SI i == key ENTONCES
    8. palabra_morse += MORSE_DICT[key] + " "
    9. FIN SI
    10. FIN PARA
    11. FIN PARA
    12. MOSTRAR "Palabra original: " + palabra
    13. MOSTRAR "Palabra en Morse: " + palabra_morse'''
    
MORSE_DICT = {
    
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}