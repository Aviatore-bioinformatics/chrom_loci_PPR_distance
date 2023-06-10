import math


class Ppr:
    def __init__(self, line):
        line_splitted = line.split("\t")
        if len(line_splitted) != 4:
            print(f"PPR class: some of the field is empty. Input line: {line}")
            exit(1)

        self.chrom = line_splitted[0]
        self.loc = line_splitted[1]
        self.start = int(line_splitted[2])
        self.end = int(line_splitted[3])

    def get_distance(self, pos: int):
        if self.start <= pos <= self.end:
            return 0

        v1 = abs(pos - self.start)
        v2 = abs(pos - self.end)

        return min(v1, v2)