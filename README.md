# my-tail

Simple tail implementation in Python.

## Usage

```bash
docker build -t my-tail .
docker run --rm -v $(pwd):/app my-tail example.txt
