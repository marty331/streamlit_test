from tkinter import *
import subprocess
import os
import psutil
import signal

root=Tk()


def helloCallBack():
   print ("Below is the output from the shell script in terminal")
   # subprocess.call(['./stream.sh']) #shell=True)
   subprocess.Popen(['./stream.sh'])

def stopApp():
    print('StopApp called')
    ids = [proc.pid for proc in psutil.process_iter() if proc.name() == "streamlit"]
    print(f"ids found {ids}")
    for id in ids:
        os.kill(id, signal.SIGKILL)

buttonCommit=Button(root, height=1, width=10, text="Run App",
                    command=helloCallBack) # retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

buttonStop = Button(root, height=1, width=15, text="Stop App", command=stopApp)
buttonStop.pack()

mainloop()
