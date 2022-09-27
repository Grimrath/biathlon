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
    print(" "*4 + " ".join([str(i+1) for i in range(len(targets))]))
    print()
    print(" "*4 + targets_to_string(targets))
    print()
    return


def random_hit():
    return bool(randint(0, 1))


def shoot(targets, target_index):
    if random_hit():
        if is_open(targets[target_index]):
            close_target(target_index, targets)
            return "Hit on open target"
        else:
            return "Hit on closed target"
    else:
        return "Miss"


def parse_target(target_str):
    if not target_str.isnumeric() or int(target_str) not in range(1, 6):
        return
    return int(target_str) - 1


def main():
    board = new_targets()
    shots = 0
    splash()
    input("Press any key to continue...")
    while board != [1]*5:
        view_targets(board)
        print(shoot(board, parse_target(input("Select target to shoot: "))))
        shots += 1
    view_targets(board)
    print("Well done! All targets hit!")
    print(f"Total shots: {shots}")
    print(f"Accuracy: {round(5*100/shots)}%")
    print("Game over.")

    if input("Play again (y/n)? ").lower() == "y":
        main()


if __name__ == '__main__':
    main()
