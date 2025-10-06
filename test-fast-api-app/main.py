import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# IMPORTANT: This imports your locally installed package
try:
    from semantiker import SemanticCacheUtility, OllamaClient
except ImportError:
    print("Error: 'semantiker' package not found. Ensure you ran 'pip install -e .' in the package root.")
    exit()

# --- 1. SETUP CORE COMPONENTS ---

# Configuration
OLLAMA_HOST = "http://localhost:11434/api/generate"
LLM_MODEL = "mistral"  # Change this to your preferred local model
SIMILARITY_THRESHOLD = 0.85

# Initialize the cache utility globally
try:
    llm_client = OllamaClient(api_url=OLLAMA_HOST)
    cache_utility = SemanticCacheUtility(
        llm_client=llm_client,
        similarity_threshold=SIMILARITY_THRESHOLD
    )
    print(f"✅ Semantic Cache Utility initialized with Ollama client ({LLM_MODEL}).")
except Exception as e:
    # A failure here means Ollama isn't running or the package is misconfigured
    print(f"❌ Failed to initialize Ollama client or Cache Utility. Error: {e}")
    # Initialize with a dummy client to allow the app to run, but all calls will fail.
    cache_utility = None 
    
# --- 2. FASTAPI APP DEFINITION ---

app = FastAPI(title="Semantic Cache Tester")

class QueryRequest(BaseModel):
    """Pydantic model for the request body."""
    query: str

class QueryResponse(BaseModel):
    """Pydantic model for the response body."""
    query: str
    response: str
    source: str
    latency_ms: int

@app.post("/ask", response_model=QueryResponse, tags=["LLM & Cache"])
async def ask_llm_with_cache(request: QueryRequest):
    """
    Handles a query, checking the semantic cache before calling the LLM.
    """
    if cache_utility is None:
        raise HTTPException(status_code=503, detail="Cache and LLM service is unavailable (Ollama connection failed).")
        
    start_time = time.time()
    
    try:
        # Call the core logic of your package
        result = cache_utility.ask(query=request.query, model=LLM_MODEL)
        
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Return the structured response
        return QueryResponse(
            query=request.query,
            response=result['response'],
            source=result['source'],
            latency_ms=latency_ms
        )
        
    except Exception as e:
        print(f"Error during query processing: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the query.")

# Simple health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "semantiker_tester"}