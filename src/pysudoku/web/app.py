from fastapi import FastAPI

app = FastAPI()

# Register all of the routes
import pysudoku.web.router