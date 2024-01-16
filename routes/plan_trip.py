from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from utils.paginations import Paginations

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from databases.connections import Database
from models.reserve_transfer import transfer_car_list,transfer_train_list
from models.tour_plan import reco_trip_plan
collection_transfer_car_list = Database(transfer_car_list)
collection_transfer_train_list = Database(transfer_train_list)
collection_transfer_airport_list = Database(transfer_train_list)
collection_reco_trip_plan = Database(reco_trip_plan)



## 여행 계획 추천
@router.post("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    concept_tour = await collection_reco_trip_plan.get_all()

    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'concept_list' : concept_tour})

@router.get("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    concept_tour = await collection_reco_trip_plan.get_all()
    concept_list = []
    for i in range(len(concept_tour)):
        concept_list.append(concept_tour[i].concept_name)
    concept_list = set(concept_list)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'concept_list' : concept_list})

## 여행 계획
@router.post("/trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request})

@router.get("/trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    condition = { }
    condition["day"] = dict(request._query_params)['trip_concept']
    print(dict(await request.form()))
    tour_plan_list = await collection_reco_trip_plan.getsbyconditions(condition) 
    pass
    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request})


## 교통 예약
@router.post("/reserve_transfer") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request})

@router.get("/reserve_transfer") # 펑션 호출 방식
async def list_post(request:Request):
    dict(request._query_params)
    print(dict(request._query_params))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request})

## 교통 예약
@router.post("/reserve_transfer_car") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    car_list = await collection_transfer_car_list.get_all()
    print(car_list)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_car.html", context={'request':request,
                                                                                           'car_list':car_list})

from typing import Optional
@router.get("/reserve_transfer_airpost/{page_number}") # 펑션 호출 방식
@router.get("/reserve_transfer_airpost") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    await request.form()
    airpost_list = await collection_transfer_airport_list.get_all()
    total = len(airpost_list)
    conditions = { }
    print(airpost_list)
    print(dict(await request.form()))
    pagination = Paginations(total,page_number)
    airpost_list_pagination, pagination = await collection_transfer_airport_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_plane.html", context={'request':request,
                                                                                           'airpost_list':airpost_list_pagination,
                                                                                           'pagination':pagination})

from typing import Optional
@router.get("/reserve_transfer_car/{page_number}") # 펑션 호출 방식
@router.get("/reserve_transfer_car") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    await request.form()
    car_list = await collection_transfer_car_list.get_all()
    total = len(car_list)
    conditions = { }
    pagination = Paginations(total,page_number)
    car_list_pagination, pagination = await collection_transfer_car_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_car.html", context={'request':request,
                                                                                           'car_list':car_list_pagination,
                                                                                           'pagination':pagination})

@router.get("/reserve_transfer_train/{page_number}") # 펑션 호출 방식
@router.get("/reserve_transfer_train") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    await request.form()
    train_list = await collection_transfer_train_list.get_all()
    conditions = { }
    total = len(train_list)
    pagination = Paginations(total,page_number)

    train_list_pagination, pagination = await collection_transfer_train_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_train.html", context={'request':request,
                                                                                           'train_list':train_list_pagination,
                                                                                           'pagination':pagination})
    
## 숙소 예약
@router.post("/reserve_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request})

@router.get("/reserve_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request})

## 투어 예약
@router.post("/reserve_tour") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request})

@router.get("/reserve_tour") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request})
