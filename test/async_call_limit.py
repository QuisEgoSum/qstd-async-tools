import asyncio

from qstd_async_tools import call_limit


counter = 0
current_execute_counter = 0


@call_limit(2)
async def test_function():
    global counter, current_execute_counter
    counter += 1
    print('Start', counter)
    current_execute_counter += 1
    assert current_execute_counter <= 2
    await asyncio.sleep(0.3)
    current_execute_counter -= 1
    assert current_execute_counter <= 2
    print('End', counter)


async def main():
    global current_execute_counter

    coro_list = []

    for i in range(10):
        coro_list.append(test_function())

    assert current_execute_counter == 0

    await asyncio.gather(*coro_list)

    assert current_execute_counter == 0


if __name__ == '__main__':
    asyncio.run(main())

