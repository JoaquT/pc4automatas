class Aleatorio:
    def __init__(self,semilla):
        self.multiplicador = 16807
        self.modulo = 2147483647
        self.actual = semilla
    def siguiente(self):
        self.actual = (self.actual * self.multiplicador)%self.modulo    
        return self.actual
    def siguiente_entero(self,limite):
        return self.siguiente()%limite
    
        
    
        
        
            
            
           
     