from random import random


threshold = 0


def main():
    global threshold
    board = new_targets()
    shots = 0
    splash()
    input("Press any key to continue...")
    threshold = select_difficulty()
    while board != [closed()]*5:
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
    global threshold
    return random() < threshold


def shoot(targets, target_index):
    if random_hit():
        if is_open(targets[target_index]):
            close_target(target_index, targets)
            return "Hit on open target"
        else:
            return "Hit on closed target"
    else:
        return "Miss"


def select_difficulty():
    diff = input("Select difficulty (hard, medium, easy): ").lower()
    if diff == "hard":
        return 0.2
    elif diff == "medium":
        return 0.5
    elif diff == "easy":
        return 0.75
    elif diff == "god_mode":
        return 1
    else:
        print("Invalid input! Try again...")
        return select_difficulty()


def parse_target(target_str):
    if not target_str.isnumeric() or int(target_str) not in range(1, 6):
        return
    return int(target_str) - 1


if __name__ == '__main__':
    main()
