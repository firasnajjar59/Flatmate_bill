from fpdf import FPDF
import webbrowser
class PdfReader:
    def __init__(self,file_name):
        self.file_name=f"{file_name}_id_{self.file_id()}.pdf"
    def generate(self,bill,first_flatmate,second_flatmate):
        # init pdf class
        pdf=FPDF(unit="pt")
        # add page
        pdf.add_page()
        # set the font for title
        pdf.set_font(family="Times",size=20,style="b")
        # add title
        pdf.cell(w=0,h=100,txt="Flatemate Bill",align="C", ln=1)
        # set font for the body file
        pdf.set_font(family="Times",size=14)
        # add period cell
        pdf.cell(w=256,h=50,txt="Flatmate:",border=1,align="L")
        pdf.cell(w=120,h=50,txt="Days",border=1,align="C")
        pdf.cell(w=162.5,h=50,txt=bill.period,border=1,align="C", ln=1)
        # add flatmate amount cell
        pdf.cell(w=256,h=30,txt=f"{first_flatmate.name}",border=1,align="L")
        pdf.cell(w=120,h=30,txt=str(first_flatmate.days_in_month),border=1,align="C")
        pdf.cell(w=162.5,h=30,txt=str(round(first_flatmate.pay(bill,second_flatmate),2)),border=1,align="C", ln=1)
        pdf.cell(w=256,h=30,txt=f"{second_flatmate.name}",border=1,align="L")
        pdf.cell(w=120,h=30,txt=str(second_flatmate.days_in_month),border=1,align="C")
        pdf.cell(w=162.5,h=30,txt=str(round(second_flatmate.pay(bill,first_flatmate),2)),border=1,align="C", ln=1)
        # add total bill
        pdf.cell(w=256,h=30,border=0,align="L")
        pdf.cell(w=120,h=30,txt="Total:",border=1,align="C")
        pdf.cell(w=162.5,h=30,txt=str(bill.amount),border=1,align="C", ln=1)
        # save the file
        file=open("counter.txt")
        file_content=file.read()
        if len(file_content)>0:
            count=str(int(file_content)+1)
            print(count)
            file.close()
            file=open("counter.txt",mode="w")
            file.write(count)
            file.close()
        else:
            count=str(1)
            file.close()
            file=open("counter.txt",mode="w")
            file.write(count)
            file.close()

        pdf.output(self.file_name)
        webbrowser.open(self.file_name)
    def file_id(self):
        # save the file
        file = open("counter.txt")
        file_content = file.read()
        if len(file_content) > 0:
            count = str(int(file_content) + 1)
            print(count)
            file.close()
            file = open("counter.txt", mode="w")
            file.write(count)
            file.close()
        else:
            count = str(1)
            file.close()
            file = open("counter.txt", mode="w")
            file.write(count)
            file.close()
        return count