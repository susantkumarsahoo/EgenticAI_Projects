"""
FastAPI Backend for Research Assistant Agent
Provides REST API endpoints and Server-Sent Events for real-time updates
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from pydantic import BaseModel
from typing import Optional, AsyncGenerator
import asyncio
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Import the research agent
from research_agent import ResearchAgent, ResearchState, create_research_graph






