# O Automato recebe [0,1,2,3]

def vai_para(lista):
    nova_lista = lista + lista + lista
    print(nova_lista)
    nova_lista.append(0)
    if 1 not in nova_lista: nova_lista.append(1) 
    if 2 not in nova_lista: nova_lista.append(2) 
    nova_lista = sorted(nova_lista)
    nova_lista.pop(len(nova_lista)-1)
    return afd(nova_lista)

def afd(lista, retorno = []):
    if len(lista) == 1:
        return {"para_nos_andares":retorno}
    else:
        if lista[0] == lista[1] and lista[0] not in retorno:
            retorno.append(lista[0])
        return afd(lista[1:], retorno)
