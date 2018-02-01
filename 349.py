def box_stack(num_stacks, boxes):
    tot = sum(boxes);
    if tot % num_stacks == 0:
        target = tot / num_stacks
        for i in range(0, num_stacks):
            stack = meet_target(boxes, target)
            if stack is not None:
                print stack
            else:
                raise SystemError('couldnt build stack')
    else:
        print '(nothing)'


def meet_target(remaining, target):
    if target in remaining:
        remaining.remove(target)
        return [target]
    if target == 0:
        return None
    for i in range(target - 1, 0, -1):
        if i in remaining:
            remaining.remove(i)
            got_it = meet_target(remaining, target - i)
            if got_it is not None:
                got_it.append(i)
                return got_it
            else:
                remaining.append(i)


def read_input(input):
    stack_string, boxes_string = input.split(' ')
    num_stacks = int(stack_string)
    boxes = list(map(int, list(boxes_string)))
    box_stack(num_stacks, boxes)


read_input('4 064876318535318')
