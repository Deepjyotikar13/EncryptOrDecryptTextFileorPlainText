from random import shuffle, choice
path = "/storage/emulated/0/"  # This is the main path where all my folders and files exist.

class MessageEncoderDecoder:
    def __init__(self, key_of_word={}):
        self.key_of_word = key_of_word

    def create_key_to_code_decode(self):
        """This function will create a key every time you run it, and every single time it will generate a random key."""
        self.character_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:",<.>?`~äöüßáóúàùâêîôûëÿãõç ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×÷ΑΒΓΔΕΖΗΘΙΚΛΜΝΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωђғә')  # These are my random character lists, and using this list, I can provide my alphabet_code dictionary 2 random characters. If you want to provide more characters more than 2 characters, then you can add more characters to character_list, but I can't get more characters so for that reason, my alphabet_code dictionary one element has a 2 random character list.
        self.alphabet_code = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': [], ' ': [], 'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': [], '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '!': [], '"': [], '#': [], '$': [], '%': [], '&': [], "'": [], '(': [], ')': [], '*': [], '+': [], ',': [], '-': [], '.': [], '/': [], ':': [], ';': [], '<': [], '=': [], '>': [], '?': [], '@': [], '[': [], '\\': [], ']': [], '^': [], '_': [], '`': [], '{': [], '|': [], '}': [], '~': [], "\n": []}  # Using this alphabet_code, I can encrypt decrypt text and you should only use the characters present in the alphabet_code in your text. Else, you will get an error. And I can't add more characters in alphabet_character because I have limited characters in character_list so I can only provide 2 characters to my alphabet code. So, if you want to increase characters in alphabet_code then you should also increase the number of characters in character_list accordingly.

        shuffle(self.character_list)  # I am shuffling the character list so that each time I run it, I will get a unique pair of 2 random characters for any of my elements in alphabet_code.
        index = 0  # So this index variable is for that I can get my current position like in which character I am currently in.
        for alphabet in self.alphabet_code:
            # I am iterating over the alphabet_code dictionary.
            for cha in range(1, 3):
                # Then I am putting 2 characters to the alphabet_code dictionary's elements list.
                self.alphabet_code[alphabet].append(self.character_list[index])
                index += 1
        return self.alphabet_code  # Now I have a unique key so I returned it.

    def create_coded_message(self, file_path, message=None, write=False):
        """Using this function I will encrypt my text or file based on what you want."""
        if file_path == None:
            # This means that you are not encrypting any file so then I will make a list of the message.
            word_list = list(message)
        else:
            # This means that you have provided a file path so I will read the file data as text.
            with open(file_path) as read_data:
                txt_data = read_data.read()
                word_list = list(txt_data)  # I made a list out of that text fron the file.
        coded_word = ""  # It's an empty string there I will store my encrypted word.
        for word in word_list:
            # Now I am iterating over the message.
            random_char = choice(self.key_of_word[word])  # Then using the random module's choice function I am choosing a random character from the key_of_word. Let's say my word is "a". So, what I will do get the list of random characters for 'a' in the key dictionary 'a':['3', "#"]. So, ['3', "#"]  this is the list of random characters. From this list I will choose any character randomly and add it to the coded_word and after doing it for the entire message i will have a encrypted message.
            coded_word += random_char

        if write:
            # do you want to save the encrypted message in the file? If write is True then it will save the encrypted message in that file.
            with open(file_path, "w") as write_code:
                write_code.write(coded_word)
            print("Done")
        else:
            # Else it will return the encrypted message and you can print it.
            return coded_word

    def create_decoded_message(self, file_path, message=None, write=False):
        """using this function I will decrypt my encrypted message from a file or the encrypted message directly provided to the function."""
        if file_path == None:
            # Again if it's none that means you have not provided any file path so then it makes a list out of the message.
            coded_list = list(message)
        else:
            # Else it will get the message from the file and then make a list out of that text.
            with open(file_path, "r") as read_data:
                txt_data = read_data.read()
                coded_list = list(txt_data)
        decoded_word = ""
        for coded_word in coded_list:
            # So, I am iterating over the encrypted message. Then I am iterating over the key of my key_dictionary.
            for word in list(self.key_of_word):
                if coded_word in self.key_of_word[word]:
                    # so I will check that if the encrypted word exists in any of that dictionary's key list Like, let's say the encrypted word is "#" then I will check through every single key of key_of_word. Then, as here I can see that "#" exists in 'a' random character list  'a':['3', "#"]. So, I can say that the decrypted version of "#" will be 'a'. So, by doing it for the entire message, I will have a decrypted message.
                    decoded_word += word

        if write:
            # Again if write is true then save the decrypted message.
            with open(file_path, "w") as write_data:
                write_data.write(decoded_word)
            print("DONE Saved")
        else:
            # Else print the decrypted word.
            print(decoded_word, "\n!Decoded Word!")


if __name__ == "__main__":
    key_of_word = {'a': ['!', 'h'], 'b': ['<', '%'], 'c': ['G', 'n'], 'd': ['V', '¸'], 'e': ['ÿ', 'α'], 'f': ['T', 'μ'], 'g': ['0', '-'], 'h': ['"', 'R'], 'i': ['[', 'Ω'], 'j': ['¥', 'Q'], 'k': ['µ', 'ç'], 'l': ['Ε', '©'], 'm': ['k', 'ë'], 'n': ['r', 'Γ'], 'o': ['θ', '1'], 'p': ['z', 'Z'], 'q': ['u', ':'], 'r': ['Ο', 'ö'], 's': ['§', 'g'], 't': ['X', 'I'], 'u': ['σ', 'ζ'], 'v': [')', '{'], 'w': ['×', 'Χ'], 'x': ['8', 'w'], 'y': ['ß', '¨'], 'z': ['^', '|'], ' ': ['û', '¦'], 'A': ['λ', 'υ'], 'B': ['³', 'O'], 'C': ['Η', 'f'], 'D': ['e', '½'], 'E': ['y', 'C'], 'F': ['W', 'B'], 'G': ['γ', 'Κ'], 'H': ['χ', 'o'], 'I': ['&', 'ü'], 'J': ['i', 'ђ'], 'K': ['5', 'Λ'], 'L': ['7', 'Υ'], 'M': ['£', 'º'], 'N': ['κ', 'õ'], 'O': ['¾', 'ι'], 'P': ['x', 'Ρ'], 'Q': ['t', 'S'], 'R': ['»', '2'], 'S': ['÷', 'Φ'], 'T': ['Σ', 'φ'], 'U': [';', 'U'], 'V': ['E', 'π'], 'W': ['¤', '¡'], 'X': ['Y', '®'], 'Y': ['L', 'η'], 'Z': ['N', 'K'], '0': ['±', 'v'], '1': ['m', 'q'], '2': ['·', 'Τ'], '3': ['á', '*'], '4': ['ξ', '¬'], '5': ['à', '$'], '6': ['¢', 'δ'], '7': ['ν', '4'], '8': ['?', '='], '9': ['M', '´'], '!': ['`', 'ä'], '"': ['Β', '#'], '#': ['_', '+'], '$': ['²', 'F'], '%': [',', 'Ζ'], '&': ['ª', '¿'], "'": ['l', '.'], '(': ['ε', 'ê'], ')': ['ã', '~'], '*': ['Ν', 'ρ'], '+': ['¯', '6'], ',': ['Μ', '('], '-': ['H', 'p'], '.': ['>', 'τ'], '/': ['¼', 'A'], ':': ['°', 'ә'], ';': ['d', 'β'], '<': ['9', 'Δ'], '=': ['ú', 'Ψ'], '>': ['Α', 'ù'], '?': ['P', 'ô'], '@': ['«', 'a'], '[': ['ψ', ']'], '\\': ['3', 'Θ'], ']': ['î', 'â'], '^': ['@', 'ω'], '_': ['¶', 'Ι'], '`': [' ', '}'], '{': ['ó', '¹'], '|': ['b', 's'], '}': ['ο', 'j'], '~': ['ғ', 'D'], '\n': ['J', 'c']}  # This is my key to encrypt or decrypt my text.
    encode_decode = MessageEncoderDecoder(key_of_word)
    # This is for plain text.
    encrypt_message = encode_decode.create_coded_message(None, "hey how are")  # In this example, I will encrypt the plain message provided in the function.
    print(encrypt_message)  # This will print the encrypted message.
    encode_decode.create_decoded_message(None, encrypt_message)

    # This is for a file.
    # encrypt_message_file = encode_decode.create_coded_message(path + "your_text_file_name.txt", None, True)  #so in this one I will encrypt a text in a file the True means that after you have encrypted the message save it.
    # print(encrypt_message_file)
    #decrypt_message_file = encode_decode.create_decoded_message(path + "Your_text_file_name.txt", None, False)  # Make sure before decrypting the encrypted message you should comment the encrypt_message_file or it will encrypt the encrypted file which will be weird. And False means that only show the decrypted message do not save it.

