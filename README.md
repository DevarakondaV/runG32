
This repo contains a python program that zips your CS project, uploads the zipped file to seasnet, unzips and compiles the program. You have the
option to run your file as well. Compilation errors and warnings are output to your local machine so you never have to directly ssh into seasnet. 

Note: If you're off campus make sure to connect to the UCLA vpn first.

| Platform | Working |
|----------|-------- |
|Windows 10| Yes     |
|Mac       | Haven't Testing|

### THIS PROGRAM IS NOT THE BE ALL END ALL. IT IS ONLY TO SPEED UP YOUR DEVELOPMENT SO YOU DON'T WASTE TIME GOING BACK AND FORTH BETWEEN MACHINES.
### USE AT YOUR OWN RISK. IF YOUR GRADE REKTS IT'S NO MY FAULT. MAKE SURE TO CHECK AGAIN DIRECTLY ON SEASNET BEFORE YOU SUBMIT YOUR PROJECT.

To run the package:


Requirements:
1) Install python3.7 and add it to path.
2) Install pipenv python [package](https://pypi.org/project/pipenv/): `pip install pipenv`

To run file:
1) Unzip contents
2) cd into directory
3) Install the required packages in a python virtual environment: `pipenv Install`
4) You can run the file with either:
   
    `pipenv run python packTest.py --host=<hostname> --user=<username> --passcode=<passcode> --projectname=<projectname> --filesDir=<filesDir>`
   
   or start the virtual environment: 

    `pipenv shell`
   
   then:
   
    `python packTest.py --host=<hostname> --user=<username> --passcode=<passcode> --projectname=<projectname> --filesDir=<filesDir>`

Arguments:

|Argument name | Required | Specifications|
|--------------|----------|---------------|
|--host        | No       | Defaults to cs32.seas.ucla.edu. It is the IP address for machine. |
|--user        | Yes      | Your seasnet username. |
|--passcode    | Yes      | Your seasnet passcode. |
|--projectname | Yes      | A UNIQUE project identifier. This will be the name of the zipped contents, directory, and executable on seasnet. |
|--filesDir    | Yes      | Location of all *.cpp, and *.h files for this project on local machine. |


Issues:
<br>
1) If you get the following output: 

`bash: g32: command not found`

Your project did not compile so don't try to run the file. You'll get an error.

You need to locate the g32 executable on your seasnet machine and change the following line in the packTest.py file

line 56:    `compile_command = "/path/to/g32 -o "+projectname+"/"+projectname+" "+projectname+"/"+"*.cpp"` 
<br>
2) Programs that require user inputs will not work.



