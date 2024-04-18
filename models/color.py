from enum import Enum

class Color(Enum):
  SPACE = {
  "label": "space",
  "value": "･"
  }

  BLACK = {
  "label": "black",
  "value": "●"
  }  

  WHITE = {
  "label": "white",
  "value": "○"
  }


  def __str__(self):
    return self.val


  @staticmethod
  def label_of(l: str) -> object:
    for k in Color:
      if k.value["label"] == l:
        return k
    raise ValueError(f"undefined Status: {l}")
   
  @property
  def val(self) -> str:
    return self.value["value"]