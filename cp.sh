#!/bin/bash
yellow="\033[1;33;40m"
red="\033[1;31;40m"
blue="\033[1;36;40m"
purple="\033[1;35;40m"
green="\033[1;32;40m"
mypath=~/CP_Parser/
function cpfetch()
{
    dir=$(pwd)
    cpclean
    mkdir Testcase && cd Testcase
    python3 $mypath/Parser.py $1
    cd $dir
}
function cprun()
{
    if [ ! -d "Testcase" ]
    then
       echo $red"Fetch Testcases First"
       return
    fi
    if [ $# -eq 0 ]
    then
        echo $red"Please Provide a file"
        return
    fi
    pre=${1%.cpp}
    dir=$(pwd)
    file=$dir/$1
    filename=${file%.cpp}
    g++-9 --std=c++17 -Wall -O2 $file -o filename
    c=$(find Testcase/ -name "$pre*.in" | wc -l)
    for ((i = 1 ; i <= $c ; i++))
    do
        $filename < "./Testcase/$pre$i.in" > myoutput.out
        echo $yellow"\nYour Output:"$green
        cat myoutput.out
        echo $yellow"\nExpexted Output:"$green
        cat "./Testcase/$pre$i.out"
        DIFF=$(diff "./Testcase/$pre$i.out" myoutput.out)
        if [ "$DIFF" != "" ]
        then
            echo $red"Failed"
            echo $DIFF
        else
            echo $blue"\nAccepted"
        fi
    done
}
function cpclean()
{
    if [ -d "Testcase" ]
    then
        rm -r Testcase
    fi
}