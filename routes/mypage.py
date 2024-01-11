from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

## mypage_info
@router.post("/info") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_info.html", context={'request':request})

@router.get("/info") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_info.html", context={'request':request})

## mypage_insert_plan
@router.post("/insert_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_insert_plan.html", context={'request':request})

@router.get("/insert_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_insert_plan.html", context={'request':request})

## mypage_main
@router.post("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_main.html", context={'request':request})

@router.get("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_main.html", context={'request':request})


## mypage_plan_list
@router.post("/plan_list") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_plan_list.html", context={'request':request})

@router.get("/plan_list") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_plan_list.html", context={'request':request})
