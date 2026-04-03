---
title: "Update Hold Status | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-hold-status"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-hold-status"
---

# Update Hold Status

Use this service to remove the Hold Status on invoices sent from another application into Spectrum.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/vendorInvoice/updateAPInvoiceHoldFlag
[Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "aPInvoiceHoldFlagImports": [
 {
 "Company_Code": "2nd",
 "Vendor_Code": "456gar",
 "Invoice_Number": "111",
 "Invoice_Type_Code": "I"
 "Selection_Flag": "H"
 }
 ]
}`
```

## Underlying File Maintenance

Prior to using this web service, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- Accounts Payable > Vendors

## Assumptions and Dependencies

To add this web service to authorized web services:

1. Go to System Administration > Installation > Data Exchange.

1. Select your Authorization ID.

1. Select Build.

1. In the Search dropdown, select AccountsPayable.

1. In the Web Service Library, locate and select UpdateAPInvoiceHoldFlag.

1. ClickSelect.

## Field Descriptions

Use the table below for reference when using this service.Element NameDescriptionRequired?TypeMaxValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_CodeCompany CodeYESText3Valid Company Code
Vendor_CodeVendor CodeYESText10Valid vendor must exist for the defined Company Code
Invoice_NumberInvoice NumberYESText20Invoice must be updated in Open Items
Invoice_Type_CodeInvoice TypeYESText1I = Invoice
C = Credit memo

Selection_FlagSelection FlagYESText1H = Hold
O = Open
