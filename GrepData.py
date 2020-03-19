import requests

url="https://www.easy-mock.com/mock/5d5f9f61039ad83a38d3a88a/codes/datas"

class GrepData():

    def query_data(self,batchCode):
        payload = {}
        payload["querycode"] = batchCode;
        session_requests = requests.Session()
        results = session_requests.get(
            url,
            params=payload
        )
        json_result = results.json()
        return json_result["data"]

