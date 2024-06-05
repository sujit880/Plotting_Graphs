#!/bin/bash

# Server connection details
SERVER="sujit_2021cs35@10.12.10.15"
REMOTE_DIR="/home/sujit_2021cs35/Github/FedLearn/result"
LOCAL_DIR=f"/mnt/c/Users/S_G/Documents/experiments/datas/d_mnit_c15_e5_b16_t_mix_nc_4_r_250_model_none_lr_01"

# Start SSH session to list files and save the list to a file
ssh $SERVER "cd $REMOTE_DIR && ls *_nc_4_mix_*_B_16*_E_5*.json > files_to_download.txt"

# Transfer file names to local machine
scp $SERVER:$REMOTE_DIR/files_to_download.txt $LOCAL_DIR

# Change to the local directory to save files
cd $LOCAL_DIR

# Read file names and download each one
while read file; do
    sftp $SERVER <<EOF
cd $REMOTE_DIR
get $file
bye
EOF
done < "files_to_download.txt"

# Clean up the temporary file on server
ssh $SERVER "rm $REMOTE_DIR/files_to_download.txt"
