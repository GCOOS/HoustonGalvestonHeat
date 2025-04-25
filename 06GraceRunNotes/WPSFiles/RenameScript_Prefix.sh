for file in iSST*; do
    newname=$(echo "$file" | sed 's/iSST?/SST/')
    mv "$file" "$newname"
done
