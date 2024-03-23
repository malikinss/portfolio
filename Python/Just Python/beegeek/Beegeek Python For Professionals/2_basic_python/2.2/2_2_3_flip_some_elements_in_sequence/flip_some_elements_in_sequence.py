'''
TODO:   
        A sequence of natural numbers from 1 to n inclusive is given. 

        Write a program that first arranges in reverse order part of the elements of this sequence from element number X to element number Y, and then from element number A to element number B.

NOTE:   
        Numbering of sequence members starts from one
'''
def generate_sequence(n):
    """Generates a sequence of natural numbers from 1 to n."""
    return [str(i) for i in range(1, n + 1)]

def flip_sequence(sequence):
    """Reverses the order of elements in the sequence."""
    return sequence[::-1]

def flip_segment_in_sequence(sequence, start_id, finish_id):
    """Flips a segment of the sequence from start_id to finish_id."""
    result_sequence = []
    
    # Extract the parts of the sequence
    before_segment = sequence[:start_id]
    segment = sequence[start_id:finish_id+1]
    flipped_segment = flip_sequence(segment)
    after_segment = sequence[finish_id+1:]

    # Construct the result sequence
    result_sequence.extend(before_segment)
    result_sequence.extend(flipped_segment)
    result_sequence.extend(after_segment)
    
    return result_sequence

def flip_some_elements_in_sequence(input_data):
    """Flips segments in the sequence based on the input data."""
    n, x, y, a, b = map(int, input_data.split())

    sequence = generate_sequence(n)

    # Flip the specified segments in the sequence
    sequence = flip_segment_in_sequence(sequence, x-1, y-1)
    sequence = flip_segment_in_sequence(sequence, a-1, b-1)

    return sequence

# Take user input and print the result
user_input = input("Enter values for n, X, Y, A, B: ")
result_sequence = flip_some_elements_in_sequence(user_input)
print(" ".join(result_sequence))