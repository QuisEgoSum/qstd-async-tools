import asyncio

from qstd_async_tools import call_limit_time


counter = 0
current_execute_counter = 0


async def base_test_function():
    global counter, current_execute_counter
    counter += 1
    print('Start', counter)
    current_execute_counter += 1
    assert current_execute_counter <= 2
    await asyncio.sleep(0.3)
    current_execute_counter -= 1
    assert current_execute_counter <= 2
    print('End', counter)


@call_limit_time(2, 1)
async def test_function():
    await base_test_function()


@call_limit_time(2, 1, 3)
async def test_function2():
    await base_test_function()


async def time_range_checker():
    global counter, current_execute_counter

    await asyncio.sleep(0.01)

    await asyncio.sleep(0.3)
    assert current_execute_counter == 0
    assert counter == 2

    await asyncio.sleep(0.7)

    assert current_execute_counter == 2
    assert counter == 4

    await asyncio.sleep(0.3)
    assert current_execute_counter == 0
    assert counter == 4

    await asyncio.sleep(0.7)
    assert current_execute_counter == 2
    assert counter == 6

    await asyncio.sleep(0.3)
    assert current_execute_counter == 0
    assert counter == 6


async def time_range_checker2():
    global counter, current_execute_counter

    await asyncio.sleep(0.01)

    await asyncio.sleep(0.25)

    assert current_execute_counter == 2
    assert counter == 2

    await asyncio.sleep(0.15)

    assert current_execute_counter == 1
    assert counter == 3

    await asyncio.sleep(0.3)

    assert current_execute_counter == 0
    assert counter == 3

    await asyncio.sleep(0.3)

    # End 1 second

    await asyncio.sleep(0.25)

    assert current_execute_counter == 2
    assert counter == 5

    await asyncio.sleep(0.15)

    assert current_execute_counter == 1
    assert counter == 6

    await asyncio.sleep(0.30)

    assert current_execute_counter == 0
    assert counter == 6

    await asyncio.sleep(0.3)

    # End 2 second

    await asyncio.sleep(0.25)

    assert current_execute_counter == 2
    assert counter == 8

    await asyncio.sleep(0.15)

    assert current_execute_counter == 1
    assert counter == 9

    await asyncio.sleep(0.30)

    assert current_execute_counter == 0
    assert counter == 9

    # End 2.7 second


async def main():
    global current_execute_counter, counter

    coro_list = []

    for i in range(6):
        coro_list.append(test_function())

    await asyncio.gather(*coro_list, time_range_checker())

    # ------------------------------------------------------------------------------------------------------------------

    counter = 0

    coro_list = []

    for i in range(9):
        coro_list.append(test_function2())

    await asyncio.gather(*coro_list, time_range_checker2())


if __name__ == '__main__':
    asyncio.run(main())
