---
title: "Get Customers | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/get-customers"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/get-customers"
---

# Get Customers

Use this service to import Get Customers information.
WSDL: GetCustomers.jws
Method: GetCustomers
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Use these tables for reference when using this service.

## Parameter Field Descriptions

Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
Element NameDescriptionReq?TypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
pCompany_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from Authorization ID if not populated.
pStatusCustomer StatusText3Leave blank for 'Active' only, or 'I' to include both Active and Inactive customers, or 'ALL' to include all customers

## Return Field Descriptions

Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Customer_CodeCustomer CodeText10Customer File Maintenance
NameCustomer NameText30Customer File Maintenance
Address_1Address 1Text30Customer File Maintenance
Address_2Address 2Text30Customer File Maintenance
CityCityText25Customer File Maintenance
StateState / ProvinceText2Customer File Maintenance
Zip_CodePostal CodeText10Customer File Maintenance
First_NamePrimary Contact First NameText20Contact Master
Last_NamePrimary Contact Last NameText30Contact Master
Phone_NumberPrimary Contact TelephoneText14Primary phone defined for Contact Master
Email1Primary Contact EmailText80Email1 defined for Contact Master
Price_Level_MaterialStandard Material Price LevelNum1Customer File Maintenance (1-5 or blank)
Taxable_FlagStandard Tax StatusText11Customer File Maintenance ('Taxable' or 'Non-Taxable' or 'No Default')
StatusCustomer StatusText8Customer File Maintenance ('Active' or 'Inactive' or 'Not Used')
