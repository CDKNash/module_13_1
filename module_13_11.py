import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(5)
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(3)
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    print("Старт")
    task1 = asyncio.create_task(start_strongman(name='Apollon', power=5))
    await asyncio.sleep(1)
    task2 = asyncio.create_task(start_strongman(name='Denis', power=4))
    await asyncio.sleep(4)
    task3 = asyncio.create_task(start_strongman(name='Pasha', power=3))
    await asyncio.sleep(5)
    await task1
    await task2
    await task3
    print("Финиш")


start = time.time()
asyncio.run(start_tournament())
finish = time.time()