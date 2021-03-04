#import modules
import os
from pathlib import Path
import platform
import argparse
import subprocess



parser = argparse.ArgumentParser(description="Iterate over Rmds in specified directory and generate pdfs - (Executes GeneratePDF.R script to generate pdfs with exams2pdf function).")
parser.add_argument('-i','--input_directory',type=str,metavar=' ',required = True, help = 'Source Directory - Specify filepath to directory containing Rmds.')
args = parser.parse_args()


def main():
    # Define command and arguments
    command = 'Rscript GeneratePDF.R {}'.format(args.input_directory)
    # check_output will run the command and store to result
    subprocess.run(command)

if __name__ == '__main__':
    main()


