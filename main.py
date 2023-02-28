from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from flask import Flask,render_template,request
from backend.bill import Bill
from backend.flatmate import Flatmate
from backend.pdfreader import PdfReader
from backend.fileShare import FileShare
app=Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")
class BillFormPage(MethodView):
    def get(self):
        bill_form=BillForm()
        return render_template("billform.html",bill_form=bill_form)
class Result(MethodView):
    def post(self):
        bill_form=BillForm(request.form)
        bill=Bill(float(bill_form.amount.data),bill_form.period.data)
        flatmate1=Flatmate(bill_form.name1.data,int(bill_form.days_in_month1.data))
        flatmate2=Flatmate(bill_form.name2.data,int(bill_form.days_in_month2.data))
        pdf_reader=PdfReader(f"bill_for_{flatmate1.name}_{flatmate2.name}_{bill.period}")
        pdf_reader.generate(bill,flatmate1,flatmate2)
        file_share=FileShare(pdf_reader.file_name)
        link=file_share.share()
        return render_template("result.html",flatmate1_name=flatmate1.name,
                               flatmate1_have_to_pay=round(flatmate1.pay(bill,flatmate2),2),
                               flatmate2_name=flatmate2.name,
                               flatmate2_have_to_pay=round(flatmate2.pay(bill,flatmate1),2),
                               link=link)
class BillForm(Form):
    amount=StringField("Bill Amount: ",default="120")
    period=StringField("Bill Period: ",default="March 2023")
    name1=StringField("name first flatmate: ",default="Firas")
    days_in_month1=StringField("days they still in house: ",default="20")
    name2=StringField("name second flatemate: ",default="John")
    days_in_month2=StringField("days they still in house: ",default="25")
    submit_buttun=SubmitField("Calculate")

app.add_url_rule("/",view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill",view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/result",view_func=Result.as_view("result"))
app.run(port=1000)