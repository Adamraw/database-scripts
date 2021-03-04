#import modules
import os
import shutil
import re
from pathlib import Path
import argparse

#set up parser for command line interface arguments
parser = argparse.ArgumentParser(description="Iterates over subfolders containing Rmds, renames these Rmds to reflect their root folder/learning goal folder and places them into a single folder and repacks these Rmds back to their original root/learning goal folders.")
parser.add_argument('-i','--input_directory',type=str,metavar=' ',required = True, help = 'Source Directory - Specify filepath to root directory containing the Learning goal folders with Rmds.')
parser.add_argument('-o','--output_directory',type=str,metavar=' ',required = True, help = 'Target Directory - Specify filepath to output directory in which proccessed Rmds should be placed.')
parser.add_argument('-m','--mode',type=str,metavar=' ',required = True, help = 'Operation mode - \n defines which operation the program should carry out.\n Set to "UnPackRename" to unpack and rename Rmds from the specified input directory to the output directory \n | Set to "RenameFolders" to rename folders in the specified input directory and create a new directory containing the renamed folders at the output directory \n | Set to "Repack" to repack Rmds in the input directory to their corresponding learning goal folders in the output directory : Note the output directory should be formatted in the same way as the output directory returned by "RenameFolders".')
args = parser.parse_args()



#define file naming conventions
file_naming_convention = "Topic_"  # naming convention implementation
folder_naming_convention = 'Learning_goal_'

#define UnPackRenamer function
def UnPackRenamer(targetdir, rootdir):
    root_src_dir = rootdir
    root_target_dir = targetdir

    operation = 'copy'  # 'copy' or 'move'

    #loop over src_dir and sub_dirs in root_src_dir
    for src_dir, dirs, files in os.walk(root_src_dir):
        counter = 0  # counts number of iteration for each subfolder
        print(src_dir) #which folder we are in
        # if its not a directory make it one
        if not os.path.exists(root_target_dir):
            os.mkdir(root_target_dir)

        # FILE COPY
        #looping over files in folder
        for file_ in files:

            if src_dir == rootdir:
                continue
            counter += 1
            # reference to file we will copy
            src_file = os.path.join(src_dir, file_)

            #defining new file name
            new_file_name = src_dir + " " + "Q" + str(counter) + ".Rmd"
            new_file_name = new_file_name.replace(str(Path(root_src_dir)), "")


            #removing slashes for both windows and unix but it works ;)
            new_file_name = new_file_name.replace('\\variants', "")
            new_file_name = new_file_name.replace('/variants', "")
            new_file_name = new_file_name.replace('\\', "")
            new_file_name = new_file_name.replace('/', "")
            print(new_file_name)

            new_file_name = file_naming_convention + new_file_name
            print(new_file_name)
            new_file_name = new_file_name.replace(" ", "-")

            #generating file path for new file
            dst_file = os.path.join(root_target_dir, new_file_name)

            # if the file already exists in the dst directory, remove it.
            if os.path.exists(dst_file):
                os.remove(dst_file)
            if operation is 'copy':
                shutil.copy(src_file, dst_file)




#define RenameFolders function
def RenameFolders(rootdir ,targetdir):
    #setting up  filepaths
    root_src_dir = rootdir
    root_trg_dir = targetdir
    folder_list = []
    dir_list = []

    #loop over src_dir and sub_dirs in root_src_dir
    for src_dir,dir,files in os.walk(root_src_dir):

        if src_dir == root_src_dir:
            continue
        #generate new folder name
        new_folder_name = src_dir.replace(str(Path(root_src_dir)), "")
        new_folder_name = new_folder_name.replace('\\variants', "")
        new_folder_name = new_folder_name.replace('/variants', "")
        new_folder_name = new_folder_name.replace("\\" , "")
        new_folder_name = new_folder_name.replace("/" , "")
        new_folder_name = folder_naming_convention + new_folder_name
        new_folder_name = new_folder_name.replace(" ", "-")
        dst_dir = os.path.join(root_trg_dir,new_folder_name)
        #creating new folders
        if new_folder_name not in folder_list:
            os.makedirs(dst_dir)
            folder_list.append(new_folder_name)
            dir_list.append(dst_dir)




#defining the Repacker function
def Repacker(rootdir,targetdir):
    source_dir = rootdir
   # looping over files in folder containing Rmds to be copied over
    for src_dir,dir,files in os.walk(source_dir):

        for file in files:
            #generating the name for the learning goal folder in which they need to be placed in, (file_name is a bit of an ambiguous variable name here)
            file_name = file.replace("Topic_","")
            file_name = re.split("\-Q", file_name)
            print(file_name)
            trg_dst = os.path.join(targetdir, file_name[0])
            trg_dst = os.path.join(trg_dst,file)
            src_dir_struct = os.path.join(targetdir,folder_naming_convention + file_name[0])
            dir_file = os.path.join(source_dir,file)
            #move files from source_dir to new learning goal folder
            shutil.copy(dir_file,src_dir_struct)

#main function that is called when programming is run from the CLI, handles logic for which function to run
def main():
    if args.mode == "UnPackRename":
         UnPackRenamer(rootdir = args.input_directory,targetdir=args.output_directory)
    elif args.mode == "RenameFolders":
        RenameFolders(args.input_directory, args.output_directory)
    elif args.mode == "RePack":
        Repacker(rootdir=args.input_directory, targetdir=args.output_directory)
    else:
        print('Invalid operation, please specify a valid operation ("UnPackRename", "RenameFolders, "Repack") - See --help option for more information.')

if __name__ == '__main__':
    main()




