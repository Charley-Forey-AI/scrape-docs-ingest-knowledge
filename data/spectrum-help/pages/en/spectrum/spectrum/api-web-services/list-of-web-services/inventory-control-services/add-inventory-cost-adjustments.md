---
title: "Add Inventory Cost Adjustments | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-cost-adjustments"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-cost-adjustments"
---

# Add Inventory Cost Adjustments

Use this service to import Inventory Cost Adjustments information.
WSDL: AddInventoryCostAdjustments.jws
Method: AddInventoryCostAdjustments
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Inventory Cost Adjustments information, the following file maintenance areas must be completed:

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > Item Main Properties

- System Administration > Installation > Inventory Control > Item Warehouse Details

- System Administration > Installation > Inventory Control > Warehouse File Maintenance

- System Administration > Installation > Inventory Control > G/L Department Maintenance

- System Administration > Installation > Inventory Control > Cost Adjustment Source Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

## Assumptions and Dependencies

- The Web Service will not support the following logic:

- Items with a 'Not Used' status

- Warehouses that have a physical inventory in progress

- The Web Service follows the majority of the same logic as manually entering Inventory Cost Adjustments, with the exceptions of the data defined here. The Spectrum Help Files can be used for troubleshooting errors along with the details defined here.

- The Transaction Type for all imported transactions will be 'Cost Adjustment'

- The import has a record limit of 990 records per Transaction_Reference

- The inventory item must exist in the defined warehouse

- If Transaction_Reference is blank in the Web Service, then the following logic will apply:

- If a Transaction_Reference exists within the unposted Inventory transaction table then the web service will add additional records until it reaches the 990 record limits then create additional Transaction_Reference as needed. A numeric type Transaction_Reference will be added to first then followed by any alpha type Transaction_Reference that exists.

- If a Transaction_Reference does not exist within the unposted Inventory transaction table then the web service will follow standard Spectrum logic and create auto-assigned reference numbers

- The Cost Adjustment amount must be non-zero and within the qualifying range, based on the Extended Cost of the item in the defined warehouse:

- Following recognition of the imported entry, Cost adjustment amount cannot result in the total extended cost being negative (for example, negative adjustment amount cannot exceed the current valuation in the warehouse)

- The GL_Credit_Account field defaults from the GL_Department field if left blank and must be a non-direct cost account.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
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

B
Company_Code
Company code
YES
Text
3
Valid company in Spectrum

C
Batch_Code
Batch code
YES
Text
10
If the Batch code exists then records will be added to the existing batch code and Reference # group
** See Assumptions and Dependencies

D
Transaction_Reference
Reference #
Text
7
Reference # must not be in use or been used. Limit of 990 records per Reference #
** See Assumptions and Dependencies

E
Transaction_Date
Transaction date
YES
Date
10
MM/DD/YYYY Format
Must be within Inventory Control Processing date range

F
From_Warehouse
Warehouse
YES
Text
10
Valid warehouse code in Spectrum

G
Item_Code
Item code
YES
Text
15
Item must be a valid combination of Inventory Item and Warehouse code
Valid item code in Spectrum, with a status other than 'Not used'

H
Extended_Cost
Cost adjustment amount
YES
Num
10
Format = -6.2
** See Assumptions and Dependencies

I
Source_Code
YES
Text
2
Valid Source code in Spectrum

J
GL_Department
Department
YES
Text
4
Valid G/L Department code in Spectrum

K
Reason
Message
Text
30

L
GL_Credit_Account
G/L credit account
Num
12
Defaults from Inventory G/L Department if left blank. Must be a non-direct cost account
Valid G/L account code in Spectrum, with a status other than 'Not used'
