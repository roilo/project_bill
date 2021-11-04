from abc import ABC, abstractmethod
import argparse

class Cipher(ABC):
    def __init__(self, text: list) -> None:
        self.text = text

    def to_upper(self) -> list:
        result = []
        for line in self.text:
            lines = []
            for string in line:
                lines.append(string.upper())
            result.append(lines)
        return result
    
    def to_lower(self) -> list:
        result = []
        for line in self.text:
            lines = []
            for string in line:
                lines.append(string.lower())
            result.append(lines)
        return result
    
    @abstractmethod
    def encode(self) -> None:
        pass

    @abstractmethod
    def decode(self) -> None:
        pass

class A1Z26(Cipher):
    def __init__(self, text: list) -> None:
        super().__init__(text)

    def encode(self) -> list:
        self.text = self.to_upper() # convert to uppercase
        # self.to_lower() # convert to lowercase
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isalpha():
                        if char.isupper():
                            word.append(
                                str(ord(char) % 65 + 1).zfill(2)
                            )
                        else:
                            word.append(
                                str(ord(char) % 97 + 1).zfill(2)
                            )
                line.append("-".join(word))
            result.append(line)
        return result

    def decode(self) -> list:
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                chars = words.split("-")
                word = []
                for char in chars:
                    # only alphabetic numbers
                    word.append(chr(int(char) + 64))
                    # word.append(chr(int(char) + 96))
                line.append("".join(word))
            result.append(" ".join(line))
        return result

class Atbash(Cipher):
    def __init__(self, text: list) -> None:
        super().__init__(text)
    
    def encode(self):
        # no need to convert to uppercase or lowercase
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isupper():
                        word.append(
                            chr(ord("Z") - ord(char) + ord("A"))
                        )
                    elif char.islower():
                        word.append(
                            chr(ord("z") - ord(char) + ord("a"))
                        )
                    else:
                        word.append(char)
                line.append("".join(word))
            result.append(line)
        return result

    def decode(self):
        # encoding is the same as decoding
        return self.encode()

def init_parser() -> argparse.ArgumentParser():
    init = argparse.ArgumentParser(
        prog="Cipher Parser",
        description=
        "Parses input files to encode or decode into output files."
    )
    init.add_argument("-i", "--input",
                      help="Input file",
                      metavar="INPUT FILE",
                      dest="infile")
    init.add_argument("-o", "--output",
                      help="Output file",
                      metavar="OUTPUT FILE",
                      dest="outfile")
    init.add_argument("-e", "--encode",
                      choices=["a1z26", "atbash"],
                      help="Encode input",
                      dest="encode")
    init.add_argument("-d", "--decode",
                      choices=["a1z26", "atbash"],
                      help="Decode output",
                      dest="decode")
    init.add_argument("-v", "--version",
                      action="version",
                      version="%(prog)s v1.0")
    return init

def main() -> None:
    # initialize parser
    parser = init_parser()

    # parse arguments from command line
    args = parser.parse_args()

    # no arguments passed
    if not any(vars(args).values()):
        parser.print_help()
        return

    # read data
    in_data = []
    with open(args.infile, mode='r', encoding='utf-8') as infile:
        in_data = [j.split(" ") for j in [i.strip("\n") for i in infile]]

    # process data
    out_data = []

    # encoding data
    if args.encode == "a1z26":
        process = A1Z26(in_data)
        out_data = process.encode()
    elif args.encode == "atbash":
        process = Atbash(in_data)
        out_data = process.encode()

    # decoding data
    if args.decode == "a1z26":
        process = A1Z26(in_data)
        out_data = process.decode()
    elif args.decode == "atbash":
        process = Atbash(in_data)
        out_data = process.decode()

    # write data
    with open(args.outfile, mode='w', encoding='utf-8') as outfile:
        for lines in out_data:
            if args.encode or args.decode == "atbash":
                line = " ".join(lines)
            elif args.decode == "a1z26":
                line = "".join(lines)

            if lines != out_data[-1]:
                outfile.writelines(line + '\n')
            else:
                outfile.writelines(line)

if __name__ == "__main__":
    main()