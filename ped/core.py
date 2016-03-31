# -*- coding: utf-8 -*-

from string import whitespace
from ped_parser import (Individual, Family)
from argparse import ArgumentParser
from version import pedtools_version
from string import whitespace
from ped_parser import family, individual, parser
import logging
import os
import string
import sys

def parse_args():
    parser = ArgumentParser()
    # parser = ArgumentParser(description="Find variants from fastqs via a mapping-free approach.")
    parser.add_argument("--version", action='version', version='%(prog)s ' + pedtools_version)
    parser.add_argument("--ped", type=str, dest="ped", help="Input pedigree file (PLINK format)", required=True)
    # parser.add_argument("--vcf", type=str, dest="vcf", help="Input variant file (vcf)", required=True)
    # parser.add_argument("--output", type=str, dest="out", help="Output file (tabular)", required=True)
    parser.add_argument("--log", type=str, help="Logs progress in specified file, defaults to stdout.")
    parser.add_argument("-v", "--verbosity", action="count", default=0)

    args = parser.parse_args()

    return args

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    print get_hmm()

def get_pedigree(pedigree_file, pedigree_type):
    """Read pedigree file and return a pedigre object."""
    print "In get_pedigree: " + pedigree_file + ":" + pedigree_type
    pedigree_iter = open(pedigree_file, 'rU')
    my_parser = parser.FamilyParser(pedigree_iter, pedigree_type)
    print 'Families found in file: {0}'.format( \
        ','.join(list(my_parser.families.keys()))
    )

    return my_parser

def get_summary(my_parser, family_type):
    for family in my_parser.families:
        logging.info('Fam: {0}'.format(family))
        if family_type in ['cmms', 'mip']:
            logging.info('Expected Inheritance Models: {0}'.format(
                my_parser.families[family].models_of_inheritance
            )
        )
        logging.info('All Individuals: ')
        for individual in my_parser.families[family].individuals:
            logging.info(individual)

        logging.info('All Affected Individuals: ')
        for individual in my_parser.families[family].affected_individuals:
            logging.info(individual)

            #logging.info(my_parser.families[family].individuals[individual])
            #logging.info('Affected individuals: {0} \n'.format(
            #    ','.join(my_parser.families[family].affected_individuals)
            #    )
            #)

def main():
    """ Main function."""
    family_type = "ped"
    args = parse_args()
    if args.log:
        logfile = args.log
        logging.basicConfig(filename=logfile, level=logging.DEBUG, \
            filemode='w', format='%(asctime)s %(message)s', \
            datefmt='%Y-%m-%d %H:%M:%S')
            # datefmt='%d:%b:%Y|%H:%M:%S')

    else:
        logfile = sys.stdout

    logging.info('Start.')
    logging.info('Command line: {}'.format(' '.join(sys.argv)))
    my_parser = get_pedigree(args.ped,family_type)
    get_summary(my_parser,family_type)
    # logging.info()

if __name__ == '__main__':
    main()
