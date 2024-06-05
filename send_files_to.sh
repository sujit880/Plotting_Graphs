#!/bin/bash

# Source and destination directories
source_dir="/home/sujit/Github/Plotting_Graphs/"
destination_dir="/mnt/c/Users/S_G/Documents/experiments/"

directory_list=("figures" "Tables")

for directory in "${directory_list[@]}"; do
    Source=$source_dir$directory
    # Check if source directory exists
    if [ ! -d "$Source" ]; then
        echo "Source directory does not exist: $Source"
        exit 1
    fi
    Destination=$destination_dir$directory
    # Check if destination directory exists, if not create it
    if [ ! -d "$Destination" ]; then
        mkdir -p "$Destination"
        echo "Created destination directory: $Destination"
    fi
    echo "Sending files of '$Source' to '$Destination'"
    # Move files and directories from source directory to destination directory
    cp -r "$Source"/* "$Destination"
    echo "Successfully Copied all files and directories from '$Source' to '$Destination'"

done

echo "Complete"



# # Move files from source directory to destination directory
# for file in "$source_dir"/*; do
#     if [ -f "$file" ]; then
#         filename=$(basename -- "$file")
#         mv "$file" "$destination_dir/$filename"
#         echo "Moved '$filename' to '$destination_dir'"
#     fi
# done


