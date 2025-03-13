from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class PopupMessage(App):
    def __init__(self):
        super().__init__()
        # Set the default properties of the pop-up message window
        self._setProperties("Default Message", "white", "black", 75, 0)

    def _setProperties(self, msg, bgColor, fontColor, fontSize, timerDuration):
        """
        Protected method: Sets all pop-up message window properties
        """
        self._message = msg
        self._bgColor = bgColor
        self._fontColor = fontColor
        self._fontSize = fontSize
        self._timerDuration = timerDuration

    
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
        
        self._setProperties(msg, bgColor, fontColor, fontSize, timerDuration)
        self.run()

    def build(self):
        """
        Kivy's abstract method that every child class must implement 
        and gets automatically invoked after App.run() is called.
        """ 
        return self._createPopup()

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