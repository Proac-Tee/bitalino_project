## EMGaming

A Novel Approach to game control using hand gestures and biosignals

---

## About the Stack

---

### Data Acquisition and Processing

## Python

### Install Dependencies

1. **Anaconda** - Follow instructions to install the latest version of anaconda distribution for your platform in the [Anaconda docs](https://www.anaconda.com/products/distribution)

2. **Virtual Environment** - We recommend working within a virtual environment whenever working on this projects. This keeps the dependencies separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Packages** - Once your virtual environment is setup and running, install the required dependencies by running the following in the anaconda shell prompt:

```
conda install sys
conda install pylsl
conda install pywt
conda install pygame

```

### Lab Streaming

---

## OpenSignal

The Opensignal software comes bundled together with the bitalino device.

---

### Run the Program

- First ensure that the bitalino device is paired via bluetooth to the target pc

- Open the open signal software and initialised the port the EMG sensor is connected

- Activate the LSL streaming channel and set to auto.

## Once the streaming signal has been initialised

- From the `base` directory after creating the virtual environment.

- To run the program, kindly execute the following command in the `anaconda` prompt or `gitlab` terminal:

```
py game.py
```

The `stop` the program run `Ctrl` + `c` from your windows laptop or `CMD` + `c` on Mac.

---

# Tasks completed in this code branch includes:

---

### Data Acquisition Layer

The data acquisition stage was implimented using python.

---

### LAB Streaming Layer 

This LSL stage has been was implimented using python.

---

### Data Cleaning Layer

This was done using wavelength transform.

---

### Feedback layer Layer

This feedback from the user stage has been fully implemented.

---

### PYGame Integration

The PYGame integratio was implimented using python threading.

---

## Graphs

---

### Chunk Before Muscle Detection
![Chunk Before Muscle Detection](graphs/emg%20chunk%20before.PNG)

---

### Chunk After Muscle Detection
![Chunk After Muscle Detection](graphs/emg%20chunk%20after.PNG)

---

### Raw Before Muscle Detection
![Raw Before Muscle Detection](graphs/raw%20before.PNG)

---

### Raw After Muscle Detection
![Raw After Muscle Detection](graphs/raw%20after.PNG)

---

### Filterd signal Before Muscle Detection
![Filterd signal Before Muscle Detection](graphs/filtered%20signal.PNG)

---

### Filtered signal After Muscle Detection
![Filtered signal After Muscle Detection](graphs/filter%20after.PNG)

---

### Rectified signal Before Muscle Detection
![Rectified signal Before Muscle Detection](graphs/rectified%20signal%20before.PNG)

---

### Rectified signal After Muscle Detection
![Rectified signal After Muscle Detection](graphs/rectified%20signal%20after.PNG)

---

### EMG Before Muscle Detection
![EMG Before Muscle Detection](graphs/signal%20not%20detected.PNG)

---

### EMG After Muscle Detection
![EMG After Muscle Detection](graphs/signal%20detected.PNG)

---

### Bar Before Muscle Detection
![Bar Before Muscle Detection](graphs/filtered%20signal%20bar%20before.PNG)

---

### Bar After Muscle Detection
![Bar After Muscle Detection](graphs/filtered%20signal%20bar%20after.PNG)

---






