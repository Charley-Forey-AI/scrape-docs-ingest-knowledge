---
title: "Add Subcontract | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-subcontract"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-subcontract"
---

# Add Subcontract

Use this service to add or update existing Subcontract information for the defined fields only.
WSDL: UpdateSubcontract.jws
Method: UpdateSubcontract
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Subcontract information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Subcontract

- System Administration > Installation > Accounts Payable > Vendor File Maintenance

- System Administration > Installation > Job Cost

- System
 AdministrationInstallationJob
 CostJobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation >  General Ledger > G/L Master File Maintenance

## Assumptions and Dependencies

- The Subcontract Web Service adds or updates existing Subcontract information for the defined fields only.

- The unique combination of the Vendor code and Subcontract number must exist in the defined Company code to change the data provided.

- The following fields are required when creating a new Subcontract record.

- Company_Code

- Vendor_Code

- Subcontract_Number

- Job_Number

- GL_Account

- The following fields are required to change an existing Subcontract record.

- Company_Code

- Vendor_Code

- Subcontract_Number

- If the Job_Number is defined it must be valid for the above data.

- The Date_Issued field must exist within the Fiscal Calendar and will default to the current processing date if left blank.

- In order to override the Vendor defaults for the Payment terms or the Discount terms their associated Override options must be defined as Y. The web service will only change the data if the override is marked with a Y.

- The Contact_Person field is not associated with the Spectrum Contacts. It is a text field for the Subcontract only.

- The standard Module Installation options will be used to create the Subcontract.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- Cost center information will only be allowed in if the Company is set to a Yes status.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
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
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Vendor_Code
Vendor Code
YES
Text
10
Vendor

D
Subcontract_Number
Subcontract Number
YES
Text
10
No duplicate combination of Vendor and Subcontract number.

E
Job_Number
Job
Text
10
Required for new record only. The Job cannot be changed on an existing Subcontract.
Jobs

F
Default_Phase_Code
Phase
Text
20
No dashes.
Phases

G
Default_Cost_Type
Cost type
Text
3
Cost Type

H
Status_Code
Status
Text
1
(A)ctive, (I)nactive or (C )omplete. If blank then default to Active when creating a new record.

I
Contract_Type
Contract type
Text
15

J
Insurance_Cert_Flag
Insurance
Text
1
(Y)es, (N)o or (A)for not applicable. Defaults from Vendor if blank.

K
Sent_Date
Date sent
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

L
Date_Issued
Date issued
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). Defaults to current processing date if blank.
Fiscal Calendar must exist.

M
Contact_Person
Contact
Text
20
Not part of the Contact Master in Spectrum.

N
Unit_Price_Flag
Unit price contract?
Text
1
(Y)es or (N)o. Defaults as yes if Unit Price Job. Defaults to N if blank.

O
Comment
Comment
Text
120

P
Routing_Code1
Invoice approval default routing code
Text
10
Routing Code Maintenance

Q
Routing_Limit
Invoice approval invoice dollar limit
Numeric
13
Positive numbers only. Format = -10.2

R
Routing_Code2
Invoice approval routing code over limit
Text
10
Routing Code Maintenance

S
GL_Account
GL Account
Numeric
12
Required when creating a new Subcontract. The GL Account code must be a direct Job cost account.
G/L Master File Maintenance

T
Retention_Percent
Invoice default Retention %
Numeric
5
Enter 10.2% as 10.2. Positive numbers only. Format = 2.1

U
Next_Payment_Number
Invoice default next payment
Numeric
5
Positive numbers only. Defaults to 1 if adding a new subcontract.

V
Pay_Override
Override standard vendor payment terms?
Text
1
Enter (Y)es to override. Defaults to N if blank.

W
Pay_Terms
Payment due Based on
Text
1
Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.
Defaults from Vendor, if Pay_Override is not a Y.

X
Pay_Days
Payment Due - number of days
Numeric
3
Positive numbers only.
Defaults from Vendor, if Pay_Override is not a Y.

Y
Disc_Override
Override standard vendor discount terms?
Text
1
Enter (Y)es to override. Defaults to N if blank.

Z
Disc_Terms
Discount due based on
Text
1
Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.
Defaults from Vendor, if Disc_Override is not a Y.

AA
Disc_Days
Discount due - number of days
Numeric
3
Positive numbers only.
Defaults from Vendor, if Disc_Override is not a Y.

AB
Disc_Perc
Discount %
Numeric
6
Enter 10.25% as 10.25. Positive numbers only.
Defaults from Vendor, if Disc_Override is not a Y.

AC
Pay_When_Paid
Pay invoices based on customer payment?
Text
1
Enter (Y)es or (N)o. Defaults to N if blank.
Pay_Override field must be defined as Y to change this field to Yes.

AD
Cost_Center_Override
Override cost center company
Numeric
10
Cost center must be a valid number and the Cost center company must be valid.
