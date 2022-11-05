#!/usr/bin/env python
import asyncio

import websockets


async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message[0])
        print(message[1])


async def main():
    async with websockets.serve(handler, "localhost", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())