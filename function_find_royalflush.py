HRF = ["10h", "Jh", "Qh", "Kh", "Ah"]
DRF = ["10d", "Jd", "Qd", "Kd", "Ad"]
CRF = ["10c", "Jc", "Qc", "Kc", "Ac"]
SRF = ["10s", "Js", "Qs", "Ks", "As"]
hand1RF = 0
hand2RF = 0
ah = 0
def royal_flush(lst):
    rH = 0
    rH = len(list(set(lst) & set(HRF)))
    if rH >=5:
        global ah
        ah = rH
    rD = 0
    rD = len(list(set(lst) & set(DRF)))
    if rD >=5:
        ah = rD
    rC = 0
    rC = len(list(set(lst) & set(CRF)))
    if rC >=5:
        ah = rC
    rS = 0
    rS = len(list(set(lst) & set(SRF)))
    if rS >=5:
        ah = rS
    if ah >=5:
        ah = 1

