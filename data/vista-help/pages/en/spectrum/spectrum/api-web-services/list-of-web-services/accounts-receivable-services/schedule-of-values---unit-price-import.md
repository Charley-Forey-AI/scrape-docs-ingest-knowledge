---
title: "Schedule of Values - Unit Price Import | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/schedule-of-values---unit-price-import"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/schedule-of-values---unit-price-import"
---

# Schedule of Values - Unit Price Import

Use this service to import Schedule of Values information for Unit Price billings.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/contract/scheduleofvalues
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Underlying File Maintenance

Prior to importing Schedule of Values information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contract

- System Administration > Installation > Accounts Receivable > Online Tax Code

- System Administration > Installation > Accounts Receivable > Set Up Standard Unit Billing Items

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

## Assumptions and Dependencies

- The service will sum up all 'Original_Amount' columns and the total must tie to the 'Original contract' amount in Contract Main Properties.

- Only (A)ctive and (I)nactive Customer codes are allowed.

- Only (A)ctive and (I)nactive Job codes are allowed.

- Only (A)ctive and (I)nactive G/L codes are allowed.

- The import will error out when the contract has information defined in the G/L Distribution for Draw Request Invoices window. When such allocation is required, first import the schedule of values and then enter the allocation percentages.

- Customer must have security to entered cost enter. Only (A)ctive cost centers are allowed.

- When the bill item is found in 'Set Up Standard Unit Billing Items' and the following fields are left blank, default the following in from the standard list:

- Group Description

- Billing Description

- Additional Billing Description

- G/L Account Code

- Online Tax Code

- The product of Billing_Unit_Price and Bid_Quantity cannot exceed $9.9 billion.

- The product of Billing_Unit_Price and Projected_Quantity cannot exceed $9.9 billion

## Sample JSON Body

```
`{
 "contracts": [
 {
 "Company_Code": "XYZ",
 "Customer_Code": "DF001",
 "Job_Number": "DF001",
 "Schedule_Of_Values_Unit": [
 {
 "Group_Code": "01",
 "Group_Description": "Group 01",
 "Billing_Item": "01",
 "Billing_Description": "Item 01",
 "Additional_Billing_Description": "00001",
 "GL_Account": "3405",
 "Taxable": "Y",
 "Unit_Of_Measure": "HR",
 "Billing_Unit_Price": 200,
 "Original_Quantity": 12,
 "Original_Amount": 2400,
 "Projected_Quantity": 12.12,
 "Projected_Revenue": 2424,
 "Memo": "Memo Memo Memo",
 "Cost_Center": "",
 "Online_Tax_Code": ""
 },
 {
 "Group_Code": "02",
 "Group_Description": "Group 02",
 "Billing_Item": "02",
 "Billing_Description": "Item 02",
 "Additional_Billing_Description": "Add'l Description 02",
 "GL_Account": "",
 "Taxable": "N",
 "Unit_Of_Measure": "LF",
 "Billing_Unit_Price": 20.12,
 "Original_Quantity": 100,
 "Original_Amount": 2012,
 "Projected_Quantity": 0,
 "Projected_Revenue": 0,
 "Memo": "",
 "Cost_Center": "",
 "Online_Tax_Code": ""
 }
 ]
 }
 ]
}`
```

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36**See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CCustomer_CodeCustomer CodeYESText10**See Assumptions and Dependencies.Customer Master File
DJob_NumberJob NumberYESText10**See Assumptions and Dependencies.Job Master File
EGroup_CodeGroup CodeYESText2
FGroup_DescriptionGroup DescriptionText30**See Assumptions and Dependencies.
GBilling_ItemBilling ItemYESText10
HBilling_DescriptionBilling DescriptionText30**See Assumptions and Dependencies.
IAdditional_Billing _DescriptionAdditional Billing DescriptionText40**See Assumptions and Dependencies.
JGL_AccountG/L Account CodeNumeric12**See Assumptions and Dependencies. No dashesG/L Master File
KTaxableTaxable?Text1(Y)es or (N)oDefaults from Contract Master File if left Blank
LUnit_of_MeasureUnit of MeasureText3
MBilling_Unit_PriceUnit PriceNumeric10**See Assumptions and Dependencies.
NOriginal_QuantityOriginal QuantityNumeric10**See Assumptions and Dependencies.
OOriginal_AmountOriginal AmountNumeric10.2**See Assumptions and Dependencies
PProjected_QuantityProjected QuantityNumeric10**See Assumptions and Dependencies.
QProjected_RevenueProjected RevenueNumeric10.2**See Assumptions and Dependencies.
RMemoMemoText25
SCost_CenterCost CenterText10**See Assumptions and Dependencies.Cost Center Maintenance; G/L Account Cost Center; Job Cost Center, Customer Cost Center
TOnline_Tax_CodeOnline Tax CodeText15
