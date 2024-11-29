from typing import Union
import pytest

def reverse_sentence(sentence: Union[str, list]) -> Union[str, list]:
  mysentence = sentence
  revertsentence = mysentence[::-1]
  print(revertsentence)
  return revertsentence

def test_reverse_sentence():
    assert reverse_sentence("hello") == "olleh"
    assert reverse_sentence([1,2,3,4,5]) == [5,4,3,2,1]


def test_reverse_multiple():
   with pytest.raises(TypeError):
       reverse_sentence(123)
       reverse_sentence(1.23)
       reverse_sentence(True)
       reverse_sentence(None)
       reverse_sentence({1,2,3})
       reverse_sentence({"a":1, "b":2}) 
       reverse_sentence((1,2,3))
       reverse_sentence(1+2j)