#!/bin/bash

path="translationfiles/zh_TW"

for filename in $path/*.pot; do
    new_filename="${filename%.pot}.po"
    mv "$filename" "$new_filename"
done