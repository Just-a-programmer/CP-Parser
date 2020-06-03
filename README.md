# CP-Parser
This is a command line Utility for parsing the testcases from codeforces. It downloads the testcases and let the user run them via a single command. It is written for C++ only but you can change the cp.sh file at the mentioned points to change make it work for any langugae.
## Intallation ##
To install the utility clone the repository at any location and them run install.sh to run:
1. `chmod +x intall.sh` this gives it execution permission
2. `./install.sh` This will declare the directory and add the path to .bashrc, if you are using any other shell do change in install.sh 
## Description ##
There are in-total three commands:
1. `cpfetch <contest_number>`: This will fetch the testcases from the codeforces to the directory TestCase in the Current directory. The contest number should be the one in the URL.
2. `cprun <file_name>`: This will compile the file and run it for the testcases, the naming convention of the file should be A.cpp, B.cpp,i.e, according to the problem index. You can add more testcases by using similar format
3. `cpclean`: This will remove the Testcase directory.
![picture alt]()
