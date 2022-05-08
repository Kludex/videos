from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def task1() -> None:
    print("Hello, world!")

def task2() -> None:
    print("This is the second world!")
    raise Exception()

def task3() -> None:
    print("Potato!!!!!!!")

@app.get("/")
def home(background_tasks: BackgroundTasks):
    background_tasks.add_task(task1)
    background_tasks.add_task(task2)
    background_tasks.add_task(task3)
