import re

def title_validator(title):
    if re.match(r"^[a-zA-Z\s]{3,30}$", title):
        return title
    else:
        raise ValueError("invalid title!!!")

def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        return brand
    else:
        raise ValueError("invalid brand!!!")

def price_validator(price):
    if re.match(r"^[0-9\s]{3,30}$", price):
        return price
    else:
        raise ValueError("invalid price!!!")
