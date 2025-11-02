import asyncio


def example(name):
    print("hi", name)
    1/0
    print("bye")


def loops():
    for i in range(3):
        print("loop", i, "start")
        if i == 1:
            1/0
        print("loop", i, "end")
    print("after loop")


def tricky():
    print("before return")
    return 1/0
    print("after return")


async def aex():
    print("astart")
    1/0
    await asyncio.sleep(0.01)
    print("aend")


class C:
    def m(self):
        print("C.m before")
        x = 1/0
        print("C.m after")
