# ConMeetup

## Purpose
Tool to organise small groups of people on a convention area, where everyone can update their current location periodically for better coordination.

## Architecture
Tool is supposed to run locally as a webserver with a HTML interface for users.
Android and/or iOS apps for leightweight access are optional later on.

## Feature List

### Basic Features
- Create a password protected group, together with a floor plan (possibly multiple levels).
- Allow users to register with a group via the distributed password and appear on the floor plan.
- Allow users to update their current position.
- Allow users to see positions of all other users in that group.

### Optional Features
- Floor plan markup, allow group leader to mark areas as rooms and name them and mark connections between rooms and floors.
- Enable easy pathfinding from one room to another and to other users respectively.
- Lightweight chat.
- Event timetable, allow group leader to add to the event timetable, as well as users to declare interest in certain events for organisation purposes 
- Option to update position of other users as well.
- Optional GPS tracking, whenever connection allows for it.

## Setup
cd into the project root, then run `python setup.py install` to install all dependencies, then run `python app.py` to run the server.

## Credits
Bottle Bootstrap kindly provided by [arsho](https://github.com/arsho/bottle-bootstrap).
