# Cache

## AXPY

Exemple :

    for (int i = 0; i < n; ++i)
    {
        Y[i] += A * X[i]
    }

**3 accès mémoire :**

- Accès pour lire Y[i]
- Accès pour écrire le nouveau Y[i]
- Accès pour lire X[i]

**2 instructions**

$I = \frac{2}{3}$ ($\frac{instruction}{acces}$)

**Exemple cache :**

- $64$ octets $/ l$
- Double (8 octet)

$r_d = \frac{1}{8} = 12.5$%

En gros, toutes les 8 accès, on créer une nouvelle ligne de cache.
