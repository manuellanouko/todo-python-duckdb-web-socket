import asyncio
import websockets


# async def hello_world():
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         # Asking the user what their name is
#         name = input("What's your name: ")
#         # Send that name to the server
#         await websocket.send(name)
#         # We will now wait for the greeting to come back
#         greeting = await websocket.recv()
#         print(greeting)

async def get_by_name():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Asking the user what their name is
        name = input("Please enter the payee name you want to search by: ")
        # Send that name to the server
        await websocket.send(name)
        # We will now wait for the greeting to come back
        payments = await websocket.recv()
        print(payments)


if __name__ == "__main__":
    asyncio.run(get_by_name())
