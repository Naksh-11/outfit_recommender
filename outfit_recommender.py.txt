def recommend_outfit(weather, occasion):
    if weather == "cold":
        return "Wear a sweater and jeans" if occasion == "casual" else "Wear a blazer and trousers"
    elif weather == "hot":
        return "T-shirt and shorts" if occasion == "casual" else "Linen shirt and chinos"
    else:
        return "Jeans and a hoodie"



weather = input("Enter the weather (hot/cold/moderate): ").lower()
occasion = input("Enter the occasion (casual/formal): ").lower()

print("Recommended outfit:", recommend_outfit(weather, occasion))

