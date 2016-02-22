#!/bin/bash

# vss_config CGI modification script
# 2016-02-22 Julien Blitte, Qognify

stream=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^stream$/{ print $2; }'`
variable=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^variable$/{ print $2; }'`
value=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^value$/{ print $2; }'`

if [[ -nz "$stream" && -nz "$variable" && -nz "$value" ]]
then
	cp '../../vss_config.txt' '../../vss_config.bak'
	
	awk -F':' 'BEGIN {OFS=FS;c=0;stream="";} $1=="ANOTHER CONF VIDEO STREAM" { c++; stream="stream"c; } \
		$1~/CONF VIDEO STREAM$/ && stream=="'$stream'" { split($2,l," "); if(l[1]=="'$variable'") $2=" "l[1]" '$value'";} \
		{print}' \
	'../../vss_config.bak' > '/tmp/vss_config.tmp'
	
	mv '/tmp/vss_config.tmp' '../../vss_config.txt'
	
	echo "OK"
	exit
fi

echo "NOK"
echo "Missing one of the parameters: stream, variable or value"

