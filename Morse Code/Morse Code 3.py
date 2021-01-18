"""
Morse Code (3 of 3)

In this kata you have to deal with "real-life" scenarios, when Morse code 
transmission speed slightly varies throughout the message as it is sent by a 
non-perfect human operator. Also the sampling frequency may not be a multiple 
of the length of a typical "dot".
For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may 
actually be received as follows:

000000001101101001110000011000000111111010011111001111110000000000011101111111
1011111011111000000101100011111100000111110011101100000100000

As you may see, this transmission is generally accurate according to the 
standard, but some dots and dashes and pauses are a bit shorter or a bit 
longer than the others.

Note also, that, in contrast to the previous kata, the estimated average rate 
(bits per dot) may not be a whole number – as the hypotetical transmitter is a 
human and doesn't know anything about the receiving side sampling rate.

For example, you may sample line 10 times per second (100ms per sample), while 
the operator transmits so that his dots and short pauses are 110-170ms long. 
Clearly 10 samples per second is enough resolution for this speed (meaning, 
each dot and pause is reflected in the output, nothing is missed), and dots 
would be reflected as 1 or 11, but if you try to estimate rate (bits per dot), 
it would not be 1 or 2, it would be about (110 + 170) / 2 / 100 = 1.4. Your 
algorithm should deal with situations like this well.

Also, remember that each separate message is supposed to be possibly sent by a 
different operator, so its rate and other characteristics would be different. 
So you have to analyze each message (i. e. test) independently, without 
relying on previous messages. On the other hand, we assume the transmission 
charactestics remain consistent throghout the message, so you have to analyze 
the message as a whole to make decoding right. Consistency means that if in 
the beginning of a message '11111' is a dot and '111111' is a dash, then the 
same is true everywhere in that message. Moreover, it also means '00000' is 
definitely a short (in-character) pause, and '000000' is a long 
(between-characters) pause.

That said, your task is to implement two functions:

1. Function decodeBitsAdvanced(bits), that should find an estimate for the 
transmission rate of the message, take care about slight speed variations that 
may occur in the message, correctly decode the message to dots ., dashes - and 
spaces (one between characters, three between words) and return those as a 
string. Note that some extra 0's may naturally occur at the beginning and the 
end of a message, make sure to ignore them. If message is empty or only 
contains 0's, return empty string. Also if you have trouble discerning if the 
particular sequence of 1's is a dot or a dash, assume it's a dot. If stuck, 
check this for ideas.

2. Function decodeMorse(morseCode), that would take the output of the previous 
function and return a human-readable string. If the input is empty string or 
only contains spaces, return empty string.
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

# From Morse Code 1
def decodeMorse(morse_code):
    morse_code = morse_code.split('   ')
    decoded = []
    for i in range(len(morse_code)):
        decoded.append(morse_code[i].split())
        decoded[i] = ''.join(MORSE_CODE[j] for j in decoded[i])
    return ' '.join(decoded).strip()


def decodeBitsAdvanced(bits):
    if '0' not in bits:
        return '.'
    sans_zeros = [i for i in bits.strip('0').split('0') if len(i) != 0] if '1' in bits.strip('0') else ['1'*10]
    sans_ones = [i for i in bits.strip('0').split('1') if len(i) != 0] if '0' in bits.strip('0') else ['1'*10]
    rate = min(len(min(sans_zeros)), len(min(sans_ones)))
    # bits_split = bits.split('000000'*rate)
    # return '   '.join([bits_split[i].strip('0').replace('000'*rate, ' ').replace('111'*rate, '-').replace('1'*rate, '.').replace('0'*rate, '') for i in range(len(bits_split))])
    return '   '.join([word.strip('0').replace('000'*rate, ' ').replace('111'*rate, '-').replace('1'*rate, '.').replace('0'*rate, '') for word in bits.split('000000'*rate)])
        

print(decodeMorse(decodeBitsAdvanced('0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000')) ==  'HEY JUDE')
print(decodeMorse(decodeBitsAdvanced('1110111')) == 'M')
print(decodeMorse(decodeBitsAdvanced('11111100111111')) == 'M')
print(decodeMorse(decodeBitsAdvanced('1')) == 'E')
print(decodeMorse(decodeBitsAdvanced('10001')) == 'EE')
print(decodeMorse(decodeBitsAdvanced('000000011100000')) == 'E')
print(decodeMorse(decodeBitsAdvanced('01110')) == 'E')
