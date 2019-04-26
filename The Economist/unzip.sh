#/bin/bash

for i in *zip
do
    dir=$(echo $i | cut -d _ -f -3)
    mkdir $dir
    unzip $i -d $dir
done
