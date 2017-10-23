# pygma-enigma
Encryption software that emulates the german enigma machine without the use of the plugboard

## User guide
• M3 encryption: with key long 4 numbers. <br />
Example: from pygma import m3 <br />
### Functions
• set_key(key_of_encryption):<br />
Initializes the starting position of the "rotors" and reflector. Every number in key corespond with the position of letters in the alphabet.<br />
Example: set_key(4321) initializes the start position of the rotors to DCB and the position of reflector to A.<br />
• enc_dec("words"):<br />
Encrypt or decrypt given words

