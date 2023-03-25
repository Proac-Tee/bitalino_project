# import the necessary libraries
import sys
from pylsl import StreamInlet, resolve_stream
import numpy as np
import pywt

# initialise the data processing function function
def data_acquisition():
    return