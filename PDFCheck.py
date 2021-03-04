#import modules
import argparse
import os


#set up parser for command line interface arguments
parser = argparse.ArgumentParser(description="Iterate over Rmds in specified directory and generate pdfs - (Executes GeneratePDF.R script to generate pdfs with exams2pdf function).")
parser.add_argument('-i','--input_directory',type=str,metavar=' ',required = True, help = 'Source Directory - Specify filepath to directory containing Rmds.')
args = parser.parse_args()

#main function that is called when script is run from the CLI
def main():
    # Define command and arguments
    command = 'Rscript GeneratePDF.R {}'.format(args.input_directory)
    # run os.system to run the command, this will call the GeneratePDF.R script with the supplied argument
    os.system(command)

if __name__ == '__main__':
    main()


