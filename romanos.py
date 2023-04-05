def decimal_to_roman(decimal):
    resultado = ''
    if decimal >= 1000:
        resultado = 'M'
        decimal -= 1000
    if decimal >= 100:
        centenas = decimal // 100
        decimal -= centenas * 100
        if centenas <= 3:
            centenas = 'C' * centenas
        elif centenas == 4:
            centenas += 'CD'
        elif centenas <= 8:
            centenas += 'D' + (centenas - 5) * 'C'
        elif centenas <= 9:
            resultado += 'CM'
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal <= 8:
        resultado += 'V' + (decimal - 5) * 'I'
    elif decimal == 9:
        return 'IX'
    elif decimal == 10:
        return 'X'
    else:
        return resultado

def roman_to_decimal(roman):
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    prev = 0
    for word in roman[::-1]:
        num = dictionary[word]
        if num < prev:
            resultado -= num
        else:
            resultado += num
        prev = num
    return resultado
