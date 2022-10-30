import imgui as im
import socketio

from core.src_core.PipeData import PipeData

session = PipeData()

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected!")

@sio.on("message")


def draw():
    im.begin("Toolbox")
    im.end()

    im.begin("Session")
    im.input_text("Prompt", )
    im.end()
