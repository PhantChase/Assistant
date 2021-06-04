import requests

url = "https://visual-crossing-weather.p.rapidapi.com/history"

querystring = {"startDateTime":"2019-01-01T00:00:00","aggregateHours":"24","location":"VietNam","endDateTime":"2019-01-03T00:00:00","unitGroup":"us","dayStartTime":"8:00:00","contentType":"csv","dayEndTime":"17:00:00","shortColumnNames":"0"}

headers = {
    'x-rapidapi-key': "d99a6bc3bdmshd4bbd2e4b09920fp16ec20jsnc15a0c2414c2",
    'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)