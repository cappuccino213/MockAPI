"""
@File : mock_archive.py
@Date : 2022/7/20 11:08
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
import fastapi

import uvicorn

from pydantic import BaseModel

mock_server = fastapi.FastAPI()


class PostCon(BaseModel):
	AccessionNumber: str
	PatientID: str
	OrganizationCode: str
	StudyBeginDate: str
	ExamType: str


class StudyData(BaseModel):
	workQueueGuid: str
	patientId: str
	patientName: str
	otherName: str
	patientAge: str
	patientBirthday: str
	patientSex: str
	modality: str
	studyDateTime: str
	accessionNumber: str
	studyInstanceUID: str
	studyDescription: str
	organizationCode: str
	errorDescription: str


class CompareFailedStudy(BaseModel):
	code: str
	data: list[StudyData]
	message: str


example1 = {
	"data": [
		{
			"workQueueGuid": "34ee32a0-8a2e-4145-8339-9b076c3050a4",
			"patientId": "FS531961",
			"patientName": "张三",
			"otherName": "zhangsan",
			"patientAge": "04 6Y",
			"patientBirthday": "1975-11-02T00:00:00",
			"patientSex": "Female",
			"modality": "DR",
			"studyDateTime": "2022-02-25T22:54:36",
			"accessionNumber": "11021433832",
			"studyInstanceUID": "1.2.156.27.87582403.20200408.224232.26274.11337.52300.58470",
			"studyDescription": "0",
			"organizationCode": "QWYHZYFZX",
			"errorDescription": "获取0条待比对检查信息"
		},
		{
			"workQueueGuid": "34ee32a0-8a2e-4145-8339-9b076c3055a4",
			"patientId": "FS53196",
			"patientName": "李四",
			"otherName": "lisi",
			"patientAge": " 4 6d",
			"patientBirthday": "1975-11-02T00:00:00",
			"patientSex": "F",
			"modality": "DR",
			"studyDateTime": "2022-02-25T12:54:36",
			"accessionNumber": "110214832",
			"studyInstanceUID": "1.2.156.27.87582403.20200408.224232.26274.11337.52300.58470",
			"studyDescription": "0",
			"organizationCode": "QWYHZYFZX",
			"errorDescription": "获取0条待比对检查信息"
		},
		{
			"workQueueGuid": "a2f8b84b-b027-4d92-a0bb-55ab4c86d739",
			"patientId": "1733967",
			"patientName": "王五",
			"otherName": "WangWu",
			"patientAge": "10w",
			"patientBirthday": "1969-09-14",
			"patientSex": "male",
			"modality": "CT",
			"studyDateTime": "2021-09-22T18:19:05",
			"accessionNumber": "ME210922CT8121",
			"studyInstanceUID": "1.2.840.113704.1.111.4276.1632305945.1",
			"studyDescription": "CT Chest Routine",
			"organizationCode": "QWYHZYFZX",
			"errorDescription": "获取0条待比对检查信息"
		},
		{
			"workQueueGuid": "a2f8b84b-b027-4d92-a0bb-55ab4c86d739",
			"patientId": "1733967",
			"patientName": "麻六",
			"otherName": "MaLiu",
			"patientAge": "10y",
			"patientBirthday": "1969-09-14",
			"patientSex": "male",
			"modality": "CT",
			"studyDateTime": "2021-09-22T18:19:05",
			"accessionNumber": "ME210922CT8120",
			"studyInstanceUID": "1.2.840.113704.1.111.4276.1632305945.1",
			"studyDescription": "CT Chest Routine",
			"organizationCode": "QWYHZYFZX",
			"errorDescription": "获取0条待比对检查信息"
		},
		{
			"workQueueGuid": "a2f8b84b-b027-4d92-a0bb-55ab4c86d739",
			"patientId": "1733967",
			"patientName": "chenqi|6268",
			"otherName": "CHENQI",
			"patientAge": "20w",
			"patientBirthday": "1969-09-14",
			"patientSex": "male",
			"modality": "CT",
			"studyDateTime": "2021-09-22T18:19:05",
			"accessionNumber": "ME210922CT8120",
			"studyInstanceUID": "1.2.840.113704.1.111.4276.1632305945.1",
			"studyDescription": "CT Chest Routine",
			"organizationCode": "QWYHZYFZX",
			"errorDescription": "获取0条待比对检查信息"
		}
	],
	"code": 0,
	"message": "Success"
}


@mock_server.get('/test')
def test():
	return f"welcome!!!"


@mock_server.post('/Exchange/GetCompareFailedStudy', response_model=CompareFailedStudy)
def get_compare_failed_study(para: PostCon):
	if para:
		return example1


if __name__ == "__main__":
	uvicorn.run(app='app.mock_archive:mock_server', port=8188, debug=True, host='0.0.0.0', reload=True)
