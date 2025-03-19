from src.popmessage.popmsg import *

'''

Run this file to execute example code putting our package into practice

'''
# Example1 default pop-up message window
myPopup1 = PopupMessage()
myPopup1.displayPopup()

# Example2 user defined pop-up message window
myPopup2 = PopupMessage()
myPopup2.displayPopup(msg="Hello World", bgColor="blue")

# Example3 user defined pop-up message window
myPopup3 = PopupMessage()
myPopup3.displayPopup(msg="foobar", bgColor="magenta", fontColor="purple")

#Example4 debug succes/error message test
myPopup4 = PopupMessage()
myPopup4.displaySFPopup(lambda: print("Code ran successfully!"))
myPopup4.displaySFPopup(lambda: 5 + 5)
myPopup4.displaySFPopup(lambda: print(hello))
myPopup4.displaySFPopup(lambda: 1 / 0)

#Example5 random pop-up message window
myPopup5 = PopupMessage()
myPopup5.displayRandomPopup()

#Example6 timer window
myPopup6 = PopupMessage()
myPopup6.displayTimerPopup(msg="Surprise!", bgColor="pink", timerSeconds=5)
myPopup6 = PopupMessage()
myPopup6.displayTimerPopup(msg="Randomly generated wait time ...", bgColor=(1, .769, 0, 1))