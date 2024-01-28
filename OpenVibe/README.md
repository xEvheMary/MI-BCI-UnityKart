# Notes

This folder contains OpenVibe scenarios and related scripts necessary for running the scenario

# Softwares

OpenVibe version: 3.4.0
Python version: 3.7 (details on the OpenVibe Website, python plugin section)

# Scenarios and files Details

## Auxiliary files
* Python_Unity_Record.py: Python script that reads the received event markers and prints them to the log. Used to check if the events are received properly.
* Python_FakeStim.py: Python script that cycles through predetermined stimulations based on the input stimulation frequency. Used to simulate classification results that are produced at certain frequency.
* MIBCI-Graz-Starter.lua: LUA script that is used for start timing control. Provide a baseline period before the start of recording.

## Recording scenarios
* LSLRecord-Demo: Use a simple sinusoidal signal to simulate EEG input. Run together with the UnityGame (BCIKart build).
* LSLRecord: Record EEG Signal received through OpenVibe Acquisition Server. Run Together with the UnityGame.

## Test Scenario
* LSLControl-Demo: Simple scenario that simulates control over the game.  Consists of a float signal (sinusoidal) and a stimulation generator. Run together with the UnityGame.
