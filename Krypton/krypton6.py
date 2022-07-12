# spam a bunch of A's and encrypt -> get ct with cycle of 30
ct = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
pt = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

a = []
for i in range(len(ct)):
    a.append(ord(ct[i]) - ord(pt[i]))

a = a[:30]

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciph = "PNUKLYLWRQKGKBE"
msg = ""
for i, c in enumerate(ciph):
    ind = alpha.index(c)
    ind -= a[i % len(a)]
    if ind < 0:
        ind += 26
    msg += alpha[ind]
print(msg)