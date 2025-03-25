import pytest
import resolve_path

from chatbot.retrieval import Retrieval

retrieval = Retrieval()


def test_retrieve() -> None:
    retrieved = retrieval.retrieve("minji")
    assert retrieved is not None

# 예시 1:
# query: who is minji? ("minji" is in json key)
# @ return "minji: The leader of NewJeans..."
retrieval = Retrieval()
result = retrieval.retrieve("who is minji?")
print(result)
# 예시 2:
# query: this is an empty query (None of the json key matches)
# @ return None
retrieval = Retrieval()
result = retrieval.retrieve("this is an empty query")
print(result)