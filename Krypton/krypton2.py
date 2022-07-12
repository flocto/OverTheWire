# Caesar cipher bash
import string
ct = "OMQEMDUEQMEK"

alpha = string.ascii_uppercase

for i in range(26): # 26 rotations, (12, 13)
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
    print(msg, i)

# best one is i = 12
# CAESARISEASY