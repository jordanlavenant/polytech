# TD1

## 1 Quatre modèles d'éxecution

### Q1

- M0

```
PUSH B
PUSH C
ADD
POP  A
```

4 instructions, 3 accès mémoire

- M1

```
LOAD  B
ADD   C
STORE A
```

3 instructions, 3 accès mémoire

- M2

```
LOAD  R0, B
ADD   R0, C
STORE R0,  A
```

3 instructions, 3 accès mémoire

- M3

```
LOAD  R0, B
LOAD  R1, C
ADD   R0, R1, R0
STORE R0, A
```

4 instructions, 3 accès mémoire

### Q2

- M0

```
PUSH B
PUSH C
ADD
POP  A

PUSH A
PUSH C
ADD
POP  B

PUSH A
PUSH B
SUB
POP  D
```

12 instructions, 9 accès mémoire

- M1

```
LOAD  B
ADD   C
STORE A

ADD   C
STORE B

LOAD  A
SUB   B
STORE D
```

8 instructions, 8 accès mémoire

- M2

```
LOAD  R0, B
ADD   R0, C
STORE R0, A

ADD   R0, C
STORE R0, B

LOAD  R0, A
SUB   R0, B
STORE R0, D
```

8 instructions, 8 accès mémoire

- M3

```
LOAD  R0, B
LOAD  R1, C
ADD   R2, R0, R1
STORE R2, A

ADD   R3, R1, R2
STORE R3, B

SUB   R4, R2, R3
STORE R4, D
```

8 instructions, 5 accès mémoire

### Q3

- M0

```
PUSH A
PUSH B
ADD

PUSH C
PUSH D
ADD

MUL

PUSH D
PUSH E
MUL

ADD

POP W
```

12 instructions, 7 accès mémoire

- M1

```
LOAD A
ADD B
STORE T

LOAD C
ADD D

MUL T
STORE T

LOAD D
MUL E

ADD T

STORE W
```

11 instructions, 11 accès mémoire

- M2

```
LOAD  R0, A
ADD   R0, B
STORE R0, T

LOAD  R0, C
ADD   R0, D

MUL   R0, T
STORE R0, T

LOAD  R0, D
MUL   R0, E

ADD   R0, T

STORE R0, W
```

11 instructions, 11 accès mémoire

- M3

```
LOAD  R0, A
LOAD  R1, B

LOAD  R2, C
LOAD  R3, D

LOAD  R4, E

ADD   R5, R0, R1
ADD   R6, R2, R3

MUL   R5, R5, R6

MUL   R6, R3, R4
ADD   R5, R5, R6

STORE R5, W
```

11 instructions, 6 accès mémoire

## 2 Instructions arithmétiques et logiques

### Q4 signé

min = -2^31
max = 2^31 - 1

### Q5 non-signé

min = 0
max = 2^32 - 1

### Q6

#### a

R8 : 0x80002016

3 => 0011 => positif
5 => 0101 => positif
8 => 1000 => négatif => overflow des bornes signés

#### b

R9 : 0x162468ACE

C => 1100 => négatif
A => 1010 => négatif
Troncation : 0x62468ACE
6 => 0110 => positif => underflow

(car l'addition de 2 nombres négatifs, ne devrait donner un nombre positif)

#### c

R10 : 0xDFFFFFEA

3 => 0011 => positif
5 => 0101 => positif
D => 1101 => négatif => good car 3-5 < 0

#### d

R11 : 0x22222222

C => 1100 => négatif
A => 1010 => négatif
2 => 0010 => positif => good

#### e

R8 : 0x80002016

Le résultats est codé en 32 bits => good

#### f

R9 : 0x162468ACE

Le résultat est codé en 33 bits => pas good

### Q7

- 0 0 => 0 (deux positifs => positif)
- 1 1 => (deux négatifs => négatif)

### Q8

#### a

```
SLL R2, R1, 3
```

#### b

```
SLL R2, R1, 3
SLL R3, R1, 1
ADD R0, R2, R3
```

#### c

```
SLL R2, R1, 5
# Décaler de 5 bits

SUB R2, R2, R1
# Soustraire le nombre de base
```

## 3 Variante ARM (optionnel)

### Q9

#### a

```
MOV R0, R1 LSL#3 # R0 = (R1 << 3) = R1 * 8
```

#### b

```
MOV R0, R1 LSL#3
ADD R0, R1 LSL#1
```

#### c

```
RSB R2, R1, R1 LSL#5
```
