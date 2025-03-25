import json


class Retrieval:
    def __init__(self, data_path: str = "./data/newjeans.json"):
        with open(data_path, "r") as file:
            data: dict[str, str] = json.load(file)
            self.data = data

    def retrieve(self, query: str) -> str | None:
        # query 는 유저의 발화문이다. self.data 에는 json 값이 key-value 형태로 저장되어 있다.
        for key, value in self.data.items():
            if key.lower() in query.lower():
        # 만약 query 가 json 의 key 값을 키워드로 포함하고 있으면 "{key}: {value}" 를 str 으로 리턴하자.
                return f"{key}: {value}"
        return None

    def print_data(self) -> None:
        print(self.data)
