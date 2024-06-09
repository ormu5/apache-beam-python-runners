# About

This repo demonstrates different Apache Beam runners with Python application code; emphasis: PortableRunner with Spark.

See `main.py` for supported runners and code related to each.

# Getting Started Locally

## Dependencies

* Docker
* Python 3.9

## Setup

* Install Python 3.9 (preferably via virtual environment)
* Install deps: `pip install -r requirements.txt`
* Activate env (e.g., `source venv/bin/activate`)

## Supporting Services

From `./dev-utils`: `docker-compose up`

## Run the Pipeline

```sh
# You can run the script file directly.
python main.py

# To run passing command line arguments.
python main.py --input-text="someMultiPart camelCased Words"

# To run the tests.
python -m unittest -v
```

## Observe

Spark executioners: http://localhost:8081/

Spark jobs: http://localhost:4040/jobs/ (this endpoint is hosted by the Beam Job server and is only available while jobs are running)

App log output: stdout of worker nodes

# Good to Know

* The Beam job server and SDK harness (workers) must share a file volume for staging.
* There is never direct communication between the job serve and SDK harness. Comms go: Beam job server -> Spark master -> Spark workers -> Beam SDK harness (workers).
* Artifact endpoint only communicates which artifacts are needed. Processes then look to above referenced volume for retrieving those artifacts.

# License

This software is distributed under the terms of both the MIT license and the
Apache License (Version 2.0).

See [LICENSE](LICENSE) for details.

# Attribution and Contributing

Beam application logic in this repo is based on https://github.com/apache/beam-starter-python.

Feel free to open a PR against this repo.

# Known Issues

* https://github.com/apache/beam/issues/29683