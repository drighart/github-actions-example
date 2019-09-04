""" Best API ever"""
from fastapi import FastAPI

from app.routers.blackjack.api_view_v1 import app as blackjack_router


DESCRIPTION = """Deze API hoort bij het voorbeeldproject voor de Openshift CI/CD
    workshop gegeven door het centrale CI/CD team. De API biedt een endpoint dat
    aangeroepen kan worden om een blackjack job te starten welke gegeven inputs 
    van kaarten berekent of dit een blackjack score is of niet.
    </br></br>
    De source-code kun je terug vinden in Github onder 
    de url: <https://github.com/Alliander/okd-cicd-workshop></br></br>
    **Technische documentatie**</br>
    Naast de `/docs` folder is er ook de `/redoc` folder. Ook is er een 
    Prometheus `/metrics` endpoint waarop door het cluster actief gemonitord kan
    worden.
"""

app = FastAPI(title='Openshift CI/CD Workshop API', # pylint: disable=C0103
              openapi_prefix='/api/v1/',
              version='1.0.0', description=DESCRIPTION)

app.include_router(blackjack_router, prefix='/blackjack', tags=['BlackJack'])
