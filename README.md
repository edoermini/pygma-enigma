# pygma-enigma
Encryption software that emulates the german enigma machine.

## User guide

### Setup your machine
* **Rotors and Reflector** <br />
  > from pygma.rotors import Rotor <br />
  > from pygma.Reflector import Reflector <br />
  >  <br />
  > r1 = Rotor("asdfghjklzxcvbnmqwertyuiop", 9) <br />
  > r2 = Rotor("qawsedrftgyhujikolpzxcvbnm", 24) <br />
  > r3 = Rotor("zxcvbnmasdfghjklqwertyuiop", 2) <br />
  > <br />
  > reflector = Reflector("adsfgjhklzcxvbmnqewrtuyiop", 12)
  
  *Rotor* funcion sets the rotor
  
 
  Initializes the start position of the rotors to DCB and the position of reflector to A.

* **Plug Board** <br />
 Simulates the electric exchange of letters in stecker side of the machine, with up to 10 exchanges. <br />
  Example: <br />
  > e.set_stecker("ac") <br />
 
  Sets the exchange of the two letters "a" and "c", so when you give letter "a" to program it will understand letter "c" and vice             versa.

### Start Encrypting and Decrypting
* **Set Encrypter and Decrypter**
 Encrypt or decrypt given words <br />
  Example: <br />
  > e.enc_dec("hello!") <br />
  > 'txxxc!' <br />
  
  Encrypts word "hello!" in "txxxc!" with the configuration of the examples.
  > e.enc_dec("txxxc!") <br />
  > 'hello!' <br />
  
  Decrypts word "txxxc!" in "hello!" with the configuration of the examples.
  
 

