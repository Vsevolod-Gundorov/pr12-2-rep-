from fastapi import FastAPI, HTTPException
from app.template import Template

templates: list[Template] = [
    Template(10, 'First doc', 'Content'),
    Template(11, 'Second doc', 'Content 2')
    ]

app = FastAPI()

@app.get("/v1/templates")
async def get_templates():
    return templates

@app.get("/v1/templates/{id}")
async def get_templates_by_id(id: int):
    result = [item for item in templates if item.id == id]
    if len(result) > 0:
        return result[0]
    return HTTPException(status_code=404, detail="Item not found")