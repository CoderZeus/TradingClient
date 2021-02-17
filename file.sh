#echo "path " $1 
#echo "filename " $2
auth="SHARATH KURIAN "
>$1'/'$2
echo "#########################################" >>$1'/'$2
echo "#### File Name : $2 " >>$1'/'$2
echo "#### Path : $1 " >>$1'/'$2
echo "#### Author $auth" >> $1'/'$2
echo "#### Creation Date $(date)" >>$1'/'$2
echo "########################################" >>$1'/'$2
#"test"

