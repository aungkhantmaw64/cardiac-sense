# CardiacSense

## Getting Started

### Build The Docker Image
Run this command when you are building the app for the first time or everytime you update the dependencies (requirements.txt, etc).
```bash
docker build -t cardiac-sense-ci:latest --progress tty .
```

## Running The Container (For Development)

Start a container with the following command, which allows the user to enter linux shell terminal by mounting the project directory to the */app* directory of the container. In addition, this command publishes the container ports: 8888 (Jupyter Server) and 8050 (Dash Server) to the host's ports 8888 and 8050, respectively.
* Linux

```bash
docker container run --rm -it -v $PWD:/app -p 8888:8888 -p 8050:8050 --name cardiac-sense cardiac-sense-ci:latest bash
```

For developers who love to use VSCode IDE, you can refer to the [Developing Inside The Container](https://code.visualstudio.com/docs/devcontainers/containers) section from the documentation. After running this command, you can keep the container running by not killing the terminal and then, attach to the running container from the VSCode.
* Windows (Powershell)

```bash
docker container run --rm -it -v ${pwd}:/app -p 8888:8888 -p 8050:8050 --name cardiac-sense cardiac-sense-ci:latest bash
```

### Formatting The Code
To format the code according to PEP8 standard, you can use the following command. This code formatting command doesn't work on Jupyter notebooks. We'll have to find out how to do this for the notebooks as well in the future.
```bash
autopep8 --aggressive --aggressive --in-place app/*.py app/models/*.py app/views/*.py -v
```

### Running Jupyter Notebook
By running this command inside the container, you can access the jupyter notebook at localhost's port 8888.
```bash
jupyter notebook --allow-root --ip 0.0.0.0 --port 8888
```

### Downloading the dataset manually

```bash
docker compose run -p 8050:8050 --rm -it cardiac-sense-ci python3 tools/dataset_downloader.py
```

### Running the Dashboard Web App

```bash
python3 app/main.py
```

## Using Docker Compose (For Production)

* Start the container, named ``cardiac-sense`` using the following command, if you are building the docker image for the first time or the requirements*.txt has been updated.

```bash
docker compose up --build
```

* Otherwise, you can run it without the **--build** flag.

* Once you finished working with the container, run the following to stop the container.

```bash
docker compose down
```

### Local Host Port Addresses
**Linux**
- [Dash App](https://0.0.0.0:8050)
- [Jupyter Notebook](https://0.0.0.0:8888)

**Windows**
- [Dash App](https://127.0.0.1:8050)
- [Jupyter Notebook](https://127.0.0.1:8888)

# Contributors

- Mr. Aung Khant Maw

- Ms. Khaing Su Thway

# Resources

* Awesome-Dash - <https://github.com/ucg8j/awesome-dash?tab=readme-ov-file>
