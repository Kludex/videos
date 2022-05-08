import asyncio
from typing import Awaitable, Callable

from fastapi import BackgroundTasks, FastAPI, Request, Response

app = FastAPI()

@app.middleware("http")
async def middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    response = await call_next(request)
    return response

async def task():
    try:
        await asyncio.sleep(10)
    except Exception:
        print("Cancelled!")
    except BaseException:
        print("Really cancelled!")

@app.get("/")
def home(bkg_tasks: BackgroundTasks):
    bkg_tasks.add_task(task)
