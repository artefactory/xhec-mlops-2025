# Prerequisites and Setup

## Table of Contents

- [How to debug](#how-to-debug)
- [Terminals](#terminals)
  - [Linux and MacOS](#linux-and-macos)
  - [Windows](#windows)
- [Python Installation](#python-installation)
  - [MacOS](#macos)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [Windows (WSL)](#windows-wsl)
- [Docker Desktop](#docker-desktop)
  - [Download and Install Docker Desktop](#download-and-install-docker-desktop)
  - [Check your Installation - Docker Desktop](#check-your-installation---docker-desktop)
- [Git](#git)
  - [Download & Install](#download--install)
  - [Configure Git](#configure-git)
  - [Check your Installation - Git](#check-your-installation---git)
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

## Terminals

<details>
  <summary><b>Linux and MacOS</b></summary>

Use your native terminal application:
- **Linux**: Open the Terminal application (usually found in your applications menu or by pressing `Ctrl+Alt+T`)
- **MacOS**: Open Terminal.app (found in Applications > Utilities or search for it using Spotlight)

</details>

<details>
  <summary><b>Windows</b></summary>

For those of you working on Windows, we recommend using Windows Subsystem for Linux (WSL), which enables Unix-like commands.

1. **Open PowerShell** as Administrator
2. **Install WSL** (if not already installed):
   ```bash
   wsl --install
   ```
3. **Update WSL** (if already installed):
   ```bash
   wsl --update
   ```
4. **Run and exit WSL**: You can simply run `wsl` from any directory to enter WSL mode within that directory. You can exit WSL mode by hitting Ctrl+D.

> [!Note]
> After installation, you should use the WSL terminal for all commands in this course.
> If you encounter issues with the WSL installation, you can continue by using the [Git Bash terminal](https://git-scm.com/downloads/win)

</details>

## Python Installation

This course requires **Python 3.11**. Follow the instructions for your operating system:

<details>
  <summary><b>MacOS</b></summary>

The recommended way to install Python 3.11 on macOS is using **Homebrew**.

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.11**:
   ```bash
   brew install python@3.11
   ```

3. **Verify the installation**:
   ```bash
   python3.11 --version
   ```

> [!Note]
> Do not use the system Python that comes with macOS, as it's intended for Apple development utilities.

</details>

<details>
  <summary><b>Linux</b></summary>
  If you’re a real Linux user, you probably already have Python 3.11 installed, or you’re about to compile it from source just for fun. Either way, you’ve got this.
</details>

<details>
  <summary><b>Windows</b></summary>

On WSL or on Git Bash, run follow the following instructions :

1. **Open terminal with WSL** and run:
   ```bash
   sudo apt update
   sudo apt install python3.11
   ```

2. **Verify the installation**:
   ```bash
   python3.11 --version
   ```

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

### Check your Installation - Docker Desktop

Once docker is installed, make sure that it is running correctly by running:

```bash
docker run -p 80:80 docker/getting-started
```

If you check the Docker App, you should see a 'getting started' container running. Once you've checked that this works correctly, remove the container via the UI.

<details>
    <summary><b>Optional</b></summary>
    You can also perform these operations directly from the command line, by running <code>docker ps</code> to check the running containers, <code>docker stop [CONTAINER-ID]</code> to stop it and <code>docker rm -f [CONTAINER-ID]</code> to remove it.
</details>


## Git


Git is a distributed version control system that allows multiple people to work on a project at the same time without overwriting each other's changes.
It's essential for any collaborative coding project.

### Download & Install

To install Git, follow the instructions on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Choose the instructions that match your operating system.

After installation, you can verify that Git is correctly installed by opening a terminal and typing:

```bash
git --version
```

This should return the version of Git that you installed.

### Configure Git

After installing Git, you need to configure it with your name and email address.
This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@foo.bar"
```

You can find full configuration instruction on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

### Check your Installation - Git

Open a terminal, you should be able to run the following commands:

```bash
git --version
```

Complete/check your setup with the following command (Type `:q` to exit):

```bash
git config --global --list
user.name=johndoe
user.email=johndoe@foo.bar
```

Try to reach pandas GitHub repo to check your connection to GitHub:

```bash
git ls-remote --get-url https://github.com/pandas-dev/pandas.git
https://github.com/pandas-dev/pandas.git
```

## Install requirements

> [!Warning]
> You will not have access to the course content before the course starts.
> So here is a sample requirements setup you should try before the course begins.

> [!Important]
> **About the `python` command:**
> The command to invoke Python depends on your installation method:
> - **MacOS (Homebrew)**: Use `python3.11` (or `python3` if you've configured aliases)
> - **Linux/WSL**: Use `python3.11` (or `python3` if available)
> - The examples below use `python` for simplicity, but **you may need to replace it with `python3` or `python3.11`** based on your system.
>
> To check which Python version a command uses, run: `python --version` or `python3 --version` or `python3.11 --version`

Follow these steps to set up your Python environment and install the required packages using `uv`.


1.  **Install `uv` globally (if not already present):**
    We recommend installing `uv` using `pipx` for a clean global installation, as done in our CI pipeline.
    ```bash
    python -m pip install --upgrade pip
    python -m pip install pipx && pipx ensurepath
    pipx install uv
    ```

2.  **Initialize Project Configuration:**
    Create an empty directory named `prerequisites` and initialize the configuration files using `uv init` inside it. This creates `pyproject.toml` and other necessary files.
    ```bash
    uv init
    ```

3.  **Add FastAPI Dependency:**
    Add the core web framework dependency using `uv add`. This updates both `pyproject.toml` and `uv.lock`.
    ```bash
    uv add fastapi
    ```

4.  **Install Dependencies:**
    Synchronize the virtual environment to install all dependencies listed in the newly created/updated files.
    ```bash
    uv sync
    ```

5.  **Activate the Virtual Environment:**
    ```bash
    source .venv/bin/activate
    ```

6.  **Verify your installation:**
    Check that all packages are installed correctly (you should see `fastapi` in the list):
    ```bash
    uv pip list
    ```
    Then, open a Python shell to verify imports:
    ```bash
    uv run python
    >>> import fastapi
    >>> fastapi.__version__ # Should be something like '0.118.0'
    >>> exit()
    ```

If you see the correct version and no errors, your environment is ready!

Thank you ✨ !
