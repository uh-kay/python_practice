def city_country(city, country, population=None):
    """Prints the provided city and country."""
    if population:
        return f"{city.title()}, {country.title()} - {population}"
    else:
        return f"{city.title()}, {country.title()}"
