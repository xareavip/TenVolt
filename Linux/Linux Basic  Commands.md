\# I. File \& Directory Operations



\## 1. `ls` — List directory contents

```bash

ls                # List files in current directory

ls -l             # Detailed list (permissions, owner, size, modification time, etc.)

ls -a             # Show hidden files (starting with .)

ls -lh            # Show file sizes in human-readable format (e.g., KB, MB)

```



\## 2. `cd` — Change directory

```bash

cd /home/user     # Enter specified directory

cd ..             # Go back to parent directory

cd \~              # Go to user's home directory

cd -              # Switch to the previous directory

```



\## 3. `pwd` — Print working directory

```bash

pwd

```



\## 4. `mkdir` — Create directories

```bash

mkdir dir1                # Create a single directory

mkdir -p dir1/dir2/dir3   # Recursively create nested directories

```



\## 5. `rmdir` / `rm` — Remove directories or files

```bash

rmdir empty\_dir           # Remove an empty directory

rm file.txt               # Remove a file

rm -r dir                 # Recursively remove a directory and its contents (use with caution!)

rm -f file.txt            # Force remove without confirmation prompt

```



\## 6. `cp` — Copy files or directories

```bash

cp file1.txt file2.txt          # Copy a file

cp -r dir1 dir2                 # Recursively copy an entire directory

```



\## 7. `mv` — Move or rename files/directories

```bash

mv old.txt new.txt        # Rename

mv file.txt /tmp/         # Move file to /tmp directory

```



\## 8. `touch` — Create an empty file or update file timestamp

```bash

touch newfile.txt

```



\# II. File Viewing \& Editing



\## 1. `cat` — View file content (suitable for small files)

```bash

cat file.txt

cat file1.txt file2.txt > combined.txt  # Merge files

```



\## 2. `more` / `less` — Page through files (suitable for large files)

```bash

less largefile.log   # Supports scrolling up/down, press q to quit

more file.txt        # Only allows scrolling down

```



\## 3. `head` / `tail` — View beginning or end of a file

```bash

head -n 10 file.txt   # Show first 10 lines

tail -n 20 file.log   # Show last 20 lines

tail -f /var/log/syslog  # Monitor log file in real-time (commonly used!)

```



\## 4. `nano` / `vim` — Text editors

```bash

nano myfile.txt       # Simple and easy-to-use editor

vim myfile.txt        # Powerful but requires learning (press i to enter insert mode, :wq to save and quit)

```



\# III. System Information \& Management



\## 1. `uname` — View system information

```bash

uname -a              # Show kernel version, hostname, architecture, etc.

```



\## 2. `df` — View disk space usage

```bash

df -h                 # Show in human-readable format (GB, MB)

```



\## 3. `du` — View space used by a directory or file

```bash

du -sh /home/user     # Show total size (-s summary, -h human-readable)

du -h --max-depth=1   # Show sizes of subdirectories in the current directory

```



\## 4. `top` / `htop` — View processes and resource usage

```bash

top                   # Real-time display of CPU, memory, processes

htop                  # More friendly interactive process viewer (requires installation)

```



\## 5. `ps` — View current processes

```bash

ps aux                # Show detailed information for all processes

ps -ef | grep nginx   # Find specific process

```



\## 6. `kill` / `pkill` — Terminate processes

```bash

kill 1234             # Terminate process with PID 1234

pkill firefox         # Terminate by process name

kill -9 1234          # Force terminate (use with caution)

```



\## 7. `free` — View memory usage

```bash

free -h               # Show memory and swap space in human-readable format

```



\## 8. `uptime` — System uptime and load average

```bash

uptime

```



\# IV. Networking Commands



\## 1. `ping` — Test network connectivity

```bash

ping google.com

```



\## 2. `ifconfig` / `ip` — View or configure network interfaces

```bash

ip addr show          # Recommended ip command (ifconfig is being phased out)

ifconfig              # Legacy command, may require net-tools installation on some systems

```



\## 3. `netstat` / `ss` — View network connections and ports

```bash

ss -tuln              # View listening TCP/UDP ports (recommended)

netstat -tuln         # Legacy method (may require installation on some systems)

```



\## 4. `curl` / `wget` — Download files or test HTTP requests

```bash

curl https://example.com

wget https://example.com/file.zip

```



\## 5. `ssh` — Remote login

```bash

ssh user@192.168.1.100

```



\# V. Permissions \& User Management



\## 1. `chmod` — Change file permissions

```bash

chmod 755 script.sh        # Numeric method (r=4, w=2, x=1)

chmod +x script.sh         # Add execute permission

chmod u+x,g-w file.txt     # Add execute for user, remove write for group

```



\## 2. `chown` — Change file owner

```bash

chown user:group file.txt

chown -R user:group dir/   # Change recursively

```



\## 3. `useradd` / `userdel` — Add/remove users

```bash

sudo useradd -m alice

sudo userdel -r alice      # -r also removes the home directory

```



\## 4. `passwd` — Change password

```bash

passwd                    # Change current user's password

sudo passwd alice         # Change another user's password

```



\# VI. Compression \& Archiving



\## 1. `tar` — Package and unpack archives

```bash

tar -cvf archive.tar dir/        # Package directory

tar -xvf archive.tar             # Unpack archive

tar -czvf archive.tar.gz dir/    # Package and compress with gzip

tar -xzvf archive.tar.gz         # Unpack gzip-compressed archive

```



\## 2. `gzip` / `gunzip` — Compress/Decompress .gz files

```bash

gzip file.txt        # Creates file.txt.gz

gunzip file.txt.gz

```



\## 3. `zip` / `unzip`

```bash

zip -r archive.zip dir/

unzip archive.zip

```



\# VII. Searching \& Filtering



\## 1. `find` — Find files

```bash

find /home -name "\*.log"        # Find by name

find . -type f -mtime -7        # Find files modified within the last 7 days

```



\## 2. `grep` — Search text

```bash

grep "error" /var/log/syslog

grep -r "TODO" ./               # Search directory recursively

grep -i "Error" file.txt        # Ignore case

```



\## 3. `which` / `whereis` — Locate command binary

```bash

which python

whereis nginx

```



\# VIII. Pipes \& Redirection



\- `>` : Overwrite a file

\- `>>` : Append to a file

\- `|` : Pass the output of the previous command as input to the next command



```bash

ls -l > filelist.txt          # Save directory listing to a file

echo "hello" >> log.txt       # Append content

ps aux | grep ssh             # Find ssh-related processes

cat access.log | grep 404 | wc -l  # Count number of 404 errors

```



\# IX. Other Useful Commands



\- `history` : View command history

\- `alias` : Set command aliases (e.g., `alias ll='ls -l'`)

\- `man` : View command manual (e.g., `man ls`)

\- `sudo` : Execute a command with superuser privileges

\- `crontab -e` : Edit scheduled tasks

\- `date` : Display or set system date/time

\- `cal` : Display a calendar



\# Tips



\- Use the `Tab` key for \*\*auto-completing\*\* filenames or commands.

\- Use the \*\*Up/Down arrow keys\*\* to recall command history.

\- If you encounter an unfamiliar command, check `man command` or `command --help`.

\- In production environments, be cautious with dangerous commands like `rm -rf /`, `chmod -R 777 /`, etc.!

```

