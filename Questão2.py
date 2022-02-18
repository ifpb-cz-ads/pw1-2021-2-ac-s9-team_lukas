class Televisão:
     def __init__(self, min, max, inicial): #parametros no construtor
         self.ligada = False
         self.canal = inicial
         self.cmin = min
         self.cmax = max
     def muda_canal_para_baixo(self):
         if(self.canal-1 >= self.cmin):
               self.canal -= 1
     def muda_canal_para_cima(self):
         if(self.canal+1 <= self.cmax):
               self.canal += 1

tv=Televisão(1, 99, 9)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)