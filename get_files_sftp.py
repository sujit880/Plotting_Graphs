import paramiko

def sftp_get_files(host, port, username, password, remote_dir, local_dir, files):
    # Establish an SSH transport channel
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)

    # Create an SFTP session
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        # Change directory to remote directory
        sftp.chdir(remote_dir)

        # Iterate over files and download them
        for file_name in files:
            remote_file_path = remote_dir + '/' + file_name
            local_file_path = local_dir + '/' + file_name
            sftp.get(remote_file_path, local_file_path)
            print(f"Downloaded {file_name} successfully")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SFTP session and transport
        sftp.close()
        transport.close()

# Example usage
host = 'your_host'
port = 22
username = 'your_username'
password = 'your_password'
remote_dir = '/path/to/remote/directory'
local_dir = '/experiments/d_mnit_c15_e5_b16_t_mix_nc_4_r_250_model_none_lr_01'
files = ['file1.txt', 'file2.txt']  # Specify the files you want to download

sftp_get_files(host, port, username, password, remote_dir, local_dir, files)
