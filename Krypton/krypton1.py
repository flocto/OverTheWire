# ROT13
import string
ct = "YRIRY GJB CNFFJBEQ EBGGRA"

alpha = string.ascii_uppercase

for i in range(26): # 26 rotations, (13, 14)
    msg = ""
    for c in ct:
        if c in alpha:
            ind = alpha.index(c)
            ind -= i
            if ind < 0:
                ind += 26
            msg += alpha[ind]
        else:
            msg += c
    print(msg)

# best one is i = 13