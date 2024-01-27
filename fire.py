from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time, subprocess, sys, shlex

CONFIG = {"logger": False, "logLVL": 0} # ex. --LOGGER=False --LOGLVL=0
FORMATS = [".js", ".h", ".cpp", ".css", ".scss", ".html", ".ts"]
BUILD_CMD = sys.argv[2] # ex. "ninja"
BUILD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[3]) # ex. ../build
START_CMD = f"{BUILD_DIR}/{sys.argv[4]}" # ex. htmlc 
PREBUILD_CMD = sys.argv[1] # ex. ../pre_build.sh

print("""
                                      
                          00                               
                          000                              
                          0000                             
                      00  00000                            
                      000000 000   0                       
                      000000 0000  00                      
                      00000  0000 0000                     
                 0   000000  0000000000                    
                 00  000000000000000000                    
                 0000000000000000000000  00                
                 0000000000000 0000000000000               
                 0000000000000   00000000000               
              0000000000000000   00000000000               
              0000000000000000    00 000000                
              0000000 0000 000    0  000000                
              0000000 000   00       000000 0              
              00000 0  000             0  000              
               0000     00            00 0000              
               00000                 00 0000               
                00000               0000000                
                  0000            0000000                  
                     000                                   
                                                           
                 0000000000000000000000000                 
                 0000000000000000000000000 
                                                           
      """)

print("fire v0.1")
print(" ")
print("---------------- Configuration -----------------")
print(f"Commande de Pré-build   :   {PREBUILD_CMD}")
print(f"Commande de Build       :   {BUILD_CMD}")
print(f"Dossier de Compilation  :   {BUILD_DIR}")
print(f"Commande d'exécution    :   {START_CMD}")
print(f"logs                    :   {CONFIG['logger']}")
print(f"Niveau de logs          :   {CONFIG['logLVL']}")
print("-----------------------------------------------")
print(" ")
print("Nous sommes prêts à compiler vos scandaleux fichiers.")
print(" ")

def formatCMD(c):
    return shlex.split(c)

def letdrain(f):
    if not os.listdir(BUILD_DIR):
        logger("Dossier de build vierge.", 1)
        return False
    else:
        logger("Preparation du dossier de build...", 1)
        for file in os.listdir(f):
            path = os.path.join(f, file)
            if os.path.isfile(path):
                os.remove(path)
    print("Votre dossier est prét !", 1)
    return True

def letexec():
    print("\nExécution de l'application...")
    subprocess.run(START_CMD, shell=True, cwd=BUILD_DIR)
    print("Exécuté avec succès.\n")

def letcompile():
    logger("Journal de Pré-build :", 1)
    subprocess.run(PREBUILD_CMD, shell=True, cwd=BUILD_DIR)
    print("Pré-build terminée avec succès.")

def letbuild():
    logger("Journal de build :", 1)
    subprocess.run(BUILD_CMD, shell=True, cwd=BUILD_DIR)
    print("Build terminé avec succès.")

def logger(l, lvl):
    if CONFIG['logger'] and CONFIG['logLVL'] == lvl:
        print(l)
    else:
        return

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.process(event)
    def on_created(self, event):
        self.process(event)
    def on_deleted(self, event):
        self.process(event)
    def process(self, event):
        logger(" ", 2) 
        logger(f"Format ok ?        :   {any(event.src_path.endswith(f) for f in FORMATS)}", 2)
        logger(f"Src                :   {event.src_path}", 2)
        logger(f"Build dir          :   {os.path.abspath(BUILD_DIR)}", 2)
        logger(f"Fichier build ?    :   {event.src_path.startswith(os.path.abspath(BUILD_DIR))}", 2)
        if event.src_path.startswith(os.path.abspath(BUILD_DIR)):
            return
        if  any(event.src_path.endswith(f) for f in FORMATS):
            time.sleep(5)
            letdrain(BUILD_DIR)
            letcompile()
            letbuild()
            letexec()
            return

if __name__ == '__main__':
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(
        event_handler, 
        path=".",
        recursive=True,
    )

    letdrain(BUILD_DIR)
    letcompile()
    letbuild()
    letexec()
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
