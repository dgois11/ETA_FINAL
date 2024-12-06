from src.models.restaurant import Restaurant

class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant = Restaurant("La Pergola", "Italiana")
        result = restaurant.describe_restaurant()
        expected = (
            "Esse restaurante chama La Pergola e serve Italiana. "
            "Esse restaurante está servindo 0 consumidores desde está aberto."
        )
        assert result == expected, "Descrição do restaurante está incorreta."

    def test_open_restaurant(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        funcionamento = restaurant.open_restaurant()

        assert funcionamento == "La Pergola agora está aberto!"

    def test_open_restaurant_true(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        funcionamento1 = restaurant.open_restaurant()
        funcionamento2 = restaurant.open_restaurant()

        assert funcionamento2 == "La Pergola já está aberto!"

    def test_close_restaurant(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        resultado = restaurant.close_restaurant()

        assert resultado == "La Pergola já está fechado!"

    def test_close_restaurant_open_closed(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        restaurant.open_restaurant()
        resultado = restaurant.close_restaurant()

        assert resultado == "La Pergola agora está fechado!"

    def test_set_number_served_fechado(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        total_pessoas = 5
        verificador = restaurant.set_number_served(total_pessoas)

        assert verificador == "La Pergola agora está fechado!"

    def test_set_number_served_open_passed(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        funcionamento1 = restaurant.open_restaurant()

        total_pessoas = 5
        verificador = restaurant.set_number_served(total_pessoas)

        assert verificador == 5

    def test_set_number_served_open_peoples_negative(self):
        restaurant = Restaurant("La Pergola", "Italiana")

        funcionamento1 = restaurant.open_restaurant()

        total_pessoas = -10
        verificador = restaurant.set_number_served(total_pessoas)

        assert verificador == "Número de clientes não pode ser negativo."














