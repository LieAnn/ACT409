exec < $1

while read line
do
../OpenFace/x64/Release/FaceLandmarkVidMulti.exe -f ../data/clips/$line
done
