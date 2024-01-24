from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time, subprocess, sys

FORMATS = [".js", ".h", ".cpp", ".css", ".scss", ".html", ".ts"]
BUILD_CMD = sys.argv[1] # "ninja"
BUILD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[2])
START_CMD = sys.argv[3] # "./crow_test"

print("""
                                  )
                  (           (  (
                   ) (           ))
                  (            )//
                 _ )  ))       __
          ,-----' |  ((      <'__`)              ____________________
          | //  : |   )       #o)#:  ))        ,'                    `.
          | //  : | )/        \\###'      ____/   Voilà au moins une    \\ 
          | //  : |           ,###.      `-._      chose qui ne sera    | 
          `-----._|     __  #######          \\     pas récupérée par    /
           _/___\\_    //)_`//  | ||]         \\   les bureaucrates !   /
     _____[_______]_[~~-_ (.L_/  ||            `.____________________,'
    [____________________]' `\\_,/'/
      ||| /          |||  ,___,'./
      ||| \\          |||,'______|
      ||| /          /|| I==||
      ||| \\       __/_||  __||__
  -----||-/------`-._/||-o--o---o---
      """)

print("fire v0.1")
print(" ")
print("----------- Configuration ------------")
print(f"Commande de compilation : {BUILD_CMD}")
print(f"Dossier de compilation : {BUILD_DIR}")
print(f"Commande d'exécution : {START_CMD}")
print("------------------------------------- ")
print(" ")
print("Nous sommes prêts à compiler vos scandaleux fichiers.")

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.process(event)
    def on_created(self, event):
        self.process(event)
    def on_deleted(self, event):
        self.process(event)

    def process(self, event):
        if  any(event.src_path.endswith(f) for f in FORMATS):
            print("\nDes modifications ont été détectées. Compilation de l'application en cours...")
            print("Journal de compilation :")
            subprocess.run(BUILD_CMD, shell=True, cwd=BUILD_DIR)
            print("Compilation terminée avec succès.")
            print("\nExécution de l'application...")
            subprocess.run(START_CMD, shell=True, cwd=BUILD_DIR)
            print("Exécution terminée avec succès.\n")

if __name__ == '__main__':
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(
        event_handler, 
        path=".",
        recursive=True,
    )
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
