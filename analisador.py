import sys
ALFABETO = "a b c d e f g h i j k l m n o p q r s t u v x y z A B C D E F G J I J K L M N O P Q R S T U V X Y Z"
NUMEROS = "0123456789."
COMPARE = "<>=!"

FRASE_OCO = "Verifique a quantidade de ocorrências"

sys.setrecursionlimit(4000)


def analise(bloco):
    bloco_otimizado = bloco.replace(' ', '')
    retorno = lex(bloco_otimizado)
    erros = identificador_de_erros(retorno)
    if erros != None: return {"retorno": erros}
    return {"retorno": retorno}


def lex(bloco, tokens=[], lendo=""):
    if bloco[0] == "(" and lendo == "se":
        tokens.append(plv_reserv("se"))
        tokens.append(simbolo("("))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    if bloco[0] == "(" and lendo == "enquanto":
        tokens.append(plv_reserv("enquanto"))
        tokens.append(simbolo("("))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    elif bloco[0] == ")" and lendo != "":
        try:
            float(lendo)
            tokens.append(numerico(lendo))
            tokens.append(simbolo(")"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo(")"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == "(" and lendo != "":
        try:
            float(lendo)
            tokens.append(numerico(lendo))
            tokens.append(simbolo("("))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo("("))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == ";" and lendo == "":
        try:
            tokens.append(simbolo(";"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo(";"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == ")" and lendo == "":
        try:
            tokens.append(simbolo(")"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo(")"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == ";" and lendo != "":
        try:
            float(lendo)
            tokens.append(numerico(lendo))
            tokens.append(simbolo(";")) 
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo(";"))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == "\"" and lendo != "":
        try:
            float(lendo)
            tokens.append(numerico(lendo))
            tokens.append(simbolo("\""))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
        except:
            tokens.append(identificadores(lendo))
            tokens.append(simbolo("\""))
            try:
                return lex(bloco[1:], tokens, lendo="")
            except:
                return tokens
    elif bloco[0] == "\"" and lendo == "":
        tokens.append(simbolo("\""))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    elif bloco[0] == "=" and lendo in COMPARE:
        tokens.append(simbolo(lendo + bloco[0]))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    elif lendo in COMPARE and lendo != "":
        tokens.append(simbolo(lendo + bloco[0]))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens

    elif bloco[0] in COMPARE and lendo != "":
        try:
            float(lendo[0])
            tokens.append(numerico(lendo))
            try:
                return lex(bloco[1:], tokens, lendo=bloco[0])
            except:
                tokens.append(simbolo(bloco[0]))
                return tokens
        except:
            tokens.append(identificadores(lendo))
            try:
                return lex(bloco[1:], tokens, lendo=bloco[0])
            except:
                tokens.append(simbolo(bloco[0]))
                return tokens
    elif bloco[0] == "(" and lendo == "":
        tokens.append(simbolo("("))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    elif bloco[0] == ")" and lendo == "":
        tokens.append(simbolo(")"))
        try:
            return lex(bloco[1:], tokens, lendo="")
        except:
            return tokens
    elif (bloco[0] in NUMEROS and lendo == ""):
        try:
            return lex(bloco[1:], tokens, lendo=lendo + bloco[0])
        except:
            tokens.append(numerico(bloco[0]))
            return tokens
    elif lendo != "" and lendo[0] in NUMEROS:
        try:
            return lex(bloco[1:], tokens, lendo=lendo + bloco[0])
        except:
            tokens.append(numerico(lendo + bloco[0]))
            return tokens
    elif ((bloco[0] in ALFABETO) or (bloco[0] in NUMEROS)):
        try:
            return lex(bloco[1:], tokens, lendo=lendo + bloco[0])
        except:
            try:
                float(lendo + bloco[0])
                tokens.append(numerico(lendo + bloco[0]))
                return tokens
            except:
                tokens.append(identificadores(lendo + bloco[0]))
                return tokens


def simbolo(simbolo):
    return (simbolo, "simbolo")


def plv_reserv(plv_reserv):
    return (plv_reserv, "palavra reservada")


def identificadores(id):
    return (id, "identificador")


def numerico(num):
    return (num, "numerico")


def identificador_de_erros(entrada):
    if entrada[len(entrada)-1][0] != ";":
        return [(";", "Falta no final do bloco")]
    elif (entrada.count((")", "simbolo")) != entrada.count(("(", "simbolo"))):
        return [("(  )", FRASE_OCO)]
    elif entrada.count(("\"", "simbolo"))%2 != 0:
        return [("  \"  ", "String Quebrada")]
    for x in entrada:
        if x[1] == 'numerico':
            try:
                float(x[0])
            except:
                return [(x[0], "Não é um tipo numérico")]
    """
    if entrada.count(("\"", "simbolo")) == entrada.count(("\"", "simbolo")):
        return [("  \"  ", "String Quebrada")]
    """


    return None

