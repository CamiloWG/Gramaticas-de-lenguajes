

class Automata:
    
    def __init__(self, texto):
        self.texto = texto
    
    def validar_cadena(self):
        estado = 1

        for i in self.texto:
            if i in ['a', 'b']:
                if estado == 1:
                    if i == 'a':
                        estado = 2
                    else: 
                        return False
                elif estado == 2:
                    if i == 'b':
                        estado = 3
                    else:
                        return False
                elif estado == 3:
                    if i == 'b':
                        estado = 4
                    else:
                        return False
                elif estado == 4:
                    return False
        return estado in [3, 4] 
    
    def print_result(self):
        return print('La cadena', self.texto, 'es CORRECTA!' if self.validar_cadena() else 'es INCORRECTA!')
    


def main():
    with open('g4_texto.txt', 'r') as archivo:
        palabra = archivo.read()
        if palabra == '': return print('Cadena vacia')
        reader = Automata(palabra)
        reader.print_result()


if __name__ == '__main__':
    main()
    
                        
