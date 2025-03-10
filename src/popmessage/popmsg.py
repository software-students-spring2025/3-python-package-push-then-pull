from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Global variables
message = "Default Message"
bkgColor = "white"       # Can be either color name or (R,G,B,A) tuple
fontColor = "black"      # Can be either color name or (R,G,B,A) tuple
font = "Arial"
fontSize = 100
timerDuration = 0

# Set all properties of the pop-up message, will use default values if not set
def setProperties(msg="Default Message", bColor="white", fColor="black", ft="Arial", ftSize=100, duration=0):
    global message, bkgColor, fontColor, font, fontSize, timerDuration
    message = msg
    bkgColor = bColor
    fontColor = fColor
    font = ft
    fontSize = ftSize
    timerDuration = duration

# Create the pop-up message using the configured properties
def createPopup():
    global message, bkgColor, fontColor, font, fontSize, timerDuration
    
    # Make sure all properties are set before displaying the pop-up message
    if None in {message, bkgColor, fontColor, font, fontSize, timerDuration}:
        raise ValueError("Error: Please set the properties before displaying the message.")
    
    Window.clearcolor = bkgColor  
    layout = BoxLayout(orientation='vertical')
    label = Label(text=message, color=fontColor, font_name=font, font_size=fontSize)
    
    layout.add_widget(label)
    return layout

class MyPopup(App):
    def build(self):
        return createPopup()

# Display the pop-up message window with the configured properties
def displayPopup():
    MyPopup().run()

if __name__ == '__main__':
    # Example popup window
    setProperties("Hello, World!", "purple", (1, 0, 0, 1), "Times New Roman", 100)
    displayPopup()