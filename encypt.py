alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
alphabet = list(map(chr,range(97,123))) # This can be used
Capital_alphabet = list(map(chr,range(65,91)))

def encrypt(ori_text,shift):
    cipher_text = ""
    for i in ori_text:
        position = alphabet.index(i) + shift
        position %= len(alphabet)
        cipher_text +=alphabet[position]

    print(f"Here is your encoded text: {cipher_text}")

def decrypt(en_text,shift):
    dec_text = ""
    for i in en_text:
        position = alphabet.index(i) - shift
        position %= len(alphabet)
        dec_text += alphabet[position]

    print(f"Here is your decoded text: {dec_text}")

def ceaser(original_text,shift,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift *= -1

    for i in original_text:

        if i not in alphabet:
            output_text += i
        else:
            position = alphabet.index(i) + shift
            position %= len(alphabet)
            output_text += alphabet[position]
    
    print(f"Here is your {encode_or_decode}d text: {output_text}")

do_continue = True
while do_continue:
    path = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    text = input("Type your messege: ").lower()
    shift = int(input("type your shift number: "))

    ceaser(text,shift,path)
    k = input("Type 'yes' if you want to go again Otherwise type 'no' : ").lower()
    if k == "yes":
         continue
    else:
         do_continue=False
         print("TATA SEE YOU")
