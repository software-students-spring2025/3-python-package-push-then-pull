from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.base import runTouchApp
from kivy.base import stopTouchApp
import random
import math
import time
import os

class PopupMessage(App):
    # List of derogatory comments for random selection when code is unsuccessful
    derogatory_comments = [
        "You suck at coding!",
        "Better luck next time!",
        "Is that even a real error?",
        "Wow, that’s a new level of failure.",
        "You’re really bad at this, huh?",
        "Do you even have a computer science degree?",
        "Who let you touch a computer?"
    ]

    # List of good comments for random selection when code is successful
    good_comments = [
        "Great job, you're doing awesome!",
        "Keep up the excellent work!",
        "You're a coding wizard!",
        "Nice work, you're on the right track!",
        "Fantastic effort, keep going!",
        "Someone was a straight A student!",
        "I'm proud of you!"
    ]

    def __init__(self):
        super().__init__()
        # Set the default properties of the pop-up message window
        self._setProperties("Default Message", "white", "black", 75, 0)

        # List of sounds for random selection when _createRandomPopup is called
        directory = os.path.dirname(os.path.abspath(__file__))
        self.sounds = [
            os.path.join(directory, "sounds", "oh-brother-this-guy-stinks.mp3"),
            os.path.join(directory, "sounds", "yippeeeeeeeeeeeeee.mp3"),
            os.path.join(directory, "sounds", "sad-meow-song.mp3"),
            os.path.join(directory, "sounds", "anime-wow-sound-effect.mp3"),
            os.path.join(directory, "sounds", "they-ask-you-how-you-are-and-you-just-have-to-say-that-youre-fine-sound-effect_IgYM1CV.mp3"),
            os.path.join(directory, "sounds", "applause-4.mp3"),
            os.path.join(directory, "sounds", "emotional-damage-meme.mp3"),
            os.path.join(directory, "sounds", "kids-saying-yay-sound-effect_3.mp3"),
            os.path.join(directory, "sounds", "george-micael-wham-careless-whisper-1.mp3"),
            os.path.join(directory, "sounds", "five-nights-at-freddys-full-scream-sound_2.mp3"),
            os.path.join(directory, "sounds", "five-nights-at-freddys-2-full-scream-sound.mp3"),
            os.path.join(directory, "sounds", "fnaf-1-music-box.mp3"),
            os.path.join(directory, "sounds", "jojos-golden-wind_kL2WElB.mp3")
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
            Window.size = (1000, 750)
            return self._createPopup()
            
    def _createPopup(self):
        """
        Protected method: Create the pop-up message window using the configured properties
        """
        Window.clearcolor = self._bgColor  
        layout = BoxLayout(orientation='vertical')
        label = Label(text=self._message, color=self._fontColor, font_size=self._fontSize)
        
        layout.add_widget(label)
        return layout
    
    def displayPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None):
        """
        Display a pop-up message window with the specified or default properties.
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
        
        self._setProperties(msg, bgColor, fontColor, fontSize, 0)
        self.run()
    
    def displayTimerPopup(self, msg=None, bgColor=None, fontColor=None, fontSize=None, timerSeconds=None):
        """
        Function that schedules a popup in a certain (specified or random) number of seconds
        """
        # set window background to "blank"/default 
        Window.clearcolor = "black"
        Window.size = (100, 100)

        # Use default values if parameters are not provided
        if msg is None:
            msg = self._message
        if bgColor is None:
            bgColor = self._bgColor
        if fontColor is None:
            fontColor = self._fontColor
        if fontSize is None:
            fontSize = self._fontSize
        if timerSeconds is None:
            seconds = random.randrange(0, 60)
            print("random time ", seconds)
        else:
            seconds = timerSeconds

        # type checking?
        if not isinstance(msg, str):
            raise TypeError("Custom message must be of type String")
        
        # set the properties of the popup
        self._setProperties(msg, bgColor, fontColor, fontSize, seconds)

        # schedule the popup to happen in x many seconds
        Clock.schedule_once(self._callback, seconds)

        # keep the app running so the program doesn't quit before the popup is called
        runTouchApp()
        

    def _callback(self, dt):
        """
        Call back function used to schedule a timed popup
        """
        # stop the previously called application instance, as the run() method will start another
        stopTouchApp()
        # run the popup
        self.run()
        # when exited, the screen will return to blank/default
        Window.clearcolor = "black"
        

    def displaySFPopup(self, code_to_execute):
        try:
            code_to_execute()
            # Sucessful code message
            msg = random.choice(self.good_comments)
            bgColor = "green" 
        except Exception as e:
            # Error Message
            msg = random.choice(self.derogatory_comments)
            bgColor = "red"
        
        self._setProperties(msg, bgColor, "white", 50, 0)
        self.run()   

    def displayRandomPopup(self):
        """
        Creates a popup with a randomly chosen message and sound
        """
        messages = self.derogatory_comments + self.good_comments
        msg = random.choice(messages)
        # random rgb values for colors, alpha(opaqueness) set to 1
        bgColor = (random.random(), random.random(), random.random(), 1)
        fontColor = (random.random(), random.random(), random.random(), 1)
        fontSize = random.randint(30, 80)
        # play a random sound
        rand_sound = random.choice(self.sounds)
        sound = SoundLoader.load(rand_sound)
        if sound:
            sound.play()

        self._setProperties(msg, bgColor, fontColor, fontSize, 0)
        self.run()

