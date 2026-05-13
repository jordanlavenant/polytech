# TD2

## Exercice 1

- LI : Lire instrution
- DI : Décodage instruction
- LR : Lecture registre
- EX1 : Exécution 1
- ER : Ecriture résultat

### Démonstration

| instruction    | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADD RO, RO, R1 | LI  | DI  | LR  | EX  | ER  |     |     |     |
| ADD R2, R2, R3 |     | LI  | DI  | LR  | EX  | ER  |     |
| ADD R4, R2, R2 |     |     | LI  | DI  |     | LR  | EX  | ER  |

Pour le troisième ADD, lorsqu'il lit le registre R2 (LR), il a besoin d'attendre la fin de l'exécution de l'instruction précédente sur R2, donc il attend un cycle.

La latence du début existe car chaque instruction a une latence de 1, pour l'instruction suivante.

### P1

#### FMUL

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LI  | DI  | LR  | EX1 | EX2 | EX3 | EX4 | ER  |     |     |     |     |     |
|     | LI  | DI  |     |     |     |     | LR  | EX1 | EX2 | EX3 | EX4 | ER  |

L'instruction suivante a dû attendre **4 cycles** (on ignore la latence initiale)

#### FADD

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LI  | DI  | LR  | EX1 | EX2 | ER  |     |     |     |
|     | LI  | DI  |     |     | LR  | EX1 | EX2 | ER  |

L'instruction suivante a dû attendre **2 cycles** (on ignore la latence initiale)

### P2

#### FMUL

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LI  | DI  | LR  | EX1 | EX2 | EX3 | EX4 | EX5 | EX6 | ER  |     |     |     |     |     |     |     |
|     | LI  | DI  |     |     |     |     |     |     | LR  | EX1 | EX2 | EX3 | EX4 | EX5 | EX6 | ER  |

L'instruction suivante a dû attendre **6 cycles** (on ignore la latence initiale)

#### FADD

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LI  | DI  | LR  | EX1 | EX2 | EX3 | EX4 | ER  |     |     |     |     |     |
|     | LI  | DI  |     |     |     |     | LR  | EX1 | EX2 | EX3 | EX4 | ER  |

L'instruction suivante a dû attendre **4 cycles** (on ignore la latence initiale)

## Exercice 2

- **LF/SF** : (load/store float) 2 de lantences
- **FMUL** : (multiplication) 4 de latences (dans P1)
- **ADD** = (incrémentation) 1 de latence
- **BNE** = (lancement de la nouvelle itération) 1 de latence

`z[i] = x[i] * y[i]`

### P1

- LF (load float) pour x[i] (latence 2)
- LF (load float) pour y[i] (latence 2)
- FMUL (load float) pour x[i] (latence 4)
- SF (store float) pour z[i] (latence 2)

Donc :

| C   | I                |
| --- | ---------------- |
| 0   | LF, F0, x[i]     |
| 1   | LF, F1, y[i]     |
| 2   | ADD, R1, R1, 1   |
| 3   | FMUL, F2, F0, F1 |
| 4   |                  |
| 5   |                  |
| 6   |                  |
| 7   | SF, F2, z[i]     |
| 8   | BNE              |

Ainsi, une itération prend **9 cycles**.

On assume via l'architecture MIPS, que l'incrémentation de $i$ n'affecte pas le stockage/lecture des flottants.

### P2

- **FMUL** : 6 de latences (dans P2)

Donc :

| C   | I                |
| --- | ---------------- |
| 0   | LF, F0, x[i]     |
| 1   | LF, F1, y[i]     |
| 2   | ADD, R1, R1, 1   |
| 3   | FMUL, F2, F0, F1 |
| 4   |                  |
| 5   |                  |
| 6   |                  |
| 7   |                  |
| 8   |                  |
| 9   | SF, F2, z[i]     |
| 10  | BNE              |

Ainsi, une itération prend **11 cycles**.

### Ordre 2 (P1)

| C   | I                |
| --- | ---------------- |
| 0   | LF, F0, x[i]     |
| 1   | LF, F1, y[i]     |
| 2   | LF, F2, x[i+1]   |
| 3   | LF, F3, y[i+1]   |
| 4   | FMUL, F4, F0, F1 |
| 5   | FMUL, F5, F2, F3 |
| 6   | ADD, R1, R1, 2   |
| 7   |                  |
| 8   | SF, F4, z[i]     |
| 9   | SF, F5, z[i]     |
| 10  | BNE              |

Ainsi, 2 itérations prend **11 cycles**, donc 1 itération prend **5.5 cycles**

### Ordre 2 (P2)

| C   | I                |
| --- | ---------------- |
| 0   | LF, F0, x[i]     |
| 1   | LF, F1, y[i]     |
| 2   | LF, F2, x[i+1]   |
| 3   | LF, F3, y[i+1]   |
| 4   | FMUL, F4, F0, F1 |
| 5   | FMUL, F5, F2, F3 |
| 6   | ADD, R1, R1, 2   |
| 7   |                  |
| 8   |                  |
| 9   |                  |
| 10  | SF, F4, z[i]     |
| 11  | SF, F5, z[i]     |
| 12  | BNE              |

Ainsi, 2 itérations prend **13 cycles**, donc 1 itération prend **6.5 cycles**.

### Ordre 4 (P1)

| C   | I                 |
| --- | ----------------- |
| 0   | LF, F0, x[i]      |
| 1   | LF, F1, y[i]      |
| 2   | LF, F2, x[i+1]    |
| 3   | LF, F3, y[i+1]    |
| 4   | LF, F4, x[i+2]    |
| 5   | LF, F5, x[i+2]    |
| 6   | LF, F6, x[i+3]    |
| 7   | LF, F7, x[i+3]    |
| 8   | ADD, R1, R1, 4    |
| 9   | FMUL, F10, F0, F1 |
| 10  | FMUL, F11, F2, F3 |
| 11  | FMUL, F12, F4, F5 |
| 12  | FMUL, F13, F6, F7 |
| 13  | SF, F10, z[i]     |
| 14  | SF, F11, z[i]     |
| 15  | SF, F12, z[i]     |
| 16  | SF, F13, z[i]     |
| 17  | BNE               |

Ainsi, 4 itérations prend **18 cycles**, donc 1 itération prend **4.5 cycles**.

### Ordre 4 (P2)

| C   | I                 |
| --- | ----------------- |
| 0   | LF, F0, x[i]      |
| 1   | LF, F1, y[i]      |
| 2   | LF, F2, x[i+1]    |
| 3   | LF, F3, y[i+1]    |
| 4   | LF, F4, x[i+2]    |
| 5   | LF, F5, x[i+2]    |
| 6   | LF, F6, x[i+3]    |
| 7   | LF, F7, x[i+3]    |
| 8   | FMUL, F10, F0, F1 |
| 9   | FMUL, F11, F2, F3 |
| 10  | FMUL, F12, F4, F5 |
| 11  | FMUL, F13, F6, F7 |
| 12  | ADD, R1, R1, 4    |
| 13  |                   |
| 14  | SF, F10, z[i]     |
| 15  | SF, F11, z[i]     |
| 16  | SF, F12, z[i]     |
| 17  | SF, F13, z[i]     |
| 18  | BNE               |

Ainsi, 4 itérations prend **19 cycles**, donc 1 itération prend **4.75 cycles**.

## Exercice 3

### Somme des carrés (P1)

| C   | I                 |
| --- | ----------------- |
| 0   | LF, F1, x[i]      |
| 1   | ADD, R1, R1, 1    |
| 2   | FMUL, F10, F1, F1 |
| 3   |                   |
| 4   |                   |
| 5   |                   |
| 6   | FADD, F0, F0, F10 |
| 7   | BNE               |

Ainsi, 1 itération prend **8 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps

### Somme des carrés (P2)

| C   | I                 |
| --- | ----------------- |
| 0   | LF, F1, x[i]      |
| 1   | ADD, R1, R1, 1    |
| 2   | FMUL, F10, F1, F1 |
| 3   |                   |
| 4   |                   |
| 5   |                   |
| 6   |                   |
| 7   |                   |
| 8   | FADD, F0, F0, F10 |
| 9   | BNE               |

Ainsi, 1 itération prend **10 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps

### Somme des carrés (ordre 2 P1)

| C   | I                  |
| --- | ------------------ |
| 0   | LF, F1, x[i]       |
| 1   | LF, F2, x[i+1]     |
| 2   | FMUL, F10, F1, F1  |
| 3   | FMUL, F11, F2, F2  |
| 4   | ADD, R1, R1, 2     |
| 5   |                    |
| 6   | FADD, F0, F0, F10  |
| 6   | FADD, F90, F0, F11 |
| 7   | BNE                |

Et

| I                 |
| ----------------- |
| FADD, F0, F0, F90 |

Ainsi, 2 itération prend **8 cycles**, donc 1 itération prend **4 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps

### Somme des carrés (ordre 4 P1)

| C   | I                  |
| --- | ------------------ |
| 0   | LF, F1, x[i]       |
| 1   | LF, F2, x[i+1]     |
| 2   | LF, F3, x[i+2]     |
| 3   | LF, F4, x[i+3]     |
| 4   | FMUL, F10, F1, F1  |
| 5   | FMUL, F11, F2, F2  |
| 6   | FMUL, F12, F3, F3  |
| 7   | FMUL, F13, F4, F4  |
| 8   | ADD, R1, R1, 4     |
| 9   | FADD, F0, F0, F10  |
| 10  | FADD, F90, F0, F11 |
| 11  | FADD, F91, F0, F12 |
| 12  | FADD, F92, F0, F13 |
| 13  | BNE                |

Et

| I                 |
| ----------------- |
| FADD, F0, F0, F90 |
| FADD, F0, F0, F91 |
| FADD, F0, F0, F92 |

Ainsi, 4 itération prend **14 cycles**, donc 1 itération prend **3.5 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps

### Somme des carrés (ordre 2 P2)

| C   | I                  |
| --- | ------------------ |
| 0   | LF, F1, x[i]       |
| 1   | LF, F2, x[i+1]     |
| 2   | FMUL, F10, F1, F1  |
| 3   | FMUL, F11, F2, F2  |
| 4   | ADD, R1, R1, 2     |
| 5   |                    |
| 6   |                    |
| 7   |                    |
| 8   | FADD, F0, F0, F10  |
| 9   | FADD, F90, F0, F11 |
| 10  | BNE                |

Et

| I                 |
| ----------------- |
| FADD, F0, F0, F90 |

Ainsi, 2 itération prend **11 cycles**, donc 1 itération prend **5.5 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps

### Somme des carrés (ordre 4 P2)

| C   | I                  |
| --- | ------------------ |
| 0   | LF, F1, x[i]       |
| 1   | LF, F2, x[i+1]     |
| 2   | LF, F3, x[i+2]     |
| 3   | LF, F4, x[i+3]     |
| 4   | FMUL, F10, F1, F1  |
| 5   | FMUL, F11, F2, F2  |
| 6   | FMUL, F12, F3, F3  |
| 7   | FMUL, F13, F4, F4  |
| 8   | ADD, R1, R1, 4     |
| 9   |                    |
| 10  | FADD, F0, F0, F10  |
| 11  | FADD, F90, F0, F11 |
| 12  | FADD, F91, F0, F12 |
| 13  | FADD, F92, F0, F13 |
| 14  | BNE                |

Et

| I                 |
| ----------------- |
| FADD, F0, F0, F90 |
| FADD, F0, F0, F91 |
| FADD, F0, F0, F92 |

Ainsi, 4 itération prend **15 cycles**, donc 1 itération prend **3.75 cycles**.

On additionne F10 dans F0 `s`, ce qui store la nouvelle valeur de `s` en même temps
