---
title: "Wire Transfer - Bank Transfer | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/cash-management-services/wire-transfer---bank-transfer"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/cash-management-services/wire-transfer---bank-transfer"
---

# Wire Transfer - Bank Transfer

Use this service to import wire transfer bank transfer information.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/cashmanagement/wiretransfer

Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST

Supported formats: JSON

## Underlying File Maintenance

Prior to importing wire transfers, the following file maintenance areas must be completed:

- Cash Management > Installation

- Cash Management > Accounts

- General Ledger > G/L Department File Maintenance

- General Ledger > G/L Master File Maintenance

- Enterprise Management > Cost Center Maintenance (if applicable)

## Assumptions and Dependencies

- If the Company_Code is blank, then use the Authorization ID default value.

- The Transfer_Type field will be available when using a Postman service to import data, but will not be available on the Excel spreadsheet.

- The sum of the Payment_Amount details must tie to the Wire_Transfer value.

- When importing multiple wire transfers at the same time with the template, ALL header fields (company code, bank account, cost center, date and wire amount) must match and the details must sum to the wire amount.

- Blank wire number is acceptable and will auto-assign based on CM Account maintenance.

- With multiple detail rows, the last memo field used will be entered onto the transaction.

- If more than one wire transfer has the SAME header fields and SAME Wire_Amount, the template will return an error. In this case, the user must separate the imports or include wire numbers in the import.

## Sample JSON Body - Bank Transfer

```
`{
 "wireTransfers": [
 {
 "Company_Code": "2ND",
 "Bank_Account": "DF001",
 "Wire_Number": "9",
 "Transfer_Type": "B",
 "Cost_Center": "DF001",
 "GL_Transaction_Date": "05/05/2019",
 "Wire_Amount": 1000.00,
 "Memo": "Thanks for the memo",
 "Bank_Transfers": [
 {
 "To_Company_Code": "2ND",
 "To_Bank_Account": "000005",
 "Transfer_Amount": 900.00,
 "To_Cost_Center": "DF001"
 },
 {
 "To_Company_Code": "2ND",
 "To_Bank_Account": "000005",
 "Transfer_Amount": 100.00,
 "To_Cost_Center": "DF001"
 }
 ]
 }
 ]
}`
```

## Sample JSON Body - Payment to Third Party

```
`{
 "wireTransfers": [
 {
 "Company_Code": "2ND",
 "Bank_Account": "DF001",
 "Wire_Number": "9",
 "Transfer_Type": "P",
 "Cost_Center": "DF001",
 "GL_Transaction_Date": "05/05/2019",
 "Wire_Amount": 1000.00,
 "Memo": "Thanks for the memo",
 "Payments": [
 {
 "To_Company_Code": "2ND",
 "GL_Account": "000005",
 "Payment_Amount": 900.00,
 "To_Cost_Center": "DF001"
 },
 {
 "To_Company_Code": "2ND",
 "GL_Account": "000005",
 "Payment_Amount": 100.00,
 "To_Cost_Center": "DF001"
 }
 ]
 }
 ]
}`
```

## Field Descriptions

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
YES
 Alpha
 3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Bank_Account
Bank Account
YES
Alpha
10
Valid bank account in Cash Management.

D
Wire_#
Wire #
Numeric
5
Must be an unused number.

Transfer_Type
Transfer Type
YES
Alpha
1
(B)ank or (P)ayment
** See Assumptions and Dependencies.

E
Cost_Center
Cost Center
Text
10
Active cost center.

F
GL_Transaction_Date
G/L Transaction Date
YES
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)

G
Wire_Amount
Wire Amount
Numeric
12.2
Positive amounts only.

H
Memo
Memo
Alpha
50

I
To_Company
Company
YES
Alpha
3
Valid company in Spectrum.

J
To_Bank_Account
Bank Account
YES
Alpha
10
For transfers to bank accounts
KGL_AccountG/L AccountYESNumeric12Valid G/L code. For payments to third party.
L
Payment_Amount
Payment amount
YES
Numeric
12.2
Sum of details must tie to Wire_Amount.

M
Cost_Center
Cost Center
Alpha
10
Active cost center
