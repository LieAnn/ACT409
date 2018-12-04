target=$1
source=$2
t1=`basename $target`
target_name=${t1%.*}
echo $target_name
echo say something
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
$DIR/../OpenFace/x64/Release/FaceLandmarkVidMulti.exe -f $target
cp processed/$target_name.csv AU.csv
#rm -rf processed/
python $DIR/../data/AUtoFEmax.py AU.csv
#rm AU.csv
python $DIR/../color_transfer/videotransfer.py -s $2 -t $1 -c AU_FE2.csv
#rm AU_FE2.csv
