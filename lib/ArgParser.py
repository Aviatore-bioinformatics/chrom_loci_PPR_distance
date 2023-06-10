# Example of a file content with PPRs
# chr9	LOC108203043	33194631	33202592
# chr9	LOC108203041	18028839	18031378
# chr9	LOC108202973	8278173	8286338

# Example of a file content with the chromosome map
# chr9_5197831            0.000  ;   66
# chr9_12136880           0.518  ;  139
# chr9_5159780           17.169  ;   65

import argparse


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-l", "--loci", help="The txt version of the chromosome map", required=True)
    arg_parser.add_argument("-p", "--ppr", help="The file with a table of PPRs", required=True)
    arg_parser.add_argument("-o", "--output", help="The output file name", required=True)

    return arg_parser.parse_args()