# TD3

## Exercice 1

- **Adresse mémoire :** Etiquette | Index | Adresse dans bloc
- **Ligne de cache :** Etiquette | Contrôle | Instructions ou données

### 1.1 / 1.2 / 1.3

Exemple pour $16$ bits :

`0000 0011 0001 0001`

8 octet/Ligne = $2^3$ (3 bits)

16 Lignes = $2^4$ (4 bits)

#### Adresse de bloc (3 bits) : `001`

`0000 0011 0001 0[001]`

#### Index (4 bits) : `0010`

`0000 0011 0[001 0]001`

#### Etiquette : `0000 0011 0`

`[0000 0011 0]001 0001`

---

**Mémoire principale :** 2 Gio $= 2^{31}$

#### 1

2 Mio $= 2^{21}$

16 octets par ligne $= 2^4$ $\rightarrow$ (ADDR)

$\rightarrow 2^{21} / 2^4 = 2^{17}$ lignes $\rightarrow$ 17 bits d'adresse (INDEX)

Etiquette : $31 - 17 - 4 = 10$ bits (ETIQUETTE)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 10        | 17    | 4    |

**Surcoût :** $\frac{10+1}{128} = 8.6$%

- $10$: bits pour etiquette
- $1$: bit de contrôle
- $128$: $16*8$

---

#### 2

4 Mio $= 2^{22}$

32 octets par ligne $= 2^5$ $\rightarrow$ (ADDR)

$\rightarrow 2^{22} / 2^5 = 2^{17}$ lignes $\rightarrow$ 17 bits d'adresse (INDEX)

2 Gio $= 2^{31}$

Etiquette : $31 - 17 - 5 = 9$ bits (ETIQUETTE)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 9         | 17    | 5    |

**Surcoût :** $\frac{9+2}{256} = 4.3$%

- $9$: bits pour etiquette
- $2$: bits de contrôle
- $256$: $32*8$

---

#### 3

4 Mio $= 2^{22}$

32 octets par ligne $= 2^5$ $\rightarrow$ (ADDR)

$\rightarrow 2^{22} / 2^5 = 2^{17}$ lignes $\rightarrow$ 17 bits d'adresse (INDEX)

Nous somme en cache **associatif**, donc on divise l'index par le nombre de voies :

$2^{17} / 2^2 = 2^{15}$ lignes
$\rightarrow 2^{22} / 2^5 = 2^{17}$ lignes

$\rightarrow$ 15 bits d'adresse (INDEX)

Etiquette : $31 - 15 - 5 = 11$ bits (ETIQUETTE)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 11        | 15    | 5    |

**Surcoût :** $\frac{11+2}{256} = 5$%

- $11$: bits pour etiquette
- $2$: bits de contrôle
- $256$: $32*8$

---

## Exercice 2

### 2.1

8 Kio $= 2^{13}$

#### 1er cas

32 octets par ligne $= 2^5$ $\rightarrow$ (ADDR)

$\rightarrow 2^{13} / 2^5 = 2^{8}$ lignes $\rightarrow$ 8 bits d'adresse (INDEX)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 19        | 8     | 5    |

#### 2e cas

32 octets par ligne $= 2^5$ $\rightarrow$ (ADDR)

$\rightarrow 2^{13} / 2^5 = 2^{8}$ lignes $\rightarrow$ 8 bits d'adresse (INDEX)

Associativité d'ensemblesde 2 blocs

$\rightarrow 2^8 / 2^1 = 2^{7}$ lignes $\rightarrow$ 7 bits d'adresse (INDEX)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 20        | 7     | 5    |

### 2.2

Le cache peut stocker 8 Kio octets organisé en blocs de **32 octets**.

Float = 32 bits = **4 octets**

$\rightarrow$ Donc par bloc, on peut stocker **8 floats**.

---

- ADDR $2^5$ (5 emplacements)
- INDEX $2^8$ (8 emplacements)

| X   | 0     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 000[0 | 0000 | 000][0 | 0000] |

| Y   | 4     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 010[0 | 0000 | 000][0 | 0000] |

| Z   | 8     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 100[0 | 0000 | 000][0 | 0000] |

| X1  | C     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 110[0 | 0000 | 000][0 | 0000] |

| Y1  | 0     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 000[0 | 0000 | 000][0 | 0000] |

| X2  | 4     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 010[0 | 0000 | 000][0 | 0000] |

| Y2  | 8     | 0    | 0      | 0     |
| --- | ----- | ---- | ------ | ----- |
|     | 100[0 | 0000 | 000][0 | 0000] |

$X = Y = Z = X1 = Y1 = X2 = Y2$

Donc les variables sont **TOUTES** à la même position du bloc dans le cache.

#### 1.

    for (i = 0; i < N; ++i)
    {
        s += X[i] * Y[i]
    }

$2$ défauts de cache / itération car $X[i]$ et $Y[i]$ sont sur la même ligne du cache.

$\rightarrow 2D/it$

#### 2.

    for (i = 0; i < N; ++i)
    {
        s1 += X1[i] + Y1[i]
        s2 += X2[i] + Y2[i]
    }

$\rightarrow 4D/it$

#### 3.

    for (i = 0; i < N; ++i)
    {
        s1 += X1[i] + Y1[i]
    }

    for (i = 0; i < N; ++i)
    {
        s2 += X2[i] + Y2[i]
    }

$\rightarrow 2D/it$

#### 4.

    for (i = 0; i < N; ++i)
    {
        s1 += X[i] + Y[i]
        s2 += X[i] + Z[i]
    }

$\rightarrow 4D/it$

---

## Exercice 3

### 3.1

**Mémoire principale :** 1 Mio $= 2^{20}$

4 Kio $= 2^{12}$

64 octets par ligne $= 2^6$ $\rightarrow$ (ADDR)

$\rightarrow 2^{12} / 2^6 = 2^{6}$ lignes $\rightarrow$ 6 bits d'adresse (INDEX)

Or, on est associatif, avec 4 blocs par ensemble.

$\rightarrow 2^{6} / 2^2 = 2^{4}$ lignes $\rightarrow$ 4 bits d'adresse (INDEX)

Etiquette : $20 - 4 - 6 = 10$ bits (ETIQUETTE)

| ETIQUETTE | INDEX | ADDR |
| --------- | ----- | ---- |
| 10        | 4     | 6    |

### 3.2

#### Données

On lit 4352 octets, 10 fois.

Accès à 1 bloc = 1 unité + 10 si le bloc n'est pas dans le cache.

#### Temps sans cache

- Accès total = $4352 * 10 = 43 520$ accès
- Sans cache, chaque accès coûte $1 + 10 = 11$ unités
- Temps total sans cache $43520 * 11 = 478720$ unités.

$\rightarrow$ 478 720 unités

#### Temps avec cache

$\frac{4352}{64} = 68$ lignes de cache

- 1ère itération : $68$ défauts de cache (car on créer tout).
- $n$-itération : $4 * 5$ défauts de cache (4 premiers ensemble ont 5 défauts de cache).
