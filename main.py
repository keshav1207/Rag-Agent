import logging
from pickle import load 
from fastapi import FastAPI
import inngest
from inngest.experimental import ai
import inngest.fast_api
from dotenv import load_dotenv
import uuid
import os
import datetime


load.env()