from fastapi import APIRouter,File,UploadFile
from typing import List
import os

app05 = APIRouter()

@app05.post("/file")
async def get_file(file:bytes = File()):
    print("file:",file)
    return {"file_size":len(file)}

@app05.post("/files")
async def get_files(files: List[bytes] = File()):
    for file in files:
        print("file_sizes:",len(file))
    return {
        "file_sizes": len(files)
    }

@app05.post("/uploadFile")
async def upload_file(file:UploadFile = File()):
    print("file:",file)

    path = os.path.join("imgs",file.filename)
    # 保存文件
    with open(path,"wb") as f:
        for line in file.file:
            f.write(line)

    return {"file_name":file.filename}

@app05.post("/uploadFiles")
async def upload_files(files:List[UploadFile] = File()):
    return {"file_names":[file.filename for file in files]}