![fire](https://github.com/adrienreveleau/fire/assets/131309787/7a8fef99-b3d3-43da-8edf-cc34a8359035)

Universal Hot reloading

#### Requirements
```bash
Python 3.11.4

$ pip install watchdog   
```

#### Lancement
```bash
$ git clone https://github.com/adrienreveleau/fire.git
```
```bash
$ python fire.py <builder> <build dest> <exec command> 
```

#### Variables

```python
FORMATS = [".js", ".h", ".cpp", ".css", ".scss", ".html", ".ts"]
BUILD_CMD = sys.argv[1] # "ninja"
BUILD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[2])
START_CMD = f"{BUILD_DIR}/{sys.argv[3]}" 
```
