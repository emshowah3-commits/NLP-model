customer_serv = ["This product was nice!", "This product was horrible", "nice"]

key_review = ['nice', '!', 'horrible']

for customers in key_review:
    Review = sum(1 for customers in key_review if customers in customer_serv)
    print(customers, '-->', 'Positive' if Review > 0 else 'Needs review' )