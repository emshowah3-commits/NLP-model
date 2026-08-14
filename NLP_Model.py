customer_serv = ["This product was nice!", "This product was horrible"]

key_review = ['nice', '!', 'horrible']

for _ in key_review:
    Review = sum(1 for _ in key_review if _ in key_review)

print(customer_serv, '-->', 'Positive' if Review > 0 else 'Needs review' )