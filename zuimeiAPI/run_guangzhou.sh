COUNT=$(ps -ef |grep "RUNthis_minute.py" |grep -v "grep" |wc -l)
echo $COUNT
if [ $COUNT -eq 0 ]; then
        python3 RUNthis_minute.py &
else
        echo is RUN
fi
