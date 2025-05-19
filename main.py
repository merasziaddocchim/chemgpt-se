from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from aizynthfinder.aizynthfinder import AiZynthFinder
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# AiZynthFinder Model: Load Once
# ===============================
CONFIG_PATH = "config.yml"
finder = AiZynthFinder(CONFIG_PATH)

@app.get("/")
def root():
    return {"message": "chemGPT-SE backend is running!"}

@app.post("/retrosynthesis")
async def retrosynthesis(req: Request):
    data = await req.json()
    smiles = data.get("smiles")
    if not smiles:
        return {"result": "⚠️ No SMILES provided."}
    try:
        finder.target_smiles = [smiles]
        finder.prepare()
        finder.run()
        if finder.routes:
            best_route = finder.routes[0]
            result_str = best_route.to_string()
            return {"result": result_str}
        else:
            return {"result": "❌ No synthesis route found."}
    except Exception as e:
        return {"result": f"Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
