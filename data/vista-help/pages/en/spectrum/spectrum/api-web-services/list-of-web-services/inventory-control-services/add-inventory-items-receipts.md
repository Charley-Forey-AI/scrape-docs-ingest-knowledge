---
title: "Add Inventory Items Receipts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-items-receipts"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-items-receipts"
---

# Add Inventory Items Receipts

Use this service to import Inventory Receipts Transaction information.
WSDL: AddInv_Receipt.jws
Method: AddInv_Receipt
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Inventory Receipts Transaction information, the following file maintenance screens must be completed:

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > G/L Department File Maintenance

- System Administration > Installation > Inventory Control > Warehouse File Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

## Assumptions and Dependencies

- The Transaction Type will default to 'Receipt' only.

- The import has a record limit of 990 records per Transaction_Reference.

- The Inventory Item must exist for the defined warehouse.

- The Transaction_Reference must not exist in the Inventory Transaction History table.

- If the Transaction_Reference is blank in the web service then the following logic will apply.

- If a Transaction_Reference exists within the unposted Inventory transaction table then the web service will add additional records until it reaches the 990 record limits then create additional Transaction_Reference as needed. A numeric type Transaction_Reference will be added to first then followed by any alpha type Transaction_Reference that exists.

- If a Transaction_Reference does not exist within the unposted Inventory transaction table then the web service will follow standard Spectrum logic and create auto-assigned reference numbers.

- GL_Credit_Account field defaults from the GL_Department field if left blank and must be a non-direct cost account.

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
Valid Company in Spectrum.

C
Batch_Code
Batch Code
YES
Text
10
If the Batch code exists then records will be added to the existing Batch code and Reference # group.
** See Assumptions and Dependencies.

D
Transaction_Reference
Reference #
Text
7
Reference # must not be in use or been used. Limit of 990 records per Reference #.
** See Assumptions and Dependencies.

E
Transaction_Date
Transaction Date
YES
Date
10
MM/DD/YYYY format.
Must be within Inventory Control Processing Date Range

F
From_Warehouse
Warehouse
YES
Text
10
Warehouse Maintenance file

G
Item_Code
Item Code
YES
Text
15
Item must be a valid combination of Inventory Item & Warehouse Code.
Inventory Item Warehouse Maintenance file.

H
Transaction_Quantity
Quantity
YES
Numeric
9
Positive numbers only. Format = 6.2

I
Unit_Cost
Unit Cost
YES
Numeric
10
Positive numbers only. Format = 5.4

J
GL_Department
Department
YES
Text
4
Inventory G/L Department Maintenance file

K
Reason
Message
Text
30

L
GL_Credit_Account
GL Credit Account
Numeric
12
Defaults from Inventory GL Department if left blank. Must be a non-direct cost account.
GL Account Master
