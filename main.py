from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["App"])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", tags=["App"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("solution", tags=["App"])
async def process_orders(orders, criterion):
    pass
