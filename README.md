# CardiacSense

## Installation
### Build The Docker Image
```bash
docker build -t cardiac-sense-ci:latest --progress tty .
```

### Start The Container

```bash
docker container run --rm -it -v $PWD:/app -p 8888:8888 cardiac-sense-ci:latest
```

### Access Jupyter Notebook
Open the browser and enter http://127.0.0.1:8888/tree.