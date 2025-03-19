# PopMessage

**PopMessage** is a Python package that enhances your development process with customizable pop-up messages. It allows you to display reminders, debug feedback, and fun surprises through pop-ups with random colors and sounds. With timer functionality, you can set delays for reminders, while error and debug pop-ups provide real-time feedback on your code. Whether you need a moment of wholesome encouragement or a playful surprise, PopMessage adds a unique touch to your coding experience.

// insert pypi badge [badge](link to workflows)

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
 - Kivy Dependencies: You many need to install additional dependecies depending on your platform. Please refer to the [Kivy installation guide](https://kivy.org/doc/stable/gettingstarted/installation.html).
 - Virtual Environment ([pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies)): We recommend you use a virtual environment to run PopMessage to isolate dependencies.

### Installing in a Seperate Project

To import the PopupMessage module into your project:

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

We recommend you use a virtual environment when running PopMessage. To do so:

Run this command in your terminal or command prompt when you are in the cloned repository:
```sh
pipenv shell
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
__init__(self)
```

Constructs an instance of the `PopupMessage` class which represents a pop-up message window. It initializes instance variables with default properties for the pop-up message window. Developers who want to create an instance of `PopupMessage` class should call `PopupMessage()`.

Upon instantiation, each PopupMessage object has the following properties with default values:

- **message**: The message to be displayed in the pop-up window. Defaults to "Default Message"
- **bgColor**: The background color in the pop-up window.Defaults to "white".
- **fontColor**: The text color of the displayed message. Defaults to "black".
- **fontSize**: The font size of the displayed message. Defaults to 75.
- **timerDuration**: The number of minutes before the pop-up window gets displayed. Defaults to 0.

**Parameters**: None

**Return**: None

### Public Methods

```python
displayPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None)
```

This method displays the pop-up message window with customized properties defined through the parameters. If any of the parameters are not specified, it will default the property to the last configured value.

**Parameters**:

- **message** (str, optional): The message to be displayed in the pop-up window. Defaults to the last configured value.
- **bgColor** (str or tuple, optional): The background color in the pop-up window.Defaults to the last configured value.
- **fontColor** (str or tuple, optional): The text color of the displayed message. Defaults to the last configured value.
- **fontSize** (int, optional): The font size of the displayed message. Defaults to the last configured value.

**Return**: None

---

```python
displayTimerPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None, timerDuration=None)
```

TO ADD

---

```python
displaySFPopup(self, code_to_execute)
```

This method displays a success or error message depending on the status on your code. If the code runs successfully, a nice comment will be displayed. If the code runs unsuccessfully, a derogatory comment will be displayed.

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

TO ADD

#### 4. Create and display a coding-feedback pop-up message window 

```python
#Example4 Create and display a debug succes/error message test
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

Link to an example Python program using our package: [demo.py](https://github.com/software-students-spring2025/3-python-package-push-then-pull/blob/main/demo.py)

## Contributing

We welcome contributions! If you'd like to contribute to our package, here's how to set up your development environment:

1. This module requires Python version 3.10 or higher. Install Python and [pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) if not already installed.
2. Clone our git repository to your local machine. Run `git clone https://github.com/software-students-spring2025/3-python-package-push-then-pull.git`
3. Go to your cloned project directory, then create and activate a virtual environment: `pipenv shell`
4. Inside your active virtual environment, install the following dependencies by running these commands:

   ```sh
   pipenv install kivy
   pipenv install pytest
   pipenv install pytest-mock
   pipenv install build
   pipenv install twine
   ```

5. For development purposes, install the package in "_editable_" mode so that changes to the package are immediately updated in the virtual environment.

- Run `pipenv install -e .` from the main project directory.

6. Check Pipfile to verify all the dependencies are installed. Make sure python_version is the 3.10 or above.
7. Now you are ready to contribute to our module. To add new features to our module, write your code under `src/popmessage` directory. The main code of our module is located in `src/popmessage/popmsg.py` file. (see [additional documentation](#-additional-documentation-for-contributors) for contributors below)
8. Any unit tests you've created should be included within the `tests` directory.
9. To run the unit tests manually, navigate to the main project directory and run: `python3 -m pytest`

- If the above command throws any error, try `pipenv run python3 -m pytest`, or exit and reactivate your virtual environment and try again.

For testing purposes you can follow these steps to build and upload your enhanced package to TestPyPI:

1. Build the project by running `python -m build` from the same directory where the `pyproject.toml` file is located.
2. Verify that the built `.tar` archive has the files you expect your package to have (including any important non-code files) by running the command: `tar --list -f dist/popmessage-0.0.3.tar.gz`, where `popmessage-0.0.3` is replaced with your own package name and version.
3. Create an account on [TestPyPI](https://test.pypi.org/) where one can upload to a test repository instead of the production PyPI repo.
4. Create a [new API token](https://test.pypi.org/manage/account/#api-tokens) on TestPyPI with the "Scope" set to “Entire account”. Save a copy of the token somewhere safe.
5. [Upload your package](popmessage) to the TestPyPI repository using twine, e.g. `twine upload -r testpypi dist/*`
6. Twine will output the URL of your package on the PyPI website - load that URL in your web browser to see your packaged published

Every time you change the code in your package, you will need to rebuild and reupload it to PyPI. You will need to build from a clean slate and update the version number to achieve this:

1. delete the autogenerated `dist` directory
2. delete the autogenerated `src/*.egg-info` directory
3. update the version number in `pyproject.toml` and anywhere else it is mentioned (do a find/replace) (e.g., from 0.0.3 to 0.0.4)
4. build the package again with `python -m build`
5. upload the package again with `twine upload -r testpypi dist/*`

Repeat as many times as necessary until the package works as expected.

Once you are satisfied with your changes, you are now ready to push your changes.

1. Before pushing your changes, make sure the version number in pyproject.toml or anywhere else it is mentioned is updated.
2. Now you can push your changes to your branch in the Github repository.
3. Once you submit a pull request, this will trigger GitHub Actions to run the automated unit tests. One of the maintainers of the repository will review your pull request. If approved, your latest code changes will be uploaded to the real PyPI by the maintainer.

### Additional Documentation for Contributors

PopupMessage class is a subclass of kivy.app.App class. The following methods are located in PopupMessage and can be enhanced by contributors.

```python
_setProperties(msg, bgColor, fontColor, fontSize, timerDuration)
```

A protected method that sets the properties of the pop-up message window.

---

```python
_createPopup(self)
```

A protected method that creates the pop-up message window with the configured properties.

Returns the layout for rendering.

---

```python
build(self)
```

Kivy's abstract method that every subclass must implement and gets automatically invoked after App.run() is called.

Returns the created pop-up window layout.

---

## Compatibility Notice

The `popmessage` package relies on the Kivy library, which may cause compatibility issues on Linux systems.

## License

[Click Here](https://github.com/software-students-spring2025/3-python-package-push-then-pull/blob/suprise-me/LICENSE) to view the license.

## Acknowledgments

- Thanks to [Kivy](https://kivy.org/) for providing a great GUI framework.
- Inspired by the need for interactive pop-up reminders in Python applications.
