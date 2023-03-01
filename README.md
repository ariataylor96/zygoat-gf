# zygoat

[![ci](https://github.com/ariataylor96/zygoat-gf/actions/workflows/ci.yml/badge.svg)](https://github.com/ariataylor96/zygoat-gf/actions/workflows/ci.yml)

<img src="https://user-images.githubusercontent.com/640862/75250233-e287ea80-57a5-11ea-9d9f-553662a17706.jpeg" />

## What is zygoat?

`zygoat` is a command line tool used to bootstrap and configure a React/Django/Postgres stack web application.

Linting, test configuration, boilerplate, and development environment are automatically taken care of using `zygoat` so that you can get up and running faster.

## How does it work?

We'll find out soon!

## Installation

```bash
pip install --upgrade zygoat
```

---

## Contribution guide

`zygoat` is developed using the [Poetry](https://python-poetry.org/docs/) packaging framework for Python projects to make development as simple and portable as possible. Install the `development` extras group to gain access to some package scripts that make development easier. This is done like so:

```bash
poetry install --all-extras
```

Then, you can run `poetry run [cmd]`, where `cmd` is one of:

- _watch_ - Runs the test suite on save
- _docs_ - Generates [`pdoc`](https://pdoc.dev/) API documentation and serves it on `localhost:8080`

---

## Documentation

[Available on ReadTheDocs](https://zygoat.readthedocs.io/en/latest/)
