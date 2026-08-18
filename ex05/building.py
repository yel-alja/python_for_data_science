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

def main():
        if len(sys.argv) != 2:
            print("Usage: python3 building.py <string to treat>")
        else:
            length = len(sys.argv[1])
            print(f"The text contains {length} characters:")
            print(f"{upperCounter(sys.argv[1])} upper letters")
            print(f"{lowerCounter(sys.argv[1])} lower letters")
            print(f"{length - lowerCounter(sys.argv[1]) - upperCounter(sys.argv[1]) - numberCounter(sys.argv[1]) - spaceCounter(sys.argv[1])}  punctuation mark")
            print(f"{spaceCounter(sys.argv[1])} spaces")
            print(f"{numberCounter(sys.argv[1])} digits")
    
if __name__ == "__main__":
    main()