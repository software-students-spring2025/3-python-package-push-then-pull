import pytest
from popmessage.popmsg import PopupMessage

from pytest_mock import MockerFixture
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import time

class Tests:

    @pytest.fixture
    def popup(self):
        """Fixture to create a new PopupMessage instance before each test"""
        return PopupMessage()
        
    # Test functions
    def test_sanity_check(self):
        """Basic test to ensure pytest runs properly"""
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_initializations(self, popup):
        assert popup._message == "Default Message"
        assert popup._bgColor == "white"
        assert popup._fontColor == "black"
        assert popup._fontSize == 75
        assert popup._timerDuration == 0

    def test_set_properties(self, popup):
        popup._setProperties("Test Message", "blue", "red", 50, 10)
        assert popup._message == "Test Message"
        assert popup._bgColor == "blue"
        assert popup._fontColor == "red"
        assert popup._fontSize == 50
        assert popup._timerDuration == 10
   
    def test_build(self, mocker: MockerFixture, popup):
        mock_create_popup = mocker.patch.object(popup, "_createPopup", return_value="Popup Created")
        assert popup.build() == "Popup Created"
        mock_create_popup.assert_called_once()

    def test_create_popup(self, popup):
        popup._bgColor = [1, 1, 1, 1]
        layout = popup._createPopup()
        
        assert Window.clearcolor == popup._bgColor, "Window.clearcolor was not set correctly!"
        assert isinstance(layout, BoxLayout), "Expected layout to be a BoxLayout"
        assert len(layout.children) == 1, "Expected layout to have 1 child"
        assert isinstance(layout.children[0], Label), "Expected child to be a Label"
        assert layout.children[0].text == popup._message, "Label text does not match expected default message"

    def test_display_popup_defaults(self, popup, mocker):
        """Test displayPopup when no arguments are provided."""
        mock_set_properties = mocker.patch.object(popup, "_setProperties")
        mock_run = mocker.patch.object(popup, "run")

        popup.displayPopup()

        # Check that _setProperties was called with default values
        mock_set_properties.assert_called_once_with(
            popup._message, popup._bgColor, popup._fontColor, popup._fontSize, 0
        )

        mock_run.assert_called_once()

    def test_display_popup_with_params(self, popup, mocker):
        """Test displayPopup with custom parameters."""
        mock_set_properties = mocker.patch.object(popup, "_setProperties")
        mock_run = mocker.patch.object(popup, "run")

        msg = "Test Message"
        bgColor = (0.5, 0.5, 0.5, 1)
        fontColor = "yellow"
        fontSize = 20

        popup.displayPopup(msg, bgColor, fontColor, fontSize)
        
        # Check that _setProperties was called with custom values
        mock_set_properties.assert_called_once_with(msg, bgColor, fontColor, fontSize, 0)

        mock_run.assert_called_once()

    # SF tests
    def test_display_sf_popup_success(self, mocker, popup):
        """Test displaySFPopup with successful code execution."""
        mock_set_properties = mocker.patch.object(popup, "_setProperties")
        mock_run = mocker.patch.object(popup, "run")
        
        # Dummy function that does not raise an error
        def successful_code():
            pass

        popup.displaySFPopup(successful_code)

        mock_set_properties.assert_called_once()
        args = mock_set_properties.call_args[0]
        assert args[1] == "green" 
        mock_run.assert_called_once()

    def test_display_sf_popup_failure(self, mocker, popup):
        """Test displaySFPopup when code raises an error."""
        mock_set_properties = mocker.patch.object(popup, "_setProperties")
        mock_run = mocker.patch.object(popup, "run")

        # Dummy function that raises an error
        def failing_code():
            raise ValueError("Oops!")

        popup.displaySFPopup(failing_code)

        mock_set_properties.assert_called_once()
        args = mock_set_properties.call_args[0]
        assert args[1] == "red" 
        mock_run.assert_called_once()

    def test_display_sf_popup_random_comment(self, mocker, popup):
        """Test that displaySFPopup picks a comment from the correct list."""
        # Force predictable choices from good/derogatory comment lists
        popup.good_comments = ["Nice work, you're on the right track!"]
        popup.derogatory_comments = ["You suck at coding!"]

        mock_set_properties = mocker.patch.object(popup, "_setProperties")
        mock_run = mocker.patch.object(popup, "run")

        def fail_func():
            raise RuntimeError()

        popup.displaySFPopup(fail_func)

        msg_arg = mock_set_properties.call_args[0][0]
        assert msg_arg == "You suck at coding!"

    # Test to check if the properties of _displayRandomPopup are correct
    def test_random_popup_properties(self, mocker, popup):
        mock_set_properties = mocker.patch.object(popup, "_setProperties", wraps = popup._setProperties)
        mock_run = mocker.patch.object(popup, "run")
        popup.displayRandomPopup()

        # Get the popup properties
        msg_args, _ = mock_set_properties.call_args
        msg = msg_args[0]
        bgColor = msg_args[1]
        fontColor = msg_args[2]
        fontSize = msg_args[3]
        timerDuration = msg_args[4]

        # Test assertions
        possible_msg = popup.derogatory_comments + popup.good_comments
        assert msg in possible_msg

        # Check bgColor
        assert len(bgColor) == 4
        assert isinstance(bgColor, tuple)
        assert bgColor[3] == 1

        # Check fontColor
        assert len(fontColor) == 4
        assert isinstance(fontColor, tuple)
        assert fontColor[3] == 1

        # Check fontSize
        assert 30 <= fontSize <= 80
        assert timerDuration == 0

        mock_run.assert_called_once()
    
    # Test random popup sound
    def test_random_popup_sound(self, mocker, popup):
        # Create a mock sound for testing
        sound = mocker.Mock()
        mock_sound_loader = mocker.patch("popmessage.popmsg.SoundLoader.load", return_value = sound)

        mocker_set_properties = mocker.patch.object(popup, "_setProperties", wraps = popup._setProperties)
        mock_run = mocker.patch.object(popup, "run")
        popup.displayRandomPopup()

        # Check if sound was loaded
        sound_args = mock_sound_loader.call_args[0][0]
        assert sound_args in popup.sounds

        sound.play.assert_called_once()
        mock_run.assert_called_once()

    # Test to see what happens when no sound gets loaded
    def test_random_popup_no_sound(self, mocker, popup):
        # No sound
        mock_sound_loader = mocker.patch("popmessage.popmsg.SoundLoader.load", return_value = None)

        mocker_set_properties = mocker.patch.object(popup, "_setProperties", wraps = popup._setProperties)
        mock_run = mocker.patch.object(popup, "run")
        popup.displayRandomPopup()

        # Check if sound was loaded
        sound_args = mock_sound_loader.call_args[0][0]
        assert sound_args in popup.sounds

        # Make sure run and set properties are still being called
        mocker_set_properties.assert_called_once()
        mock_run.assert_called_once()

    # check that appropriate Exceptions are thrown if timer functions are called with incorrect parameters
    def test_timer_incorrect_params(self):
        # custom message must be String
        try:
            pop = PopupMessage()
            pop.displayTimerPopup(msg=7)
        except TypeError:
            assert True 
        else:
            assert False
        
        # timer duration must be an integer
        try:
            pop = PopupMessage()
            pop.displayTimerPopup(timerSeconds=9.9)
        except TypeError:
            assert True 
        else:
            assert False

        # timer duration must be >=1
        try:
            pop = PopupMessage()
            pop.displayTimerPopup(timerSeconds=-7)
        except ValueError:
            assert True 
        else:
            assert False


    # Test to check if the properties of the timer function are correct
    def test_timer_properties_default(self, mocker, popup):
        mock_set_properties = mocker.patch.object(popup, "_setProperties", wraps = popup._setProperties)
        mock_run = mocker.patch.object(popup, "run")
        popup.displayTimerPopup(timerSeconds=5)

        # Get the popup properties
        msg_args, _ = mock_set_properties.call_args
        msg = msg_args[0]
        bgColor = msg_args[1]
        fontColor = msg_args[2]
        fontSize = msg_args[3]
        timerDuration = msg_args[4]

        # Check properties (default for all)
        assert msg == "Default Message"
        assert bgColor == "white"
        assert fontColor == "black"
        assert fontSize == 75
        assert timerDuration > 0
        assert timerDuration <=60

        # ensure popup has been run 
        mock_run.assert_called_once()

    # Test to check if the properties of the timer function are correct
    def test_timer_properties_specified(self, mocker, popup):
        # Parameters
        set_msg = "timer!"
        set_bg = "red"
        set_font = "blue"
        set_size = 30
        set_timer = 5

        mock_set_properties = mocker.patch.object(popup, "_setProperties", wraps = popup._setProperties)
        mock_run = mocker.patch.object(popup, "run")
        start = time.perf_counter()
        popup.displayTimerPopup(set_msg, set_bg, set_font, set_size, set_timer)
        end = time.perf_counter()

        # Get the popup properties
        msg_args, _ = mock_set_properties.call_args
        msg = msg_args[0]
        bgColor = msg_args[1]
        fontColor = msg_args[2]
        fontSize = msg_args[3]
        timerDuration = msg_args[4]

        # Check properties (default for all)
        assert msg == set_msg
        assert bgColor == set_bg
        assert fontColor == set_font
        assert fontSize == set_size
        assert timerDuration == 5

        # Time elapsed for popup function call should be ABOUT five seconds
        assert (end - start) > 4.9
        assert (end - start) < 5.1

        # ensure popup has been run 
        mock_run.assert_called_once()