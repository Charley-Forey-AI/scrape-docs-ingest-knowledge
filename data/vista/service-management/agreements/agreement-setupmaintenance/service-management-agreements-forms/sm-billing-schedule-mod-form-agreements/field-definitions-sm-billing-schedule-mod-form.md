---
title: "Field Definitions: SM Billing Schedule Mod Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-billing-schedule-mod-form-agreements/field-definitions-sm-billing-schedule-mod-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-billing-schedule-mod-form-agreements/field-definitions-sm-billing-schedule-mod-form"
---

# Field Definitions: SM Billing Schedule Mod Form

The following is a list of field descriptions for the SM
 Billing Schedule Mod form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Billing Seq

The Billing Seq field on the agreement SM Billing Schedule Mod form.
For existing billing sequences, this field is
 display only and cannot be changed.
If adding a new billing sequence, enter N, New, or
 + to have the system
 automatically assign the next sequential number available.
Note: Because the grid displays only
 those billing sequences that have not yet been invoiced, once you apply your changes, the
 system will automatically update the sequence number on the Billing Schedule tab based on
 existing billing sequences. For example, a new sequence may default as "2" here, but if the
 original billing schedule contains 5 billing sequences, once you apply the changes here,
 the system will update the new billing sequence to "6".

## Tax Type

The Tax Type field on the agreement SM Billing Schedule Mod form.
Optional.
If adding a new billing sequence, select the tax type or leave blank if taxes are not applicable.

- 1 - Sales

- 2 - Use

- 3 - VAT
For existing sequences, change the tax type if applicable; otherwise, skip this field.
Note: For Australian and Canadian companies (where SM company's AR company is set up with a Default Country of AU or CA in HQ Company Setup), this field defaults to 3-VAT.

## Tax Code

The Tax Code field on the agreement SM Billing Schedule Mod form.
This field is enabled and required only if you
 specified a Tax
 Type (previous field).
If adding a new billing sequence, enter a tax
 code. Must be a valid tax code for the specified tax type. Press F4 for a list of valid tax codes.
Note: If you specified a tax type of 3-VAT, you must enter a
 VAT tax code (i.e. tax code with the Value Added Tax (VAT) checkbox selected
 in HQ Tax Codes).
For existing sequences, modify the tax code if applicable; otherwise, skip this field.

## Tax Basis

The Tax Basis field on the agreement SM Billing Schedule Mod form.
This field is only enabled if you specified a
 Tax
 Type for this sequence.
If adding a new billing sequence, enter the
 tax basis. The Tax
 Amount field will update with the tax amount based on the tax basis and the
 specified tax code.
For existing sequences, change the tax code if applicable; otherwise, skip this field.

## Date

The Date field on the agreement SM Billing Schedule Mod form.
Required.
If adding a new billing sequence, enter the billing date. Billing date must fall within the agreement term dates.
For existing sequences, change the billing date if applicable; otherwise, skip this field.

## Billing Amount

The Billing Amount field on the agreement SM Billing Schedule Mod form.
Required.
If adding a new billing sequence, enter the
 billing amount.
 For existing sequences, you can change the billing
 amount if applicable.
 In either case, the billing amount must be equal to or greater than 0.00; no negative amounts are allowed.
Note: Regardless of whether you are adding a new billing sequence or adjusting the billing amount for an existing sequence, the system updates the Total Remaining (based on the agreement price)
 accordingly. When you have completed entering or adjusting billing sequences, the Total Remaining amount must equal 0.00. If it does not, you must adjust the remaining billing sequences until it does.
