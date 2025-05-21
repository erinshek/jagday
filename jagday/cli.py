from jagday.monitor import SystemMonitor

def main_cli():
    monitor = SystemMonitor()
    processes = monitor.get_process_list()

    # Header
    print(f"{'PID':<5} {'Name':<25} {'CPU(%)':<7} {'Memory(MB)':<10}")
    print("-" * 52) # Separator line

    for proc in processes:
        pid = proc.get('pid', 'N/A')
        name = proc.get('name', 'N/A')[:25] # Truncate name if too long
        cpu_percent = proc.get('cpu_percent', 'N/A')
        
        mem_info = proc.get('memory_info')
        # psutil returns a namedtuple, rss is one of its attributes.
        # On some systems, memory_info might be a basic tuple or dict,
        # so we'll access 'rss' carefully.
        if hasattr(mem_info, 'rss'):
            mem_mb = mem_info.rss / (1024 * 1024)
            mem_str = f"{mem_mb:<10.2f}"
        elif isinstance(mem_info, dict) and 'rss' in mem_info:
            mem_mb = mem_info['rss'] / (1024 * 1024)
            mem_str = f"{mem_mb:<10.2f}"
        else:
            # Handle cases where rss might not be available or mem_info is None/unexpected
            mem_str = "N/A" 

        print(f"{pid:<5} {name:<25} {cpu_percent:<7.2f} {mem_str}")

if __name__ == "__main__":
    main_cli()
