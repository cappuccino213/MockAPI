"""
@File : demo.py
@Date : 2022/7/12 16:22
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
import time

import fastapi

import uvicorn

from typing import Optional

from pydantic import BaseModel

mock_server = fastapi.FastAPI()


class FollowInfo(BaseModel):
	id_card: str
	name: str
	is_follow: str


class TestInfo(BaseModel):
	path: Optional[str]
	id: Optional[int]


PATIENT_LIST = ["411381198810013456", "710000201209260734","854125199008299527"]

SUCCESS_MSG = {
	"code": 200,
	"msg": "推送成功",
	"time": f"{round(time.time())}",
	"data": ""
}

FAIL_MSG = {
	"code": 400,
	"msg": "推送失败，未找到对应的身份证号数据",
	"time": f"{round(time.time())}",
	"data": ""
}


@mock_server.get('/test')
def test(user: str):
	return f"welcome {user}!!!"


@mock_server.post('/api/notify/follow')
def notify_follow(follow_info: FollowInfo):
	if follow_info.id_card in PATIENT_LIST:
		return SUCCESS_MSG
	else:
		return FAIL_MSG


@mock_server.post('/api/test/path')
def notify_follow(test_info: TestInfo):
	if test_info.id:
		test_info.path = "通过id获取路径"
	return test_info.path


if __name__ == "__main__":
	uvicorn.run(mock_server, port=5000, debug=True, host='0.0.0.0')
