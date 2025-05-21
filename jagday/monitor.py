import psutil
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class SystemMetrics:
    """Container for system metrics."""
    cpu_percent: float
    cpu_percent_per_core: List[float]
    memory: Dict[str, Any]
    disk: Dict[str, Any]
    network: Dict[str, Any]
    uptime: float
    processes: List[Dict[str, Any]]
    timestamp: float
    

class SystemMonitor:
    """Class for monitoring system metrics."""
    
    def __init__(self):
        """Initialize the system monitor."""
        self._last_net_io = None
        self._last_net_time = None

    def get_process_list(self) -> List[Dict[str, Any]]:
        """Get a list of processes and their metrics."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                process_info = {
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_info': proc.info['memory_info']
                }
                processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that have terminated or are inaccessible
                pass
        return processes
