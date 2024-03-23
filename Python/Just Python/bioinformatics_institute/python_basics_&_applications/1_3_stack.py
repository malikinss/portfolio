def get_top(stack):
    return len(stack) - 1

def push(stack, element):
    stack.append(element)
    top = get_top(stack)

    return stack, top

def pop(stack):
    top = get_top(stack)
    poped_element = stack.pop(top)
    top = get_top(stack)

    return stack, top, poped_element


stack = [1, 2, 3, 4]
top = get_top(stack)

print(f'stack = {stack}, top = {top}, stack_len = {len(stack)}')

stack, top = push(stack, 7)
stack, top = push(stack, 8)
stack, top = push(stack, 3)
stack, top = push(stack, 7)

print(f'stack = {stack}, top = {top}, stack_len = {len(stack)}')

stack, top, element = pop(stack)
stack, top, element = pop(stack)

print(element)
print(f'stack = {stack}, top = {top}, stack_len = {len(stack)}')