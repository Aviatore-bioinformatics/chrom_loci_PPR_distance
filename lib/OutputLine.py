class OutputLine:
    def __init__(self, marker, distance_on_map, gene, distance_from_ppr):
        self.marker = marker
        self.distance_on_map = distance_on_map
        self.gene = gene
        self.distance_from_ppr = distance_from_ppr

    def __str__(self):
        return f"{self.marker}\t{self.distance_on_map}\t{self.gene}\t{self.distance_from_ppr}"
