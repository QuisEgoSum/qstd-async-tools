import asyncio

from qstd_async_tools import trace, gather


async def gather_executor():
    assert len(trace.get_trace_ids()) == 2


async def main():
    assert len(trace.get_trace_ids()) == 0

    trace.add_trace_id()

    assert len(trace.get_trace_ids()) == 1

    await gather(gather_executor(), gather_executor())

    assert len(trace.get_trace_ids()) == 1

    with trace.trace_id() as trace_id:
        assert len(trace.get_trace_ids()) == 2
        assert trace_id in trace.get_trace_ids()

    assert len(trace.get_trace_ids()) == 1


if __name__ == '__main__':
    asyncio.run(main())

    assert len(trace.TASK_ADDRESS_TO_TRACE_IDS.keys()) == 0
