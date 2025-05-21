# jagday
An open-source project built on Python for monitoring server status and processes running on it

## Installation
You can install `jagday` using pip:
```bash
pip install jagday
```
(If publishing to PyPI, otherwise: `pip install .` for local install from source)

## Usage
Once installed, you can view running processes by typing:
```bash
jps
```

## Output
The `jps` command will display a list of currently running processes with the following information:
- PID: Process ID
- Name: Process Name
- CPU(%): CPU usage percentage
- Memory(MB): Memory usage in Megabytes
