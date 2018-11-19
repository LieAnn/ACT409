exec < $1
while read line
do
line=${line%\.mp4}
line=${line}.csv
python $2 clips/processed/$line
done
