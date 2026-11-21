import os
from numbers_parser import Document
from classes.loan import Loan
from classes.expence import Expance
from classes.income import Income
from classes.meta import Meta

file = os.path.expanduser('~/Library/Mobile Documents/com~apple~Numbers/Documents/Finances.numbers')

def get_loans():
    doc = Document(file)
    sheets = doc.sheets
    tables = sheets("Loans").tables
    loans = []

    for row in tables[0].rows():
        if row[0].value != None:
            loan = Loan(row[0], row[1], row[2], row[3])
            loans.append(loan)

    return loans

def get_expences():
    doc = Document(file)
    sheets = doc.sheets
    tables = sheets("Expences").tables
    expences = []

    for row in tables[0].rows():
        if row[0].value != None:
            expence = Expance(row[0], row[1])

    return expences

def get_incomes():
    doc = Document(file)
    sheets = doc.sheets
    tables = sheets("Income").tables
    incomes = []

    for row in tables[0].rows():
        if row[0].value != None:
            income = Income(row[0], row[1], row[2], row[3])
            incomes.append(income)
    
    return incomes

def get_meta():
    doc = Document(file)
    sheets = doc.sheets
    tables = sheets("Meta").tables