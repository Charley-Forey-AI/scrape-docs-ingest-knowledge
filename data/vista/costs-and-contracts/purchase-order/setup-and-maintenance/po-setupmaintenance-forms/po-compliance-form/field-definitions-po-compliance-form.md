---
title: "Field Definitions: PO Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form/field-definitions-po-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form/field-definitions-po-compliance-form"
---

# Field Definitions: PO Compliance Form

The following is a list of field descriptions for the PO
 Compliance form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO#

Enter the purchase order number or press
 F4
 to select a PO from a list.
The vendor associated with the selected purchase order will display in the upper portion of the form, and the compliance codes associated with the PO will display in the lower portion of the form.
If a compliance group was selected on the
 purchase order in the PO Purchase Order Entry form (Info tab> [Compliance Group](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-0003092f--en) field), all compliance codes assigned to
 the compliance group will populate in the lower portion of the form. Compliance groups are
 created and maintained using the [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form) form.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance
[](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form)HQ Compliance Groups

## Compliance Code

Enter the compliance code number or press
 F4
 to select one from a list.
Compliance codes are created and maintained using the [HQ Compliance Codes](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form) form.
You can add the same compliance code to a purchase order multiple times, for example Receipt of Material Safety Data Sheets or Receipt of Certifications of Specifications. Each duplicate compliance code will be assigned a unique sequence number. [More](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form/field-definitions-po-compliance-form#ID-0002fdd1--en)

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance
[](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form)HQ Compliance Codes

## Sequence Number (Seq#)

This field is display only and identifies the sequence of each compliance code on the purchase order. If there is only one occurrence of each compliance code, the sequence number will always be 1.
If a compliance code is added to a purchase order multiple times (such as Receipt of Material Safety Data Sheets or Receipt of Certifications of Specifications), the Seq # will be the next sequential number for that occurrence of the compliance code.
Example:

Purchase Order :113001

Comp Code
Seq #
Description
Verify
Exp Date
Complied

MSDS
1
Material Safety Data Sheets
Y

Y

COS
1
Cert of Specifications
Y

Y

COS
2
Cert of Specifications
Y

N

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Description

Enter a description of this compliance code, or accept the default description (assigned in HQ Compliance Codes).

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Comp Type

This field is display only and indicates whether compliance code is a 'Date' or 'Flag' type code.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

##  Supplier

 If this compliance code relates to an additional vendor/supplier (2nd party), enter the
 vendor number (from AP Vendors). If you do not know the vendor number, enter the vendor
 sort name, or press F4 for a list of vendors.
If this compliance code relates only to the vendor on the purchase order, leave this field blank.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Verify

This field initially defaults according to the selection in [HQ Compliance Codes ](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form).
Check this box if this compliance should be verified in Accounts Payable. Verification depends on flags checked in [AP Company Parameters ](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form), on the Audit Options tab. If compliance is not met, then you may be warned at the time of invoice entry, invoices may not be pulled for payment, or you may just receive a warning on the AP Payment Preview with Compliance report, which is run when payments are selected.
Do not check this box if compliance does not need to be verified in AP.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Exp Date

For Date type compliance codes, specify the date this code is effective through.
If using the Verify feature, this date is checked when printing the AP Payment Preview With Compliance report. If the code has expired (expiration date is older than the invoice date), a warning displays stating that the purchase order is out of compliance.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Complied

This field only applies to “Flag” type
 compliance codes - "Flag" is selected in the Comp Type field.
Check this box if compliance has been met.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance

## Vendor Memo

This field is display only and shows memos entered for the vendor/compliance code in AP Vendor Compliance. Memos cannot be edited/modified here, edit/modify them in AP Vendor Compliance and changes will be updated here.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)PO Compliance
