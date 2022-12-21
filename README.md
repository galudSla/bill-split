<h1 align="center"> Bill Split </h1> <br>
<p align="center">
  <a href=https://github.com/galudSla/bill-split>
    <img alt="Dollar sign" title="Dollar" src="https://www.nicepng.com/png/full/28-287043_money-bag-dollar-icon.png" height="150">
  </a>
</p>


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Executing](#executing)
- [Examples](#examples)
- [Issues](#issues)
- [Authors](#authors)


## Introduction

CLI application that calculates the best way to split the bill. 


## Features

A few of the things you can do with Bill Split:

* Multiple users with many expense inputs
* Stores the legder
* Not an one way app, can access every command every time
* Supports multiple in-line commands 


## Getting Started

### Dependencies

* Python 3.x and needs pre-installed python packages.\
re, os

* Library requirements are stored in requirements.txt\
click==8.1.3\
colorama==0.4.6


## Installation

* `git clone https://github.com/galudSla/bill-split.git`
* `cd to bill-split folder directory`
* `python -m venv <yourvenvname>`
* `activate virtual environment`
* `pip install -r requirements.txt`


## Executing

* When running `bill-splitt.py [-f [filename]]` -f (--filename) optional argument is not required but suggested to be provided. If filename option is not provided you will be asked inside Bill Split. The option filename searches either for an existing legder file with the filename given, if not found it creates one with the same name
*  There is an optional argument -s (--show) when calling `bill-splitt.py [-f [filename]] [-s [show]]` that prints previous inputs when at the beggining. Optional argument show can be set regardless filename argument existence
* The optional argument --help can be used for more information about the CLI script call

* Bill split commands
```
-h  --help          Help
-p  --print         Print your inputs so far
-w  --wipe          Delete everything
-i  --input         Add users [user1 user2 ...]
-d  --delete        Remove user completely [user1 users2 ...]
-a  --add           Add expense for one user at a time [user expense-name amount]
-u  --update        Update the expense of a user [user expense-name new-amount]
-r  --remove        Remove the expense for a specific user [user expense-name]
-e  --each          How much each one paid
-t  --total         Total amount paid
-c  --calculate     Calculate
-q  --quit          Quit
```
### Examples
* `bill-splitt.py -f fooTrip`\
the filename fooTrip does not exist, so a file fooTrip.txt is created to store the misc inputs
* `[+] -i Anne John Roger George`\
the names provided are saved 
* `[+] -a Anne ChineseRestaurant 50`\
the bill ChineseRestaurant is now stored to Anne's bill
* So, you forgot to add your friend Leah\
`[+] -i Leah`
* Now you want to see what you have done so far `[+] -p`
```
[*] Anne: ChineseRestaurant -> 50
[*] John: No inputs
[*] Roger: No inputs
[*] George: No inputs
[*] Leah: No inputs
```
* Now John buys beer for the party `[+] -a John BeerNight 100`
* Later Anne buys gas for the car, `[+] -a Anne Gas 43`
* -e checks how much money did each one spend in total and -t the total amount paid by the group `[+] -e -t `
```
[*] Anne: 93
[*] John: 100
[*] Roger: 0
[*] George: 0
[*] Leah: 0
[*] Total amount: 193
```
* Finally, it is time for the first split `[+] -c`
```
[$] Roger -> Anne 38.6
[$] George -> Anne 15.8
[$] George -> John 22.8
[$] Leah -> John 38.6
```
##### There are more commands you can explore by visiting [-h --help] inside Bill Split


## Issues 

Although Bill Split supports many in line arguments, it only supports different ones.\
`-i Giannis Mike -i Joanna` will only store Joanna.\
`-a Giannis Car 200 -p -e -t` works just fine.


## Authors

@galudSla\
email: tedgiann@gmail.com

