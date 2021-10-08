import cProfile, pstats, io
import threading


def print_to_file(message: str, filename: str = "profile.txt"):

    with open(filename, 'a') as f_file:
        f_file.write(message)


def profile(func):
    """
    A decorator that uses cProfile to profile a function
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(f'{func.__qualname__}.txt')
        thread1 = threading.Thread(target=print_to_file, args=[s.getvalue(), f'{func.__qualname__}.txt'])
        thread1.start()
        #print(s.getvalue())
        return retval

    return inner
