from bill import Bill
from fileShare import FileShare
from flatmate import Flatmate
from pdfreader import PdfReader

bill=Bill(amount=float(input("Please enter the bill amount. ")),period=input("Enter the month for the bill. E.g. (March 2023) "))
first_flatmate=Flatmate(name=input("Enter the name  for the first flatmate. "),days_in_month=int(input("Please how many days stay in the apartment. ")))
second_flatmate=Flatmate(name=input("Enter the name  for the second flatmate. "),days_in_month=int(input("Please how many days stay in the apartment. ")))
print(first_flatmate.pay(bill,second_flatmate))
print(second_flatmate.pay(bill,first_flatmate))
pdf_reader=PdfReader(f"bill_for_{first_flatmate.name}_{second_flatmate.name}_{bill.period}")
pdf_reader.generate(bill,first_flatmate,second_flatmate)
share_file=FileShare(pdf_reader.file_name)
print(share_file.share())