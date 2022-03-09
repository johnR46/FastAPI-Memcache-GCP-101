import time
import logging

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.apis import api_have_cache, api_with_out_cache

origins = ['*']

app = FastAPI(
    title="FastAPI-Memcache-GCP-101",
    description="Deploy FastAPI And Memcache In GCP ",
    debug=False,
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logging.info("Application startup ...")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# add endpoint
app.include_router(router=api_with_out_cache.router, prefix="/api/v1")
app.include_router(router=api_have_cache.router, prefix="/api/v2")
