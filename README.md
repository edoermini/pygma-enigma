# pygma-enigma
Encryption software that emulates the german enigma machine both the m3 version and m4

## User guide
• Two types of encryption: m3 with key long 4 numbers and m4 with key long 5 numbers.
  • from pygma import m3
  • from pygma import m4
### Functions
• set_key(key_of_encryption):
Initializes the starting position of the "rotors". Every number in key corespond with the position of letters in the alphabet.
Example: set_key(4321) initializes the start position of the rotors to DCBA.
• dec_enc("words"):
Encrypt or decrypt given words

