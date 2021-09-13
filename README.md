# Fetch Rewards Coding Exercise - SDET

## Requirements:

### Python 3 
You can download and install Python [here](https://www.python.org/downloads/)

### Selenium
You can install selenium by running on your command line:
`pip install selenium`

Alternatively you can install requirements by running:
`pip install requirements.txt`

### Chrome Webdriver
You must download and install Chrome through [here](https://www.google.com/chrome/)

You must also download and extract the version of ChromeDriver, [here](https://sites.google.com/chromium.org/driver/downloads?authuser=0), that matches your installation of Chrome into the root directory of this program.

## Balancing Problem

Given a [balance scale](http://ec2-54-208-152-154.compute-1.amazonaws.com/) and 9 gold bars of the same size and look. You don’t know the exact weight of each bar, but you know they are the same weight, except for only one fake bar. It weighs less than others. You need to find the fake gold bar by only bars and balance scales.You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.

This program will solve this problem through automation, using Selenium, by splitting the gold bars into 3 sets. Initially it will weigh the first two sets to get the information needed to solve the problem. If `Set 1` and `Set 2` weigh the same, then we know the fake bar is in `Set 3`. If `Set 1` is lighter than `Set 2`, then we know that the fake bar is in `Set 1`, and vice versa. After finding out which set the fake bar is in, we can weigh two out of the three bars in the set that has the fake bar, and determine exactly which one is the fake within 2 weighs.

## Executing Code:
You can run this code on your preferred Python IDE or run this command on your command line:
`python main.py`
