import asyncio
from xml.dom.minidom import ProcessingInstruction


async def fetch_data():
    return "data"

async def waiting():
    # await is used inside async function to pause execution until something finishes
    # Note/Rule:- I can be used only inside async function
    await fetch_data()


# simple example
async def task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task finished")

# asyncio.run(task())

# Concurrent async tasks
async def task1(name, delay):
    print(f"Task Started by {name}")
    await asyncio.sleep(delay)
    print(f"Task finished by {name}")


async def main():
    await asyncio.gather(
        task1("A",4),
        task1(name="B",delay=3),
        task1(name="C",delay=7),
        task1(name="D",delay=5),
    )

# asyncio.run(main())


