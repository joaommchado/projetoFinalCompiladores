class firstParser:
    #construtor
    def __init__(self, lista):
        self.lista = lista

    #escreva
    def verificar_escreva(self):
        index = []
        i = 0
        for linha in self.lista:
            if('ESCREVA' in linha):
                self.lista[i] = linha.replace('ESCREVA', '')
                index.append(i)
            i = i + 1
        return self.lista, index
    
    #programa_declara_bloco
    def verificar_programa_declara_bloco(self):
        verificador = False
        if('programa Declara Bloco' in self.lista[0]):
            verificador = True
            self.lista[0] = '1'
        return self.lista, verificador

    #fimprog
    def verificar_fimprog(self):
        verificador = False
        if("fimprog" in self.lista[len(self.lista) - 1]):
            verificador = True
            self.lista[len(self.lista) - 1] = '1'
        return self.lista, verificador

    #chamar
    def retornar_final(self):
        self.lista, index = self.verificar_escreva()
        self.lista, v1 = self.verificar_programa_declara_bloco()
        self.lista, v2 = self.verificar_fimprog()

        return self.lista, index, (v1 and v2)


    