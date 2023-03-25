# import the necessary libraries
import sys
from pylsl import StreamInlet, resolve_stream
import numpy as np
import pywt

# initialise the data processing function function
def data_acquisition():
    # MAC address for the local device connected to the Bitalino device
    pc_mac_address = "xx:xx:xx:xx:xx:xx"  # stored in the 'pc_mac_address' variable

    # LSL stream from the Bitalino device resolved via OpenSignals
    print(
        f"Awaiting OpenSignals stream from device {pc_mac_address}..."
    )  # string output to the user
    streams = resolve_stream("type", pc_mac_address)
 