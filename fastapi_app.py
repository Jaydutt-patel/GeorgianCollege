from fastapi import FastAPI
from multimodal_search import MultimodalSearch
from fastapi.responses import FileResponse

app = FastAPI()

# Instantiate the class
mm_search = MultimodalSearch()

@app.get("/")
async def search(query: str = "jacket", top_k: int = 3):
    # Perform a search
    results = mm_search.search(query=query, top_k=top_k)

    # Return the results
    return results

@app.get("/image/{filename}")
async def get_image(filename: str):
    # Assuming result.content contains the file path of the image
    # Adjust this according to your actual implementation
    return FileResponse(filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
