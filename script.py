import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print visits.head()
print cart.head()
print checkout.head()
print purchase.head()

visits_cart = pd.merge(visits, cart, how='left')
print len(visits_cart) #2052 entries
print visits_cart.head()
print len(visits_cart[visits_cart.cart_time.isnull()])
#1652 users who have visited the site but not added anything to their cart
no_cart_percentage = float(len(visits_cart[visits_cart.cart_time.isnull()]))/len(visits_cart)
print no_cart_percentage #80% of users didn't add an item to the cart

cart_checkout = cart.merge(checkout, how='left')
no_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
no_checkout_percentage = float(no_checkout)/len(cart_checkout)
print no_checkout_percentage #21% of users that added an item to the cart didn't checkout

cart_checkout = pd.merge(visits_cart, checkout, how='left')
all_data = pd.merge(cart_checkout, purchase, how='left')
print all_data.head()

checkout_purchase = checkout.merge(purchase, how='left')

print float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))/len(all_data) #about 3.9% of users began to checkout but did not purchase a shirt 

#visit to cart is the weakest step of the funnel. To change this, Cool T-Shirts Inc. should offer a wider range of shirts and products that users who visit their site would want to add to their carts

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print all_data.time_to_purchase
print all_data.time_to_purchase.mean()
