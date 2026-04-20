import logging
from pickle import load 
from fastapi import FastAPI
import inngest
from inngest.experimental import ai
import inngest.fast_api
import uuid
import os
import datetime
from dotenv import load_dotenv


load_dotenv()

inngest_client = inngest.Inngest(
    app_id="rag-agent",
    logger = logging.getLogger("uvicorn"),
    is_production = False,
    serializer=inngest.PydanticSerializer()
)

@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event= "rag/ingest_pdf")
)

async def rag_ingest_pdf(ctx: inngest.Context):
    return {"Hello": "World"}

app = FastAPI()

inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf])
