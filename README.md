# Paylead Challenge <!-- omit in toc -->

Paylead technical challenge

## Table of contents <!-- omit in toc -->

- [Setup](#setup)
  - [Local setup with pyenv and poetry](#local-setup-with-pyenv-and-poetry)
  - [Docker setup](#docker-setup)
- [Usage](#usage)
## Setup

### Local setup with pyenv and poetry

1. Install Python 3.x using [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#installation)

<details>
    <summary>Install on Mac OS X</summary>

    ```sh
    #eg on Mac Os X
    brew update
    brew install pyenv
    pyenv install 3.6.12 # or any other ^3.6
    ```

</details>

<details>
    <summary>Install on Ubuntu Desktop</summary>

    ```bash
    git clone https://github.com/pyenv/pyenv ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc # or >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc # or >> ~/.bashrc
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc # or ~/.bash_profile
    source ~/.zshrc # or >> ~/.bashrc
    pyenv install 3.6.12 # or any other ^3.6
    ```

</details>

<details>
    <summary>Install on Windows</summary>

    Follow you prefered installation from [pyenv-win](https://github.com/pyenv-win/pyenv-win#get-pyenv-win)

    ```powershell
    pyenv install 3.6.12 # or any other ^3.6
    ```

</details>

2. Install [Poetry](https://poetry.eustace.io/) for dependency management

```sh
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
source $HOME/.poetry/env
poetry --version
```

3. Install dependencies in virtual environement

```sh
poetry config virtualenvs.in-project true # Can be set globally
poetry shell # initialize `.venv/` virtualenv directory
poetry install
```

### Docker setup

You can use the script `dev.dockerfile.build.sh` in `.devcontainer/` to build an image with all the dependencies.
Then you can use the script `dev.dockerfile.run.sh` in `.devcontainer/` the other one to run and attach to a container.

Another way can be to use the built-in feature of [remote
container](https://code.visualstudio.com/docs/remote/containers) from vscode

## Usage

if you made the installation for virtual env

```sh
poetry run uvicorn paylead_challenge.main:api --host 0.0.0.0 --port 80
```

or use the script `dev.dockerfile.run.sh`

```sh
./.devcontainer/dev.dockerfile.run.sh
```

Both should link to your localhost on port 80.
