#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0    # O(1)
    while (a < n * n * n * n)    # O(n)
        a = a + n * n   # O(1)

    total runtime = O(n)


b)  sum = 0     # O(1)
    for i in range(n)   # O(n)
        j = 1       # O(1)
        while j < n     # O(n)
        j *= 2      # O(n*2)
        sum += 1    # O(1)

    total runtime = O(n^2)


c)  def bunnyEars(bunnies):     
        if bunnies = 0:     # O(1)
            return 0        # O(1)

        return 2 + bunnyEars(bunnies-1)     # O(n)

## Exercise II


some notes: eggs are broken if thrown off floor F or higher, do not break if dropped below floor F

if n-story > floor-f:
    don't throw egg
else:
    throw egg

ways to optimize floor: take amount of dropped eggs in the past from each floor to determine which floor is safe to throw eggs from

runtime complexity = O(n)??????