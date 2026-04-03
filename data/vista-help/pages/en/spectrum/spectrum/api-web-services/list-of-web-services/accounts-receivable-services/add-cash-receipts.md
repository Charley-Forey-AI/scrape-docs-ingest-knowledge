---
title: "Add Cash Receipts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-cash-receipts"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-cash-receipts"
---

# Add Cash Receipts

Use this service to import Cash Receipts information.
WSDL: AddCash_Receipts.jws
Method: AddCash_Receipts
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Cash Receipts information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > General Ledger

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Transaction Code File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Equipment Control > Equipment File Maintenance

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The AR Cash Receipts web service creates Non-customer cash receipts and Customer specific cash receipts.

- The AR Cash Receipts web service requires the total transaction amount to be positive. If any adjustments, credits or reversals of data need to be made (that is, wrong details added and the need to be reversed), then the user must make these entries within Spectrum.

- Non-Customer Cash Receipts

- The following fields are required to create the record:

- Payer_Name

- Misc_Cash_Remarks

- GL_Account

- Remarks

- Job_Number

- Phase_Code

- Cost_Type

- Equipment_Code

- Cost_Category_Code

- PM_Work_Order

- The following fields need to be blank:

- Customer_Code

- Invoice_Number

- Invoice_Type

- Customer Cash Receipts

- Allows you to define a specific invoice number and apply the specific amount.

- The Invoice being paid must be an open Item for the Customer.

- The Cash Receipts header contains the following fields which must match to add the detail lines to an existing receipt.

- Fields

- Company_Code

- Batch_Code

- Customer_Code

- Transaction_Code

- Reference_Number

- Reference_Date

- ABA_Number

- Cost_Center_Header (if applicable)

- If a mismatch exists between the Reference_Number and the existing transaction fields it won't be added. Solution is to change the Reference_Number to be unique.

- If the Customer_Code is defined then the following fields will be ignored if defined because they are used for non-customer entries:

- Payer_Name

- Misc_Cash_Remarks

- GL_Account

- Remarks

- Job_Number

- Phase_Code

- Cost_Type

- Equipment_Code

- Cost_Category_Code

- PM_Work_Order

- If the Customer_Code is NOT defined and the following fields are defined then it will review the Open items to default the Customer Code:

- Invoice_Number

- Invoice_Type

- The Transaction_Amount field is the Total Check amount and Payment_Amount is the individual Invoice paid amounts.

- If the total Transaction amount exceeds the Payment amount for the same Customer Header fields (see list above) then an over payment record will be created for the Customer.

- The Transaction amount field cannot be less than the Payment amount records.

- Based on the defined Transaction code, it controls whether the value is positive or negative and if an overpayment can be created. Positive transactions can be created.

- The Invoice_Type defines the type of transaction being made.

- I = Invoice

- This allows you to define a specific amount to be paid to an Invoice.

- Negative amounts are allowed.

- Invoice_Number is required when used.

- If the Transaction_Amount field is greater than the Payment_Amount field then an overpayment will automatically be created during the standard Update Processing. It will not appear on the Spectrum entry screen.

- C = Credit Memo

- This allows you to define a specific amount to be paid to a Credit Memo.

- Negative amounts are allowed.

- R = Retention

- This allows you to define a specific amount to be paid to open customer items that have retention.

- Negative amounts are allowed.

- Invoice_Number is required when used.

- P = Payment

- This allows you to make an Overpayment/Prepayment to the Customer.

- This transaction type can be used to apply payments directly to customer accounts.

- The Transaction_Amount field is required and must match the Payment_Amount field.

- If the Payment_Amount is blank, then it will assume the Transaction Amount is the payment amount.

- The web service allows the user to make overpayments using one of the following methods:

- It can be defined in the record using the Invoice_Type of P (see notes above).

- It can be automatically created when the Transaction_Amount exceeds the Payment_Amount fields using the Invoice_Type of I (see notes above).

- This web service will keep a running total of individual payment amounts to calculate the transaction amount. Transactions are posted one at a time, meaning that if an invoice amount is greater than the header transaction amount but the overall payment balances because of negatives, the invoice with the greater amount MUST be posted last, otherwise it will return an error for insufficient amount.

- The Misc_Cash_Remarks and Remark fields will be truncated if they exceed the Max character length.

- Cost center information will only be allowed if the Company is set to a Yes status.

- The transaction data being submitted using this web service are stored within the Cash Receipts / Adjustment Entry screen; the data must be manually updated within Spectrum.

- This web service will not work for customers using multi-currency.

## Field Descriptions

Use the table below for reference when using this service.
Excel
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

B
Company_Code
Company Code
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Batch_Code
Batch Code
YES
Text
10

D
Customer_Code
Customer Code
Text
10
Customer must have an Active or Inactive status. Field is blank for non-customer cash receipts. ** See Assumptions and Dependencies.
Customer File Maintenance

E
Transaction_Code
Transaction Code
Text
10
Transaction Code File Maintenance

F
Reference_Number
Check # (Reference)
Text
10
Required for payment type Transaction codes.
Must be unique Customer_Code and Reference_Number

G
Reference_Date
G/L date
Date
10
If blank, defaults to current AR Processing date.
Must be within the AR Processing dates.

H
Transaction_Amount
Amount (Check)
Numeric
14
Amount of the total check and used for validation.
** See Assumptions and Dependencies.

I
ABA_Number
ABA routing #
Text
10
Cannot exceed 8 characters

J
Invoice_Number
Invoice #
Text
10
Required for customer specific transactions.
Invoice must be an Open Item for the Customer.

K
Invoice_Type
Transaction
Text
1
(I)nvoice, (C)redit Memo, (P)ayment or (R)etention portion for customer-specific transactions. Blank for non-customer.
** See Assumptions and Dependencies.

L
Payment_Amount
Applied Amount (Detail line)
Numeric
14
Amount for individual payments. If blank for a payment then will use the defined Transaction Amount.

M
Discount_Taken
Discount Taken
Numeric
14
Allows negatives. Cannot exceed Invoice Total.

N
Cost_Center_Header
Cost Center (header)
Numeric
10
Cost Center Maintenance

O
Payer_Name
Payer
Text
30
Used for non-customer entries only.

P
Misc_Cash_Remark
Remarks-Header
Text
100
Used for non-customer entries only.

Q
GL_Account
G/L account
Numeric
12
Used for non-customer entries only. Required if Customer_Code is blank. No dashes.
GL_Account cannot be a 'direct work order cost' code.

R
Remark
Remarks-Detail
Text
100
Used for non-customer entries only.

S
Job_Number
Job
Text
10
Used for non-customer entries only.
Jobs

T
Phase_Code
Phase
Text
20
Used for non-customer entries only. No dashes.
Phases

U
Cost_Type
Cost type
Text
3
Used for non-customer entries only.
Cost Type

V
Equipment_Code
Equipment Code
Text
10
Used for non-customer entries only.
Equipment Master File

W
Cost_Category_Code
Equipment Cost Category
Text
4
Used for non-customer entries only.
Equipment Cost Categories

X
PM_Work_Order
Equipment W/O
Text
10
Used for non-customer entries only.
Equipment Item must exist on the Equipment Work Order for required or optional settings.

Y
Cost_Center_Detail
Cost Center (detail)
Numeric
10
Used for non-customer entries only. Defaults based on cost center hierarchy for GL Account logic.
Cost Center Maintenance

Z
Overpayment_Flag
Flag for negative payments and invoice overpayments
Text
1
'Y'(es) or 'N'(o) only
