# CardiacSense

## Installation

### Build The Docker Image

```bash
docker build -t cardiac-sense-ci:latest --progress tty .
```

### Start The Container

* Linux

```bash
docker container run --rm -it -v $PWD:/app -p 8888:8888 -p 8050:8050 --name cardiac-sense cardiac-sense-ci:latest bash
```

* Windows (Powershell)

```bash
docker container run --rm -it -v ${pwd}:/app -p 8888:8888 -p 8050:8050 --name cardiac-sense cardiac-sense-ci:latest bash
```

### Using Docker Compose

* Start the container, named ``cardiac-sense`` using the following command, if you are building the docker image for the first time or the requirements*.txt has been updated.

```bash
docker compose up --build
```

* Otherwise, you can run it without the **--build** flag.

* Once you finished working with the container, run the following to stop the container.

```bash
docker compose down
```

* If you want to run the dashboard, use this command.
It will be running on <http://0.0.0.0:8050/>. Open the browser to access it.

```bash
docker compose run -p 8050:8050 --rm -it cardiac-sense-ci python3 app/main.py
```

* Download the dataset manually (For Development)

```bash
docker compose run -p 8050:8050 --rm -it cardiac-sense-ci python3 tools/dataset_downloader.py
```

### Contributors

- Mr.Aung Khant Maw
* Ms.Khaing Su Thway

### Resources

- Awesome-Dash - <https://github.com/ucg8j/awesome-dash?tab=readme-ov-file>
