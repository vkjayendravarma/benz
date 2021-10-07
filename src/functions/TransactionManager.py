import datetime

class TransactionManager: 
    @staticmethod
    def initNewTransactionId():
        dateTime = datetime.datetime.now()
        return dateTime.strftime("%Y") + dateTime.strftime("%V") + dateTime.strftime("%H") +dateTime.strftime("%M") + dateTime.strftime("%f")
