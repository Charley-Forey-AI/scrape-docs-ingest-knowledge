---
title: "Example: Set Parameters for Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-reports"
---

# Example: Set Parameters for Reports

This example discusses creating a button on AP Transaction
 Entry that, when clicked, will open the AP Transactions by Vendor report parameter setup
 form (the Crystal Reports Launcher).
This setup will specify one vendor for the vendor
 range parameters.

1. On the Info tab in VA
 Custom Form Buttons, create the custom form button. Make sure to specify AP
 Transaction Entry as the form you are placing the button on, and the AP
 Transactions by Vendor report in the Action field.

1. On the Parameters tab,
 in the Parameter ID field, enter a + to create a new entry and
 have the system automatically assign the next available ID number.

1. In the
 Name field, press F4, select
 the ?BegVendNumber parameter, and select OK.


1. Select 3-Form Input
 value from the DefaultType
 dropdown.

1. In the
 DefaultValue field, press F4,
 select the field name that contains the value that the report will default in
 its parameter field, and select OK. In this example,
 select Vendor from the F4 lookup.  The system defaults the field’s
 sequence number in the DefaultValue field. In this example, the sequence is
 15.

1. Repeat steps 4 – 6 for
 the Ending vendor number. Select the ?EndVendNumber parameter in
 the Name field.

1. Save the record.

1. Open the AP Transaction
 Entry form and move the button to a new location, as necessary.

1. In AP Transaction Entry,
 enter transaction details, including the vendor number.

1. Click the custom form
 button. 

The AP Transactions by Vendor report parameter setup form
 appears with the vendor specified in the Vendor field in AP Transaction Entry in the
 beginning and ending parameter fields.
