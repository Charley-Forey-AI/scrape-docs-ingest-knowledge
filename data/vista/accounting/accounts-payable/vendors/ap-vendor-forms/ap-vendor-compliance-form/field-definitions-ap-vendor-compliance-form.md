---
title: "Field Definitions: AP Vendor Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-compliance-form/field-definitions-ap-vendor-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-compliance-form/field-definitions-ap-vendor-compliance-form"
---

# Field Definitions: AP Vendor Compliance Form

The following is a list of field descriptions for the AP Recurring Invoices form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Vendor

 Indicate the vendor for which you are tracking compliance.

## Compliance Code

The Compliance Code field on the AP Vendor Compliance form.

Enter a valid compliance code for this vendor. The description of the compliance code displays to the right of this field.
Compliance codes assigned here automatically apply to any new subcontract and/or purchase order transactions posted to this vendor; however, this applies only to 'standard' compliance codes (those with the Use This Code for All Invoice Compliance checkbox unselected in HQ Compliance Codes). Compliance codes with the Use This Code for All Invoice Compliance checkbox selected apply to non-PO/SL invoices only.
When a 'standard' compliance code is added (or deleted), if there are any existing purchase orders and/or subcontracts for the vendor, a window displays with the following options:

- Update Compliance to Purchase Orders

- Update Compliance to Subcontracts

Checking either (or both) of these options will update the compliance information in the PO and SL Compliance Tracking tables, as appropriate. (Option is only enabled if there are existing transactions.)

## Use this Code to Verify Compliance

 Check this box if you want compliance verified. Compliance will be checked either when transactions are entered, or when loading the payment batch, depending on which option you selected in the AP Company Parameters program.
 Do not check this box if you do not want compliance verified.

## Vendor is in Compliance

 For Flag-type compliance codes, indicates whether compliance has been met or not.
 Check this box to indicate that vendor is in compliance.
 Do not check this box if vendor in out of compliance.

## Expiration Date

 For Date-type compliance codes, indicate the date through which vendor is in compliance. If an invoice date is later than this date, it is considered out of compliance.

## Memo

 Use this memo field to enter miscellaneous notes or information about this vendor/compliance code. Field allows up to 255 characters.
