piKiln
==========

Turns a Raspberry Pi into a cheap, universal & web-enabled electric kiln controller.
Based heavily on [picoReflow](https://github.com/apollo-ng/picoReflow) with the following changes:
* Renaming for kiln-related activities
* Removal of unrelated routines
* Addition of logging and review for past firings

**Standard Interface**

To be updated

**Curve Editor**

To be updated

**Firing History**

To be updated

## Hardware

  * Tetlow K4A FL 15A Electric Kiln
  * Raspberry Pi (Rev 3B)
  * MAX 31855 Driver board
  * Cold-Junction K-Type Thermocouple
  * 25A Solid State Relay
  * Relay heatsink
  * Microswitch for door detection

### Schematic
WIP

## Installation

### Dependencies

The original developer tried to keep external dependencies to a minimum to make it easily
deployable on any flavor of open-source operating system. If you deploy it
successfully on any other OS, please update this:

#### Currently tested versions

  * greenlet-0.4.2
  * bottle-0.12.4
  * gevent-1.0
  * gevent-websocket-0.9.3

#### Ubuntu/Raspbian

    $ sudo apt-get install python-pip python-dev libevent-dev
    $ sudo pip install ez-setup
    $ sudo pip install greenlet bottle gevent gevent-websocket

#### Gentoo

    $ emerge -av dev-libs/libevent dev-python/pip
    $ pip install ez-setup
    $ pip install greenlet bottle gevent gevent-websocket

#### Raspberry PI deployment

If you want to deploy the code on a Pi for production:

    $ pip install RPi.GPIO

This **only applies to non-Raspbian installations**, since Raspbian ships
RPi.GPIO with the default installation.

### Clone repo

    $ git clone https://github.com/ninjajazza/piKiln.git
    $ cd piKiln

## Configuration

All parameters are defined in config.py, just copy the example and review/change to your mind's content.

    $ cp config.py.EXAMPLE config.py

## Usage

### Server Startup

    $ ./picoReflowd.py

### Autostart Server on Boot
If you want the server to autostart on boot, run the following commands

    sudo cp /home/pi/piKiln/lib/init/pikiln /etc/init.d/
    sudo chmod +x /etc/init.d/pikiln
    sudo update-rc.d pikiln defaults

### Client Access

Open Browser and go to http://127.0.0.1:8081 (for local development) or the IP
of your Pi and the port defined in config.py (default 8081).

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Support & Contact

Please use the issue tracker for project related issues.
