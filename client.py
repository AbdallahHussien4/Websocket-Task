#!/usr/bin/env python
import asyncio
import websockets



async def hello():
    async with websockets.connect("ws://localhost:8001") as websocket:
        speed = input("Enter the speed : ")
        height = input("Enter the height : ")
        while speed != str(-1) and height != str(-1):
            await websocket.send((speed,height))
            msg = await websocket.recv()
            print(msg)
            speed = input("Enter the speed : ")
            height = input("Enter the height : ")
        await websocket.send("close")
        print("client CLOSED")

asyncio.run(hello())