# Miraculix
A library for all your examination processes at RWTH Aachen University.

You can use this library to write your own Python scripts. With this, you can automate tasks such as:
* Creating examination protocols for written exams
* Automated room assignment for participants
* Exporting easy to use .csv files for the use in Microsoft Excel
* Automated evaluation and assignment of grades
* Native import and export to RWTHOnline

## Getting started
Miraculix is build in Python 3.x and relies on some external packages.
Fortunately, you only need to have Python 3.x installed, since all important
dependencies are included within an virtual environment. If you do not want to 
us the virtual environment, you can install the following dependencies manually:
* sqlite3
* docxtpl

This can be done using pip.


### Install Python 3.x
#### Linux
Usually, Python 3.x is already included within the standard installation of linux. 
If not, you can get it by using
```
sudo apt-get install python3
```

#### Windows
To install Python 3.x on Windows machines, please go to [Python.org](https://www.python.org/downloads/windows/)
and download the Windows installation file for the latest release. The installation client will guide you through
the installation process.

## Documentation
You can find the documentation to this software within the Gitlab-Wiki.

## First Steps
If you want to write your own simple scripts to manage your examination process,
you can find a simple example in the examples directory of this project. This example 
is well documented and will guide you through the main stages of your examination 
process. These are e.g.
* Creating and saving a new exam
* Importing data from RWTHOnline
* Evaluating the examination
* Exporting final grades to RWTHOnline
* ...

## For Developers
### Running test
Unfortunately, there haven't been implemented any tests until now.

## Authors
* **Lukas Lamm** - [Institute of Applied Mechanics, RWTH Aachen University](http://www.ifam.rwth-aachen.de/aw/cms/IFAM/Themen/mitarbeiter/~wmw/lamm-lukas/?lang=de)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details