import uvicorn
from fastapi import FastAPI

DUMMY_ITEMS = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello backend"}

if __name__ == "__main__":
    uvicorn.run("backend:app", port=8000, reload=True)
