import pytest
from pytest_mock import MockerFixture
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from src.popmessage.popmsg import PopupMessage  

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
        assert popup._type == PopupMessage.POPUP_TYPE_REGULAR
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
        mock_create_popup = mocker.patch.object(popup, "_createPopup", return_value="Regular Popup")
        mock_create_timer_popup = mocker.patch.object(popup, "_createTimerPopup", return_value="Timer Popup")
        mock_create_sf_popup = mocker.patch.object(popup, "_createSFPopup", return_value="Success/Fail Popup")
        mock_create_random_popup = mocker.patch.object(popup, "_createRandomPopup", return_value="Random Popup")

        popup._type = PopupMessage.POPUP_TYPE_REGULAR
        assert popup.build() == "Regular Popup"
        mock_create_popup.assert_called_once()

        popup._type = PopupMessage.POPUP_TYPE_TIMER
        assert popup.build() == "Timer Popup"
        mock_create_timer_popup.assert_called_once()

        popup._type = PopupMessage.POPUP_TYPE_SUCCESS_FAIL
        assert popup.build() == "Success/Fail Popup"
        mock_create_sf_popup.assert_called_once()

        popup._type = PopupMessage.POPUP_TYPE_RANDOM
        assert popup.build() == "Random Popup"
        mock_create_random_popup.assert_called_once()

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
        assert popup._type == PopupMessage.POPUP_TYPE_REGULAR

        # Check that _setProperties was called with default values
        mock_set_properties.assert_called_once_with(
            popup._message, popup._bgColor, popup._fontColor, popup._fontSize, popup._timerDuration
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
        timerDuration = 7.5

        popup.displayPopup(msg, bgColor, fontColor, fontSize, timerDuration)
        assert popup._type == PopupMessage.POPUP_TYPE_REGULAR
        
        # Check that _setProperties was called with custom values
        mock_set_properties.assert_called_once_with(msg, bgColor, fontColor, fontSize, timerDuration)

        mock_run.assert_called_once()
