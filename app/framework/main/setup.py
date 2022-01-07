from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.framework.routes import (
    flavour,
    price,
    allergen,
    nutrition,
    product,
    category,
    ingredients,
)


def setup(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    app.include_router(product.router, tags=["Product"])
    app.include_router(category.router, tags=["Category"])
    app.include_router(flavour.router, tags=["Flavour"])
    app.include_router(allergen.router, tags=["Allergen"])
    app.include_router(nutrition.router, tags=["Nutrition"])
    app.include_router(price.router, tags=["Price"])
    app.include_router(ingredients.router, tags=["Ingredient"])

    return app
