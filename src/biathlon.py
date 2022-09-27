from random import randint


def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    return


def open():
    return 0


def closed():
    return 1


def is_open(target):
    return target == open()


def is_closed(target):
    return target == closed()


def new_targets():
    return [open() for _ in range(5)]


def close_target(target_index, targets):
    targets[target_index] = closed()
    return targets


def hits(targets):
    return targets.count(closed())


def target_to_string(target):
    if is_closed(target):
        return "0 "
    elif is_open(target):
        return "* "
    return


def targets_to_string(targets):
    return "".join([target_to_string(target) for target in targets])


def view_targets(targets):
    print()
    print(" "*4 + " ".join([str(i) for i in range(len(targets))]))
    print()
    print(" "*4 + targets_to_string(targets))
    print()
    return


def random_hit():
    return bool(randint(0, 1))


