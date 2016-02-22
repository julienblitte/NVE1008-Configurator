#!/bin/bash

# vss_config CGI display script
# 2016-02-22 Julien Blitte, Qognify

stream=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^stream$/{ print $2; }'`
variable=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^variable$/{ print $2; }'`
value=`echo $QUERY_STRING | sed 's/&/\n/g' | awk -F= '$1~/^value$/{ print $2; }'`

if [[ -z "$stream" ]]
then
	awk -F':' 'BEGIN {c=0;stream="";} \
		$1=="ANOTHER CONF VIDEO STREAM" { if (c>0) print ""; c++; stream="stream"c; print "["stream"]"; } \
		$1~/CONF VIDEO STREAM$/ { split($2,l," "); print l[1]"="l[2];}' \
	'../../vss_config.txt'
fi

if [[ -nz "$stream" && -z "$variable" ]]
then
	echo "[$stream]"
	awk -F':' 'BEGIN {c=0;stream="";} \
		$1=="ANOTHER CONF VIDEO STREAM" { c++; stream="stream"c; } \
		$1~/CONF VIDEO STREAM$/ && stream=="'$stream'" { split($2,l," "); print l[1]"="l[2];}' \
	'../../vss_config.txt'
fi 
 
if [[ -nz "$stream" && -nz "$variable" ]]
then
	awk -F':' 'BEGIN {c=0;stream="";} \
		$1=="ANOTHER CONF VIDEO STREAM" { c++; stream="stream"c; } \
		$1~/CONF VIDEO STREAM$/ && stream=="'$stream'" { split($2,l," "); if(l[1]=="'$variable'") print l[2];}' \
	'../../vss_config.txt'
fi

