# fire
Universal Hot reloading

### Lancement

```bash
$ python fire.py <builder> <build dest> <exec command>
```

### Variables

```python
FORMATS = [".js", ".h", ".cpp", ".css", ".scss", ".html", ".ts"]
BUILD_CMD = sys.argv[1] # "ninja"
BUILD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[2])
START_CMD = sys.argv[3] # "./crow_test"
```
