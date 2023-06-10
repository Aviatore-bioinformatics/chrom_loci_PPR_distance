import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")
from lib.Loci import Loci
from lib.Ppr import Ppr
from lib.Parser import Parser
from lib.OutputLine import OutputLine


class ParserTests(unittest.TestCase):
    def test_locus_within_ppr(self):
        parser = Parser("")
        parser.get_ppr = MagicMock(return_value=None)
        parser.get_loci = MagicMock(return_value=None)
        parser.loci = [
            Loci("chr9_200            0.000  ;  101"),
        ]
        parser.ppr = [
            Ppr("chr9	LOC108203043	150	250")
        ]

        output = parser.get_output()
        expected_output = [
            OutputLine(marker="chr9_200", distance_from_ppr=0, distance_on_map="0.000", gene="LOC108203043")
        ]
        self.assertEqual(str(output[0]), str(expected_output[0]))

    def test_locus_outside_left_ppr(self):
        parser = Parser("")
        parser.get_ppr = MagicMock(return_value=None)
        parser.get_loci = MagicMock(return_value=None)
        parser.loci = [
            Loci("chr9_200            0.000  ;  101"),
        ]
        parser.ppr = [
            Ppr("chr9	LOC108203043	250	350")
        ]

        output = parser.get_output()
        expected_output = [
            OutputLine(marker="chr9_200", distance_from_ppr=50, distance_on_map="0.000", gene="LOC108203043")
        ]
        self.assertEqual(str(output[0]), str(expected_output[0]))

    def test_locus_outside_right_ppr(self):
        parser = Parser("")
        parser.get_ppr = MagicMock(return_value=None)
        parser.get_loci = MagicMock(return_value=None)
        parser.loci = [
            Loci("chr9_400            0.000  ;  101"),
        ]
        parser.ppr = [
            Ppr("chr9	LOC108203043	250	350")
        ]

        output = parser.get_output()
        expected_output = [
            OutputLine(marker="chr9_400", distance_from_ppr=50, distance_on_map="0.000", gene="LOC108203043")
        ]
        self.assertEqual(str(output[0]), str(expected_output[0]))


if __name__ == '__main__':
    unittest.main()
