import numpy as np

kierunki = [1, 1, -1, -1]

tablica = np.zeros((5, 5))
print(tablica)

ktore = 0
licz = 1
i = 0
j = 0
while 0 in tablica:

    while 0 in tablica:
        tablica[i][j] = licz
        licz += 1
        try:
            if tablica[i + kierunki[ktore]][j] == 0:
                i += kierunki[ktore]
            else:
                break
        except IndexError:
            break

    ktore += 1
    j += kierunki[ktore]

    if ktore > 3:
        ktore = 0

    while 0 in tablica:
        tablica[i][j] = licz
        licz += 1
        try:
            if tablica[i][j + kierunki[ktore]] == 0:
                j += kierunki[ktore]
            else:
                break
        except IndexError:
            break

    ktore += 1
    if ktore > 3:
        ktore = 0
    i += kierunki[ktore]

print(tablica)
