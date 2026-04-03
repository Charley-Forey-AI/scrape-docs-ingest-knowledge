---
title: "Equipment Entries | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/equipment-entries"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/equipment-entries"
---

# Equipment Entries

Multi-company equipment transactions can occur when using AP, PR, EU, and ES transaction types. Note that when using equipment entry in Payroll, the equipment lookup window will display only the equipment that has been set up in the current company. For example, if you are logged on to company YYY, but are charging payroll hours to an XYZ job, the Equipment Code window will display equipment that has been set up in company YYY. Company XYZ's equipment will be unavailable.
AP type transactions will be recorded as follows:

## COMPANY PAYING BILLS

DebitCredit
Intercompany AccountAccounts Payable
(from installation page)(from invoice header)

## COMPANY THAT OWNS EQUIPMENT

DebitCredit
Equipment ExpenseIntercompany Account
(from invoice detail)(from installation page)

PR type transactions will be recorded as follows:

## COMPANY PAYING PAYROLL

DebitCredit
Intercompany AccountCash & Liabilities

## COMPANY THAT OWNS EQUIPMENT

DebitCredit
Equipment ExpenseIntercompany Account

EU (usage "R"evenue) type transactions will be recorded as follows:

## COMPANY INCURRING EXPENSE

DebitCredit
Expense AccountIntercompany Account

## COMPANY THAT OWNS EQUIPMENT

DebitCredit
Intercompany AccountEquip. Usage Allocated

ES (usage "R"evenue) type transactions will be recorded as follows:
COMPANY INCURRING EXPENSE
DebitCredit
Expense AccountIntercompany Account

COMPANY THAT OWNS EQUIPMENT
DebitCredit
Intercompany AccountEquip. Usage Allocated

Related information

- [Multi-Company Transactions](/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions)
