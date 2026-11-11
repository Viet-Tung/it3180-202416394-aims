def search_by_title(cart, title):
    matched = [dvd for dvd in cart.items if title.lower() in dvd.title.lower()]
    return matched