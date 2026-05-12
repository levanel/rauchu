from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
#QfYu85CaXsrXpOzb
app =  FastAPI()

client = MongoClient("mongodb+srv://rauchu67_db_user:0YYDY9JFUcymGmOa@cluster0.3q8nxce.mongodb.net/?appName=Cluster0")
db= client.project_db
task_collection = db.tasks

class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False

@app.get("/")

def read_root():
    return {"message": "Gohan ni suru? Ofuro ni suru? Soretomo…… watashi?"}

@app.post("/tasks/")
def create_task(task: Task):
    task_dict = task.model_dump()
    task_collection.insert_one(task_dict)

    return {"message": "created successfully.", "task": task.title}

@app.put("/tasks/{task_title}")
def update_task(task_title: str, is_completed: bool):
    result = task_collection.update_one(
        {"title": task_title},
        {"$set": {"is_completed": is_completed}}
    )
    if result.matched_count ==0:
        return {"error": "Task not found"}

    return {"message": f"Task '{task_title}'updated successfully"}

@app.delete("/tasks/{task_title}")
def delete_task(task_title: str):
    result = task_collection.delete_one({"title": task_title})

    if result.deleted_count ==0:
        return {"error": "task not found"}

    return {"message": "'{task_title}' deleted successfully"}

@app.get("/tasks/")
def get_all_tasks():
    tasks = list(task_collection.find({}, {"_id": 0}))
    return {"tasks": tasks}
