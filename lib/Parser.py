from lib.Loci import Loci
from lib.Ppr import Ppr
import sys
from lib.OutputLine import OutputLine


class Parser:
    def __init__(self, args):
        self.args = args
        self.loci = []
        self.ppr = []

    def get_loci(self):
        with open(self.args.loci, 'r') as file:
            for line in file:
                self.loci.append(Loci(line))

    def get_ppr(self):
        with open(self.args.ppr, 'r') as file:
            for line in file:
                self.ppr.append(Ppr(line))

    def print_output(self, output):
        with open(self.args.output, 'w') as file:
            for line in output:
                file.write(f"{line.marker}\t{line.distance_on_map}\t{line.gene}\t{line.distance_from_ppr}\n")

    def get_output(self):
        self.get_loci()
        self.get_ppr()
        output = []

        for locus in self.loci:
            if locus.chrom_position is not None:
                closest_ppr = None
                min_distance = sys.maxsize
                for ppr in self.ppr:
                    diff = ppr.get_distance(locus.chrom_position)
                    if diff < min_distance:
                        min_distance = diff
                        closest_ppr = ppr
                output.append(OutputLine(locus.marker, locus.map_position, closest_ppr.loc, min_distance))
            else:
                output.append(OutputLine(locus.marker, locus.map_position, "", ""))

        return output

    def parse(self):
        output = self.get_output()

        self.print_output(output)
