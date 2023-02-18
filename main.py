import tkinter as tk
import webbrowser
import time
import os
import cv2
import threading
from dotenv import dotenv_values

config = dotenv_values(".env")

def rick_roll():
    if (config['BROWSER_REDIRECT'] == 'True'):
        webbrowser.open(config['RICK_ROLL_URL'], new=2)
    else:
        video_thread = threading.Thread(target=play_video, args=("rickroll.mp4",))
        video_thread.start()

def play_video(filename):
    cap = cv2.VideoCapture(filename)
    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
        else:
            break
        cv2.waitKey(25)
    cap.release()
    cv2.destroyAllWindows()

def shutdown():
    print("Shutting down...")
    os.system('shutdown -t 0 -r -f')

def key_press(event):
    root.unbind("<Key>")
    root.unbind("<Button-1>")
    rick_roll()

    if (config['WILL_REBOOT'] == 'True'):
        print("Rebooting in " + config['DELAY_REBOOT'] + " seconds...")
        time.sleep(int(config['DELAY_REBOOT']))
        shutdown()

# creating the tkinter window
root = tk.Tk()
root.configure(bg="black")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.overrideredirect(True)

root.bind('<Key>', key_press)
root.bind("<Button-1>", key_press)

# focus on the window
root.focus_set()
root.mainloop()