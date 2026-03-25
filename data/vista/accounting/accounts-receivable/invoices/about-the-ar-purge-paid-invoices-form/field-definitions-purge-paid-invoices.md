---
title: "Field Definitions: Purge Paid Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-purge-paid-invoices-form/field-definitions-purge-paid-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-purge-paid-invoices-form/field-definitions-purge-paid-invoices"
---

# Field Definitions: Purge Paid Invoices

The following is a list of field descriptions for the AR Purge Paid Invoices form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Purge Through Month

 Initially defaults to the last month closed in GL Month End Close. Accept the default, or enter the month through which all paid invoices will be purged.

## Purge By

- Customer - Select this option to purge paid invoices by customer.

- Contract - Select this option to purge invoices by contract. The system purges all invoices associated with the selected contract.

##  Beginning Customer Number

 Enter the beginning customer number in a range of customer numbers with which to begin the purge.
Leave blank to being the purge with the first customer number.

##  Ending Customer Number

Enter the ending customer number in a range of customers number with which to end the purge.
Leave blank to end the purge with the last customer number.

##  Exclude Invoices That Have Contracts

 Check this box to exclude all invoices that have contracts associated with them when purging invoices by customer.
 Do not check this box if you want all invoices and their associated contracts purged.

## Delete Temporary Customers

Check this box to purge temporary customers from the AR files. When checked, monthly totals for the AR company and customer will be cleared, as long as no transactions exist for the customer and AR company. If no other companies have monthly totals for the customer, the customer will then be purged from the AR files.
Note: To purge a customer from the Customer Master that is shared by other companies, you must purge paid invoices for the customer in the ‘sharing’ companies, as well as purge the monthly totals by checking this option in each company. Only then will the ‘temporary’ customer be deleted from the Customer Master.
Do not check this box if you do not want to purge temporary customers.

## Delete Inactive Customers

Check this box to purge inactive customers (status of “Inactive” in AR Customers) from the AR files. When checked, monthly totals will be cleared for the AR Company and customer, as long as no transactions exist for that customer and AR company. If no other companies have monthly totals for the customer, the customer will then be purged from the Customer Master.
Note: To purge a customer from the Customer Master that is shared by other companies, you must purge paid invoices for the customer in the ‘sharing’ companies, as well as purge the monthly totals by checking this option in each company. Only then will the ‘inactive’ customer be deleted from the Customer Master.
Do not check this box if you do not want to purge inactive customers.

##  JC Company

 Specify the Job Cost company for the contract(s) from which all invoices are to be purged.

##  Beginning Contract

 Enter the contract with which to begin the purge.
Note: If you enter a contract that has been purged in JC, a warning displays indicating that the contract is not on file; however, entry will be allowed.

## Ending Contract

Enter the contract with which to end the
 purge.
Note: If you enter a contract that has been purged in JC, a
 warning displays indicating that the contract is not on file; however, entry is
 allowed.
