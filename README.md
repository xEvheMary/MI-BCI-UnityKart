# MI BCI Application on Unity Kart Game

This project is the application of Brain-Computer Interface, using Motor Imagery to control a kart in the game.

This repository contains the game, the unity package, OpenVibe scenarios, and relevant Python code

The game is a modified version of [Unity's Karting Microgame](https://learn.unity.com/project/karting-template).

I use [OpenVibe](http://openvibe.inria.fr/) to process and record the EEG signals and events.

![](https://github.com/xEvheMary/MI-BCI-UnityKart/blob/main/UnityBCIKart%20(2).gif)

# Requirements

* Unity (If you want to modify the source code further or make a completely new game)
* OpenVibe (Version 3.4 +)
* Python (Version 3.7, the version must suit OpenVibe [requirement](http://openvibe.inria.fr/tutorial-using-python-with-openvibe/))
* Python-MNE
* sklearn

# Details

The game has two main game modes that can be utilized, Calibration Mode and Test Mode.

<img src="https://github.com/xEvheMary/MI-BCI-UnityKart/blob/main/GameModes.png" width="800">

## Calibration Mode

The purpose of this mode is to gather data and use it to train classifiers for the test mode. In this mode, the game will essentially play itself. It works similarly to a tutorial, just that it's relatively long (4-6 minutes). In the duration of the mode, it encourages the user to imagine controlling the kart by imagining moving a part of their body (left hand, right hand, or foot in this scenario).

The game works as a cue and feedback of some sort for the user and is responsible for sending event markers to OpenVibe to be recorded alongside the signal. OpenVibe runs in the background to receive both the signal and events and record it. The kart will go around the track as many as the lap set on the menu screen (image shown above) and will automatically end the recording after finishing all the laps)

## (Auxiliary) Training Pipeline

The training pipeline is the process outside both the game and openvibe. It is done after the calibration mode and process the signal into data that can be used to train classifiers for the test mode. This process can be done through many methods and it is up to the researcher/user (I personally use Google Colab to train and save the classifier). 

## Test Mode

The purpose of this mode is to test out the results of the training. In this mode, the control is given to the user and we make use of the classifier trained using previously recorded data. Unfortunately, Motor Imagery BCI is still not quite able to perform classification on complex and/ or compound movement. For that reason, we choose to let the user control only the steering wheel while the gas and brake are done automatically by the game. This limits the required control to only 3 options, which can be handled by the classifier we currently have access to. In this scenario, we use OpenVibe's Python Box to handle the classification.

OpenVibe has a Python interface/ box that can run Python script in real-time at specific intervals (or when it receives an input). With this interface, I implement my own machine-learning methods in Python. OpenVibe has its own machine learning and other processing and classifier boxes that can be used (can be found on the OpenVibe tutorial scenario that comes with the installed application), but those more familiar with Python (or their preferred language) might be more comfortable designing their own pipeline.

The classification result is then converted into an OpenVibe event marker and then sent to the game via LSL (Optionally, we can also send some float value through another LSL channel to act as variable steering). The game will make use of the received events to control the kart steering angle. The test mode is finished after they complete several laps (laps option are on the screen shown above)

# Instructions

## Calibration Mode

## Test Mode

# Other
The game also has some options that can be changed to suit your objective (not fully utilized for now).

<img src="https://github.com/xEvheMary/MI-BCI-UnityKart/blob/main/GameSettings.png" width="800">

General settings and Kart settings are personalized settings for every user.

The important function for now is the LSL settings. This option for now is set to follow OpenVibe settings, this includes the type of event received in the game (which is hard-coded for now). If anyone doesn't want to use OpenVibe specifically and has their own pipeline, these options can be changed to follow suit.

Settings purpose (might add a tooltip on the menu in the future):
* Signal Inlet: only read 1 channel, double type data. The default purpose is for the classifier's confidence, used to control the steering degree.
* Marker Inlet: 1 channel, integer type data. The default purpose is for the classifier's class (in the form of OpenVibe [Stimulation Codes](http://openvibe.inria.fr/stimulation-codes/), used for steering direction).
* Signal Outlet: Send 1 channel, double type data. No purpose for now.
* Marker Outlet: Send 1 channel, integer type data. The default purpose is for the event markers during the recording. It also returns the received stimulation from the inlet.

# Improvement possibilities
* Centralized control for both OpenVibe and the game (might not necessarily use OpenVibe, maybe a custom application)
* Automatic classifier training after recording (can quickly move on to testing)
* Add Gas control (the function is there, but not possible right now classifier-wise)
* Compound movement (forward and turning at the same time)
* Option expansion (some options are still hard-coded in the game source code, might add more UI for more flexibility)
