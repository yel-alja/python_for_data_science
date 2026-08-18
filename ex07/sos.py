import sys
NESTED_MORSE = {
     " ": "/ ",
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

def encoding():
    """encoding the first argument to the morse code"""
    res = []
    for i in sys.argv[1]:
        if i.upper() in NESTED_MORSE:
            res.append(NESTED_MORSE.get(i))
        else:
            raise ValueError("AssertionError: the arguments are bad")
    return res

    
def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        try:
            res = encoding()
            for i in res:
                print(i , end=" ")
            
        except Exception as e:
            print(e)

        
        
        


if __name__ == "__main__":
    main()