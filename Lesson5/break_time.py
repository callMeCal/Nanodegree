import time
import webbrowser

total_breaks = 3
break_count = 0

while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=Pgg0tvF22EI")
    break_count += 1
