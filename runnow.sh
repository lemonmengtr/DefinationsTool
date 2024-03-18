#!/bin/bash
username="menlin"
password="Qazwsx_112"

cur_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

date=$(date "+%Y-%m-%d %H-%M-%S %s%N")

export LANG="zh_CN.UTF-8"

for release in TRUNK 5G21A XL21B
do
   ${cur_dir}/pm/extract-pms.sh $release $username $password >> /var/www/html/NIDD-extractions/"${date}".txt 2>&1
   $cur_dir/autoMR/autoMR.sh $release
   python ${cur_dir}/sendMail.py $release
done

export http_proxy="http://10.144.1.10:8080"
export https_proxy="http://10.144.1.10:8080"



unset http_proxy
unset https_proxy

#$cur_dir/autoMR/autoMR.sh master >> /var/www/html/NIDD-extractions/"${date}".txt 2>&1
#$cur_dir/autoMR/autoMR.sh xL19A >> /var/www/html/NIDD-extractions/"${date}".txt 2>&1
#${cur_dir}/pm/extract-pms.sh $release $username $password >> /var/www/html/NIDD-extractions/"${date}".txt 2>&1

