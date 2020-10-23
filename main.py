# @FILENAME : main
# @AUTHOR : lonsty
# @DATE : 10/23/20 11:17 PM
import uvicorn

from fastapi_demo.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
