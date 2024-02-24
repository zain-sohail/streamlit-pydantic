import streamlit as st
from pydantic import BaseModel, Field, HttpUrl

import streamlit_pydantic as sp
from pydantic_extra_types.color import Color


class ExampleModel(BaseModel):
    url: HttpUrl
    color: Color
    email: str = Field(..., max_length=100, pattern=r"^\S+@\S+$")


data = sp.pydantic_form(key="my_form", model=ExampleModel)
if data:
    st.json(data.json())
