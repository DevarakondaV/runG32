from zipfile import ZipFile
import argparse
import paramiko
import os
import re

def zip_files(directory,projectname):
    """Function zips files in directory
    directory: String. Path to files
    projectname: string. name fo the project
    """
    
    zip_file_name = projectname+".zip"
    #grab files
    files = [i for i in os.listdir() if re.search(".*\.(cpp|h)",i)]

    #zip files
    with ZipFile(zip_file_name,"w") as zip:
        for f in files:
            zip.write(f)
    print("ZIPPED FILES: ",directory+"\\"+zip_file_name)
    return directory+"\\"+zip_file_name


def cpy_to_host(ssh_client,zipped_path,projectname):
    """Function copies to home directory of user at hostname
    ssh_client: SSH Object. 
    zipped_path: String. Zipped files path
    projectname: Stirng. 
    """

    #Deletes the files in host if this command was run once before
    stdin, stdout, stderr = ssh_client.exec_command("rm -rf "+projectname+".zip "+projectname)

    print("Uploading Files")
    ftp_client = ssh_client.open_sftp()
    ftp_client.put(zipped_path,projectname+".zip")
    ftp_client.close()
    print("Upload Complete")


def unzip_compile(ssh_client,projectname):
    """Function unzips and compiles on host. Prints out the response
    ssh_client: SSH Object.
    projectname: String.
    """

    ishell = ssh_client.invoke_shell()

    print("UNZIPPING FILES AND COMPILING")
    unzipcommand = "unzip "+projectname+".zip"+" -d "+projectname
    stdin, stdout,stderr = ssh_client.exec_command(unzipcommand)
    for line in stdout.readlines():
       print(line)

    print("COMPILING")
    compile_command = "/usr/local/cs/bin/g32 -o "+projectname+"/"+projectname+" "+projectname+"/"+"*.cpp"
    stdin, stdout,stderr = ssh_client.exec_command(compile_command)
    lines = stdout.readlines()
    for line in lines:
       print(line)
    lines = stderr.readlines()
    for line in lines:
        print(line)

def main():


    #load args
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",default="cs32.seas.ucla.edu",required=False)
    parser.add_argument("--user",required=True)
    parser.add_argument("--passcode",required=True)
    parser.add_argument("--projectname",required=True,type=str)
    parser.add_argument("--filesDir",required=True)
    args = parser.parse_args()

    host = args.host
    user = args.user
    passcode = args.passcode
    projectname = args.projectname
    filesDir = args.filesDir

    #Change to files directory and zip them
    os.chdir(filesDir)
    zipped = zip_files(filesDir,projectname)    

    #create ssh client and connect
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username=user,password=passcode)

    #copy files to host
    cpy_to_host(ssh_client,zipped,projectname)
    
    #unzip files and compile
    unzip_compile(ssh_client,projectname)

    rfile = input("Run file?:y/n ")
    if (rfile == "y"):
        run_command = "./"+projectname+"/"+projectname
        stdin,stdout,stderr = ssh_client.exec_command(run_command)
        lines = stdout.readlines()
        for line in lines:
            print(line)
        lines = stderr.readlines()
        for line in lines:
            print(line)

    #close the client
    ssh_client.close()



if __name__ == "__main__":
    main()