# CP-Parser
This is a Testcase Parser written for codeforces.
To use it clone the repository add to your bash_profile:
`source /path/to/repository/cp.sh`
And edit mypath in cp.sh to:
`/path/to/repository`
There are in-total three commands:
1. `cpfetch <contest_number>`: This will fetch the testcases from the codeforces to the directory TestCase in the Current directory. The contest number should be the one in the URL.
2. `cprun <file_name>`: This will compile the file and run it for the testcases, the naming convention of the file should be A.cpp, B.cpp,i.e, according to the problem index. The current support is for only c++, you can edit the compile script for any language.
3. `cpclean`: This will remove the Testcase directory.
For Any Query feel free to ping me.
