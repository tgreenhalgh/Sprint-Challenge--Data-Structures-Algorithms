Add your answers to the Algorithms exercises here.

```
a)  a = 0
    while (a < n * n * n) # (a < n^3)
      a = a + n * n # a += n^2
```

simplifies to O(n)

```
b)  sum = 0
    for (i = 0; i < n; i++) # O(n)
      for (j = i + 1; j < n; j++) # O(n / 2)
        for (k = j + 1; k < n; k++) # O(n / 4)
          for (l = k + 1; l < 10 + k; l++) # O(1)
            sum++
```

simplifies to O(n^3)

```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1) # O(n)
    }
```

O(n)

**Exercise II**:

Start on floor n/2

loop until have the floor where egg breaks and doesn't break difference of 1

- if egg breaks, go to half way down current floor and bottom and test again
- if egg doesn't break, go to half way up current floor and top and test again

This gives us O(log n) running time
