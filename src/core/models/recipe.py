from typing import TYPE_CHECKING, List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


from .base import Base

if TYPE_CHECKING:
    from .Ingredient import Ingredient


class Recipe(Base):
    """
    Описание рецептов
    """

    recipe_name: Mapped[str] = mapped_column(String(100))
    cooking_time: Mapped[int] = mapped_column(default=5)
    views: Mapped[int] = mapped_column(default=0)
    recipe_description: Mapped[str] = mapped_column(
        Text, default="__"
    )

    used_ingredients: Mapped[list["Ingredient"]] = relationship(
        back_populates="used_in_recipe", secondary="ingredients_in_recipes"
    )

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.recipe_name}"