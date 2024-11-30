alphabet = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','*',"1",'2','3','4','5','6','7','8','9','@',"!"]

direction = input("TYpe 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("TYpe your message:\n").lower()
shift = int(input("TYpe the shift number:\n"))
encrypt_value = ""


def encrypt(text,shift,encrypt_value,direction):
   
        for character in text:
            if " " in character:
                encrypt_value += " "
            else:
                real_value = alphabet.index(character)
                if direction == "encode":
                    value_find = real_value + shift
                elif direction == "decode":
                    value_find = real_value - shift
                else:
                    print("put correct encode or decode")
                    return
                encrypt_value += alphabet[value_find]
                
        print(encrypt_value)         


encrypt(text,shift,encrypt_value,direction)
