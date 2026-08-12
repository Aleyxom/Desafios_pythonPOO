from transportes import *

t1 = Moto(30)
t1.calc_frete()

t2 = Caminhao(49)
t2.calc_frete()

t3 = Caminhao(100)
t3.calc_frete()

t4 = Drone(9)
t4.calc_frete()

t5 = Drone(12)
t5.calc_frete()

t5.consultar()