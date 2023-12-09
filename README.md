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

### Using Docker Compose
Start the container, named ``cardiac-sense`` using the following command, if you are building the docker image for the first time or the requirements*.txt has been updated.
```bash
docker compose up --build
```
Otherwise, you can run it without the **--build** flag.

Once you finished working with the container, run the following to stop the container.
```bash
docker compose down
```

### Contributors
- Mr.Aung Khant Maw
- Ms.Khaing Su Thway