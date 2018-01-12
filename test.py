#test
h1 = ["Ks", "Kd", "Qs", "10s", "Kh", "Kc", "Js"]
h2 = ["7h", "3h", "4h", "5h", "6h", "7c", "7s"]

weight1 = 0
sum1 = 0

#checking on royal flush
from function_find_royalflush import royal_flush
royal_flush(h1)
from function_find_royalflush import ah
if ah == 1:
    weight1 = 10
print("RF = ", ah)

#checking on straight flush (hearts)
from function_find_straightflush_hearts import straight_flush_hearts
straight_flush_hearts(h1)
from function_find_straightflush_hearts import SF
from function_find_straightflush_hearts import sSF
if SF == 1:
    weight1 = 9
    sum1 = sSF
print("SF = ", SF, sSF)

#checking on straight flush (D)
from function_find_straightflush_d import straight_flush_d
straight_flush_d(h1)
from function_find_straightflush_d import SF
from function_find_straightflush_d import sSF
if SF == 1:
    weight1 = 9
    sum1 = sSF
print("SF = ", SF, sSF)

#checking on straight flush (C)
from function_find_straightflush_c import straight_flush_c
straight_flush_c(h1)
from function_find_straightflush_c import SF
from function_find_straightflush_c import sSF
if SF == 1:
    weight1 = 9
    sum1 = sSF
print("SF = ", SF, sSF)

#checking on straight flush (S)
from function_find_straightflush_s import straight_flush_s
straight_flush_s(h1)
from function_find_straightflush_s import SF
from function_find_straightflush_s import sSF
if SF == 1:
    weight1 = 9
    sum1 = sSF
print("SF = ", SF, sSF)

#checking on quads
from function_find_quads import quads
quads(h1)
from function_find_quads import Q
from function_find_quads import sQ
if Q == 1:
    weight1 = 8
    sum1 = sQ
print("Q = ", Q, sQ)

#checking on full house





