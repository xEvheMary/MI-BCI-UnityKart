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

The game works as a cue and feedback of some sort for the user and is responsible for sending event markers to OpenVibe to be recorded alongside the signal.

## Test Mode

OpenVibe has a Python interface/ box that can run Python script in real-time at specific intervals (or when it receives an input). With this interface, I implement my own machine-learning methods on python. OpenVibe has its own machine learning and other processing and classifier boxes that can be used (can be found on the OpenVibe tutorial scenario that comes with the installed application), but those more familiar with Python (or their preferred language) might be more comfortable designing their own pipeline.
