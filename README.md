# jagday
An open-source project built on Python for monitoring server status and processes running on it

## Installation
Install from source for local
```bash
git clone git@github.com:erinshek/jagday.git
cd jagday
pip install .
```

## Usage
Once installed, you can view running processes by typing:
```bash
jps
```
or
```
jps > processes.txt
```

## Output
The `jps` command will display a list of currently running processes with the following information:
- PID: Process ID
- Name: Process Name
- CPU(%): CPU usage percentage
- Memory(MB): Memory usage in Megabytes
