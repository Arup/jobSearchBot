import time
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog import events
from fileRename import renameFile

class MyHandler(PatternMatchingEventHandler):
    _patterns = ["*.html"]
    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
    # the file will be processed there
        
        filename=str(events.FileCreatedEvent.src_path)
        print ('before even fired'+filename)
        renameFile(filename)
    # print now only for degug
    #def on_modified(self, event):
        #self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()