from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    id: int
    name: str

# Внешние данные, имитирует входящий JSON
external_data = {
    "id": "123",
    "name": "John Doe"
}
# имитируем распаковку входящих данных в коде приложения
user = User(**external_data)