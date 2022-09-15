"""This code is to encrypt the normal text to MORSE code and also decrypt the MORSE code to normal text."""
import datetime
import pytz

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(word):
    code_list1 = []
    for letter in word.upper():
        code_list1.append(MORSE_CODE_DICT[letter])
    return code_list1


def decrypt(mo_code):
    word = ""
    code_list2 = mo_code.split("|")
    for c in code_list2:
        for k, v in MORSE_CODE_DICT.items():
            if c == v:
                word = str(word) + str(k)
            else:
                continue
    return word


print("What do you want to do. Choose one!\n"
      "1. Encrypt\n"
      "2. Decrypt\n")
choice = input()
if choice == "1":
    print("Choose one input method\n"
          "1. Command line\n"
          "2. Text file\n")
    in_choice = input()
    if in_choice == "1":
        code = ""
        code_list = []
        sentence = input("Enter the sentence\n")
        sentence_list = sentence.split(" ")
        for w in sentence_list:
            en_result = encrypt(w)
            code_list.append(en_result)
        for values in code_list:
            for c in values:
                code = str(code) + str(c) + str("|")
            code = str(code) + str(" ")
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        current_time_str = current_time.strftime("%d %B,%Y : %H:%M:%S")
        with open(r"C:\Users\subclu\Desktop\TASK\U\MORSE\output_data\code.txt", "a+") as file:
            file.write(current_time_str + " :::> " + code)
            file.write("\n")
        print("MORSE code generated successfully!!!")
    elif in_choice == "2":
        code = ""
        text = ""
        code_list = []
        file_name = input("Enter the full file path of the source.\n")
        with open(file_name, 'r') as file:
            text_list = file.readlines()
        for tx in text_list:
            text = text + " " + str(tx)
        text = text.replace("\n", " ")
        sentence_list = text.split(" ")
        for w in sentence_list:
            en_result = encrypt(w)
            code_list.append(en_result)
        for values in code_list:
            for c in values:
                code = str(code) + str(c) + str("|")
            code = str(code) + str(" ")
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        current_time_str = current_time.strftime("%d %B,%Y : %H:%M:%S")
        with open(r"C:\Users\subclu\Desktop\TASK\U\MORSE\output_data\code.txt", "a+") as file:
            file.write(current_time_str + " :::> " + code)
            file.write("\n")
        print("MORSE code generated successfully!!!")
    else:
        print("You enter the wrong choice\n")

elif choice == "2":
    print("Choose one input method\n"
          "1. Command line\n"
          "2. Text file\n")
    in_choice = input()
    if in_choice == "1":
        sentence = ""
        m_code = input("Enter the morse code\n")
        m_code_list = m_code.split(" ")
        for cd in m_code_list:
            de_result = decrypt(cd)
            sentence = sentence + str(" ") + str(de_result)
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        current_time_str = current_time.strftime("%d %B,%Y : %H:%M:%S")
        with open(r"C:\Users\subclu\Desktop\TASK\U\MORSE\output_data\text.txt", "a+") as file:
            file.write(current_time_str + " :::> " + sentence)
            file.write("\n")
        print("Decrypted Successfully!!")
    elif in_choice == "2":
        file_name = input("Enter the full file path of the source.\n")
        with open(file_name, 'r') as file:
            text_list = file.readlines()
        sentence = ""
        ms_code = ""
        for tx in text_list:
            ms_code = ms_code + " " + str(tx)
        ms_code = ms_code.replace("\n", " ")
        m_code_list = ms_code.split(" ")
        for cd in m_code_list:
            de_result = decrypt(cd)
            sentence = sentence + str(" ") + str(de_result)
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        current_time_str = current_time.strftime("%d %B,%Y : %H:%M:%S")
        with open(r"C:\Users\subclu\Desktop\TASK\U\MORSE\output_data\text.txt", "a+") as file:
            file.write(current_time_str + " :::> " + sentence)
            file.write("\n")
        print("Decrypted Successfully!!")
    else:
        print("You enter the wrong choice\n")
else:
    print("Wrong Choice please choose correctly\n")
