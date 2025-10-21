from time import monotonic, sleep


class SimpleStopWatch:
    def __init__(self) -> None:
        self.total = 0.0
        self.start_time = None
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = monotonic()
            self.running = True

    def stop(self):
        if self.running:
            self.total += monotonic() - self.start_time
            self.start_time = None
            self.running = False

    def reset(self):
        if not self.running:
            self.total = 0.0
            self.start_time = None

    def elapsed(self) -> float:
        if not self.running:
            return self.total
        else:
            return self.total + (monotonic() - self.start_time)


timer = SimpleStopWatch()

timer.start()
sleep(1)

timer.stop()
sleep(1)

timer.start()
sleep(1)

timer.stop()

print(timer.elapsed())
