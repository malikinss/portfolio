'''
TODO:
        Given a sequence of numbers 𝑎1, 𝑎2, ..., 𝑎𝑛.
        We call a pair (𝑎𝑖, 𝑎𝑗) an inversion if:
            (𝑖 < 𝑗) and (𝑎𝑖 > 𝑎𝑗).

        For example, the sequence 3,1,4,2 has three inversions:
            (3,1)
            (3,2)
            (4,2)

        Each inversion is a pair of elements that violate the order.

        Implement the inversions() function that takes one argument:
            sequence — a sequence whose elements are numbers

        The function must return a single number — the number of
        inversions in the sequence.

NOTE:
        A sequence is an object that has a length and supports indexing.
        For example, objects of type list or range are sequences.
'''


def inversions(sequence: list[int]) -> int:
    inversion_count = 0

    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] > sequence[j]:
                inversion_count += 1

    return inversion_count


sequence = [3, 1, 4, 2]
print(inversions(sequence))
