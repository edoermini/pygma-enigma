# pygma-enigma
Encryption software that emulates the german enigma machine without the use of the plugboard

## User guide
• M3 encryption: with key long 4 letters. <br />
Example: <br />
>from pygma import m3 <br />
> e = m3() <br />
> e.set_key("acvt") <br />
### Functions
• set_key(key_of_encryption):<br />
Initializes the starting position of the "rotors" and reflector. <br />
Example: set_key("dcba") initializes the start position of the rotors to DCB and the position of reflector to A.<br />
<br />
• set_stecker("letter1letter2, letter3letter4, ..."):<br />
Simulates the electric exchange of letters in stecker side of the machine, with up to 10 exchanges.<br />
Example: set_stecker("ac") sets the exchange of the two letters "a" and "c", so when you give letter "a" to program it will understand letter "c" and vice versa.<br />
<br />
• enc_dec("words"):<br />
Encrypt or decrypt given words

