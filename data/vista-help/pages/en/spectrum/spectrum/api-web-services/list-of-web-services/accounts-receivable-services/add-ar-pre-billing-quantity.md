---
title: "Add AR Pre Billing Quantity | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-pre-billing-quantity"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-pre-billing-quantity"
---

# Add AR Pre Billing Quantity

Use this service to import Accounts Receivable Pre-Billing Quantity information.
WSDL: ARPreBillingQuantity.jws
Method: ARPreBillingQuantity
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing AR Pre-Billing Quantity information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Job Cost

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contracts

- System Administration > Installation > Accounts Receivable > Contracts > Schedule of Values

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The AR Pre-Billing Quantity web service will add or update to the existing unique combination of Job number, Customer and Batch code defined. If it does not exist then it will be created.

- A Billing Item exists on the Schedule of Values for the Contract. The type of Job defines how the billing item will be defined in the layout.

- Unit Price contract require both the billing group and billing items to be defined with a max number of 10 characters between the two fields.

- Fixed Price contracts require only the billing item field be populated in the layout with a max number of 10 characters. The Billing_Group_Code field will be ignored if defined.

- The Web Service will not create new Billing Item automatically. The Billing Item must exist on the Contract.

- Quantity Type field will default from the Accounts Receivable Installation screen based on the data defined on the Draw Request Tab.

- Quantity field

- The Site Map > System Administration > Installation > Accounts Receivable > Draw Request screen controls whether the Pre-Billing Quantities are enter for the
 Period or Job-to-Date.

- Based on your installation setting and the 'Unit of Measure's' price method defined on a Unit Price Contract, the 'Quantity' field can have one of the following formats -

- -9.2

- -8.2

- -7.2

- -3.2

- For Unit Price jobs, the quantity defined multiplied by the unit price on the Contract will override the records defined Amount.

- For non-unit price jobs this field is considered a percentage and is calculates as a percentage of the Amount divided by the Bid $ Amount field value.

- Amount field

- If the field is defined for a non-unit price job then this value will be used in the transaction.

- If this field is defined for a unit price job along with the Quantity value and the Amount value based on the defined Quantity multiplied by the Unit Price on the Contract does not match then the calculated value will used.

- To change data for an existing entry then the following fields must exist-

- Job_Number

- Customer_Code

- Batch_Code

- Billing_Group_Code

- Billing_Item_Code

- Quantity_Date

- Quantity_Type

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The transaction data being submitted using this web service are stored within the Customer AR Pre-Billing Quantity screen; the data must be manually updated within Spectrum.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
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
Job_Number
Job
YES
Text
10
Unique combination of Job and Customer must exist. ** See Assumption and Dependencies.
Job

D
Customer_Code
Customer
YES
Text
10
Unique combination of Job and Customer must exist. ** See Assumption and Dependencies.
Customer

E
Batch_Code
Batch code
YES
Text
10
If Job, Customer and Batch combination exists add to the existing batch.

F
Billing_Group_Code
Billing Group
Text
2
Define the CO_Billing_Group_Code and CO_Billing_Item_Code for Unit Price jobs. ** See Assumptions and Dependencies.
Contract Schedule of Value

G
Billing_Item_Code
Billing Item
YES
Text
10
For Fixed Price Jobs define the Billing Item and leave the CO_Billing_Group_Code blank. See Assumptions and Dependencies.
Contract Schedule of Value

H
Quantity_Date
Date
Date
10
If left blank then use system date. Enter as: MM/DD/CCYY (e.g.: 01/05/2011)

I
Quantity_Type
Type
Text
1
(A)ctual or (E )ngineering. If blank then will default from the AR Installation screen.
Installation screen default

J
Quantity
Quantity
Numeric
10
Allows negative numbers. ** See Assumption and Dependencies.

K
Amount
Amount
Numeric
13
Allows negative numbers. Format = -9.2 If defined then the Quantity value is recalculated. If blank then calculated for unit price jobs. ** See Assumption and Dependencies.
