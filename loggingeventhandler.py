#!/usr/bin/python
#adding random comment
#want to remove comment
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fileRename import renameFile

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print ("Got it, modified eventcalled!")
        print (event.event_type,event.src_path)
    def on_created(self, event):
        print ("New file created")
        #print (event.event_type,event.src_path)
        filename=str(event.src_path)
        print ('before even fired'+filename)
        renameFile(filename)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()