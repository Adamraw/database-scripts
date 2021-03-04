# database-scripts
A collection of python scripts for unpacking, moving,renaming and checking folders and Rmds files.


<b> Quick Start Guide </b>

Prerequisites:
R-exams must be installed and working.

Installation:

1. Download repository and place into desired directory.

2. Open favourite command line interface and move into direcoty containing the repository.

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
1. UnPackRenamer
2. DuplicateChecker
3. PDFChecker

References:
This repo contains fast-duplicate-finder by Carl Beech(https://github.com/carlbeech/fast-duplicate-finder). This is used by the DuplicateChecker script. 
