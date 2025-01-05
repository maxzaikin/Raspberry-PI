""" 
Project: Smart-House

Author: Maks V. Zaikin
Date: 06-Jan-2025
"""

from abc import ABC, abstractmethod

class Device(ABC):
    """Abstract device class"""
    @abstractmethod
    def update(self):
        """update Updates device's state

        _extended_summary_
        """
        pass