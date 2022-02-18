class Televisão:
    def __init__(self, min, max, inicial): #parametros no construtor
        self.ligada = False
        self.canal = inicial
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if(self.canal-1 >= self.cmin):
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if(self.canal+1 <= self.cmax):
            self.canal += 1
        else:
            self.canal = self.cmin

tv1 = Televisão(1, 20, 8)
tv1.muda_canal_para_cima()
print(tv1.canal)
tv1.muda_canal_para_baixo()
print(tv1.canal)

tv2 = Televisão(1, 55, 5)
tv2.muda_canal_para_cima()
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)

tv3 = Televisão(1, 99, 1)
tv3.muda_canal_para_cima()
print(tv3.canal)
tv3.muda_canal_para_baixo()
print(tv3.canal)