# CardiacSense

## Installation

### Build The Docker Image
```bash
docker build -t cardiac-sense-ci:latest --progress tty .
```

### Start The Container

* Linux
```bash
docker container run --rm -it -v $PWD:/app -p 8888:8888 --name cardiac-sense cardiac-sense-ci:latest
```
* Windows (Powershell)
```bash
docker container run --rm -it -v ${pwd}:/app -p 8888:8888 --name cardiac-sense cardiac-sense-ci:latest
```
### Access Jupyter Notebook
Open the browser and enter http://127.0.0.1:8888/tree.

Run ```jupyter notebook``` in the bash shell inside the container.
Then, open the browser and enter http://127.0.0.1:8888/tree.

### Using Docker Compose
You can do all the above operations with just one line using **docker-compose**.
```bash
docker compose up
```
```bash
docker compose down
```

### Authors
- Mr.Aung Khant Maw
- Ms.Khaing Su Thway