#!/usr/bin/python3
# coding=utf-8


def take_pieces(n_pieces):
    return max(1,(n_pieces-1)%8)


if __name__ == "__main__":

    tests = [
        (1, None),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 6),
        (8, 7),
    ]

    for (test, correct_answer) in tests:
        answer = take_pieces(test)

        if answer not in (1, 2, 3, 4, 5, 6, 7):
            print("Funksjonen returnerte en ugyldig verdi: {:}".format(answer))

        if answer != correct_answer and correct_answer is not None:
            print(
                "Koden feilet for følgende antall fyrstikker: {:}".format(test)
            )
