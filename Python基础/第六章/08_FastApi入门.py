from fastapi import FastAPI

#创建FastAPI实例
app = FastAPI()

#定义API接口,-->该函数返回值表示API接口返回的数据,接口访问路径为/,请求方式为get
@app.get("/")
def root():
    return {"message": "Hello World"}

#定义API接口
@app.get("/users")
def get_users():
    return[
        {"id":1,"name":"zhangsan"},
        {"id":2,"name":"lisi"},
        {"id":3,"name":"wangwu"},
    ]
# 快捷键ctrl c结束运行

#uvicorn Python中的轻量级的Web服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)