for file in FILE*; do
    newname=$(echo "$file" | sed 's/^FILE./SST:/')
    echo "Renaming: '$file' -> '$newname'"
    mv "$file" "$newname"
done
