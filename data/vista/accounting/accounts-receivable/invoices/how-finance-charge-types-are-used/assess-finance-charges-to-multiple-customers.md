---
title: "Assess Finance Charges to Multiple Customers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/assess-finance-charges-to-multiple-customers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/assess-finance-charges-to-multiple-customers"
---

# Assess Finance Charges to Multiple Customers

The system can calculate and assess finance charges to many customers at once.

- In the AR Company Parameters form, Finance Charges tab:

- Select the Calculate Finance Charge radio button.

- If you want to include previously assessed finance
 changes in the calculation, select the Include Previous Finance Charges in
 Calculation checkbox.

- if you want to exclude customers with balances below a
 certain amount, enter the threshold value in the Minimum Balance field.


- In the AR Customers form, Add'l Info tab:

- Select an option from the Finance Charge Type drop down field.


- Enter a value in the Finance Charge % field.

 Note:

- If you do not specify a rate for the customer, the system uses the rate from the same-named field in the AR Company Parameters form.

- If you also have not specified a rate in AR Company Parameters form, the system skips the customer

Take these steps calculate and assess finance charges to many customers at once.

1. Enter New, N, or + in the Seq # field to start a new sequence.

1. Click Calculate FC Charges.The AR Calculate Finance Charge form displays.

1. Use the AR Calculate Finance Charge form to set criteria for calculating finance charges. For more information, see [AR Calculate Finance Charge](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-finance-charge-form).

1. Click OK and Close.All invoices meeting the criteria display as sequences in the AR Finance Charge form.

All invoices meeting the criteria display as sequences in the AR Finance Charge form.

- For each customer with an Open Item statement account, the system generates a separate record for each line on the invoice.

- For each customer with a Balance Forward statement account, the system creates only one detail line to represent the finance charge calculated on the overdue portion of the customer's account.

- Use the AR Customers form, Statements section of the Add'l Info tab to set statement types by customer.
