import asyncio
import websockets
from payments_model import get_by_name, initialise_db

# # an API function?
# async def hello_world(websocket):
#     # When the function runs, it will expect a name from a client
#     name = await websocket.recv()
#     print(f"Server received: {name}")
#     greeting = f"Hello {name}"
#     # Send the response to the client
#     await websocket.send(greeting)
#     print(f"Server sent back: {greeting}")



async def search_payment_by_name(websocket):
    name = await websocket.recv()
    print(f"Server received: {name}")
    get_by_name(name)
    await websocket.send("list printed successfully")

async def serve():
    # port 8765 is the standard port for web sockets
    async with websockets.serve(search_payment_by_name, "localhost", 8765):
        await asyncio.Future() # This means run forever

if __name__ == "__main__":
    initialise_db()
    asyncio.run(serve())
