# pygma-enigma
Encryption software that emulates the german enigma machine both the m3 version and m4 without the use of the plugboard

## User guide
• Two types of encryption: m3 with key long 4 numbers and m4 with key long 5 numbers. <br />
• from pygma import m3 <br />
• from pygma import m4 <br />
### Functions
• set_key(key_of_encryption):<br />
Initializes the starting position of the "rotors" and reflector. Every number in key corespond with the position of letters in the alphabet.<br />
Example: set_key(4321) initializes the start position of the rotors to DCB and the position of reflector to A.<br />
• dec_enc("words"):<br />
Encrypt or decrypt given words

