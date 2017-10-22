# pygma-enigma
Encryption software that emulates the german enigma machine both the m3 version and m4

## User guide
• Two types of encryption: m3 with key long 4 numbers and m4 with key long 5 numbers.\n
\t• from pygma import m3\n
\t• from pygma import m4\n
### Functions
• set_key(key_of_encryption):\n
\tInitializes the starting position of the "rotors". Every number in key corespond with the position of letters in the alphabet.\n
\tExample: set_key(4321) initializes the start position of the rotors to DCBA.\n
• dec_enc("words"):\n
\tEncrypt or decrypt given words

