#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 20, 11, 2026
# This program uses nested loops to
# print RGB colours.


def main():
    counterR = 0
    counterG = 0
    counterB = 0

    # add the for loops
    for counterR in range(counterR, 3):
        for counterG in range(counterG, 3):
            for counterB in range(counterB, 3):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        counterR,
                        counterG,
                        counterB,
                        "RGB("
                        + str(counterR)
                        + ","
                        + str(counterG)
                        + ","
                        + str(counterB)
                        + ")",
                    )
                )


if __name__ == "__main__":
    main()
