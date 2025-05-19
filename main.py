from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "chemGPT-SE backend is running!"}

@app.post("/retrosynthesis")
async def retrosynthesis(req: Request):
    data = await req.json()
    smiles = data.get("smiles")
    if not smiles:
        return {"result": "⚠️ No SMILES provided."}
    # TODO: Plug in AiZynthFinder here
    return {"result": f"Pretend prediction for {smiles} (AiZynth to be connected)"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
