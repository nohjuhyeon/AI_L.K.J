from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()
from beanie import PydanticObjectId
from databases.connections import Database

from models.user_list import User_list # 컬랙션을 연결하고, 컬렉션에 저장/불러오기 하는 방법 
collection_user_list = Database(User_list)

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

@router.post("/reserve_list") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_reserve_list.html", context={'request':request})

@router.get("/reserve_list") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_reserve_list.html", context={'request':request})

@router.get("/{object_id}")                     
async def login_main_get(request:Request, object_id:PydanticObjectId):
    print(dict(request._query_params))
    user_dict = await collection_user_list.get(object_id)
    print(user_dict)
    return templates.TemplateResponse("mypage/mypage_main.html",{'request':request,
                                                   'user_dict': user_dict})

@router.post("/{object_id}")                      
async def lgoin_main_post(request:Request, object_id:PydanticObjectId):
    await request.form()
    print(dict(await request.form()))
    user_dict = await collection_user_list.get(object_id)
    print(user_dict)
    return templates.TemplateResponse("mypage/mypage_main.html",{'request':request,
                                                   'user_dict': user_dict})

@router.post("/info/{object_id}") # 펑션 호출 방식
async def list_post(request:Request, object_id:PydanticObjectId):
    await request.form()
    user_dict = await collection_user_list.get(object_id)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_info.html", context={'request':request,
                                                                               'user_dict': user_dict})

@router.get("/info/{object_id}") # 펑션 호출 방식
async def list_post(request:Request, object_id:PydanticObjectId):
    await request.form()
    user_dict = await collection_user_list.get(object_id)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="mypage/mypage_info.html", context={'request':request,
                                                                               'user_dict': user_dict})