

class Transformador:
    def __init__(self):
        
        self.ruta=None
        self.glifo=[]
        self.glifos=[]
        self.tabla={1:{1:"Σ",5:"Λ",10:"Ω"},2:{1:"Ω",5:"Δ",10:"Φ"},3:{1:"Φ",5:"Ψ",10:"Ξ"},4:{1:"Ξ",5:""}}
        self.numeros=[]         
        self.n_individual=[]
    
    def cargar_datos(self,ruta): #Carga de datos, recibe el nombre del archivo como parametro
        
        self.ruta=ruta
        num=0
        self.glifo.clear() 
        try:
            with open(self.ruta,'r',encoding='utf-8') as archivo:
                
                for linea in archivo:
                    
                    linea=linea.strip()
                    
                    if linea.isdigit():
                        
                        num=(int(linea))
                        
                        if num < 4000 and num > 0:
                            
                            self.numeros.append(num)
                            self.transformar(num,1,0)
                            self.glifos.append(list(self.glifo))
                            self.glifo.clear()
                            
                        elif num==0:
                            break
                        else:  
                            
                            self.numeros.append(num)
                            self.glifos.append("ERROR: Número fuera de rango (1-3999).")   
                    else:
                        
                        self.numeros.append(linea)
                        self.glifos.append("ERROR: Formato de entrada inválido. No es un número.")
            
        except FileNotFoundError:
            
            print("No se encontro el archivo")
            
    def individual(self,numero): #Transforma un numero a la vez, se implementa en la interfaz
        
        self.glifo.clear()
        self.transformar(numero,1,0)
        self.n_individual.append(list(self.glifo))
        self.numeros.append(numero)
        self.glifos.append(list(self.glifo)) 
              
    def exportar(self): #Genera mi archivo salidaglifos.txt
        
        try:
            with open("salidaglifos.txt","w",encoding="utf-8") as archivo:
                
                for nume, glif in zip(self.numeros,self.glifos):
                    glif="".join(glif)
                    archivo.write(f"{nume} {glif}\n")    
                return True
            
        except Exception as e:
            
            print(f"Error al crear el archivo de texto {e}")
            return False
                   
    def transformar(self,num,nivel,n): #Funcion recursiva para mapeo de claves y transformación de numeros
        
        if num==0 and n==0:             #Condicción de parada
            self.glifo.reverse()
            return
        
        if n==0:
            n=num%10
            num=int(num/10)
            if n==0:
                self.transformar(num,nivel+1,0)
                return  
   
        if n in self.tabla[nivel]:
            self.glifo.append(self.tabla[nivel][n])
            self.transformar(num,nivel+1,0)
            
        else: 
            clave_sig=next((clave for clave in self.tabla[nivel] if clave > n),None)

            if clave_sig - n == 1:
                self.glifo.append(self.tabla[nivel][clave_sig])
                self.glifo.append(self.tabla[nivel][1])
                self.transformar(num,nivel+1,0)
                
            else:
                self.glifo.append(self.tabla[nivel][1])
                n-=1
                self.transformar(num,nivel,n)


        
if __name__=="__main__": #llamada inicial
    trans=Transformador()
    trans.cargar_datos("glifos.txt")
    trans.exportar()