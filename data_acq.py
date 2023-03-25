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
    
    if len(streams) == 0:
        print(
            """Stream not found!!!
            Ensure that the Bitalino is connected and OpenSignals is running.
            Also make sure that the lab streaming layer is checked to allow the signal flow
            """
        )
        sys.exit()
    print("EMG Stream identified!!!")

    # inlet to receive data from the stream instantiated
    inlet = StreamInlet(streams[0])
    
    # Set up wavelet parameters for preprocessing the signal
    sampling_rate = 1000  # sampling rate in Hz
    wavelet = "db4"  # type of wavelet to use
    level = 6  # level of decomposition
    mode = "symmetric"  # signal extension mode

    # wavelet transform variable to store extracted features from the signal
    wavelet = pywt.Wavelet("sym4")

    # Buffer for storing incoming samples
    buffer_size = 100
    buffer = np.zeros((buffer_size, 8))

    # Threshold to trigger for muscle movement detection
    threshold = 0.1

    # Boolean state to check if a jump has occurred during the current iteration of the while loop
    jumped = False
    
    # A loop to continuously receive and preprocess EMG data from gotten the Bitalino device via open-signals lsl
    while True:
        # Extract the chunk of samples from the inlet
        chunk, timestamps = inlet.pull_chunk(timeout=1.0, max_samples=buffer_size)
        if chunk:
            # Append chunk to buffer
            buffer = np.roll(buffer, -len(chunk), axis=0)
            buffer[-len(chunk) :, :] = np.array(chunk)[
                :, 1:9
            ]  # EMG data from chunk channel extraction. In this case it is connected to channel A1

            # Concatenate buffer rows to form input signal
            input_signal = buffer.flatten()