# Contexte

Enumerer les triplets Pythagoriciens :

$$a^2 + b^2 = c^2$$

Avec $a,b,c \le n$ et $a < b < c$

## Foction naïve

     Pour a de 1 à n-2:
        Pour b de a+1 à n-1:
            Pour c de b+1 à n:
                Si a*a + b*b = c*c:
                    Afficher(a, b, c)

## Idée 1

Stocker les carrés parfaits avec leur racine

    t <- tab de taille n*n + 1 init à None
    Pour c de 1 à n:
        t[c*c] <- c

    Pour a de 1 à n-2:
        Pour b de a+1 à n-1:
            Si t[a*a + b*b] non vide:
                Afficher (a, b, t[a*a + b*b])

## Idée 2
