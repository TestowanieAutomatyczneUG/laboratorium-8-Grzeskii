import requests as r

class GetMealById:

    def getter_id(self, mealId):
        payload = {"i": mealId}
        response = r.get("https://www.themealdb.com/api/json/v1/1/lookup.php", params=payload)
        if response.json()["meals"] == None:
            return "Invalid ID"
        name = response.json()["meals"][0]["strMeal"]
        category = response.json()["meals"][0]["strCategory"]
        instructions = response.json()["meals"][0]["strInstructions"]
        print(f"Fullname: {name}\nCategory: {category}\nInstructions: {instructions}")
        return response.json()
