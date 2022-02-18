class Televisao:
    def __init__(self):
           self.ligada = False
           self.canal = 2
           self.tamanho = 42
           self.marca = "Sony"
    def muda_canal_para_baixo(self):
           self.canal -= 1
    def muda_canal_para_cima(self):
           self.canal += 1
    def imprime(self):
        print("A Marca da TV é %s e de %d polegadas"%(self.marca, self.tamanho))

tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.imprime()
