def sftp_get_files(host, port, username, password, remote_dir, local_dir, files):
    import paramiko
    import os

    # Change to local working directory
    os.chdir('/home/sujit/Github/Plotting_Graphs')
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    # Execute remote command to list files into a text file
    command = f"cd {remote_dir} && ls *_nc_4_mix_*_B_16*_E_5*.json > files_to_download.txt"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdout.channel.recv_exit_status()  # Wait for exec to finish
    # Read output from stdout and stderr
    stdout_output = stdout.read().decode()
    stderr_output = stderr.read().decode()

    # Print output
    print("STDOUT:")
    print(stdout_output)

    print("STDERR:")
    print(stderr_output)

    # Setup SFTP client to transfer files
    sftp = ssh.open_sftp()

    # Download the file containing the list of files to local directory
    remote_file_list = os.path.join(remote_dir, "files_to_download.txt")
    local_file_list = os.path.join(local_dir, "files_to_download.txt")
    sftp.get(remote_file_list, local_file_list)

    # # Change to local directory
    # os.chdir(local_dir)

    # Read local list file and download each file listed
    with open(local_dir+"/files_to_download.txt", 'r') as file_list:
        for file_name in file_list:
            file_name = file_name.strip()
            if file_name:
                remote_file_path = os.path.join(remote_dir, file_name)
                local_file_path = os.path.join(local_dir, file_name)
                sftp.get(remote_file_path, local_file_path)
                # print(remote_file_path, local_file_path)

    # Clean up: Remove the file list from the server
    sftp.remove(remote_file_list)
    # Check if the file exists before attempting to delete
    if os.path.exists(local_file_list):
        os.remove(local_file_list)
        print(f"{local_file_list} has been deleted successfully.")
    else:
        print(f"The file {local_file_list} does not exist.")
    # Close SFTP and SSH connections
    sftp.close()
    ssh.close()

# Example usage
host = 'your_host'
port = 22
username = 'your_username'
password = 'your_password'
remote_dir = '/path/to/remote/directory'
local_dir = '/experiments/d_mnit_c15_e5_b16_t_mix_nc_4_r_250_model_none_lr_01'
files = ['file1.txt', 'file2.txt']  # Specify the files you want to download

sftp_get_files(host, port, username, password, remote_dir, local_dir, files)
