# Using SSH

## What is SSH

SSH (Secure Shell) is a cryptographic protocol that provides secure remote login and other secure network services over an insecure network.  It is commonly used ot securely connect to a remote machine, execute commands, or transfer files.  SSH encrypts the session to ensure that data, such as passwords, command outputs, and other sensitive information is protected.

### Basic SSH Commands

```shell
ssh user@remote_host
```

This command will initiate a connection to a remote host (remote_host) as the specified user (user)

So if your username is fflintstone and you are trying to connect to a remote server with a hostname bedrock.construction.inc

```shell
ssh fflintstone@bedrock.construction.inc
```

## What is SCP?

SCP (Secure Copy) is a command-line utility that uses SSH to securely transfer files between a local and a remote host, or between two remote hosts. SCP ensures data confidentiality by using SSH for encryption.

```shell
scp source_file user@remote_host:/path/to/destination
```

This command will copy source_file from the local machine to the /path/to/destination directory on the remote machine remote_host.

## Generating SSH Keys

SSH keys are a pair of cryptographic keys (a public key and a private key) used for authenticating a user during an SSH session. The private key stays on your local machine, while the public key is installed on the remote server.

### Steps to Generate SSH Keys:

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- -t rsa: Specifies the key type (RSA in this case).
- -b 4096: Specifies the key length (4096 bits for stronger encryption).
- -C "your_email@example.com": Adds a label to the key for identification purposes.


When prompted, you can specify a location to save the key (default is ~/.ssh/id_rsa):

```plaintext
Enter file in which to save the key (/home/your_user/.ssh/id_rsa):
```

Optionally, provide a passphrase for additional security:

```plaintext
Enter passphrase (empty for no passphrase):
```

Just press enter here.

After generation, two files will be created:

- **Private Key**: ~/.ssh/id_rsa (keep this file secure and private).
- **Public Key***: ~/.ssh/id_rsa.pub (this will be copied to the remote server).

## Installing SSH Keys Manually

After generating SSH keys, the public key must be copied to the remote server to enable passwordless SSH login.

### Steps to Install SSH Keys Manually:


Step 1. **Copy the Public Key to the Remote Server**:
Append the content of your public key to the authorized_keys file on the remote server.

You can do this manually or use SH to automate the process:

#### Manual Method:

- Copy the contents of the public key (~/.ssh/id_rsa.pub) using cat):

```shell
cat ~/.ssh/id_rsa.pub
```

On the remote server, open the ~/.ssh/authorized_keys file and paste the public key:

```shell
nano ~/.ssh/authorized_keys
```

Save the file and ensure correct permissions

```shell
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

#### Automated Method (using ssh-copy-id):

Alternatively, you can use the ssh-copy-id command to automate the copying of your public key to the remote server:


```shell
ssh-copy-id user@remote_host
```

Step 2. **Verify SSH Key Installation**:

You can now test the SSH connection using your key:

```shell
ssh user@remote_host
```

If they key was installed correctly, you will be logged in without being prompted for password.

#### Using SSH

SSH can be used to log into a remote system, execute commands, or start a session.

##### Basic Usage:

```shell
ssh user@remote_host
```

This will start a secure session on the remote host as the specified user.

- **Run a command on a remote host**:

```shell
ssh user@remote_host "command"
```

Example:

```shell
ssh user@remote_host "ls -l /var/www
```

- **Connect using a specific private key**:

```shell
ssh -i /path/to/private_key@remote_host
```

- Port forwarding

Forward a local port to a remote port through SSH:

```shell
ssh -L local_port:remote_host:remote_port user@remote_host
```

## Using SCP

SCP is useful for transferring files securely between a local and remote system.

```shell
scp source_file user@remote_host:/path/to/destination
```

Copy a file from your local machine to a remote server:

```shell
scp file.txt user@remote_host:/home/user/
```

Copy a file from a remote server to your local machine:

```shell
scp user@remote_host:/home/user/file.txt /local/directory/
```

Copy an entire directory recursively

```shell
scp -r /local/directory user@remote_host:/remote/dierctory/
```

Use a specific SSH key with SCP

```shell
scp -i /path/to/private_key source_file user@remote_host:/path/to/destination
```

## Conclusion

SSH and SCP are powerful tools for secure remote access and file transfer. By using key-based authentication, you can simplify the login process and increase security. With the steps outlined above, you should be able to generate SSH keys, install them on remote systems, and effectively use SSH and SCP for secure communication.