
class Flatmate:
    def __init__(self,name,days_in_month):
        self.name=name
        self.days_in_month=days_in_month
    def pay(self,bill,the_other_flatmate):
        return (bill.amount/(the_other_flatmate.days_in_month+self.days_in_month))*self.days_in_month