from fastapi import FastAPI               
app = FastAPI()

# from databases.connections import Settings

# settings = Settings()
# @app.on_event("startup")
# async def init_db():
#     await settings.initialize_database()


from routes.admin import router as admin_router                   
from routes.mypage import router as second_router
from routes.plan_trip import router as users_router
from routes.consult import router as consult_router
from routes.event import router as event_router

app.include_router(admin_router, prefix="/admin")
app.include_router(second_router, prefix="/mypage")
app.include_router(users_router, prefix="/plan_trip")
app.include_router(consult_router, prefix="/consult")
app.include_router(event_router, prefix="/event")

from fastapi import Request                                
from fastapi.templating import Jinja2Templates              

from fastapi.middleware.cors import CORSMiddleware             
app.add_middleware(
    CORSMiddleware,            
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles
# # url 경로(url에서 입력해야 하는 주소), 자원 물리 경로(directory; 실제 경로), 프로그래밍 측면(key의 이름 지정)
app.mount("/css", StaticFiles(directory="resources\\css\\"), name="static_css")
app.mount("/images", StaticFiles(directory="resources\\images\\"), name="static_images")

templates = Jinja2Templates(directory="templates/")    

@app.get("/")                     
async def root(Request:Request):
    return templates.TemplateResponse("main.html",{'request':Request})


@app.post("/")                      
async def root(Request:Request):
    return templates.TemplateResponse("main.html",{'request':Request})

@app.get("/login")                     
async def root(Request:Request):
    return templates.TemplateResponse("login.html",{'request':Request})


@app.post("/login")                      
async def root(Request:Request):
    return templates.TemplateResponse("login.html",{'request':Request})

@app.get("/community")                     
async def root(Request:Request):
    return templates.TemplateResponse("community.html",{'request':Request})


@app.post("/community")                      
async def root(Request:Request):
    return templates.TemplateResponse("community.html",{'request':Request})

@app.get("/insert")                     
async def root(Request:Request):
    return templates.TemplateResponse("insert.html",{'request':Request})


@app.post("/insert")                      
async def root(Request:Request):
    return templates.TemplateResponse("insert.html",{'request':Request})

