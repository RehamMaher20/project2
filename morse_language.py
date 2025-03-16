morse_en = {"a": "*-", "b": "-***", "c": "-*-*", "d": "-**", "e": "*", "f": "**-*", "g": "--*", "h": "****", "i": "**",
            "j": "*---", "k": "-*-", "l": "*-**", "m": "--", "n": "-*", "o": "---", "p": "*--*", "q": "--*-",
            "r": "*-*", "s": "***", "t": "-", "u": "**-", "v": "***-", "w": "*--", "x": "-**-", "y": "-*--",
            "z": "--**"}

morse_ar = {"ا": "*-", "ب": "-***", "ت": "-", "ث": "-*-*", "ج": "*---", "ح": "****", "خ": "---", "د": "-**",
            "ذ": "--**", "ر": "*-*", "ز": "---*", "س": "***", "ش": "----", "ص": "-**-", "ض": "***-", "ط": "**-",
            "ظ": "-*--", "ع": "*-*-", "غ": "--*", "ف": "**-*", "ق": "--*-", "ك": "-*-", "ل": "*-**", "م": "--",
            "ن": "-*", "ه": "**-**", "و": "*--", "ي": "**", "ء": "*", "ئ": "*", "ؤ": "*", "ة": "**-**", "ى": "**",
            "إ": "*-", "أ": "*-"}

symbols = {"0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****",
           "7": "--***", "8": "---**", "9": "----*", " ": " ", ".": "*-*-*-", ",": "--**--", "،": "--**--",
           ";": "--**--", "؛": "--**--", ":": "---***", "?": "**--**", "!": "-*-*--", "-": "-****-", "/": "-**-*",
           "(": "-*--*-", ")": "-*--*-", '"': "*-**-*", "'": "*----*", "`": "*----*", "+": "*-*-*", "=": "-***-",
           "_": "**--*-", "$": "***-**-", "@": "*--*-*", "&": "*-***"}

def translate(message):
    chars =''
    for i in message:

        if i in morse_en :
            chars += 'e'
        elif i in morse_ar:
            chars += 'r'
        elif i in symbols:
             pass
        else:
            chars += 'f'
            
    
        if 'f' in chars:
            print('Your message included unsuported letters')
        elif  'e' in chars and 'r' in chars:
            print('Your message has mixed languages ')
        elif 'e' in chars:
            print(morse(message,morse_en)) 
        elif 'r' in chars:
            print(morse(message,morse_ar))
        else:
            print(morse(message,symbols))

def morse(text, dict):
    message = ''
    for letter in text:
        if letter == ' ':
            message += ' '
        elif letter in symbols:
            message += symbols[letter] + ' '
        #elif letter in morse_en:
         #   message += morse_en[letter] + ' ' 
        #elif letter in morse_ar:
         #   message += morse_ar[letter] + ' '
       
        else:
            message += dict[letter] + ' ' 
    return message


def translate(message):
    chars =''
    for i in message:

        if i in morse_en :
            chars += 'e'
        elif i in morse_ar:
            chars += 'r'
        elif i in symbols:
             pass
        else:
            chars += 'f'
            
    
    if 'f' in chars:
        print('Your message included unsuported letters')
    elif  'e' in chars and 'r' in chars:
        print('Your message has mixed languages ')
    elif 'e' in chars:
        print(morse(message,morse_en)) 
    elif 'r' in chars:
        print(morse(message,morse_ar))
    else:
        print(morse(message,symbols))
                


start = True
while start:
    text = input('Your message: ').lower()
    if text == 'quitgame':
        start = False
        print('FINNISH')
    else:
        translate(text)
                
