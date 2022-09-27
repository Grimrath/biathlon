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
