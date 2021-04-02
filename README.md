# HVN-Generator
[![Build Status](https://travis-ci.com/davidholton/hvn-generator.svg?branch=main)](https://travis-ci.com/davidholton/hvn-generator)

## Installing
First you will need to make a clone of this repository using the following command or through your favorite source control application. Make sure to change your working directory into the cloned project folder.

`git clone https://github.com/davidholton/hvn-generator/ && cd hvn-generator`

### Dependencies
Ensure your system has at least Python 3.6 in order to build HVN-Generator.

To install the required Python packages run the following command in the project folder.

`python -m pip install -r requirements.txt`

You are now all set!

## Running Tests
From inside the root `hvn-generator/` directory run `python -m pytest`.

Verbose testing can be ran with the `-s -v` flags: `python -m pytest -s -v` to enable printing from inside test cases.

An example of the HVN of the output data can be tried by running `pytest -s test/repetition.py`.

### To run GUI version

Start with `python gui.py`
