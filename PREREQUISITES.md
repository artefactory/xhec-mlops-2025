# Prerequisites and Setup

## Table of Contents

- [How to debug](#how-to-debug)
- [Docker Desktop](#docker-desktop)
  - [Download and Install Docker Desktop](#download-and-install-docker-desktop)
    - [✅ Check your Installation - Docker Desktop](#✅-check-your-installation---docker-desktop)
    - [Pull a Docker Image](#pull-a-docker-image)
    - [✅ Check your Installation - Docker Pull](#✅-check-your-installation---docker-pull)
  - [Git](#git)
    - [Download & Install](#download--install)
    - [Configure Git](#configure-git)
    - [✅ Check your Installation - Git](#✅-check-your-installation---git)
- [Install requirements](#install-requirements)

> [!Important]
> The course is dense.
>
> You won't have time to install and configure everything on D-day.
>
> You won't be able to follow the course if you don't have everything installed and working.
>
> 📣 **Please make sure you have everything installed and working before the course starts.** 📣
>
> You know your school WiFi better than we do, don't gamble on it.

> [!Important]
> We will be using Docker for this course, which can use up a lot of your disk.
> Make sure to have at least 10Gb available in your disk before starting this course. Otherwise you risk running into some obscure errors.

> [!Note]
> Each section has a **Check your Installation** section.
> Please make sure you can run the commands in that section before moving on to the next section.

## How to debug

1. Check and try to understand your error message
2. ChatGPT it / Google it / StackOverflow it
3. If you can't find a solution, ask your friends
4. If your friends can't help you, ask us on Slack

<details>
  <summary>📚 Table of Contents</summary>

- [Docker Desktop](#docker-desktop)
  - [Download and Install Docker Desktop](#download-and-install-docker-desktop)
  - [✅ Check your Installation](#✅-check-your-installation---docker-desktop)
  - [Pull a Docker Image](#pull-a-docker-image)
  - [✅ Check your Installation](#✅-check-your-installation---docker-pull)
- [Git](#git)
  - [Install Git](#install-git)
    - [Download & Install](#download-&-install)
    - [Configure Git](#configure-git)
  - [✅ Check your Installation](#✅-check-your-installation---git)
- [Install requirements](#install-requirements)
  - [Create and install requirements](#create-and-install-requirements)
  - [✅ Check your Installation](#✅-check-your-installation---requirements)

</details>

## Docker Desktop

Docker Desktop is a tool for MacOS and Windows machines for the building and sharing of containerized applications and microservices. It includes Docker Engine, Docker CLI client, Docker Compose, Notary, Kubernetes, and Credential Helper. It also features an intuitive user interface that makes managing your Docker images and containers locally much easier.

### Download and Install Docker Desktop

> [!Warning]
> 📣 **This step is the most time consuming one. You will not be able to perform it at HEC.** 📣

If you do not have `Docker Desktop` installed, you will need to install it. You can follow the official instructions:

- [Install Docker - Mac OS](https://docs.docker.com/desktop/install/mac-install/)
- [Install Docker - Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Install Docker - Windows](https://docs.docker.com/desktop/install/windows-install/)

For those of you working on Windows, you might need to update Windows Subsystem for Linux. To do so, simply open PowerShell and run:

```bash
wsl --update
```

### ✅ Check your Installation - Docker Desktop

Once docker is installed, make sure that it is running correctly by running:

```bash
$ docker run -p 80:80 docker/getting-started
```

If you check the Docker App, you should see a 'getting started' container running. Once you've checked that this works correctly, remove the container via the UI.

<details>
    <summary><b>Optional</b></summary>
    You can also perform these operations directly from the command line, by running <code>docker ps</code> to check the running containers, <code>docker stop [CONTAINER-ID]</code> to stop it and <code>docker rm -f [CONTAINER-ID]</code> to remove it.
</details>

### Pull a Docker Image

During session 2 of this course, you will need to build a Docker image yourself. To speed up the building process, you can pre-build your image.

Place your terminal at the root of the project and run:

```bash
$ docker build -t "nyc-taxi:prerun" -f "lessons/02-model-deployment/Dockerfile.app" ./lessons/02-model-deployment
```

### ✅ Check your Installation - Docker Pull

You should be able to see your image in the Docker Desktop UI:

![Docker Image](./images/example_image.png)

You can also check that it worked that by running:

```bash
$ docker images
REPOSITORY   TAG        IMAGE ID       CREATED         SIZE
nyc-taxi     prerun     1878dadc8ab5   6 minutes ago   118MB
```

<details>
    <summary><b>Optional</b></summary>
    Once you've checked that this works correctly, remove the image by running in your terminal: <code>docker rmi [IMAGE ID]</code>
</details>

## Git


Git is a distributed version control system that allows multiple people to work on a project at the same time without overwriting each other's changes.
It's essential for any collaborative coding project.

### Download & Install

To install Git, follow the instructions on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Choose the instructions that match your operating system.

After installation, you can verify that Git is correctly installed by opening a terminal and typing:

```bash
$ git --version
```

This should return the version of Git that you installed.

### Configure Git

After installing Git, you need to configure it with your name and email address.
This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "you email@foo.bar"
```

You can find full configuration instruction on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

<details>
  <summary>Windows only: <code>git bash</code></summary>

If you are using Windows, you can use PowerShell as your terminal.
But Powershell is limited and doesn't support all the commands we will use in this course.
You will need to install [`git bash`](https://gitforwindows.org/) to have access to all the commands we will use in this course.

Please carefully follow [instructions here](https://github.com/git-for-windows/git/releases/tag/v2.42.0.windows.2).

> [!Note]
> You can also use WSL terminal, but it's a bit more complicated to use.

</details>

### ✅ Check your Installation - Git

Open a terminal, you should be able to run the following commands:

```bash
$ git --version

```

Complete/check your setup with the following command (Type `:q` to exit):

```bash
$ git config --global --list
user.name=johndoe
user.email=johndoe@foo.bar
```

Try to reach pandas GitHub repo to check your connection to GitHub:

```bash
$ git ls-remote --get-url https://github.com/pandas-dev/pandas.git
https://github.com/pandas-dev/pandas.git
```

<<<<<<< HEAD
## Package management

#### Create and install requirements
=======


## Install requirements
>>>>>>> 622a97e (fix: update prerequisites and course timeline in README and PREREQUISITES)

> [!Warning]
> You will not have access to the course content before the course starts.
> So here is a sample requirements setup you should try before the course begins.

<<<<<<< HEAD
Be sure to have Python already installed.

1. Install pip
Check the [documentation](https://pip.pypa.io/en/stable/installation/) and run the following command to install.

```bash
python -m ensurepip --upgrade
```

2. Install uv
Check the [official documentation](https://docs.astral.sh/uv/pip/environments/).
=======
Follow these steps to set up your Python environment and install the required packages:
>>>>>>> 622a97e (fix: update prerequisites and course timeline in README and PREREQUISITES)

1. **Install `uv`** (a fast Python package manager):

<<<<<<< HEAD
3. Sync a virtual environment with the defined requirements in `pyproject.toml` file, and activate the environment.

```bash
uv sync
source .venv/bin/activate
```
=======
  ```bash
  pip install uv
  ```
2. **Create a sample `pyproject.toml` file** in your working directory with the following content:

  ```toml
  [project]
  name = "xhec-mlops-2025-sample"
  version = "0.1.0"
  description = "Sample project for MLOps course prerequisites."
  authors = [
      { name = "Your Name", email = "your.email@example.com" }
  ]
  requires-python = ">=3.11"
  dependencies = [
      "fastapi==0.88.0"
  ]
  ```
>>>>>>> 622a97e (fix: update prerequisites and course timeline in README and PREREQUISITES)

3. **Install all dependencies** listed in the `pyproject.toml` file. This will create a virtual environment (if needed) and install everything:

<<<<<<< HEAD
4. Check your requirements can be found in your virtual env by running:
=======
  ```bash
  uv sync
  ```
>>>>>>> 622a97e (fix: update prerequisites and course timeline in README and PREREQUISITES)

4. **Verify your installation:**
  - List installed packages to check that everything is present (for example, `fastapi`):

<<<<<<< HEAD
5. Check you can access them from python
=======
    ```bash
    uv pip list
    ```
    You should see something like:
    ```
    fastapi==0.88.0
    ...
    ```
>>>>>>> 622a97e (fix: update prerequisites and course timeline in README and PREREQUISITES)

  - Open a Python shell and check you can import the packages:

    ```bash
    uv run python
    >>> import fastapi
    >>> fastapi.__version__
    '0.88.0'
    ```

If you see the correct version and no errors, your environment is ready!

Thank you ✨ !
