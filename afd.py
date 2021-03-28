
def afd(lista, valor = 0):
    
    if lista[0] == 'A' or lista[0] == 'B' or lista[0] == 'C':
        if lista[0] == 'A':
            if valor == 6:
                return {"doce" : "A", "troco": 0}
            else:
                return {"doce" : "A", "troco": valor - 6}
        elif lista[0] == 'B':
            if valor == 6:
                return {"doce" : "B", "troco": 0}
            else:
                return {"doce" : "B", "troco": valor - 7}
        else:
            if valor == 6:
                return {"doce" : "C", "troco": 0}
            else:
                return {"doce" : "C", "troco": valor - 8}
    return afd(lista[1:], valor = valor + int(lista[0]))
            
