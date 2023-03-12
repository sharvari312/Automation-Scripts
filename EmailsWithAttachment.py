
import pandas
import yagmail

sender="sender@gmail.com"

pd=pandas.read_csv('Contacts.csv')
print(pd)
subject="Bill Payment"

yag=yagmail.SMTP(user=sender,password=PASSWORD)
for index,row in pd.iterrows():
    contents = [f"HI, {row['name']}, You have to pay Rs. {row['amount']}. Attached is your bill!",row['filepath']]
    yag.send(to=row['email'],subject=subject,contents=contents)
    print("Email Send")

