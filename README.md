# pygma-enigma
Encryption software that emulates the german enigma machine.

## User guide

### Setup your machine
* **Rotors** <br />
  > from pygma.rotors import Rotor <br />
  >  <br />
  > r1 = Rotor("asdfghjklzxcvbnmqwertyuiop", 9) <br />
  > r2 = Rotor("qawsedrftgyhujikolpzxcvbnm", 24) <br />
  > r3 = Rotor("zxcvbnmasdfghjklqwertyuiop", 2) <br />
  
  The **Rotor** function sets the rotor and it requires 2 arguments, the first the alphabet that will correspond to the rotor, and the second the rotor starting point. <br />
  
* **Reflector** <br />
  > from pygma.reflector import Reflector <br />
  > <br />
  > reflector = Reflector("adsfgjhklzcxvbmnqewrtuyiop", 12) <br />
  
  The **Reflector** function sets the reflector and similarly to the Rotor function it requires 2 arguments, the first the alphabet that will correspond to the reflector, and the second the reflector starting point. <br />

* **Plug Board** <br />
  > from pygma.plugboard import PlugBoard <br />
  > <br />
  > pb = PlugBoard("as,de,fr") <br />
  
  The **Stecker** function sets the exchange between two letters it requires 1 arguments that corresponds to the groups of letters to be exchanged. <br />
  <br />
  *Example:* <br />
  Stecker("as,de,fr") means that letter a must be exchanged with s and vice versa, as well as for d and e letters, and for f and r letters. <br />

### Start Encrypting and Decrypting
* **Set Encrypter and Decrypter** <br />
  > from pygma.machine import Machine <br />
  > <br />
  > e = Machine([r1, r2, r3], reflector, pb)
  
  The **Machine** function sets the machine with the declared elements. <br />
  
* **Encrypt and decrypt** <br />
  > e.enc_dec("hello!") <br />
  > 'krcpy!' <br />
  > e.enc_dec("krcpy!") <br />
  > 'hello!' <br />
  
  The **enc_dec** function encrypts and decrypts given words with the configuration previously set.
  
 

