from faker import Faker
fake = Faker(locale='en_CA')
advantage_shopping_cart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_register_url = 'https://advantageonlineshopping.com/#/register'
my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
my_order_url = 'https://advantageonlineshopping.com/#/MyOrders'
new_username = fake.user_name()
if len(new_username) > 15:
    new_username = new_username[0:14]
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
city = fake.city()
phone = fake.phone_number()
address = fake.street_address().replace("\n", "")
province = fake.province_abbr()
postal_code = fake.postalcode()
full_name = f'{first_name} {last_name}'


