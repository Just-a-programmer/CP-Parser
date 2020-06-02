#!/bin/bash
function cpfetch()
{
    dir=$(pwd)
    cpclean
    mkdir Testcase && cd Testcase
    python3 ~/Documents/Programming/CP_parser/Parser.py $1
    cd $dir
}
function cprun()
{
    if [ ! -d "Testcase" ]
    then
       echo "Fetch Testcases First"
       return
    fi
    if [ $# -eq 0 ]
    then
        echo "Please Provide a file"
        return
    fi
    pre=${1%.cpp}
    dir=$(pwd)
    file=$dir/$1
    filename=${file%.cpp}
    g++-9 --std=c++17 -Wall -O2 $file -o filename
    echo "Hello"
    c=$(find Testcase/ -name "$pre*.in" | wc -l)
    echo $c
    for ((i = 1 ; i <= $c ; i++))
    do
        $filename < "./Testcase/$pre$i.in" > myoutput.out
        echo "\nYour Output:"
        cat myoutput.out
        echo "\nExpexted Output:"
        cat "./Testcase/$pre$i.out"
        DIFF=$(diff "./Testcase/$pre$i.out" myoutput.out)
        if [ "$DIFF" != "" ]
        then
            echo $DIFF
        else
            echo "Accepted"
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