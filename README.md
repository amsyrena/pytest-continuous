# Pytest Continuous Plugin

This pytest plugin allows running tests continuously until they fail, the process is manually interrupted, or a specified timeout is reached. This feature is useful for detecting flaky tests and ensuring stability over multiple iterations.

## Features

- **Continuous Testing**: Run your tests in a continuous loop.
- **Flexible Control**: Stop testing automatically on failure, manual interruption, or after a defined timeout.
- **Signal Handling**: Gracefully handles interruption signals (e.g., CTRL+C) to stop the test run.

## Installation

Install `pytest-continuous` using pip:

```bash
pip install pytest-continuous
```

## Usage

To use the plugin, you can specify the --continuous option when running pytest. This option can be used alone to run tests indefinitely, or it can be followed by an equals sign and a timeout value in seconds to limit the test duration.

Command Line Options
- **--continuous**: Run tests in a continuous loop without a timeout.
- **--continuous=<timeout>**: Run tests continuously for a specified number of seconds before stopping.


## Example

1. Run without a timeout:
```bash
pytest --continuous
```
This command runs your tests continuously until you interrupt manually or a test fails.

2. Run with a timeout:
```bash
pytest --continuous=300
```
This command runs your tests continuously for up to 300 seconds. If no test fails within this period, the testing will stop automatically.
