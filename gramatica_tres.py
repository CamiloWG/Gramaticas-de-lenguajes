# se define la clase Automata
class Automata:
    # el método constructor inicializa el estado a '0'
    def __init__(self):
        self.estado = '0'
        self.cont_a = 0
        self.cont_b = 0

    # el método transicion define las reglas de transición del autómata
    def transicion(self, simbolo):
        # Si el estado actual es '0'
        if self.estado == '0':
            # Si el símbolo es 'a', cambia el estado a '1' (Regla: S -> Ab)
            if simbolo == 'a':
                self.estado = '1'
                self.cont_a += 1
            # Si el símbolo no es 'a', cambia el estado a 'error'
            else:
                self.estado = 'error'
        # Si el estado actual es '1'
        elif self.estado == '1':
            # Si el símbolo es 'a', mantiene el estado en '1' (Regla: A -> aAb)
            if simbolo == 'a':
                self.estado = '1'
                self.cont_a += 1
            # Si el símbolo es 'b', cambia el estado a '2' (Regla: A -> ab)
            elif simbolo == 'b':
                self.estado = '2'
                self.cont_b += 1
            # Si el símbolo no es ni 'a' ni 'b', cambia el estado a 'error'
            else:
                self.estado = 'error'
        # Si el estado actual es '2'
        elif self.estado == '2':
            # Si el símbolo es 'b', mantiene el estado en '2' (Regla: A -> ab)
            if simbolo == 'b':
                self.estado = '2'
                self.cont_b += 1
            # Si el símbolo no es 'b', cambia el estado a 'error'
            else:
                self.estado = 'error'
                
   # el método procesar_cadena procesa una cadena de símbolos a través del autómata
    def procesar_cadena(self, cadena):
        for simbolo in cadena:
            self.transicion(simbolo)
        if self.estado == '2' and self.cont_b == self.cont_a + 1 and self.cont_a > 0:  
            return True
        else:
            return False


# La función main es la función principal del programa
def main():
    with open('g3_texto.txt', 'r') as archivo:
        palabra = archivo.read().strip()  # Eliminar espacios en blanco al inicio y al final
        if palabra == '':
            return print('Cadena vacia')
        automata = Automata()
        resultado = automata.procesar_cadena(palabra)
        if resultado:
            print('La cadena cumple con las reglas gramaticales.')
        else:
            print('La cadena no cumple con las reglas gramaticales.')

#  se llama a la función main
if __name__ == "__main__":
    main()