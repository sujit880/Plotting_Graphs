import paramiko
import os

# Server connection details
SERVER = "sujit_2021cs35@10.12.10.15"
REMOTE_DIR = "/home/sujit_2021cs35/Github/FedLearn/result"
LOCAL_DIR = "experiments/d_mnit_c15_e5_b16_t_mix_nc_4_r_250_model_none_lr_01"
USERNAME, HOST = SERVER.split('@')

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
ssh.connect(HOST, username=USERNAME)

# Execute remote command to list files into a text file
command = f"cd {REMOTE_DIR} && ls *_nc_4_mix_*_B_16*_E_5*.json > files_to_download.txt"
stdin, stdout, stderr = ssh.exec_command(command)
stdout.channel.recv_exit_status()  # Wait for exec to finish

# Setup SFTP client to transfer files
sftp = ssh.open_sftp()

# Download the file containing the list of files to local directory
remote_file_list = os.path.join(REMOTE_DIR, "files_to_download.txt")
local_file_list = os.path.join(LOCAL_DIR, "files_to_download.txt")
sftp.get(remote_file_list, local_file_list)

# Change to local directory
os.chdir(LOCAL_DIR)

# Read local list file and download each file listed
with open("files_to_download.txt", 'r') as file_list:
    for file_name in file_list:
        file_name = file_name.strip()
        if file_name:
            remote_file_path = os.path.join(REMOTE_DIR, file_name)
            local_file_path = os.path.join(LOCAL_DIR, file_name)
            sftp.get(remote_file_path, local_file_path)

# Clean up: Remove the file list from the server
sftp.remove(remote_file_list)

# Close SFTP and SSH connections
sftp.close()
ssh.close()
