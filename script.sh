#!/bin/sh

a=`uname -a`
b="Darwin"
c="centos"
d="ubuntu"
n=0
if [[ $a =~ $b ]];then
    n=1
elif [[ $a =~ $c ]];then
    n=2
elif [[ $a =~ $d ]];then
    n=2
else
    echo $a
    n=1
fi

#window script while git is installed
if [[ $n -eq 1 ]];then
    py -3 -m venv venv 
    virtualenv.exe venv 
    venv\Scripts\activate 
    
    set FLASK_APP=project
    set FLASK_ENV=development
    flask run -h 0.0.0.0 -p 80
#linux script
else 
    apt-get install python3-venv -y
    python3 -m venv venv
    source venv/bin/activate

    export FLASK_APP=project
    export FLASK_ENV=development
    flask run -h 0.0.0.0 -p 80
    # flask run -h 0.0.0.0 -p 80 --cert= --key=
    # nohup flask run -h 0.0.0.0 -p 80 > /dev/null 2>&1&
fi

