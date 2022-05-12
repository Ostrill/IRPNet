import time


class Timer:

    """The class needed to time the execution of some calculations"""

    def __init__(self):
        """Initializes a variable for timing"""
        self.last_time = 0

    def __calc_time(self, seconds):
        """Transform seconds to a readable string format"""
        secs, mins, hours = seconds, 0, 0
        if secs >= 60:
            mins = int(secs // 60)
            secs = secs % 60
        if mins >= 60:
            hours = int(mins // 60)
            mins = mins % 60
        return f'{hours:02}:{mins:02}:{round(secs, 3)}'

    def start(self):
        """Starts the timer"""
        self.last_time = time.time()

    def stop(self):
        """Prints the time elapsed since the start() was called"""
        elapsed_time = self.__calc_time(time.time() - self.last_time)
        print(f'Завершено за {elapsed_time}')

    def elapsed(self):
        """Returns (without printing) the time elapsed since the start() was called"""
        elapsed_time = self.__calc_time(time.time() - self.last_time)
        return elapsed_time

    def split(self):
        """Equivalent to sequential call of stop() and start()"""
        self.stop()
        self.start()


def progress_bar(value, total, size=20):
    """Returns the progress bar like [====>.....] 50%

    Arguments:
    value -- value of progress
    total -- total value of progress (which equals 100%)
    size -- length of the progreess bar (default 20)

    """
    l, f, a, e, r = '[=>.]'
    progress = round(value / total * size)
    arrow = f'{a}{f}'[value == total] if progress > 0 else ''
    bar = f"{l}{f * (progress - 1)}{arrow}{e * (size - progress)}{r}"
    percent = f'{round(value / total * 100)}%'
    return f'{bar} {percent:<4}'