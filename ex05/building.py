import sys

def upperCounter(string: str) -> int:
        """upper letters counter"""
        count = 0
        for c in string:
                if c >= 'A' and c <= 'Z':
                        count += 1                        
        return count

def lowerCounter(string: str) -> int:
        """lower letters counter"""
        count = 0
        for c in string:
            if c >= 'a' and c <= 'z':
                count += 1
        return count

def numberCounter(string: str) -> int:
        """numbers counter"""
        count = 0
        for c in string:
            if c >= '0' and c <= '9':
                count += 1
        return count

def spaceCounter(string: str) -> int:
        """spaces counter"""
        count = 0
        for c in string:
            if c.isspace():
                count += 1
        return count

def treat(string: str):
        length = len(string)
        print(f"The text contains {length} characters:")
        print(f"{upperCounter(string)} upper letters")
        print(f"{lowerCounter(string)} lower letters")
        print(f"{length - lowerCounter(string) - upperCounter(string) - numberCounter(string) - spaceCounter(string)}  punctuation mark")
        print(f"{spaceCounter(string)} spaces")
        print(f"{numberCounter(string)} digits")

def main():
        if len(sys.argv) != 2:
            inp = input("What is the text to count?\n")
            treat(inp + "\n")
        else:
            treat(sys.argv[1])
           
    
if __name__ == "__main__":
    main()