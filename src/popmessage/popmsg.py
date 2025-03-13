from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class PopupMessage(App):
    POPUP_TYPE_REGULAR = 0
    POPUP_TYPE_TIMER = 1
    POPUP_TYPE_SUCCESS_FAIL = 2
    POPUP_TYPE_RANDOM = 3

    def __init__(self):
        super().__init__()
        self._type = self.POPUP_TYPE_REGULAR
        # Set the default properties of the pop-up message window
        self._setProperties("Default Message", "white", "black", 75, 0)

        # List of derogatory comments for random selection when code is unsuccessful
        self.derogatory_comments = [
            "You suck at coding!",
            "Better luck next time!",
            "Is that even a real error?",
            "Wow, that’s a new level of failure.",
            "You’re really bad at this, huh?"
        ]

        # List of good comments for random selection when code is successful
        self.good_comments = [
            "Great job, you're doing awesome!",
            "Keep up the excellent work!",
            "You're a coding wizard!",
            "Nice work, you're on the right track!",
            "Fantastic effort, keep going!"
        ]

    def _setProperties(self, msg, bgColor, fontColor, fontSize, timerDuration):
        """
        Protected method: Sets all pop-up message window properties
        """
        self._message = msg
        self._bgColor = bgColor
        self._fontColor = fontColor
        self._fontSize = fontSize
        self._timerDuration = timerDuration

    def build(self):
            """
            Kivy's abstract method that every child class must implement 
            and gets automatically invoked after App.run() is called.
            """ 
            if self._type == PopupMessage.POPUP_TYPE_REGULAR:
                return self._createPopup()
            elif self._type == PopupMessage.POPUP_TYPE_TIMER:
                return self._createTimerPopup()
            elif self._type == PopupMessage.POPUP_TYPE_SUCCESS_FAIL:
                return self._createSFPopup()
            elif self._type == PopupMessage.POPUP_TYPE_RANDOM:
                return self._createRandomPopup()
            
    def _createPopup(self):
        """
        Protected method: Create the pop-up message window using the configured properties
        """
        Window.clearcolor = self._bgColor  
        layout = BoxLayout(orientation='vertical')
        label = Label(text=self._message, color=self._fontColor, font_size=self._fontSize)
        
        layout.add_widget(label)
        return layout
    
    def displayPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None, timerDuration=None):
        """
        Display the pop-up message window with the specified or default properties.
        """
        # Use default values if parameters are not provided
        if msg is None:
            msg = self._message
        if bgColor is None:
            bgColor = self._bgColor
        if fontColor is None:
            fontColor = self._fontColor
        if fontSize is None:
            fontSize = self._fontSize
        if timerDuration is None:
            timerDuration = self._timerDuration
        
        self._type = PopupMessage.POPUP_TYPE_REGULAR
        self._setProperties(msg, bgColor, fontColor, fontSize, timerDuration)
        self.run()

    # Add code to the following functions
    def _createTimerPopup(self):
        pass
    
    def displayTimerPopup(self):
        self._type = PopupMessage.POPUP_TYPE_TIMER
        self.run()

    def _createSFPopup(self):
        pass

    def displaySFPopup(self):
        self._type = PopupMessage.POPUP_TYPE_SUCCESS_FAIL
        self.run()

    def _createRandomPopup(self):
        pass

    def displayRandomPopup(self):
        self._type = PopupMessage.POPUP_TYPE_RANDOM
        self.run()

if __name__ == '__main__':
    # Example1 default pop-up message window
    myPopup1 = PopupMessage()
    myPopup1.displayPopup()

    # Example2 user defined pop-up message window
    myPopup2 = PopupMessage()
    myPopup2.displayPopup(msg="Hello World", bgColor="blue")

    # Example3 user defined pop-up message window
    myPopup3 = PopupMessage()
    myPopup3.displayPopup(msg="foobar", bgColor="magenta", fontColor="purple")