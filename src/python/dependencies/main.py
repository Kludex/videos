from fastapi import Depends, FastAPI

app = FastAPI()


class Potato:
    def __init__(self, name: str):
        self.name = name

    def __call__(self):
        return self.name

potato = Potato("potato")

@app.get("/")
def home(dep: str = Depends(potato)):
    return dep


def banana() -> str:
    return "banana"

app.dependency_overrides[potato] = banana
