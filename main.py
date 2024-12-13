from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.endpoints.commision_endpoints import commission_router
from src.app.endpoints.generated_kwc_endpoints import generated_kwc_outlet
from src.app.endpoints.payement_endpoints import payment_router
from src.app.endpoints.projects_endpoints import project_router
from src.app.endpoints.team_endpoints import team_router
from src.app.endpoints.team_memebers_endpoints import team_members_router
from src.app.endpoints.user_endpoints import user_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(generated_kwc_outlet)
app.include_router(team_router)
app.include_router(project_router)
app.include_router(team_members_router)
app.include_router(commission_router)
app.include_router(payment_router)
