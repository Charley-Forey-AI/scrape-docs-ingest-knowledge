---
title: "Field Defintions: SL Worksheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form/field-defintions-sl-worksheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form/field-defintions-sl-worksheet-form"
---

# Field Defintions: SL Worksheet Form

The following is a list of field descriptions for the SL
 Worksheet form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## JC Co#

 Enter a valid JC Company or press F4 to select
 one from a list.
 If you have already initialized the
 worksheet, this is the company that you want to work on.
 If you are adding a single subcontract to the
 worksheet, this is the company in which the subcontract was set up. This must be entered
 before the subcontract can be added.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Job

Enter a job or press F4 to select
 one from a list. The job must be associated with the selected JC company.
If you have already initialized the worksheet,
 this is the job that you wish to edit.
If you are adding a single subcontract to the
 worksheet, this is the job for which the subcontract was set up. This must be entered
 before the subcontract can be added.
Note: If you enter a soft- or hard-closed job, the status
 displays in red above the tab page. You can enter work complete and stored materials
 information for items on the subcontract and update the subcontract to AP, regardless of
 whether you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
 However, you will only be able to post the resulting AP invoice if you allow posting to
 soft- or hard-closed jobs.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Subcontract

 This field displays the currently selected subcontract. You cannot use this field to add new subcontracts to the worksheet.
See [Add a Subcontract to a Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/add-a-subcontract-to-a-worksheet) for information on
 adding a subcontract to the worksheet.

[Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)
[SL Worksheet Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)

## Pay Control

Enter the payment control code for the subcontract, or accept the
 default.
The pay control code is used to group invoices
 together for payment, and it allows you to easily pay the subcontractors when you get paid
 by the owner.
This field defaults the pay control code from
 AP Vendors (Pay Control field),
 unless you specified a code when you added or initialized this subcontract to the worksheet
 (SL Add to Worksheet or SL Worksheet Initialization).
When using [AP Payment Posting ](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form) or [AP Payment Workfile ](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form), you can select the invoices that should be paid by payment control code, and all invoices that have the same payment control code are added to the payment work file.

## AP Reference

The AP Reference field on the SL Worksheet form, header Info tab.
 Enter the AP reference number for this subcontract, or accept the default specified when this subcontract was initialized or added to the worksheet.
The entry in this field is validated based on the
 selection in the Check for unique AP Reference field (AP Company Parameters, Audit Options tab).
For example if By Vendor &
 Co is selected, a validation error will display if the AP reference number
 has already been used on an invoice for that vendor in the same company.
The system only checks existing invoices in
 the AP module, it does not check AP reference numbers already entered in either of the
 following:

- On claims that have not been posted to
 AP (via SL Subcontract Claims).

- On subcontracts added to a worksheet in
 SL Worksheet

## Invoice Description

 Enter the invoice description for this subcontract.
This field will populate with any default value entered when the subcontract was added to the worksheet or the worksheet was initialized.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Invoice Date

 Enter the invoice date for this subcontract.
This field will populate with the default entered when the subcontract was added to the worksheet, or the worksheet was initialized.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Pay Terms

Use this field to set the payment terms of the
 subcontract. Enter a payment term code or press F4 to select one from a list.
Payment terms are created and maintained using
 the [ HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form) form. You can open this form by pressing
 F5
 in this field.
By default this field populates with the
 payment terms entered on the subcontract (SL Subcontract Entry> Info tab in the upper
 portion of the form> Pay Terms field).
If payment terms were not set up on the
 subcontract, this field populates with the payment terms set up on the vendor (AP
 Vendors> Info tab> Payment Terms field).

## Due Date

Use this field to set the due date of the invoice.
If you selected payment terms, this field defaults a calculated due date based on the payment terms and invoice date.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## CM Account

 Use
 this field to select the CM Account that will pay the invoices for this subcontract.
Enter a SM account or press F4 to select
 one from a list. CM accounts are created and maintained using the [CM Accounts ](/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-the-cm-accounts-form) form. You can open this form by pressing
 F5
 in this field.
Note: If you initialized the subcontract, this field defaults from the CM
 Account field from SL Worksheet Initialization. If you leave the CM Account field in SL
 Worksheet Initialization blank, the system updates this field with the number from the CM
 Account field in AP Vendors. If the CM Account field in AP Vendors is blank, the system
 uses the number from the CM Account# field in AP Company Parameters.
Note: If you added the subcontract to the worksheet, this field initially
 defaults from the CM Account field from SL Add to Worksheet. If you leave the CM Account
 field blank on SL Add to Worksheet, the system updates this field with the number from the
 CM Account field in AP Vendors. If the CM Account field in AP Vendors is blank, the system
 uses the number from the CM Account# field in AP Company Parameters.

## Hold Code

Use this field to enter a hold code on the
 subcontract. Enter a hold code or press F4 to select one from a list.
Hold codes are created and maintained using
 the [HQ Hold Codes ](/en/vista/vista/administration/headquarters/company-setup/hq-hold-codes-form) form. Press F5 in this
 field to open this form.

## Ready

The Ready checkbox on the SL Worksheet, header Grid/Info tabs.
Select this checkbox if this subcontract is ready to be updated to AP. When the update to AP is run, this subcontract will be included in the update, provided all required information has been entered.
Note: You must specify a CM account for this line before this box can be checked. Additionally, if you have not specified a Reference number, you will receive a warning stating that the AP Reference column is blank, and though not required for posting, it is recommended for reporting and to prevent a warning on duplicate reference numbers. However, box can still be checked and update to AP will be allowed.
Leave this checkbox unselected if this subcontract should not be updated to AP.
If you set up a maximum retention amount on the subcontract and you have exceeded that
 amount, a warning displays. Select Yes to have the system calculate and distribute retention
 amounts. Select No to
leave retention amounts alone and mark the worksheet as ready to update to AP. The system calculates and distributes retention amounts as set up for the subcontract in SL Subcontract
 Entry.

## Notes

 Use this field to enter any notes on the subcontract. You can also use the Notes tab in the lower portion of the form to enter notes on each specific subcontract item.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Item

This field displays the subcontract item
 number that displays on the Info tab in the lower portion of the form. To view a different
 item, enter the item number in the field or press F4 to select it from a list.
You cannot use this field to add new
 subcontract items to the worksheet. See [Add a Subcontract to a Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/add-a-subcontract-to-a-worksheet).

[Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)
[SL Worksheet Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)

## Line Description

 This field displays the description of the subcontract item. The value in this field can be up to 60 characters long.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Supplier

 Use this field if a third party other than the subcontractor is involved in the subcontract
 item.
 Enter the supplier number or press F4 to select
 the supplier from a list ([AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)).

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Notes

Use this tab to enter notes on a specific subcontract item. You can also use the Notes tab in the upper portion of the form to enter notes on a subcontract.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Work Completed: WC Ret%

This field defaults the retainage percentage
 for work complete as specified for the subcontract item in SL Subcontract Entry (Work Completed Retanage
 % field). You can override this value as necessary.
If you either initialized or manually added
 subcontracts to the worksheet, and you used Job Billing to bring in invoice amounts, this
 field will default the work complete retainage percent from Job Billing.
Note: If you have set maximum retention amounts for this
 subcontract, the system may change this value when you hit the maximum retention amount.
 See [Applying
 Maximum Retention Amounts to Subcontracts](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts) for more information.
[Add a Subcontract to a Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/add-a-subcontract-to-a-worksheet)
[Initialize Subcontracts to Worksheets](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/initialize-subcontracts-to-worksheets)
[Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)
[SL Worksheet Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)

## Work Completed: % Cmpl To Date

Enter the total percent of work complete to date. If you added or initialized the subcontract, and you used Job Billing (JB) to set invoice amounts, this field will default the percent complete from JB.
If the unit of measure for the item is LS (lump sum), this amount reflects total cost. If the unit of measure is not LS, this amount reflects units. You can override this field.
Tip: Because entry in this field automatically updates all other fields, (does not include the Stored Materials section) you might consider using only this field to enter invoice amounts. By entering the appropriate amount here and then pressing the Page Down key, you can quickly move through all subcontract items. You must still use the Subcontract tab/Items tab to select the subcontract and first item.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

##  Work Completed This Invoice: Cost

 If invoice amounts were initialized from Job Billing, this field defaults the current costs for this invoice. May be overridden.
 If not initializing invoice amounts from Job Billing, enter the total cost for this invoice. Once entered, all other fields are adjusted to reflect this amount.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Work Completed This Invoice: Units

If invoice amounts were initialized from Job Billing, this field defaults the current units complete for this invoice. May be overridden.
If not initializing invoice amounts from Job Billing, enter the units complete for this invoice. Once entered, all other fields are adjusted to reflect this amount.
Tip: Because entry in this field automatically updates all other fields, (does not include the Stored Materials section) you might consider using only this field to enter invoice amounts. By entering the appropriate amount here and then pressing the Page Down key, you can quickly move through all subcontract items. You must still use the Subcontract tab/Items tab to select the subcontract and first item.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

##  Work Completed This Invoice: Retainage

 The total retainage for work completed this invoice. May be overridden.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

##  Work Completed To Date: Cost

 The total work completed to-date. This amount is the sum of Previous Work Completed and Work Completed This Invoice. If overridden, will recalculate This Invoice and % Complete.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

##  Work Completed To Date: Units

 The total units completed to-date. This amount is the sum of Previous Units Complete and Units Completed This Invoice. If overridden, will recalculate This Invoice and % Complete.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Stored Materials: Purchased This Invoice

Enter the total dollar value of the materials
 that the subcontractor has purchased and stored on this job for this billing cycle. This
 will default to zero (even if initializing from Job Billing and there were purchased stored
 materials for the related contract item). The amount entered here will increase the amount
 of stored materials to be invoiced on this billing (Net This Invoice field).
Note: A separate line will be generated for stored materials
 on the AP invoice, with a line description of "Stored Materials for Item ##", where ## is
 the subcontract item number.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Stored Materials: Installed This Invoice

Enter the total dollar value of materials the
 subcontractor installed during this billing cycle that were previously billed as stored
 materials. This default will be zero (even if initializing from Job Billing and there were
 installed stored materials for the related contract item). The amount entered here will
 decrease the amount of stored materials to be invoiced on this billing (Net This
 Invoice field).
Note: Make sure that ‘Work Completed’ on this invoice includes any materials installed on this invoice.
A separate line will be generated for stored
 materials on the AP invoice, with a line description of "Stored Materials for Item ##",
 where ## is the subcontract item number.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

##  Stored Materials: Retainage

 Defaults the retainage percentage for Stored Materials specified for the subcontract item in SL Entry. May be overridden.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Stored Materials Retainage This Invoice

The total retainage for stored materials this invoice. May be overridden.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet

## Notes

 Use this field to enter any notes on the subcontract. You can also use the Notes tab in the lower portion of the form to enter notes on each specific subcontract item.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)SL Worksheet - Overview
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)SL Worksheet
