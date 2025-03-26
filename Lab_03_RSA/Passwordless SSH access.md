# Passwordless SSH (Secure Shell) access

It is possible to configure your Raspberry Pi to allow access from another computer without needing to provide a password each time you connect.
To do this, you need to use an SSH key instead of a password.

See also: https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md 
          https://en.wikipedia.org/wiki/Secure_Shell
          https://code.visualstudio.com/docs/remote/ssh-tutorial
          https://github.com/gloveboxes/Raspberry-Pi-with-Visual-Studio-Code-Remote-SSH-and-C-or-C-Development/blob/master/README.md
          

## Step 1: Generate new SSH keys

1. Open the Command Prompt in Windows 10: Press Windows+R to open “Run” box. Type “cmd” and then click “OK” to open a regular Command Prompt.

2. cd c:\users\<your user name>

Display information about the ssh-keygen command:
```
ssh-keygen help
```

To generate new SSH keys enter the following command:
```
ssh-keygen -t rsa -b 4096
```
Upon entering this command, you will be asked where to save the key. Saving it in the default location by pressing Enter.

You will also be asked to enter a passphrase, which is optional. The passphrase is used to encrypt the private SSH key, so that if someone else copied the key, they could not impersonate you to gain access. If you choose to use a passphrase, type it here and press Enter, then type it again when prompted. Leave the field empty for no passphrase.

Now look inside your ```c:\users\<your user name>\.ssh``` directory and you should see the files **```id_rsa```** and **```id_rsa.pub```**:

- The **```id_rsa```** file is your private key. Keep this file on your computer.
- The **```id_rsa.pub```** file is your public key. This is what you share with machines that you connect to: in this case your Raspberry Pi. When the machine you try to connect to matches up your public and private key, it will allow you to connect.

## Step 2: Copy your public key to your Raspberry Pi
Using the computer which you will be connecting from, append the public key to your ```~\.shh\authorized_keys``` file on the Raspberry Pi by sending it over SSH:
- Windows
  ```
  cd c:\users\<your user name>\.ssh
  ```

  ```
  type id_rsa.pub | ssh pi@10.0.0.1 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
  ```
  Now you need enter once the Raspberry Pi password.

- Linux
  ```
  ssh-copy-id pi@10.0.0.1
  ```
  Now you need enter once the Raspberry Pi password.


 ## Step 3: Try to login without password
```
ssh pi@10.0.0.1
```

# Passwordless SCP (secure copy)

Create a txt file. Replace my name with your name.
```
echo "my name" > my_name.txt
```

Use the secure copy protocol to copy your text file to the remote lab server:
```
scp my_name.txt pi@10.0.0.1:~/security_lab
```
