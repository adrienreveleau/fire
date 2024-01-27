![fire](https://github.com/adrienreveleau/fire/assets/131309787/7a8fef99-b3d3-43da-8edf-cc34a8359035)

Universal Hot reloading

#### Installation
```bash
$ git clone https://github.com/adrienreveleau/fire.git
```
#### Requirements
```bash
Python 3.11.4

$ pip install watchdog  
```
#### Lancement

```bash
$ python fire.py <pre-build cmd> <builder> <build dest> <exec cmd> 
```
*Pour que votre fichier puisse être exécutable par **fire** il vous faudra exécuter la commande suivante :*
```bash
$ chmod +x chemin/vers/votre/fichier.sh
```
#### Variables

```python
CONFIG = {"logger": False, "logLVL": 0} # ex. --LOGGER=False --LOGLVL=0
FORMATS = [".js", ".h", ".cpp", ".css", ".scss", ".html", ".ts"]
BUILD_CMD = sys.argv[2] # ex. "ninja"
BUILD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[3]) # ex. ../build
START_CMD = f"{BUILD_DIR}/{sys.argv[4]}" # ex. htmlc 
PREBUILD_CMD = sys.argv[1] # ex. ../pre_build.sh
```
