oFolder=`PWD`
nFolder="ad:server:/root/path/"
nPort=33628
echo "ofolder ${oFolder}"
echo "nfolder ${nFolder}"
while inotifywait -r -e modify,create,delete ${oFolder}
do
         rsync -avz -e "ssh -p ${nPort}" ${oFolder} ${nFolder}
done
