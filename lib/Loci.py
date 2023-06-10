import re


class Loci:
    def __init__(self, line):
        self.chrom_position = None
        self.map_position = None

        splitter = re.compile("\s+")
        line_splitted = splitter.split(line)
        first_column_splitted = line_splitted[0].split("_")

        self.marker = line_splitted[0]
        self.map_position = line_splitted[1]

        if len(first_column_splitted) == 2:
            self.chrom_position = int(first_column_splitted[1])
