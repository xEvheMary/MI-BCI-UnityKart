# Notes

This folder contains OpenVibe scenarios and related scripts necessary for running the scenario

# Softwares

OpenVibe version: 3.4.0
Python version: 3.7 (details on the OpenVibe Website, python plugin section)

# Details

## Auxiliary
* Python_Unity_Record.py: Python script that reads the received event markers and prints them to the log. Used to check if the events are received properly.
* MIBCI-Graz-Starter.lua: LUA script that is used for start timing control. Provide a baseline period before the start of recording.

## Recording
* LSLRecord-Demo: Use a simple sinusoidal signal to simulate EEG input. Run together with the UnityGame (BCIKart build).
* LSLRecord: Record EEG Signal received through OpenVibe Acquisition Server. Run Together with the UnityGame.
