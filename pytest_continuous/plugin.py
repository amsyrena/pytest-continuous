import signal
import time

should_stop = False


def pytest_addoption(parser):
    parser.addoption(
        "--continuous", action="store", default=False, nargs='?', const=True,
        help="Run tests continuously until failure, interruption, or optional timeout in seconds."
    )


def handle_stop_signal(signum, frame):
    global should_stop
    should_stop = True
    print("\nReceived stop signal, finishing after this test run...")


def pytest_sessionstart(session):
    if session.config.getoption("--continuous"):
        signal.signal(signal.SIGINT, handle_stop_signal)
        print("Running tests continuously. Press CTRL+C to stop...")
        global start_time
        start_time = time.time()  # Record the start time


def pytest_runtestloop(session):
    continuous = session.config.getoption("--continuous")
    if continuous:
        timeout = None
        try:
            timeout = float(continuous) if continuous is not True else None
        except ValueError:
            print("Invalid timeout value. Using continuous mode without timeout.")

        while not should_stop:
            for item in session.items:
                if timeout:
                    # Check if the current time exceeds the start time by the timeout duration
                    if time.time() - start_time > timeout:
                        print(f"Timeout reached after {timeout} seconds.")
                        return True

                nextitem = session.items[(session.items.index(item) + 1) % len(session.items)] if (session.items.index(
                    item) + 1) < len(session.items) else None
                session.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
                if session.testsfailed or should_stop:
                    return True
