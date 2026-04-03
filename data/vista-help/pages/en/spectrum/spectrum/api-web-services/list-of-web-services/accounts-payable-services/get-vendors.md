---
title: "Get Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/get-vendors"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/get-vendors"
---

# Get Vendors

Use this service to get active vendors from Spectrum.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/vendors/Company_Code
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: GET

## Underlying File Maintenance

- Accounts Payable > Vendor File Maintenance

- Accounts Payable > Vendor Locations

## Assumptions and Dependencies

- Only active vendors are returned.

## Parameter Fields

If you want to filter by items such as state or city, pCostCenter is a required parameter.
Important: If you're using Postman, send the filter parameters as part of the query parameters.
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36
pCompany_CodeCompany CodeYESText 3Valid Company in SpectrumDefaults from the Authorization ID if not populated
pTypeVendor TypeText6
pCityVendor CityText25
pStateVendor StateText2
pNameVendor NameText30
pCostCenterCost CentersText3Specific cost center or 'ALL'

## Return Fields

Element NameDescriptionReqTypeMaxFormatValidation
Company_CodeCompany CodeText3Valid Spectrum Company
Vendor_CodeVendor CodeText10Vendor File Maintenance
NameVendor NameText30Vendor File Maintenance or Vendor Location Maintenance
Address_1Address 1Text30Vendor File Maintenance or Vendor Location Maintenance
Address_2Address 2Text30Vendor File Maintenance or Vendor Location Maintenance
CityCityText30Vendor File Maintenance or Vendor Location Maintenance
StateState / ProvinceText2Vendor File Maintenance or Vendor Location Maintenance
Zip_CodePostal CodeText10Vendor File Maintenance or Vendor Location Maintenance
First_NamePrimary Contact First NameText20Contact Master
Last_NamePrimary Contact Last NameText30Contact Master
Phone_NumberPrimary Contact PhoneText14Primary phone defined for Contact Master
 EmailPrimary Contact EmailText80Email defined for Contact Master
Account_Reference Account ReferenceText25Vendor File Maintenance
Payment_TermsPayment Due TermsText1When A = Invoice Date. When B = Prox Terms
Payment_Term_Days Payment Number of DaysNumeric12
Discount_Terms Discount TermsText1When A = Invoice Date. When B = Prox Terms
Discount_Term_Days Discount Number of DaysNumeric12
Discount_Percent  Discount PercentNumeric3.2
Purchase_Location_Name Purchase LocationText30Locations
Purchase_Address_1 Text30Locations
Purchase_Address_2 Text30Locations
Purchase_City Text30Locations
Purchase_State Text2Locations
Purchase_Zip Numeric10Locations
Payment_Location_Name Payment LocationText30Locations
Payment_Address_1 Text30Locations
Payment_Address_2 Text30Locations
Purchase_City Text30Locations
Purchase_State Text2Locations
Purchase_Zip Numeric10Locations
