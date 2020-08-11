"""
Morse Code (1 of 3)

In this kata you have to write a simple Morse code decoder. While the Morse 
code is now mostly superseded by voice and digital data communication channels,
it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". 
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 
1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital 
letters are used. When the message is written in Morse code, a single space is 
used to separate the character codes and 3 spaces are used to separate words. 
For example, the message HEY JUDE in Morse code is 
···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be 
ignored.

In addition to letters, digits and some punctuation, there are some special 
service codes, the most notorious of those is the international distress 
signal SOS (that was first issued by Titanic), that is coded as ···−−−···. 
These special codes are treated as single special characters, and usually are 
transmitted as separate words.

Your task is to implement a function that would take the morse code as input 
and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not 
Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Good luck!
"""

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
              '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
              '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', 
              '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', 
              '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', 
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', 
              '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', 
              '.--.-.': '@', '...---...': 'SOS'}

def decodeMorse(morse_code):
    morse_code = morse_code.split('   ')
    decoded = []
    for i in range(len(morse_code)):
        decoded.append(morse_code[i].split())
        decoded[i] = ''.join(MORSE_CODE[j] for j in decoded[i])
    return ' '.join(decoded).strip()  # see note below

# string.strip() (without any arguments) removes trailing and leading spaces.
# alt. return: ' '.join(decoded)[k for k in decoded if k != '' and k != ' ']

if __name__ == '__main__':
    print(decodeMorse('.... . -.--   .--- ..- -.. .')) # 'HEY JUDE'
    print(decodeMorse('   .   . ')) # 'E E'
    print(decodeMorse(' . ')) # 'E'
    print(decodeMorse('...   ---   ...')) # 'S O S'
    print(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ')) # 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
