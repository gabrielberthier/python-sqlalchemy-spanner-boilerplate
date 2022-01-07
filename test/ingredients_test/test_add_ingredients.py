from unittest import TestCase, main, mock
import os
from app.infrastructure.services.ingredient_services.ingredients_service import (
    IngredientsService
)
class TestAddressRepository(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env_patcher = mock.patch.dict(os.environ, {"MODE": "test"})
        cls.env_patcher.start()

    
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

        cls.env_patcher.stop()

    # def test_complete(self):
