from django import template

register = template.Library()


@register.filter(name="is_available")
def is_available(product, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True
    return False


@register.filter(name="quantity")
def quantity(product_id, cart):
    keys = cart.keys()

    for key in keys:
        if int(key) == product_id:
            return cart[key]
    print(product_id)
    return 0

@register.filter(name="total_sum")
def total_sum(product,cart):
    return product.price*cart.get(str(product.id))

@register.filter(name="total_bill")
def total_bill(products,cart):
    sum = 0

    for product in products:
        sum+=total_sum(product,cart)

    return sum
