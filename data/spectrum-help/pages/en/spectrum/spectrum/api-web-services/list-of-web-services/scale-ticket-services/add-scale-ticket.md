---
title: "Add Scale Ticket | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/scale-ticket-services/add-scale-ticket"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/scale-ticket-services/add-scale-ticket"
---

# Add Scale Ticket

Use this service to import Scale Ticket information.
WSDL: AddScaleTicket.jws
Method: AddScaleTicket
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Field Descriptions

Use the table below for reference when using this service.
Element Name
Description
Req?
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

Company_Code
Company code
YES
Text
3
Valid company in Spectrum

Plant_Code
Plant / Pit
YES
Text
5
Valid plant / pit code must exist in the defined company

Customer_Code
Customer Code
Text
10
Valid customer code must exist in the defined company

Job_Number
Job Code
Text
10
Valid job code must exist in Job Company, if defined, and otherwise in the Spectrum company defined on the ticket

To_Warehouse
To Warehouse
Text
10
Ignore this field unless both Job and Customer are blank or invalid
Valid warehouse code must exist in the defined company

Ticket_Number
Ticket #
YES
Text
15
Cannot already exist for define Plant / Pit

Ticket_Date
Ticket Date
Date
10
Format = MM/DD/CCYY
If left blank, assign current M/M processing date

Ticket_Time
Ticket Time
Num
6
Format HHMMSS
Hours cannot exceed 24, minutes and seconds cannot exceed 59.

Item_Code
Item Code
YES
Text
15
Valid item code must exist in the defined company
Status cannot be 'Not Used'

Ticket_Net_Weight
Net Quantity
Num
13
Max allowable value = 9,999,999.99 (commas optional)
Disallow negative value

Sell_Price
Sell Price
Num
16
Max allowable value = 99,999,999.9999 (commas optional)

Freight_Charge
Freight Charge
Num
14
Maximum allowable price = 99,999,999.99 (commas optional)

Misc_Charges
Misc Charge
Num
14
Maximum allowable price = 99,999,999.99 (commas optional)

Sales_Tax_Code
Sales Tax Code
Text
15
Required for Customer ticket
Valid A/R sales tax code must exist in the defined company

Sales_Tax_Amount
Sales Tax Amount
Num
14
Maximum allowable price = 99,999,999.99 (commas optional)

Area_Code
Area / Customer's Job
Text
10
For a Job ticket, valid area code must exist in the defined company.
For a customer ticket, valid 'customer job' must exist for the Customer Code in the defined company.

Phase_Code
Phase Code
Text
20
No dashes
Required for Job ticket

Cost_Type
Cost Type
Text
3
Required for Job ticket
Valid Phase Code + Cost Type Code combination for the Job Code must exist in the Job's company
Phase Code + Cost Type Code cannot be 'Completed'

Truck_Code
Truck #
Text
10
Valid truck code must exist in the defined company

Hauler_Code
Hauler
Text
10
Valid hauler code must exist in the defined company

PO_Number
Customer P.O.
Text
10

Salesman
Salesperson
Text
3
Valid salesperson code must exist in the defined company

Message
Message
Text
30

Batch_Code
Batch Code
Text
10
If left blank, assign Operator code (from Authorization_ID)
