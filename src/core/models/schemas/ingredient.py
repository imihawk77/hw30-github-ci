from pydantic import BaseModel, ConfigDict


class IngredientBase(BaseModel):
    ingredient_name: str = "Рис (Наименование)"
    ingredient_description: str = "Мягкий, рассыпчатый. (Описание)"


class IngredientCreate(IngredientBase):
    pass


class IngredientRead(IngredientBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id:int
