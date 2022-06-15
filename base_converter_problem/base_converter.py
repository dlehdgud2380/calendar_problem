from typing import Any


class Transformer:
    def __init__(self, digits: str) -> None:
        self.digits: str = digits # base N digits
        self.decimal_digits: str = '0123456789' # base 10 digits
        
    def from_decimal(self, i: int) -> str: # base 10 -> base N
        return self._convert(i, self.decimal_digits, self.digits, "convert")
    
    def to_decimal(self, s: str) -> int: # base N -> base 10
        return int(self._convert(s, self.digits, self.decimal_digits, "reverse"))
    
    def _convert(self, number: Any, fromdigits: str, todigits: str, mode: str) -> str:
        """### Base 10 to Base N and Base N to Base 10 Convert function

        Args:
            number (str): Data for Transform
            fromdigits (str): Convert from Base 10 or Base N digit data
            todigits (str): Convert to Base 10 or Base N digit data
            mode (str): 'convert' Base N or 'reverse' to Base 10
        """
        
        result: str = ''
        length_fromdigits = len(fromdigits)
        length_todigits = len(todigits)
        
        if mode == "convert":
            quotient: int = number
            remainder: int = 0
            while True:
                quotient, remainder = divmod(quotient, length_todigits)
                result += todigits[remainder]
                if quotient == 0:
                    break
            result = result[::-1] # reverse string
            
        if mode == "reverse":
            temp = 0
            for index, char in enumerate(number):
                temp += (fromdigits.index(char) * pow(length_fromdigits, (len(number)-index)-1))
            result = str(temp)
        
        return result
    
def unittest(transformer: Transformer, answer1: int, answer2: str):
    """Unittest module for _convert function from Transformer class

    Args:
        transformer (Transformer): Transformer Object
        answer1 (int): base10 to baseN answer
        answer2 (str): baseN to base10 answer
    """
    base10_to_baseN = transformer.from_decimal(answer1)
    baseN_to_base10 = transformer.to_decimal(answer2)
    
    assert base10_to_baseN == answer2, f"incorrect result -> Expected: {answer2}, Result: {base10_to_baseN}"
    assert baseN_to_base10 == answer1, f"incorrect result -> Expected: {answer1}, Result: {baseN_to_base10}"
    
    print(f"Test Pass -> {answer2}: {base10_to_baseN}, {answer1}: {baseN_to_base10}")

if __name__ == '__main__':
    base20 = Transformer('0123456789abcdefghij')
    unittest(base20, 1234, '31e')
    #base20.from_decimal(1234))
    #base20.to_decimal('31e'))
    
    binary_transformer = Transformer('01')
    unittest(binary_transformer, 3500, '110110101100')
    #binary_transformer.from_decimal(3500))
    #binary_transformer.to_decimal('110110101100'))
    
    hex_transformer = Transformer('0123456789ABCDEF')
    unittest(hex_transformer, 2222, '8AE')
    #hex_transformer.from_decimal(2222)
    #hex_transformer.to_decimal('8AE')
    
    base62_transformer = Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
    unittest(base62_transformer, 45523, 'LqP')
    #print(base62_transformer.from_decimal(45523))
    #print(base62_transformer.to_decimal('LqP'))