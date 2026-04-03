---
title: "Business Example: Document Tracking Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance/business-example-document-tracking-codes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance/business-example-document-tracking-codes"
---

# Business Example: Document Tracking Codes

Scenario: We want to make sure that we have a current insurance certificate before we issue checks to a vendor or subcontractor. Is there a way to automate this within Spectrum?
You will need to create a group of tracking codes that you can use for insurance certificates. The following steps walk through setting up two tracking codes: one for the actual insurance certificate expiration date and one for use as a 30-day warning.

1. Navigate to Accounts Payable  >  Maintenance  >  Document Tracking
 Items.

1. Click New.

1. Enter information for the insurance certificate expiration date tracking code:

1. Enter a name in the Tracking Item Code field, up to 10 characters. For example: INS_EXPIRE.

1.  Enter a description in the Description field. For example: Insurance Certificate Expiration Date.

1.  Enter a message to display in the Message field. For example: Insurance Certificate has expired!

1. Enter the expiration date in the Trigger field.

1.  Select the following checkboxes in Actions: Print on Tracking Item Exception Report, Put new invoices on hold, and Print on Check Distribution Action Report.

1. Enter information for the 30-day warning code:

1. Enter a name in the Tracking Item Code field, up to 10 characters. For example: INS_30DAYS.

1. Enter a description in the Description field. For example: Insurance Certificate 30 Day Warning .

1. Enter a message to display in the Message field. For example: Insurance Certificate Expires in 30 days!

1. Enter the 30-day warning date in the Trigger field.

1. Select the following checkboxes in Actions: Print on Tracking Item Exception Report and Print on Check Distribution Action Report.

1. Save the codes.

1. Navigate to Accounts Payable > Maintenance > Document Tracking to assign tracking codes to the vendor and/or
 subcontractor.

1. Enter the appropriate vendor code and subcontract
 number to assign these codes to a specific subcontract. Enter only the vendor
 code if this insurance certificate is to be used for any subcontracts for the
 vendor.

1. Add the two tracking codes. For INS_EXPIRE, enter the expiration date of the insurance certificate in the Date field. For INS_30DAYS, enter a date 30 days prior to the insurance certificate's expiration in the Date field.

1. Save your changes.
