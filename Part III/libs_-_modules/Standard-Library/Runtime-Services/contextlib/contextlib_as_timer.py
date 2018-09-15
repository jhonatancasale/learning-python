from time import perf_counter
from array import array
from contextlib import contextmanager


@contextmanager
def timming(label: str):
    t0 = perf_counter()
    try:
        yield lambda: (label, t1 - t0)
    finally:
        t1 = perf_counter()


with timming('Array tests') as total:
    with timming('Array creation innermul') as inner:
        x = array('d', [0] * 1_000_000)


    with timming('Array creation outermul') as outer:
        x = array('d', [0]) * 1_000_000

print('Total [%s]: %.6f s' % total())
print(' Timing [%s]: %.6f s' % inner())
print(' Timing [%s]: %.6f s' % outer())
