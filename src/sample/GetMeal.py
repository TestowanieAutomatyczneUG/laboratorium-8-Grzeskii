import requests as r

class GetMeal:

    def getter(self, name):
        payload = {"s": name}
        response = r.get("https://www.themealdb.com/api/json/v1/1/search.php", params=payload)
        if response.json()["meals"] == None:
            return print("This meal doesn't exist!")
        name = response.json()["meals"][0]["strMeal"]
        category = response.json()["meals"][0]["strCategory"]
        instructions = response.json()["meals"][0]["strInstructions"]
        print(f"Fullname: {name}\nCategory: {category}\nInstructions: {instructions}")
        return response.json()