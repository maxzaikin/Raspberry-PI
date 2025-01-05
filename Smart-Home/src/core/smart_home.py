""" 
Project: Smart-House

Author: Maks V. Zaikin
Date: 06-Jan-2025
"""

class SmartHome:
    """ _summary_

    _extended_summary_
    """
    
    def __init__(self):
        self.devices= []
        
    def add_device(self, device):
        """add_device _summary_

        _extended_summary_

        Arguments:
            device -- _description_
        """
        
        self.devices.append(device)
        
    def update_devices(self):
        """update_devices _summary_

        _extended_summary_
        """
        
        for device in self.devices:
            device.update()