---
title: "Field Definitions: SL Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form/field-definitions-sl-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form/field-definitions-sl-compliance-form"
---

# Field Definitions: SL Compliance Form

The following is a list of field descriptions for the SL
 Compliance form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## SL

Enter the subcontract to access for compliance information. The JC company, job, job description, and vendor information associated with this subcontract display in the applicable fields in the header area of the form.

## Comp Code

Enter the compliance code (as set up in HQ Compliance Codes) to add.
If a compliance group was specified for this subcontract in SL Entry, all compliance codes assigned to the compliance group are already initialized to this subcontract. Select the code you wish to modify.

## Description

Enter a description of this compliance code, or accept the default description (assigned in HQ Compliance Codes).

## Comp Type

This field is display only and indicates whether this is a “Date” or “Yes/No” type compliance code (as set up in HQ Compliance Codes).

## Sequence #

The Sequence # field on the SL Compliance form.
This field is display only and shows the number assigned by the system to identify the sequence of each compliance code on the subcontract.
When adding new compliance codes, this field automatically defaults to 1. If a compliance code is added to a subcontract multiple times (such as for certified payrolls, where compliance must be met more than once), the sequence number will be the next highest sequential number for that occurrence of the compliance code.
Example:
Subcontract:11300-0001

Compliance Code
Sequence #
Description
Verify
Expiration Date
Complied

CP
1
Cert Payroll
Y
01/31/09
Y

CP
2
Cert Payroll
Y
02/31/09
N

CP
3
Cert Payroll
Y
03/31/09
N

LR
1
Lien Release
Y

N

CR
1
Contract Received
Y

Y

## Supplier

If this compliance code relates to a supplier, enter the vendor number
 (from AP Vendors). If you do not know the vendor number, enter the vendor sort name, or
 press F4 for a list of vendors. The Supplier’s name displays in the Name field.
If this compliance code relates to the subcontractor only, leave this field blank.
Once you enter a vendor here, the system
 defaults the vendor's phone number and email address in the Supplier Phone#
 and Supplier
 Email fields, respectively.

## Name

This field is display only and shows the name of the supplier that was specified in the Supplier field.

## Verify

This field initially defaults according to either the designation in HQ Compliance Codes or the override setting in AP Vendor Compliance.
Check this box if this compliance should be verified in Accounts Payable to prevent payment or to warn that compliance has not been met.
Do not check this box if compliance does not need to be verified in AP.

## Expiration Date

For “Date” type compliance codes, specify the date through which this code is effective.
When the Verify checkbox is selected, this date is checked based on options chosen in various forms. If the code has expired, (expiration date is older than the invoice date), the subcontract is considered out of compliance.

## Complied

For “Yes/No” type compliance codes.
Check this box if compliance has been met.
Do not check this box if compliance has not been met.
When the Verify checkbox is selected, the Complied flag is checked in various forms and, based on the options selected, either provides warnings or prevents payment.

## Receive Date

Enter the date notification was received that this item was in compliance. For example, the date the signed contract was received, the date you received the Certificate of Insurance, etc.
Note: This field is information only and is not used anywhere in the system. It can be used for any date; there are no restrictions on this field.

## Limit

Specify the limit for this compliance code, up to 10 digits and 2 decimals.For example, use this field to indicate bond and insurance limits.
Note: This field is information only and is not used anywhere in the system. It can be used for any numeric entry; there are no restrictions on this field.

##  AP Ref

 Enter the AP reference number to associate with this compliance code for non-compliance. By associating a reference number here, the system allows you to make payments on this subcontract for other invoices that are in compliance, but prevent payment for the specific AP invoice associated with this reference number.
