#!/bin/bash
#!/bin/bash
ps_out=`ps -ef | grep 'shanghai_minutes' | grep -v 'grep' | grep -v $0`
result=$(echo $ps_out | grep "shanghai_minutes")
if [[ "$result" != "" ]];then
    echo "Running"
else
    paths=`pwd`
    echo $paths
    python3 $paths/shanghai_minutes.py
fi