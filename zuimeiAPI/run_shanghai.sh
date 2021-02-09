COUNT=$(ps -ef |grep "RUN_shanghai2_minute.py" |grep -v "grep" |wc -l)
echo $COUNT
if [ $COUNT -eq 0 ]; then
        python3 RUN_shanghai2_minute.py &
else
        echo is RUN
fi
