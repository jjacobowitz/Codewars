"""
Morse Code (2 of 3)

In this kata you have to write a Morse code decoder for wired electrical 
telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, 
connects the wires together, which can be detected on a remote station. 
The Morse code encodes every character being transmitted as a sequence of 
"dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in 
fact different operators would transmit at different speed. An amateur person 
may need a few seconds to transmit a single character, a skilled professional 
can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the
 hardware that checks the line periodically, and if the line is connected (the 
key at the remote station is down), 1 is recorded, and if the line is not 
connected (remote key is up), 0 is recorded. After the message is fully 
received, it gets to you for decoding as a string containing only symbols 0 
and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be 
received as follows:

110011001100110000001100000011111100110011111100111111000000000000001100111111
0011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the 
standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the 
message, correctly decode the message to dots ., dashes - and spaces (one 
between characters, three between words) and return those as a string. Note 
that some extra 0's may naturally occur at the beginning and the end of a 
message, make sure to ignore them. Also if you have trouble discerning if the 
particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous 
function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not 
Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its 
identifier in your language).

All the test strings would be valid to the point that they could be reliably 
decoded as described above, so you may skip checking for errors and 
exceptions, just do your best in figuring out what the message is!

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

# From Morse Code 1
def decode_morse(morse_code):
    morse_code = morse_code.split('   ')
    decoded = []
    for i in range(len(morse_code)):
        decoded.append(morse_code[i].split())
        decoded[i] = ''.join(MORSE_CODE[j] for j in decoded[i])
    return ' '.join(decoded).strip()


def decode_bits(bits):
    if '0' not in bits:
        return '.'
    sans_zeros = [i for i in bits.strip('0').split('0') if len(i) != 0] if '1' in bits.strip('0') else ['1'*10]
    sans_ones = [i for i in bits.strip('0').split('1') if len(i) != 0] if '0' in bits.strip('0') else ['1'*10]
    rate = min(len(min(sans_zeros)), len(min(sans_ones)))
    # bits_split = bits.split('000000'*rate)
    # return '   '.join([bits_split[i].strip('0').replace('000'*rate, ' ').replace('111'*rate, '-').replace('1'*rate, '.').replace('0'*rate, '') for i in range(len(bits_split))])
    return '   '.join([word.strip('0').replace('000'*rate, ' ').replace('111'*rate, '-').replace('1'*rate, '.').replace('0'*rate, '') for word in bits.split('000000'*rate)])
        

print(decode_morse(decode_bits('000011001100110011000000110000001111110011001111110011111100000000000000110011111100111111001111110000001100110011111100000011111100110011000000110000')) ==  'HEY JUDE')
print(decode_morse(decode_bits('1110111')) == 'M')
print(decode_morse(decode_bits('11111100111111')) == 'M')
print(decode_morse(decode_bits('1')) == 'E')
print(decode_morse(decode_bits('10001')) == 'EE')
print(decode_morse(decode_bits('000000011100000')) == 'E')
print(decode_morse(decode_bits('01110')) == 'E')
