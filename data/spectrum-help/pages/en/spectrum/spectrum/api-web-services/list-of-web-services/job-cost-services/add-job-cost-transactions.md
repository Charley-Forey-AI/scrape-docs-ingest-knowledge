---
title: "Add Job Cost Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job-cost-transactions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job-cost-transactions"
---

# Add Job Cost Transactions

Use this service to import Job Cost Transaction information.
WSDL: AddJCTrans.jws
Method: AddJCTrans
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Job Cost Transaction information, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Transaction Type defaults to JC for Job Cost
 Transactions.

- The combination of the Tran_Date and Batch_Code will be used to define the group of transactions to be stored together in that batch.

- Each group or batch can contain a maximum number of 9000 records. The user must define the combination of the Tran_Date and Batch_Code for each record submitted and control the number of records.

- If the combination already exists within Spectrum, the records will be added to the batch until the record count reaches the maximum limit.

- Once the limit is reached, an error is sent and the Web Service will stop to allow the user to review the remaining records.

- If Post to job cost history in detail? checkbox
 selected in the Cost Type File Maintenance screen, then it will
 post transactions in detail. If it is cleared, it will summarize the transactions by the
 Reference number.

- The Job Cost Installation defines the phase mask and fill option which are used to validate the phases.

- Define unique batch codes for groups of records for easy balancing to eliminate duplicate table keys in Spectrum.

- Cost center companies need to supply the credit cost center for the General Ledger code. The Debit General Ledger cost center defaults from the Job phase or Job depending on the hierarchy for cost centers.

- Cost center information will only be allowed if the
 Company is set to a Yes status.

- The transaction data being submitted using this web service are stored within
 the Job Cost Transaction Entry screen; the data must manually be
 updated within Spectrum.

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
Valid Company in Spectrum

C
Tran_Date
Transaction Date
YES
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)
Within Fiscal Year Calendar and Job Cost Processing Date Range

D
Batch_Code
Batch Code
YES
Text
10
Recommend using a unique batch code to keep them separate while validating and updating Job Cost Transactions.
Limit the 'Batch Code/Tran Date' quantity of Record to 9000.

E
Reference_1
Reference Number
YES
Text
15
Needs to be unique if detail transactions are needed. If not it will summarize the same Reference numbers into one record as defined on the Cost Type File Maintenance.

F
Description
Description
Text
30

G
Job_Number
Job Number
YES
Text
10
Jobs

H
Phase_Code
Phase Code
YES
Text
20
No dashes.
Job Phases

I
Cost_Type
Cost Type
YES
Text
3
Cost Type File Maintenance defines how transactions are posted--Detail or Summary--based on the Reference Number
Cost Type File Maintenance and Job Phases

J
Total_Hours
Hours
Numeric
10
 Negative numbers are allowed. Enter (-) at the beginning of the number

K
Tran_Amount
Amount
YES
Numeric
12
 Negative numbers are allowed. Enter (-) at the beginning of the number.

L
GL_Debit_Account
Debit G/L Code
YES
Text
12
G/L Account code must be a direct job cost account. No dashes.
G/L Master File Maintenance

M
GL_Credit_Account
Credit G/L Code
YES
Text
12
G/L Account code must be a non-direct cost account. No dashes.
G/L Master File Maintenance

N
Cost_Center_Credit
Credit Cost Center
Text
10
Credit Cost Center only.
Cost Center Maintenance; Phase Cost Center, Job Cost Center and G/L Account Cost Center
