#import modules
import os
from pathlib import Path
import platform
import argparse

#set up parser for command line interface arguments
parser = argparse.ArgumentParser(description="Find and delete duplicate files in target directory.")
parser.add_argument('-i','--input_directory',type=str,metavar=' ',required = True, help = 'Source Directory - Specify filepath to the directory in which duplicate files should be found.')
parser.add_argument('-m','--mode',type=str,metavar=' ', help = 'Optional mode parameter - set to "fd" to find and delete files in one go, set to "d" to delete files in the dup.sh/bat script or if left unspecified duplicate files will just be found and not deleted.')
args = parser.parse_args()

#define path to fdf_scanner, this script contains the duplicate checking logic
fdf_scanner_path = Path('./duplicate_scripts/fdf_scanner.py')

#define find_dups
def find_dups(src_dir,trg_dir = '.\dup' ):
    command = r'python {} -i {} -o {} -w '.format(fdf_scanner_path,src_dir,trg_dir)
    os.system(command)

#define remove_ups, runs dup file, which will delete found duplicate files. Toggle for OS
def remove_dups():
    if platform.system() == 'Windows':
        command = r'dup.BAT'
    else:
        command = r'dup.sh'
    os.system(command)

#main function that is called when script is run from the CLI, handles logic for which mode to run the function in
def main():
    #check if input_dir exists
    if os.path.exists(args.input_directory):
        #togggle for find and delete
        if args.mode == 'fd':
            find_dups(r'{}'.format(args.input_directory))
            remove_dups()
        #toggle for delete
        elif args.mode == 'd':
            remove_dups()
        #default
        else:
            find_dups(r'{}'.format(args.input_directory))
    else:
        print('Invalid filepath - filepath does not exist. Please specify a valid filepath.')






if __name__ == '__main__':
    main()






