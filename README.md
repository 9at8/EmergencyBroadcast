# EmergencyBroadcast
Uses a Raspberry Pi 2 to broadcast FM signals from user input text over a specific range of frequencies in case of an emergency.
This project is built on top of [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds).
Thanks a lot to [@ChristopheJacquet](https://github.com/ChristopheJacquet) for building [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds).

## Hardware Requirements
- Raspberry Pi
- A wire!

## Dependencies
- [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds)
- Pico Text to Speech

## Installation
- Clone the repository.
  `git clone https://github.com/9at8/EmergencyBroadcast.git`
- Install [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds) using the instructions given in the link.
- Install Pico Text to Speech
  `sudo apt-get install libttspico-utils`
- Edit `main.py` to:
  - Set `player_location` as the location of the [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds) executable
  - Set `audio_name` as the temporary name for TTS audio
  - Set `audio_location` as the temporary location for the TTS audio file
- Run! `./main.py`
