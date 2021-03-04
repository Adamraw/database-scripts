# database-scripts
A collection of python scripts for unpacking, moving, renaming and checking folders and Rmds files.


<b> Quick Start Guide </b>

Prerequisites:
R-exams must be installed and the exams2pdf function must be working. (This is only neccesary if you want to utilize the PDFCheck.py script).

Installation:

1. Download repository and place into desired directory.

2. Open favorite command line interface and move into directory containing the repository.

3. Call scripts as shown below.

Usage:

```
python <scriptname>.py [-i] [-o] [-m]
```

Example:
```
python UnPackerRename.py -i C:\Users\AdamRaw\Desktop\LearningGoalFolderwithRmds -o C:\Users\AdamRaw\Desktop\FolderIWantRmdsIn -m "UnPackRename"
```

Call scripts with -h argument to see a list of all options.

All scripts that can be called are:
1. UnPackerRename
2. DuplicateCheck
3. PDFCheck

References:
This repo contains fast-duplicate-finder by Carl Beech(https://github.com/carlbeech/fast-duplicate-finder). This is used by the DuplicateCheck script. 
