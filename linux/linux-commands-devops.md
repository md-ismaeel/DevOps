# 🐧 Linux Commands for DevOps Engineers

A comprehensive reference of essential Linux commands with real-world usage examples, organized by category.


## 📋 Table of Contents

- [Linux Folder Structure](#linux-folder-structure)
- [File & Directory Commands](#file--directory-commands)
- [Text Processing Commands](#text-processing-commands)
- [Process Management](#process-management)
- [Permissions & Ownership](#permissions--ownership)
- [Networking Commands](#networking-commands)
- [System Commands](#system-commands)
- [Package Management](#package-management)


## Linux Folder Structure

The folder structure follows the **Filesystem Hierarchy Standard (FHS)**.

| Directory | Description |
|-----------|-------------|
| `/bin` | Essential command-line binaries available to all users |
| `/boot` | Boot files — kernel, initrd, bootloader config |
| `/dev` | Device files for hardware access |
| `/etc` | System-wide configuration files |
| `/home` | Home directories for individual users |
| `/lib` / `/lib64` | Shared libraries needed by the system and apps |
| `/media` | Mount point for removable media (USB, optical discs) |
| `/mnt` | General-purpose temporary mount point |
| `/opt` | Optional/self-contained software packages |
| `/proc` | Virtual filesystem exposing process and kernel info |
| `/root` | Home directory for the root user |
| `/run` | Runtime data for services, cleared on reboot |
| `/sbin` | System binaries for root/administrative use |
| `/srv` | Data for system-provided services |
| `/sys` | Virtual filesystem exposing kernel configuration |
| `/tmp` | Temporary files, cleared on reboot |
| `/usr` | User programs, libraries, documentation, shared data |
| `/var` | Variable data — logs, databases, spool files |


## File & Directory Commands

### `ls` — List files and directories

```bash
ls                          # List files in current directory
ls -l                       # Long format with permissions, size, date
ls -la                      # Long format including hidden files
ls -lh /var/log             # Human-readable file sizes
ls -lt                      # Sort by modification time
ls -lS                      # Sort by file size
```


### `cd` — Change directory

```bash
cd /etc/nginx               # Go to absolute path
cd ..                       # Move up one level
cd ~                        # Go to home directory
cd -                        # Switch to previous directory
```


### `pwd` — Print working directory

```bash
pwd                         # Print current directory path
```


### `mkdir` — Create directory

```bash
mkdir my_folder             # Create a single directory
mkdir -p /opt/app/config    # Create nested directories
mkdir -m 755 releases       # Create with specific permissions
```


### `rm` — Remove files or directories

```bash
rm file.txt                 # Remove a file
rm -r dist/                 # Remove directory recursively
rm -rf /tmp/cache           # Force remove without prompt (use with caution!)
rm -i *.log                 # Interactive prompt before each deletion
```


### `cp` — Copy files or directories
linux-commands-devops.md
```bash
cp app.conf app.conf.bak           # Copy and rename
cp -r src/ build/                  # Copy directory recursively
cp -p file.txt /backup/            # Preserve permissions and timestamps
cp -u source/ dest/                # Copy only newer files
```


### `mv` — Move or rename

```bash
mv old.txt new.txt                 # Rename a file
mv build/ /opt/releases/v2         # Move directory
mv *.log /var/log/archive/         # Move multiple files
```


### `touch` — Create empty file or update timestamps

```bash
touch app.log                      # Create empty file
touch -t 202401010000 file.txt     # Set specific timestamp
```


### `find` — Search files and directories

```bash
find /var/log -name "*.log"        # Find by name
find . -type f -mtime -7           # Files modified in last 7 days
find / -size +100M 2>/dev/null     # Files larger than 100MB
find . -type f -name "*.sh" -exec chmod +x {} \;   # Find and execute
find /tmp -type f -empty -delete   # Find and delete empty files
```


### `tar` — Archive and compress

```bash
tar -czf backup.tar.gz /opt/app    # Create gzip archive
tar -xzf archive.tar.gz -C /opt   # Extract to directory
tar -tzf archive.tar.gz            # List archive contents
tar -cjf backup.tar.bz2 /data     # Create bzip2 archive
tar -xvf archive.tar --strip-components=1  # Extract without top-level dir
```


### `du` — Disk usage

```bash
du -sh /var/log                    # Summary of directory size
du -h --max-depth=1 /              # Size of each top-level dir
du -sh * | sort -rh | head -10     # Top 10 largest items
```


### `df` — Disk free space

```bash
df -h                              # Human-readable sizes
df -hT                             # Include filesystem type
df -i                              # Inode usage
```


### `rsync` — Sync files efficiently

```bash
rsync -avz src/ user@host:/dest           # Sync to remote host
rsync -avz --delete /backup/ /mnt/nas/    # Mirror with deletion
rsync -avzn source/ dest/                 # Dry run (no changes)
rsync -avz --exclude='*.log' src/ dest/   # Exclude pattern
```


### `ln` — Create links

```bash
ln -s /opt/app/current /usr/local/bin/app   # Symbolic link
ln file.txt hardlink.txt                     # Hard link
```


### `zip / unzip` — ZIP archives

```bash
zip -r archive.zip ./project       # Create ZIP archive
unzip archive.zip -d /tmp/out      # Extract to directory
unzip -l archive.zip               # List contents
```


### `mount / umount` — Mount filesystems

```bash
mount /dev/sdb1 /mnt/data                     # Mount a disk
mount -t nfs 10.0.0.1:/share /mnt/nfs         # Mount NFS share
umount /mnt/data                              # Unmount
```


## Text Processing Commands

### `cat` — Concatenate and display files

```bash
cat /etc/os-release                # View file content
cat -n file.txt                    # Show with line numbers
cat file1 file2 > merged.txt       # Merge files
```


### `less` — Page through file content

```bash
less /var/log/syslog               # View file with paging (q to quit)
less +F /var/log/app.log           # Follow mode like tail -f
```


### `head` / `tail` — View file ends

```bash
head -n 20 app.log                 # First 20 lines
tail -n 50 app.log                 # Last 50 lines
tail -f /var/log/nginx/error.log   # Follow new output in real time
tail -f -n 100 app.log             # Follow with last 100 lines shown
```


### `grep` — Search for patterns

```bash
grep "ERROR" app.log               # Search in a file
grep -r "TODO" ./src               # Search recursively
grep -i "warn" *.log               # Case-insensitive
grep -v "DEBUG" app.log            # Invert match (exclude)
grep -n "FATAL" app.log            # Show line numbers
grep -c "ERROR" app.log            # Count matching lines
ps aux | grep nginx                # Filter command output
```


### `awk` — Pattern scanning and processing

```bash
awk '{print $1, $NF}' access.log              # Print first and last fields
awk -F':' '{print $1}' /etc/passwd            # Custom delimiter
awk '/ERROR/{count++} END{print count}' app.log  # Count errors
awk '{sum += $3} END {print sum}' data.txt    # Sum a column
awk 'NR==10,NR==20' file.txt                  # Print lines 10–20
```


### `sed` — Stream editor

```bash
sed 's/foo/bar/g' config.txt                   # Replace all occurrences
sed -i 's/localhost/10.0.0.1/g' app.conf       # In-place replacement
sed '/^#/d' config.ini                         # Delete comment lines
sed -n '10,20p' file.txt                       # Print lines 10–20
sed 's/^/  /' file.txt                         # Indent all lines
```


### `cut` — Extract fields from lines

```bash
cut -d',' -f1,3 data.csv           # Fields 1 and 3 from CSV
cut -c1-10 file.txt                # First 10 characters per line
cut -d':' -f1 /etc/passwd          # Extract usernames
```


### `sort` — Sort lines

```bash
sort file.txt                      # Alphabetical sort
sort -r file.txt                   # Reverse order
sort -n -k2 data.txt               # Numeric sort on column 2
du -sh * | sort -rh                # Sort by human-readable size
sort -u file.txt                   # Sort and deduplicate
```


### `uniq` — Filter duplicate lines

```bash
sort errors.log | uniq             # Remove duplicates
sort errors.log | uniq -c | sort -rn  # Count and rank occurrences
```


### `wc` — Word/line/char count

```bash
wc -l app.log                      # Count lines
wc -w document.txt                 # Count words
ls -1 | wc -l                      # Count files in directory
```


### `diff` — Compare files

```bash
diff config.old config.new         # Show differences
diff -u config.old config.new      # Unified diff format
diff -r dir1/ dir2/                # Compare directories recursively
```


### `tr` — Translate or delete characters

```bash
echo 'hello world' | tr 'a-z' 'A-Z'   # Uppercase conversion
tr -d '\r' < windows.txt > unix.txt    # Remove carriage returns
tr -s ' ' < file.txt                   # Squeeze multiple spaces
```


### `tee` — Write to file and stdout simultaneously

```bash
command | tee output.log           # Write to file and display
make build 2>&1 | tee build.log    # Capture all output including stderr
```


### `xargs` — Build and execute commands from stdin

```bash
find . -name "*.tmp" | xargs rm        # Delete found files
cat urls.txt | xargs wget              # Download a list of URLs
ls *.log | xargs grep "ERROR"          # Search across multiple files
find . -type f | xargs wc -l           # Count lines in all files
```


## Process Management

### `ps` — List running processes

```bash
ps aux                             # All processes (BSD style)
ps -ef                             # All processes (UNIX style)
ps -eo pid,comm,pcpu,pmem --sort=-pcpu  # Sort by CPU usage
ps aux | grep nginx                # Filter by name
```


### `top` / `htop` — Real-time process monitor

```bash
top                                # Interactive process viewer
top -u www-data                    # Filter by user
top -p 1234                        # Monitor specific PID
htop                               # Enhanced interactive viewer (install separately)
```


### `kill` / `killall` / `pkill` — Terminate processes

```bash
kill 1234                          # Send SIGTERM to PID
kill -9 1234                       # Force kill (SIGKILL)
killall nginx                      # Kill all processes by name
pkill -f "python script.py"        # Kill by full command string
pkill -u deploy nginx              # Kill nginx owned by deploy user
```


### `nohup` — Run process immune to hangups

```bash
nohup python app.py &                         # Run in background, persist after logout
nohup ./deploy.sh > deploy.log 2>&1 &         # Capture all output
```


### `jobs / fg / bg` — Job control

```bash
jobs -l                            # List background jobs
fg %1                              # Bring job 1 to foreground
bg %2                              # Resume job 2 in background
# Ctrl+Z                           # Suspend current job
```


### `watch` — Repeat a command at intervals

```bash
watch -n 2 df -h                   # Disk usage every 2 seconds
watch -n 1 "ps aux | grep nginx"   # Monitor process every second
```


### `lsof` — List open files

```bash
lsof -i :8080                      # What's using port 8080
lsof -u nginx                      # Files opened by user nginx
lsof /var/log/app.log              # Processes using this file
lsof -i tcp -n                     # All TCP connections
```


### `strace` — Trace system calls

```bash
strace -p 1234                     # Attach to running process
strace -e trace=open,read ./app    # Filter specific syscalls
strace -o trace.log ./script.sh    # Write output to file
```


## Permissions & Ownership

### Permission Model

```
-rwxr-xr--  1 user group 1234 Jan 01 file.txt
 |||||||
 ||||||+--- Others: r-- (read only)
 |||+++---- Group:  r-x (read + execute)
 +++------- Owner:  rwx (read + write + execute)
```

| Octal | Symbolic | Meaning |
|-------|----------|---------|
| `7` | `rwx` | Read, write, execute |
| `6` | `rw-` | Read and write |
| `5` | `r-x` | Read and execute |
| `4` | `r--` | Read only |
| `0` | `---` | No permissions |


### `chmod` — Change permissions

```bash
chmod 755 script.sh                # rwxr-xr-x
chmod 644 config.txt               # rw-r--r--
chmod u+x deploy.sh                # Add execute for owner
chmod o-rwx secrets.env            # Remove all for others
chmod -R 644 /var/www/html         # Recursive
chmod a+r public.txt               # Add read for everyone
```


### `chown` — Change ownership

```bash
chown www-data:www-data /var/www          # Set owner and group
chown -R deploy:deploy /opt/app           # Recursive
chown :developers /shared/dir             # Change group only
```


### `chgrp` — Change group ownership

```bash
chgrp developers /opt/project             # Change group
chgrp -R staff /var/data                  # Recursive
```


### `umask` — Default permission mask

```bash
umask                              # Show current mask
umask 022                          # New files: 644, dirs: 755
umask 027                          # New files: 640, dirs: 750
```


### `stat` — File status details

```bash
stat file.txt                      # Full file metadata
stat -c "%A %U %G" /etc/passwd     # Permissions, owner, group
```


### `getfacl / setfacl` — Access Control Lists

```bash
getfacl /var/data                             # View ACLs
setfacl -m u:alice:rwx /shared/dir           # Grant user ACL
setfacl -R -m g:developers:rx /opt/app       # Recursive group ACL
setfacl -x u:alice /shared/dir               # Remove user ACL
```


## Networking Commands

### `ip` — Network interface management (modern)

```bash
ip addr show                       # Show all interfaces and IPs
ip link show                       # Show link state of interfaces
ip route show                      # Show routing table
ip addr add 10.0.0.5/24 dev eth0   # Add IP to interface
ip link set eth0 up                # Bring interface up
ip route add default via 192.168.1.1  # Add default gateway
ip neigh show                      # Show ARP cache
```


### `ifconfig` — Interface config (legacy)

```bash
ifconfig                           # Show all interfaces
ifconfig eth0                      # Show specific interface
ifconfig eth0 up                   # Bring interface up
```


### `ping` — Test host reachability

```bash
ping google.com                    # Continuous ping
ping -c 4 8.8.8.8                  # Send 4 packets
ping -i 0.2 host                   # Interval between pings
```


### `traceroute` / `mtr` — Network path tracing

```bash
traceroute google.com              # Trace packet route
traceroute -n 8.8.8.8              # Skip DNS resolution
mtr google.com                     # Real-time combined ping + traceroute
mtr --report google.com            # Non-interactive report
```


### `nslookup` / `dig` / `host` — DNS lookups

```bash
nslookup google.com                # Simple DNS lookup
nslookup -type=MX example.com      # Query MX records

dig google.com                     # Detailed DNS query
dig @8.8.8.8 example.com           # Query specific DNS server
dig MX example.com +short          # Short output
dig example.com +trace             # Trace DNS resolution

host google.com                    # Quick lookup
host 8.8.8.8                       # Reverse DNS lookup
```


### `ss` — Socket statistics (modern netstat)

```bash
ss -tuln                           # Listening TCP/UDP ports
ss -tp                             # TCP connections with processes
ss -s                              # Summary statistics
ss -lnp | grep :80                 # What's on port 80
```


### `netstat` — Network statistics (legacy)

```bash
netstat -tuln                      # Listening ports
netstat -an | grep LISTEN          # All listening sockets
netstat -rn                        # Routing table
```


### `curl` — Transfer data from/to URLs

```bash
curl https://api.example.com                          # GET request
curl -I https://example.com                           # Headers only
curl -X POST -H "Content-Type: application/json" \
  -d '{"key":"value"}' https://api.example.com        # POST with JSON
curl -o file.txt https://example.com/file             # Download to file
curl -u user:pass https://api.example.com             # Basic auth
curl -k https://self-signed.example.com               # Skip SSL verify
curl -L https://example.com                           # Follow redirects
```


### `wget` — Download files

```bash
wget https://example.com/file.tar.gz         # Download file
wget -O output.html https://example.com      # Save with custom name
wget -c https://example.com/large.iso        # Resume incomplete download
wget -r -np https://example.com/docs/        # Recursive download
```


### `ssh` — Secure Shell

```bash
ssh user@host                               # Basic connection
ssh -i ~/.ssh/id_rsa user@host              # With identity file
ssh -p 2222 user@host                       # Custom port
ssh -L 8080:localhost:80 user@host          # Local port forward
ssh -R 9090:localhost:9090 user@host        # Remote port forward
ssh -N -D 1080 user@host                    # SOCKS proxy
```


### `scp` — Secure copy

```bash
scp file.txt user@host:/tmp                 # Copy file to remote
scp -r /opt/app user@host:/opt/             # Copy directory
scp user@host:/remote/file.txt ./           # Copy from remote
```


### `nmap` — Network scanner

```bash
nmap -sV 192.168.1.0/24            # Scan subnet with service detection
nmap -p 80,443 example.com         # Check specific ports
nmap -A -T4 target                 # Aggressive scan
nmap -sn 192.168.1.0/24            # Ping scan only (no port scan)
```


### `tcpdump` — Capture network traffic

```bash
tcpdump -i eth0                              # Capture on interface
tcpdump -i any port 80                       # Capture HTTP traffic
tcpdump -w capture.pcap host 10.0.0.1       # Write to file
tcpdump -r capture.pcap                      # Read capture file
```


### `iptables` — Firewall management

```bash
iptables -L -n -v                                    # List all rules
iptables -A INPUT -p tcp --dport 80 -j ACCEPT        # Allow HTTP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT        # Allow SSH
iptables -A INPUT -s 10.0.0.0/8 -j DROP             # Drop subnet
iptables -P INPUT DROP                               # Default deny
iptables-save > /etc/iptables.rules                  # Save rules
iptables-restore < /etc/iptables.rules               # Restore rules
```


### `nc` (netcat) — Networking swiss army knife

```bash
nc -l 8080                         # Listen on port 8080
nc host 8080                       # Connect to port
nc -zv host 20-80                  # Port scan
cat file.txt | nc host 9000        # Transfer file
```


### `route` — Routing table

```bash
route -n                                          # Show routing table
route add -net 192.168.0.0/24 gw 192.168.1.1     # Add route
route delete default gw 192.168.1.1              # Delete route
```


## System Commands

### `uname` — System info

```bash
uname -a                           # All system info
uname -r                           # Kernel version
uname -m                           # Machine architecture
```


### `hostname` — System hostname

```bash
hostname                           # Display hostname
hostname -I                        # Display all IPs
hostnamectl set-hostname myserver  # Set hostname
```


### `uptime` — System uptime and load

```bash
uptime                             # Uptime and load average
uptime -p                          # Pretty format
```


### `free` — Memory usage

```bash
free -h                            # Human-readable
free -m                            # In megabytes
watch -n 1 free -h                 # Monitor in real time
```


### `vmstat` — Virtual memory statistics

```bash
vmstat                             # Snapshot
vmstat 2 5                         # 5 samples, every 2 seconds
vmstat -s                          # Memory stats summary
```


### `iostat` — I/O statistics

```bash
iostat                             # CPU and I/O stats
iostat -xz 1                       # Extended stats, 1-second intervals
iostat -d /dev/sda                 # Specific device
```


### `dmesg` — Kernel messages

```bash
dmesg | tail -30                   # Last 30 kernel messages
dmesg -T | grep -i error           # With timestamps, filter errors
dmesg --level=err,warn             # Show errors and warnings only
```


### `journalctl` — Systemd logs

```bash
journalctl -xe                                     # Latest logs with context
journalctl -u nginx.service                        # Logs for a service
journalctl --since "2024-01-01" --until "2024-01-02"  # Date range
journalctl -f -u docker                            # Follow service logs
journalctl -p err -b                               # Errors since last boot
journalctl --disk-usage                            # Log disk usage
```


### `systemctl` — Service management

```bash
systemctl status nginx             # Check service status
systemctl start nginx              # Start service
systemctl stop nginx               # Stop service
systemctl restart nginx            # Restart service
systemctl reload nginx             # Reload config without restart
systemctl enable docker            # Enable on boot
systemctl disable docker           # Disable on boot
systemctl list-units --type=service   # List all services
```


### `crontab` — Schedule tasks

```bash
crontab -e                         # Edit cron jobs
crontab -l                         # List cron jobs
crontab -r                         # Remove all cron jobs
```

**Cron syntax:**
```
* * * * * /path/to/command
│ │ │ │ └─ Day of week (0-7, Sun=0 or 7)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

**Examples:**
```bash
0 2 * * * /opt/scripts/backup.sh          # Daily at 2:00 AM
*/5 * * * * /opt/scripts/monitor.sh       # Every 5 minutes
0 9 * * 1 /opt/scripts/weekly.sh          # Every Monday at 9 AM
```


### `env / export` — Environment variables

```bash
env                                # Show all environment variables
printenv HOME                      # Show specific variable
export PATH=$PATH:/opt/bin         # Extend PATH
export DATABASE_URL=postgres://localhost/mydb
unset MY_VAR                       # Remove a variable
```


### `alias` — Command shortcuts

```bash
alias ll='ls -lah'                 # Long list with hidden files
alias k='kubectl'                  # Kubernetes shortcut
alias gs='git status'              # Git status
alias ..='cd ..'                   # Go up a directory
alias grep='grep --color=auto'     # Colorize grep
```


### `history` — Command history

```bash
history                            # Show all history
history | grep git                 # Search history
!42                                # Re-run command #42
!!                                 # Re-run last command
history -c                         # Clear history
```


### `date` / `timedatectl` — Date and time

```bash
date                               # Current date and time
date '+%Y-%m-%d %H:%M:%S'         # Formatted output
date -u                            # UTC time

timedatectl                        # Full time and timezone info
timedatectl set-timezone UTC       # Set timezone
timedatectl set-ntp true           # Enable NTP sync
```


### `shutdown / reboot` — System power control

```bash
shutdown now                       # Immediate shutdown
shutdown -r now                    # Immediate reboot
shutdown -h +10 "Maintenance"      # Halt in 10 minutes with message
reboot                             # Reboot
```


### `su / sudo` — Switch user / superuser

```bash
sudo apt update                    # Run as root
sudo -i                            # Open root shell
su - deploy                        # Switch to deploy user
sudo -u postgres psql              # Run command as postgres
```


### `useradd / usermod / groupadd` — User management

```bash
sudo useradd -m -s /bin/bash deploy    # Create user with home + shell
sudo usermod -aG docker ubuntu         # Add user to group
sudo usermod -aG sudo newuser          # Grant sudo
sudo groupadd developers               # Create group
sudo userdel -r olduser                # Delete user and home dir
id username                            # Show UID/GID/groups
who                                    # Show logged-in users
last | head -10                        # Recent login history
```


### `echo` — Print output

```bash
echo "Hello DevOps"                # Print string
echo $HOME                         # Print variable
echo -e "line1\nline2"             # Enable escape sequences
echo -n "no newline"               # No trailing newline
```


## Package Management

### Debian / Ubuntu — `apt`

```bash
sudo apt update                    # Refresh package lists
sudo apt upgrade -y                # Upgrade all packages
sudo apt install nginx             # Install package
sudo apt remove nginx              # Remove package
sudo apt purge nginx               # Remove with config files
sudo apt autoremove                # Remove unused dependencies
apt list --installed               # List installed packages
apt search python3                 # Search for packages
apt show nginx                     # Package details
```


### RHEL / CentOS / Fedora — `yum` / `dnf`

```bash
sudo yum install nginx             # Install (CentOS 7)
sudo dnf update                    # Update all (CentOS 8+, Fedora)
sudo dnf install nginx             # Install package
sudo dnf remove nginx              # Remove package
yum list installed                 # List installed packages
dnf search python3                 # Search packages
```


### Low-level package tools

```bash
# Debian/Ubuntu
dpkg -l | grep nginx               # Check if installed
sudo dpkg -i package.deb           # Install .deb file
dpkg -L nginx                      # List files in package

# RHEL/CentOS
rpm -qa | grep nginx               # Check if installed
sudo rpm -ivh package.rpm          # Install .rpm file
rpm -ql nginx                      # List files in package
```


### `snap` — Universal packages

```bash
snap list                          # Installed snaps
sudo snap install code --classic   # Install VS Code
sudo snap refresh                  # Update all snaps
```


### `which / whereis` — Locate commands

```bash
which python3                      # Path of executable
whereis nginx                      # Binary, source, and man page locations
which -a python                    # All matching executables
```


## Useful One-Liners

```bash
# Find top 10 largest files in a directory
find / -type f -printf '%s %p\n' 2>/dev/null | sort -rn | head -10

# Watch log for errors in real time
tail -f /var/log/app.log | grep --line-buffered "ERROR"

# Count HTTP status codes in nginx access log
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn

# Find all listening ports and their processes
ss -tlnp | awk 'NR>1 {print $4, $6}'

# Check which process is using a port
lsof -i :8080

# Disk usage of current directory, sorted
du -sh * | sort -rh

# List all failed systemd services
systemctl list-units --state=failed

# Search recursively and replace in all files
grep -rl "old_string" . | xargs sed -i 's/old_string/new_string/g'

# Show real-time network connections count
watch -n 1 'ss -tn | grep ESTABLISHED | wc -l'

# Kill all processes matching a pattern
ps aux | grep 'pattern' | awk '{print $2}' | xargs kill -9

# Find recently modified config files
find /etc -type f -mtime -1 2>/dev/null

# Check SSL certificate expiry
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```


## Quick Reference — Permission Octal Table

| Octal | Binary | Permissions |
|-------|--------|-------------|
| `0` | `000` | `---` |
| `1` | `001` | `--x` |
| `2` | `010` | `-w-` |
| `3` | `011` | `-wx` |
| `4` | `100` | `r--` |
| `5` | `101` | `r-x` |
| `6` | `110` | `rw-` |
| `7` | `111` | `rwx` |

**Common permission sets:**

| Octal | Use case |
|-------|----------|
| `644` | Web files, config files |
| `755` | Executables, directories |
| `600` | Private keys, sensitive files |
| `700` | Private directories |
| `777` | Fully open — avoid in production |


## Signal Reference

| Signal | Number | Description |
|--------|--------|-------------|
| `SIGTERM` | 15 | Graceful termination (default for `kill`) |
| `SIGKILL` | 9 | Forceful termination — cannot be caught |
| `SIGHUP` | 1 | Reload configuration |
| `SIGINT` | 2 | Interrupt (Ctrl+C) |
| `SIGSTOP` | 19 | Pause process |
| `SIGCONT` | 18 | Resume paused process |


*For full documentation on any command, run `man <command>` or `<command> --help`.*
