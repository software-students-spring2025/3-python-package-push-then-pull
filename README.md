# PopMessage

**PopMessage** is a Python package that enhances your development process with customizable pop-up messages. It allows you to display reminders, debug feedback, and fun surprises through pop-ups with random colors and sounds. With timer functionality, you can set delays for reminders, while error and debug pop-ups provide real-time feedback on your code. Whether you need a moment of wholesome encouragement or a playful surprise, PopMessage adds a unique touch to your coding experience.

// insert pypi badge [badge](link to workflows)

## Table of Contents

1. [Teammates](#teammates)
2. [PyPI Page](#pypi-link)
3. [Features](#features)
4. [Installation](#installation)
5. [Documentation](#documentation)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgements](#acknowledgments)

## Teammates

- [Shamaamah Ahmad](https://github.com/shamaamahh)
- [Maya Humston](https://github.com/mayhumst)
- [Jessica Chen](https://github.com/jessicahc)
- [Catherine Huang](https://github.com/Catherine1342)

## PyPI Link

[PopMessage on PyPI](link) broken link for now

## Features

- **Popup Windows Setup**: Helper functions to create and display popup messages with specified or default properties.
- **Timer Functionality**: Set a timer for reminders to display pop-up messages after a specified delay.
- **Error and Debug Pop-ups**: Receive success or error messages with feedback on the status of your code.
- **Surprise Me!**: Display random messages such as wholesome reminders, fun surprises, and even a few playful or humorous ones.
- **Random Colors and Sounds**: Each pop-up can have randomly generated colors and sounds for extra fun.

## Installation

Please make sure you have installed

- Python: version 3.10 or higher.
- Git: To clone the repository.
- Kivy: You need to install the Kivy library in order to use our package. Please refer to the [Kivy installation guide](https://kivy.org/doc/stable/gettingstarted/installation.html).
- Virtual Environment ([pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies)): We recommend you use a virtual environment to run PopMessage to isolate dependencies.


### Installing in a Separate Project

In your active virtual environment, you can download and install the latest version of our package from PyPI by running the command:

```sh
pipenv install popmessage
```

You also need to install the Kivy library to use our package. Run the command:

```sh
pipenv install "kivy[base]"
```

#### To import the PopupMessage module into your project:

```python
from popmessage.popmsg import PopupMessage
```

### Cloning Locally

To clone the repository, please open terminal or command prompt on your system and run:

```sh
git clone https://github.com/software-students-spring2025/3-python-package-push-then-pull.git
cd 3-python-package-push-then-pull
```

#### Setup a Virtual Environment

We recommend you use a virtual environment when running PopMessage. To set up your virtual environment and install dependencies, run these commands in your terminal or command prompt when you are in the cloned repository:

```sh
pipenv lock
pipenv install -e .
```

#### Running PopMessage

Once you make sure all dependencies have been installed, please execute the following command to run PopMessage:

```sh
pipenv run python -m popmessage.popmsg
```

Please note executing this command won't do anything as no functions from the package will be called.

To see examples of pop-up messages using PopMessage's functions, please execute the following command:

```sh
pipenv run python demo.py
```

## Documentation

You can easily import PopMessage into your Python project and start using the functions right away. Here's how you can use the package:

### Constructor

```python
PopupMessage()
```

Constructs an instance of the `PopupMessage` class which represents a pop-up message window. It initializes instance variables with default properties for the pop-up message window. To display a popup message window, you must first create an instance of `PopupMessage` class by calling this constructor.

Upon instantiation, each PopupMessage object has the following properties with default values:

- `message`: The message to be displayed in the pop-up window. Defaults to "Default Message"
- `bgColor`: The background color in the pop-up window. Defaults to "white".
- `fontColor`: The text color of the displayed message. Defaults to "black".
- `fontSize`: The font size of the displayed message. Defaults to 75.
- `timerDuration`: The number of seconds before the pop-up window gets displayed. Defaults to 0.

**Parameters**: None

**Return**: None

### Public Methods

```python
displayPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None)
```

This method displays the pop-up message window with customized properties defined through the parameters. If any of the parameters are not specified, it will default the property to the last configured value.

**Parameters**:

- `msg` (str, optional): The message to be displayed in the pop-up window. Defaults to the last configured value.
- `bgColor` (str or tuple, optional): The background color in the pop-up window. Defaults to the last configured value.
- `fontColor` (str or tuple, optional): The text color of the displayed message. Defaults to the last configured value.
- `fontSize` (int, optional): The font size of the displayed message. Defaults to the last configured value.
- `timerSeconds` (int, optional): The amount of time, in seconds, to wait before the popup will be shown. Defaults to a random integer between 1 and 60.  

**Return**: None

---

```python
displayTimerPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None, timerSeconds=None)
```

This method will display a popup message similar to the previous function, with customizable properties, but will schedule the popup to be executed with a delay. The timer can be used to schedule a popup reminder, or to keep you on your toes when developing. If the timer duration is not specified, the function will randomize a timer duration of up to 60 seconds. If any of the other parameters are not specified, they will default to the last configured value. 

**Parameters**:

- `msg` (str, optional): The message to be displayed in the pop-up window. Defaults to the last configured value.
- `bgColor` (str or tuple, optional): The background color in the pop-up window. Defaults to the last configured value.
- `fontColor` (str or tuple, optional): The text color of the displayed message. Defaults to the last configured value.
- `fontSize` (int, optional): The font size of the displayed message. Defaults to the last configured value.

**Return**: None

---

```python
displaySFPopup(self, code_to_execute)
```

This method displays a success or error message depending on the status of your code. If the code runs successfully, a nice comment will be displayed. If the code runs unsuccessfully (throws an exception), a derogatory comment will be displayed.

**Parameters**:

- `code_to_execute`: A lambda function

**Return**: None

---

```python
displayRandomPopup(self)
```

This method displays a pop-up message window with randomly chosen properties. A random message will be displayed and a random sound will be played when this method is called.

**Parameters**: None

**Return**: None

### Examples

#### 1. Create and display a pop-up message window with default properties

You can create a basic pop-up message window by creating an instance of PopupMessage class first and then call displayPopup() with no parameters specified.

```python
# Example1: Create and display a pop-up message window with default properties
myPopup1 = PopupMessage()
myPopup1.displayPopup()
```

#### 2. Create and display a pop-up message window with customized properties

To customize a basic pop-up message window, you can invoke displayPopup() method on an existing instance of PopupMessage and specify the properties you want to customize through its parameters.

```python
# Example2: Create and display a pop-up message window with customized properties
myPopup2 = PopupMessage()
myPopup2.displayPopup(msg="Hello World", bgColor="blue", fontSize=75)
```

#### 3. Create and display a delayed / timed pop-up message window with customized properties

You can create a delayed popup by invoking the displayTimerPopup() function. Parameters may be specified if desired. If no delay is specified, the timer duration will be randomized. 

**Note: Be sure to save the instance of PopupMessage() in a variable before invoking this method. If not, unpredictable behavior will occur and the timed function may not be called.**

```python
#Example3 timer window
myPopup3 = PopupMessage()
myPopup3.displayTimerPopup(msg="Surprise!", bgColor="pink", timerSeconds=5)
myPopup3 = PopupMessage()
myPopup3.displayTimerPopup(msg="Randomly generated wait time ...", bgColor=(1, .769, 0, 1))
```

#### 4. Create and display a coding-feedback pop-up message window

```python
#Example4 Create and display a debug success/error message test
myPopup4 = PopupMessage()
myPopup4.displaySFPopup(lambda: print("Code ran successfully!"))
myPopup4.displaySFPopup(lambda: 5 + 5)
myPopup4.displaySFPopup(lambda: print(hello))
myPopup4.displaySFPopup(lambda: 1 / 0)
```

#### 5. Create and display a random pop-up message window

You can create a random pop-up message window by creating an instance of PopupMessage class first and then call displayRandomPopup() with no parameters specified.

```python
# Example5: Create and display a random pop-up message window with randomized properties
myPopup5 = PopupMessage()
myPopup5.displayRandomPopup()
```

#### 6. Sample program

Link to a sample program: [demo.py](https://github.com/software-students-spring2025/3-python-package-push-then-pull/blob/main/demo.py)

Note: Due Kivy library's limitation, although multiple windows are created in this program, only one pop-up window is displayed at a time. The user must close the existing pop-up window displayed to view the next pop-up window.

## Contributing

We welcome contributions! If you'd like to contribute to our package, here's how to set up your development environment:

1. This module requires Python version 3.10 or higher. Install Python and [pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) if not already installed.
2. Create a fork of our repository by clicking on the Fork button at the top-right corner of the repository page.
3. Clone your fork of our repository to your computer.

```sh
git clone https://github.com/your-username/3-python-package-push-then-pull.git
```

4. Go to your cloned project directory, then create and activate a virtual environment with `pipenv`. Regenerate the Pipfile.lock file for your machine specifications. 

```sh
pipenv lock
```

5. Inside your active virtual environment, install all necessary dependencies with the following command.For development purposes, the packages will be installed in "_editable_" mode so that changes to the package are immediately updated in the virtual environment.

```sh
pipenv install -e .
```

6. Create a new branch in your local repository.
7. Now you are ready to contribute to our module. To add new features to our module, write your code under `src/popmessage` directory. The main code of our module is located in `src/popmessage/popmsg.py` file.
8. Add unit tests for any new functions you've added to the module. To run the unit tests, see the [How to test popmessage package](#how-to-test-popmessage-package) section.
9. Make sure the version number in pyproject.toml or anywhere else it is mentioned is updated before you are ready to push your new changes.
10. Before committing your changes, pull the latest changes from the upstream repository, and merge them into your local branch.
11. Once you are satisfied with your changes, add and commit your changes. Push your changes to your remote repository on GitHub.
12. Go to the original repository. Select your branch and submit a Pull Request (PR) for review. One of the maintainers of the repository will review your pull request. If approved, your latest code changes will be uploaded to PyPI by the maintainer.

### How to test `popmessage` package

- Our unit test file is `test_popmsg.py`, located in the `tests` directory. You can add more unit test cases in this file.
- To run the unit test manually, navigate to the main project directory. 
   - If you are working without a virtual environment, run: `python -m pytest`
   - If you are working with the `pipenv` virtual environment, run: `pipenv run python -m pytest`

### How to build `popmessage` package

Build the project from the root directory where the `pyproject.toml` file is located. 
- If you are working without a virtual environment, run: `python -m build`
- If you are working with the `pipenv` virtual environment, run: `pipenv run python -m build`

Verify that the `dist` directory now contains a wheel and a zipfile with the correct version number in the filename. 

For your development testing purposes, you can follow this [tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to use twine to upload the package with your latest changes to TestPyPI.

---

**Note:** The `popmessage` package has been manually tested with Python 3.10, 3.12, and 3.13 on MacOS, Windows, and Ubuntu. Because this package relies on the Kivy library which requires graphical libraries available on the local OS, if you experience any compatibility issues on your local machine, please refer to [Kivy official website](https://kivy.org/).

## License

[Click Here](https://github.com/software-students-spring2025/3-python-package-push-then-pull/blob/suprise-me/LICENSE) to view the license.

## Acknowledgments

- Thanks to [Kivy](https://kivy.org/) for providing a great GUI framework.
- Inspired by the need for interactive pop-up reminders in Python applications.
