def recommend_outfit(weather, preferences):
    if weather["condition"] == "sunny" and weather["temperature"] > 25:
        return "Shorts and sunglasses"
    elif weather["condition"] == "sunny":
        return "T-shirt and jeans"
    return "Jacket and trousers"
