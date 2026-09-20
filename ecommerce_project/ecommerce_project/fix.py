import pathlib
pathlib.Path("shop/templates/shop/checkout.html").write_text("""{% extends 'shop/base.html' %}
{% block content %}
<div style="max-width:600px; margin:20px auto; padding:20px; border:1px solid #ddd;">
<h2>Checkout</h2>
<p>Total: <b>Rs.{{ total }}</b></p>
<hr>
<form method="POST">
{% csrf_token %}
<textarea name="address" required placeholder="Full Address" style="width:100%;height:80px"></textarea><br><br>
<input type="text" name="phone" required placeholder="Phone" style="width:100%;padding:10px"><br><br>
<button type="submit" style="width:100%;padding:12px;background:black;color:white;">Place Order</button>
</form>
</div>
{% endblock %}
""", encoding='utf-8')

pathlib.Path("shop/templates/shop/base.html").write_text("""<!DOCTYPE html>
<html><head><title>My Shop</title></head>
<body>
<nav style="background:black;padding:15px">
<a href="/" style="color:white;margin-right:10px">Home</a>
<a href="/cart/" style="color:white">Cart</a>
</nav>
<div style="padding:20px">{% block content %}{% endblock %}</div>
</body></html>
""", encoding='utf-8')

print("DONE - Files Created!")