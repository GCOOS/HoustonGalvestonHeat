for file in SST:*_12; do
  newfile1="${file%_12}_00"
  cp "$file" "$newfile1"
  newfile2="${file%_12}_03"
  cp "$file" "$newfile2"
  newfile3="${file%_12}_06"
  cp "$file" "$newfile3"
  newfile4="${file%_12}_09"
  cp "$file" "$newfile4"
  newfile5="${file%_12}_15"
  cp "$file" "$newfile5"
  newfile6="${file%_12}_18"
  cp "$file" "$newfile6"
  newfile7="${file%_12}_21"
  cp "$file" "$newfile7"
done

