import pytest
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from src.popmessage import popmsg

class Tests:
    
    @pytest.fixture
    def popup(self):
        """Fixture to create a new PopupMessage instance before each test"""
        popup_instance = popmsg.PopupMessage()
        return popup_instance
        
    # Test functions
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_initializations(self, popup):
        assert popup._message == "Default Message"
        assert popup._bgColor == "white"
        assert popup._fontColor == "black"
        assert popup._fontSize == 75
        assert popup._timerDuration == 0
        assert popup._type == popmsg.PopupMessage.POPUP_TYPE_REGULAR