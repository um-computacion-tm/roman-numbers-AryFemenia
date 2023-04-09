#DEC TO ROM
def decimal_to_roman(decimal):
    val = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    roman = ''
    for num, word in val:
        while decimal >= num:
            roman += word
            decimal -= num
    return roman
# se le pasa el valor "decimal"
# recorre la lista leyendo los "val"
# limpia la variable "roman"
# lee "num" "word" en la lista
# mientras "decimal" sea mayor a un "num" de la lista
#  va a sumar a "roman" la "word" y 
#  a continuacion a "decimal" le va a restar el numero correspondiente a la letra asignada en la linea anterior
#  devuelve el valor asignado a "roman" para que en la pasada siguiente(si es que existe) se valla sumando el valor

#ROM TO DEC
def roman_to_decimal(roman):
    dictionary = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000}
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

# se le pasa el valor "roman"
# recorre la lista leyendo el "dictionary"
# limpia las variables "resultado" y "prev"
# lee el valor "roman" al reves
# asigna al valor "num" el correspondiente a "dictionary" en la posicion "word"
# si el valor "num" es menor a "prev"
# asgina a "resultado" el valor "resultado" - "num"(para descontar el asignado en la linea de "num")
# si el valor "num" es mayor o igual a "prev"
# asgina a "resultado" el valor "resultado" + "num"(para agregar el asignado en la linea de "num")
# asigna a "prev" el valor "num" que acabo de analizar
# devuelve la suma guardada en "resultado"
