from pseudointegers import Aleatorio
import numpy as np
class Gramatica:
    def __init__(self,seed):
        self.diccionario = {}
        self.aleatorio = Aleatorio(seed)
    def agregar_regla(self,regla):
        if regla.left not in self.diccionario:
            self.diccionario[regla.left] = []
        self.diccionario[regla.left].append(regla)        
        
        
    def seleccionar(self,left):
        if left not in self.diccionario:
            return tuple()
        reglas = self.diccionario[left]
        total = 0
        for r in reglas:
            total +=r.cont
        
        indice = self.aleatorio.siguiente_entero(total)
        
        elegido = None
        
        for regla in reglas:
            indice = indice - regla.cont
            
            if indice <=0:
                elegido = regla
                break
        for regla in reglas:
            if regla is not elegido:
                regla.cont+=1
        
        return elegido.right  #type:ignore     
    def generar(self, cadena):
        
        resultado = ""

        if cadena in self.diccionario: 
            produccion = self.seleccionar(cadena) 
            for simbolo in produccion:
                
                resultado += self.generar(simbolo) 
                
        else:
            resultado += cadena + " "
            
        return resultado                
                
                    
class Regla:
    def __init__(self,izquierda,derecha:tuple):
        self.left = izquierda
        self.right = derecha
        self.cont = 1
    def __repr__(self):
        derecha = " ".join(self.right)
        return f"{self.cont} {self.left} -> {derecha}"





def probar_gramatica():
    print("--- Iniciando Prueba de Gramática ---")
    #Definir semilla como número aleatorio
    aleatorio = np.random.randint(0, 10000)

    # 1. Crear la gramática
    g = Gramatica(seed=aleatorio)

    # <inicio> -> <historia>
    g.agregar_regla(Regla('<inicio>', ('<historia>',)))
    
    # <historia> -> <frase> (Caso base para que termine)
    g.agregar_regla(Regla('<historia>', ('<frase>',)))
    # <historia> -> <frase> y <historia>
    g.agregar_regla(Regla('<historia>', ('<frase>', 'y', '<historia>')))
    # <historia> -> <frase> sino <historia>
    g.agregar_regla(Regla('<historia>', ('<frase>', 'sino', '<historia>')))
    
    # <frase> -> <articulo> <sustantivo> <verbo> <articulo> <sustantivo>
    g.agregar_regla(Regla('<frase>', ('<articulo>', '<sustantivo>', '<verbo>', '<articulo>', '<sustantivo>')))
    
    # <articulo> -> el | la | al
    g.agregar_regla(Regla('<articulo>', ('el',)))
    g.agregar_regla(Regla('<articulo>', ('la',)))
    g.agregar_regla(Regla('<articulo>', ('al',)))
    
    # <sustantivo> -> gato | niño | perro | niña
    g.agregar_regla(Regla('<sustantivo>', ('gato',)))
    g.agregar_regla(Regla('<sustantivo>', ('niño',)))
    g.agregar_regla(Regla('<sustantivo>', ('perro',)))
    g.agregar_regla(Regla('<sustantivo>', ('niña',)))
    
    # <verbo> -> perseguia | besaba
    g.agregar_regla(Regla('<verbo>', ('perseguia',)))
    g.agregar_regla(Regla('<verbo>', ('besaba',)))
    
    # 3. Generar historias
    print("\nGenerando 3 historias aleatorias:\n")
    
    for i in range(3):
        historia = g.generar('<inicio>')
        print(f"Historia {i+1}: {historia}")

    # 4. Verificar que los pesos cambian
    print("\nEstado de los contadores de <articulo> (deben ser diferentes de 1):")
    for r in g.diccionario['<articulo>']:
        print(r)

if __name__ == "__main__":
    probar_gramatica()        
        
    
        
        

            
        