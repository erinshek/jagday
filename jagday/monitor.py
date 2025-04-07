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
