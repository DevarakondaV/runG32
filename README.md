
This repo contains a python program that zips your CS project, uploads the zipped file to seasnet, unzips and compiles the program. You have the
option to run your file as well. Compilation errors and warnings are output to your local machine so you never have to directly ssh into seasnet. 

Note: If you're off campus make sure to connect to the UCLA vpn first.

| platform | Working |
|----------|-------- |
|Windows 10| Yes     |
|Mac       | Haven't Testing|

### THIS PROGRAM IS NOT THE BE ALL END ALL. IT IS ONLY TO SPEED UP YOUR DEVELOPMENT SO YOU DON'T WASTE TIME GOING BACK AND FORTH BETWEEN MACHINES.
### USE AT YOUR OWN RISK. IF YOUR GRADE REKTS IT'S NO MY FAULT. MAKE SURE TO CHECK AGAIN DIRECTLY ON SEASNET BEFORE YOU SUBMIT YOUR PROJECT.

To run the package:


Requirements:
1) Install python3.7 and add it to path
2) Install pipenv python [package](https://pypi.org/project/pipenv/): pip install pipenv

To run file:
1) Unzip contents
2) cd into directory
3) Install the required packages in a python virtual env: pipenv Install
4) You can run the file with either:
    pipenv run python packTest.py --host=<hostname> --user=<username> --passcode=<passcode> --projectname=<projectname> --filesDir=<filesDir>
   or start the virtual env: 
    pipenv shell
   then:
    python packTest.py --host=<hostname> --user=<username> --passcode=<passcode> --projectname=<projectname> --filesDir=<filesDir>

Arguments:

|Argument name | Required | Specifications|
|--------------|----------|---------------|
|--host        | No       | defaults to : cs32.seas.ucla.edu. It is the IP address for machine |
|--user        | Yes      | seasnet username |
|--passcode    | Yes      | seasnet passcode |
|--projectname | Yes      | UNIQUE project identifier. This will be the name of the zipped contents, directory, and executable on seasnet. |
|--filesDir    | Yes      | Location of all *.cpp, and *.h files for this project on local machine. |
