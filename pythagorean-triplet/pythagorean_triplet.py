import math
# We can solve this with math:
# a < b < c (0)
# a^2 + b^2 = c^2 (1)
# a + b + c = N (2)
# From (2), we get c = N - a - b
# Applying that to (1):
# a ^2 + b^2 = (N - a - b)^2
# a^2 + b^2 = N ^2 + a^2 + b^2 - 2Na - 2Nb + 2ab
# 0 = N ^2 - 2Na - 2Nb + 2ab => 2Nb - 2ab = N^2 - 2Na
# 2b(N - a) = N^2 - 2Na
# b = (N^2 - 2Na)/ 2(N-a)
# If b is an integer, we got it!
# But we don't need to stop there.
# Using (0) with c, we get: a < b < N - a - b => a < N - a -b => a < (N-b) /2
# Also, b < N - a -b => b < (N-a) / 2 and since a < b, we get: a < (N-a) /2 => 2a < (N -a)
# So, 3a < N => a < N/3!

def triplets_with_sum(number):
    viable_triplets = []
    for a_candidate in range(1, int(number/3)):
        a_squared = a_candidate * a_candidate
        b_candidate = ((number * number) - (2 * number * a_candidate)) / (2 * (number - a_candidate))
        if b_candidate % 1 == 0:
            c_candidate_squared = (number - a_candidate - b_candidate) ** 2 # Equation(1)
            triplet = list(set([a_candidate, int(b_candidate), int(math.sqrt(c_candidate_squared))])) # Just to guarantee triplets are not repeated.
            if a_squared + b_candidate * b_candidate == c_candidate_squared and triplet not in viable_triplets:
                viable_triplets.append([a_candidate, int(b_candidate), int(math.sqrt(c_candidate_squared))])
    return viable_triplets
