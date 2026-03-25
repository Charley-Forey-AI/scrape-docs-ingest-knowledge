---
title: "Field Definitions: AP Unapproved Invoice Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form"
---

# Field Definitions: AP Unapproved Invoice Entry Form

The following is a list of field descriptions for the AP Unapproved Invoice Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Month

 Enter the unapproved invoice month. This is generally the expense month, although you can update the transaction to another month when approved and posted.

## Seq #

 Enter the existing sequence to work on, or enter 'N', 'New' or '+' to add a new sequence. The system assigns the next available sequence number. Use F4 to look up existing transactions for the month.

## Change Status

Change
 Status button in the AP Unapproved Invoice Entry form header.
Press this button when you have completed your invoice entry and want to release the invoice lines into the review workflow. The status will change from
 0 - Not Ready
 to
 1 - Ready
 and the applicable reviewers will be able to view their lines in the AP Unapproved Invoice Review form.
Until
 you press the button to indicate the invoice is ready for review, the assigned reviewers
 cannot view any invoice lines in the AP Unapproved Invoice Review form.
You can
 click this button to release this invoice into the review workflow if all of the following
 are true:

- The invoice has at least one line

- Each invoice line has at least one reviewer assigned

- The line total amounts match the header Invoice
 Total amount (if the Require invoice total to equal sum of all
 lines checkbox is selected, AP Company Parameters, Invoice Options
 tab). Line total is defined as:
Gross + Misc Amt
 + Tax
 Amt (where Tax Type <> 2) - Ret Amt (in CA/AU)

Note: If you want to remove the manual requirement to mark invoices as ready for review by
 having the system automatically mark all invoices as ready after you have inserted the
 minimum required data, select the Automatically mark unapproved invoices
 Ready checkbox in the AP Company Parameters form

After
 the invoice is marked as ready, if you make any changes to the invoice that would cause any
 of the above to become untrue, or if you add any new lines, the system will automatically
 update the invoice status back to 0 - Not Ready. Once you make the required
 changes/corrections, you can click the button to mark it as ready for review.
If any
 reviewers take action on the invoice lines that cause the invoice status to change back to
 0 - Not
 Ready, the system prevents reviewers from seeing the invoice but preserves
 their review history shown on the Reviewers tab in the footer. If you want to require their
 review again based on the new changes, delete the history.

Related information

- [Automatically mark unapproved invoices Ready](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005a89--en)

- [Invoice Status](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-0000723b--en)

- [Show Ready](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form/field-definitions-ap-unapproved-invoice-status-form#ID-000077e8--en)

- [Show Not Ready](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form/field-definitions-ap-unapproved-invoice-status-form#ID-000077fa--en)

- [Display All Reviewer Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form#ID-0000769e--en)

- [AP Unapproved Invoice Status Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form)

## Invoice Status

Invoice
 Status column in the AP Unapproved Invoice Entry form header, Grid tab
Change
 the invoice status to 1 - Ready when you have completed your
 invoice entry and want to release the invoice lines into the review workflow. The
 applicable reviewers will be able to view their lines in the AP Unapproved Invoice Review
 form.
Until
 you change the status to 1 - Ready, the assigned reviewers cannot
 view any invoice lines in the AP Unapproved Invoice Review form.
You can
 select 1 -
 Ready to release this invoice into the review workflow if all of the
 following are true:

- The invoice has at least one line

- Each invoice line has at least one reviewer assigned

- The line total amounts match the header Invoice
 Total amount (if the Require invoice total to equal sum of all
 lines checkbox is selected, AP Company Parameters, Invoice Options
 tab). Line total is defined as:
Gross + Misc Amt + Tax
 Amt (where Tax Type <> 2) - Ret Amt (in CA/AU)

Note: If you want remove the manual requirement to mark invoices as ready for review by
 having the system automatically mark all invoices as ready after you have inserted the
 minimum required data, select the Automatically mark unapproved invoices
 Ready checkbox in AP Company Parameters.

After
 the invoice is marked as ready, if you make any changes to the invoice that cause any of
 the above to become untrue, or if you add any new lines, the system will automatically
 update the invoice status back to 0 - Not Ready. After you make the
 required changes/corrections, you can select 1 - Ready to mark it as ready for
 review.
If any
 reviewers take action on the invoice lines that cause the invoice status to change back to
 0 - Not
 Ready, the system prevents reviewers from seeing the invoice but preserves
 their review history shown on the Reviewers tab in the footer. If you want to require their
 review again based on the new changes, delete the history.

Related information

- [Automatically mark unapproved invoices Ready](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005a89--en)

- [Change Status](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-00007205--en)

- [Show Ready](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form/field-definitions-ap-unapproved-invoice-status-form#ID-000077e8--en)

- [Show Not Ready](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form/field-definitions-ap-unapproved-invoice-status-form#ID-000077fa--en)

- [Display All Reviewer Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form#ID-0000769e--en)

- [AP Unapproved Invoice Status Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-status-form)

## Vendor

Entry in this field is required.
Enter the vendor (from AP Vendors) for this
 unapproved invoice. If you do not know the vendor number, enter alpha characters, which
 will be matched to the vendor sort name for the first closest match. The system displays
 the resulting vendor number, and the vendor’s name displays to the right.
Note: If you are tracking vendor compliance for non-PO/SL
 invoices and this vendor is out of compliance, an ***Out of Compliance*** warning is
 displayed in red above the header; however, the system allows entry. For more information,
 refer to AP Unapproved Invoice Entry in Related Topics below.

[](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)AP Unapproved Invoice Entry

## AP Reference

The AP Reference field on the AP Unapproved Invoice Entry form, header Info tab.
Enter the invoice number provided by the vendor for this transaction, up to 30 characters.

Related information

- [Check for Unique AP Reference Numbers](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers)

- [Enable Case-Insensitivity on AP References](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005b04--en)

## PO

The PO field on the AP Unapproved Invoice Entry form, header Info tab.

Entry in this field is not required.
 Enter the purchase order for this unapproved invoice or press F4 to select from a list of valid purchase orders.
If you enter a PO here, when adding items to the invoice, the system automatically sets the line type to 6-PO and defaults this PO number. You may override the line type and/or purchase order as needed.
Note: If you also entered a subcontract in the invoice header (in the SL field), the system still auto-sets the line type to 6-PO for new items; however, you may change the line type as needed.

## SL

The SL field on the AP Unapproved Invoice Entry form, header Info tab.

Entry in this field is not required.
 Enter the subcontract for this unapproved invoice or press F4 to select from a list of valid subcontracts.
If you enter a subcontract here, when adding items to the invoice, the system automatically sets the line type to 7-SL and defaults this subcontract number. You may override the line type and/or subcontract as needed.
Note: If you also entered a purchase order in the invoice header (in the PO field), the system automatically sets the line type to 6-PO for new items and defaults the PO number; however, you may change the line type as needed.

## Reviewer Group

The Reviewer Group field on the AP Unapproved Invoice Entry form, Info tab of Invoice Header section.
Optional field.
Enter a reviewer group for this invoice if you want all reviewers (group or individual) to be added to each line (current and subsequent).
Reviewer groups (and reviewers) removed from the header Reviewer tab will cause the reviewers and the reviewers in the group to be removed from every line. The system will then check if there are any remaining reasons to justify retaining reviewers on the line and retain them if any are found (job, vendor, etc.).
Press F4 for a list of active reviewer groups.
 Press F5 to access the HQ Reviewer Group form for reviewer-group management.
All reviewers from the group without an assigned threshold amount display on the Reviewers tab in the header and default from there onto each line. For more information on setting threshold amounts, refer to [About Thresholds for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices).
Note: If you have defined rejection notification recipients for this
 group in HQ Reviewer Groups (Email Options for Rejection section), the system will send
 email notifications to the specified recipients when reviewers in this group reject this
 invoice in AP Unapproved Invoice Review. For more information, see the F1 help for the
 [Rejected](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form#ID-000076e7--en) checkbox in AP Unapproved Invoice Review.

### Re-Adding Reviewers to an Invoice/Line

If you delete a reviewer from an invoice header or invoice line that was initialized via a reviewer group, you can manually add the reviewer back to the invoice header or applicable invoice lines as needed.
 However, if you use the AP Unapproved Invoice Status form and plan to filter by responsible person, you cannot use the manual method to re-add reviewers to the invoice/line, as it will result in the invoice being excluded from the result set when filtering by the responsible person associated with that reviewer group.
Instead, you must delete the reviewer group from the invoice/line, save the record, and then reassign the reviewer group to the invoice/line. This ensures that all reviewers in the group are properly initialized to the invoice/line. Then when filtering by that responsible person in AP Unapproved Invoice Status, the invoice is included in the filtered results.

[](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)HQ Reviewer Groups

## Description

 Entry in this field is not required.
 Enter a description of this unapproved invoice, up to 30 characters. This description prints on the check stub, as well as on certain reports.

## Invoice Date

 Initially defaults to the current date. Accept the default, or enter a new invoice date.
 Entry in this field is not required.

## Discount Date

Initially defaults a discount date based on the payment terms assigned
 to the specified vendor in AP Vendors. Accept the default, or enter a new discount date. If
 you manually enter a new date, the system will display a warning if the date is equal to or
 greater than the date in the Due Date field.
Entry in this field is not required.

## Entered By

The Entered By field on the AP Unapproved Invoice Entry form, header Info tab.
Display only, the user name of the person who entered this unapproved invoice, whether via manual entry, import, or auto invoicing.

## Due Date

 Initially defaults a due date based on the
 payment terms assigned to the specified vendor in AP Vendors. Accept the default, or enter
 a new due date.
 Entry in this field is not required; however, once the invoice is approved, you will need to assign a due date in order to post the invoice to an AP batch.

## Invoice Total

The Invoice Total field on the AP Unapproved Invoice Entry form, header Info tab.
 Entry in this field is required. However, can be 0.00 amount.
 Enter the total amount of this invoice. If the Require Invoice Total to Equal Sum of all Lines option in AP Company Parameters is checked, this amount is compared to the total of all invoice lines, and if amounts do not match, a warning is displayed. Amounts must match before you can add or edit another transaction.

## Hold Code

The Hold Code field in the AP Unapproved Invoice Entry form, Payment Overrides tab
Entry in this field is not required. However, if entry is made, must be valid.
Specify the hold code (from HQ Hold Codes) for this unapproved invoice, if applicable. Hold codes prevent the invoice from being paid until the hold code is released. The hold code entered here is in addition to any hold code automatically placed on the transaction (or any portion of the transaction) because of retainage or a vendor hold.

## Pay Control

Enter the pay control code for this unapproved
 invoice. This field defaults the pay control code from AP Vendors (Pay Control
 field).
The pay control code is used to group invoices together for payment. For example, you could code all loan payments with the same control code. Then when initializing the payment batch, you can select all invoices with that pay control code. For subcontract invoices, you might use the owner’s application number to facilitate “pay when paid” process (the SL Worksheet will update this field for that purpose).

## Pay Method

The Pay Method field on the AP Unapproved Invoice Entry form, Payment Overrides tab.

Specify the payment method for this invoice. Payment methods include:

- N-ePayments

- C-Check

- E-EFT

- S-Credit Service

This field's default value comes from the Pay Method field in the AP Vendors form (Payment Method tab) for the selected vendor.
Tip: If this is a prepaid transaction,you must select C-Check.

### N-ePayments

If you select the N-ePayments pay method, you must meet the setup requirements before you can generate and upload an ePayments file. For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

### E-EFT

If you select the E-EFT pay method, and you have not set up bank routing information for the specified vendor in AP Vendors (Payment Method tab), the system displays a warning, but allows you to save the record.

### S-Credit Service

You should only select the S-Credit Service pay method if you have set up the appropriate information in AP Company Parameters (Payment Services tab) and AP Vendors (Payment Method tab). For more information, see [Set up Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-card-payments).

## CM Acct

Enter the CM account for paying this transaction. The entry must be a
 valid account set up in CM Accounts.
Note: If you have specified a credit service CM account in
 the AP Company Parameters form, and you are paying this vendor with a different method
 (either check or EFT), the system will display a warning if you enter the credit service CM
 account. You will be allowed to save the record, however.
This field defaults depending on where you generate the transaction from. You can override this field, regardless of the default.

- If you are updating AP from SL (that is, using the
 SL Update to AP form, accessed from SL Worksheet), this field defaults the account
 number from the CM Account field in SL Worksheet.
 If that field is blank, the system defaults the number from the CM
 Account field in the AP Vendors form. If that field is blank, the
 system uses the number from the CM Account# field in the AP Company
 Parameters form.

- If you are paying this vendor by credit card, this
 field will default from the CM Acct # field in the AP Company
 Parameters form (Payment Services tab).

## Separate Payment

Check this box if this transaction is to be paid separately. When payments are initialized (in AP Payment Posting), a separate payment is generated for this transaction.
Note:If you are generating separate payments per job or subcontract, and this option is checked, this transaction will be paid separately from all other transactions for a subcontract or job.

Do not check this box if this transaction is not to be paid separately. When payments are initialized, this transaction will be grouped together with other transactions having the same vendor on a single invoice.

## Include in 1099 Totals

 This field initially defaults based on the vendor’s setup (AP Vendors).
 Check this box if this invoice’s amounts are to be included in the specified vendor’s 1099 totals.
 Do not check this box if this invoice’s amounts are not to be included in the specified vendor’s 1099 totals.
Click for the Australian field definition: [Include in Payments Reporting](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-00051bc7--en).
Click for the Canadian field definition: [Include in T5018 Totals](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-00051bcf--en).

## Include in T5018 Totals

 This field initially defaults based on the vendor’s T5018 setup in AP Vendors (T5018 Info
 fields, Add'l Info tab)
Check this box if this transaction should be included in T5018 totals.
Additional Information
[T5018 Reporting: Canada](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/about-t5018-reporting-canada)
[Setting Vendors Subject to T5018 Reporting](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/set-vendors-subject-to-t5018-reporting-canada)

## Include in Payments Reporting

Check this box if this invoice's vendor/subcontractor is subject to
 Taxable Payments reporting.
Note:This box is checked by default if the
 vendor/subcontractor is set as subject to Taxable Payments in AP Vendors (you checked
 the Subject to
 taxable payments reporting box, Add'l Info tab).

For more information see [Generating Taxable Payments Annual Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/taxable-payment-reporting/generate-taxable-payments-annual-reports-australia).

## Type

Entry in this field is not required.
This field defaults to the 1099 type specified
 for this vendor (in AP Vendors).
If 1099 amounts are to be included when printing 1099’s or creating 1099 electronic files (AP 1099 Processing), you must specify a 1099 type of “MISC” (Miscellaneous Income), “INT” (Interest Income), or “DIV” (Dividends/Distributions).
Note:If you are only using 1099 types for informational or reporting purposes, any type is acceptable.

## Box#

 Defaults initially based on the vendor’s setup (AP Vendors).
 Press F4 to select from a list of valid boxes
 on the 1099 form that will be used to accumulate and print 1099 amounts.

## Address Seq#

Specify the payment address sequence to use for this transaction. Must be a valid address sequence defined for the vendor in AP Additional Addresses, and must be an address sequence flagged as 'Payment' or 'Both'.
Note:If you previously entered an override address (to the right), entering an address sequence in this field will cause the 'Override Payment Address' checkbox to be cleared, and the override address to be replaced with the address defined for this address sequence.

## Override Payment Address

Check this box if you want to override the name and/or address
 specified for this vendor in the AP Vendors. Use of this option will allow for a single
 vendor number to be used for all one-time purchases from various vendors. The override name
 and address will be used on all checks, and will be stored with the transaction for check
 history. When invoices are pulled for payment, separate sequences–and therefore separate
 checks–are printed for each transaction in the batch where the override box has been
 checked.
Do not check this box if you do not want to override the payment address for this vendor.
Note:This checkbox is only for use when entering an override payment address (to the left). If you check this box, then enter an Address Seq (above), this box will automatically be cleared.

## Name

If the Override Payment Address option is
 checked, you may enter an override name here (up to 60 characters). If
 nothing is entered, the name will default from the AP Vendors when the
 record is saved. Overriding the name will allow a single vendor to be
 used for one-time purchases from various vendors.

-  you enter an override name, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address Seq# field,
 the system disables this field and it automatically
 defaults the vendor specified for the address sequence
 (Additional Address tab in AP Vendors).

## Add'l Info

 Defaults the additional information specified for this vendor in AP Vendors; may be
 overridden. Up to 60 characters allowed. Information entered here will be included when
 printing checks for this vendor (e.g. Attention line, Garnishment Case #, etc.).
If you entered a value in the Address Seq#
 field, the system disables this field and it automatically defaults the Addl Address
 specified for the address sequence (Additional Address tab in AP Vendors).

## Address

If the Override Payment Address option is
 checked, you may enter an override address here (up to 60 characters). If
 nothing is entered, the address will default from the AP Vendors form
 when the record is saved.

- If you enter an override address, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address Seq# field,
 the system disables this field and it automatically
 defaults the address specified for the address sequence
 (Additional Address tab in AP Vendors).

- If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## City

If the
 Override Payment Address option is checked, you may override the city here (up to 30
 characters). If nothing is entered, the city will default from the AP Vendors form when the
 record is saved.

- If you enter an override city, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address
 Seq# field, the system disables this field and it automatically
 defaults the city specified for the address sequence (Additional Address tab in the
 AP Vendors form).

- If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## State

If the Override Payment Address option is
 checked, you may override the state here. If this field is blank, the
 state defaults from the AP Vendors when you save the record.
Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

- If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

- If you enter an override state, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address Seq# field,
 the system disables this field and it automatically
 defaults the state specified for the address sequence
 (Additional Address tab in AP Vendors).

## Zip Code

If the Override Payment Address option is
 checked, you may override the zip code here (up to 12 characters). If
 nothing is entered, the zip code will default from the AP Vendors when
 the record is saved.

- If you enter an override zip code, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address Seq# field,
 the system disables this field and it automatically
 defaults the zip code specified for the address
 sequence (Additional Address tab in AP Vendors).

- If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Country

You may override the country code if you
 selected the Override Payment Address checkbox. If this field is blank,
 the country defaults from the Vendors form when you save the record.
Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

- If you enter an override country, a separate check will print for each transaction for the same vendor in the payment batch.

- If you entered a value in the Address Seq# field,
 the system disables this field and it automatically
 defaults the country code specified for the address
 sequence (Additional Address tab in AP Vendors).

## Reviewer

The Reviewer field on the Reviewer tab of the AP Unapproved Invoice form, header section.
Enter the reviewer’s initials. Press
 F4
 for a list of active reviewers. Press F5 to access HQ Reviewers for reviewer
 management.
If you assigned a reviewer group to the invoice header, all reviewer in the group are added to this grid. If there is a reviewer assigned to the vendor, it will also default here.

### Re-Adding Reviewers to an Invoice Header

If you delete a reviewer from the invoice header that was initialized via a reviewer group, you can manually add the reviewer back to the invoice header as needed.
 However, if you use the AP Unapproved Invoice Status form and plan to filter by responsible person, you cannot use the manual method to re-add reviewers to the invoice header, as it will result in the invoice being excluded from the result set when filtering by the responsible person associated with that reviewer group.
Instead, you must delete the reviewer group from the invoice header, save the record, and then reassign the reviewer group to the invoice header. This ensures that all reviewers in the group are properly initialized to the invoice header, as well as to invoice lines. Then when filtering by that responsible person in AP Unapproved Invoice Status, the invoice is included in the filtered results.

## Approval Seq

 Enter the sequence number (0-255) for this reviewer.
 If you are using a hierarchical method of invoice approval, this sequence number should represent the order in which this reviewer is to review and approve this invoice. For example, if this reviewer must approve this invoice before anyone else, enter the sequence as '1'. Reviewers with sequences greater than '1' (i.e. 2, 3, etc.) will be unable to review and approve this invoice until this reviewer has marked the invoice as approved.
 If you are not using a hierarchical method of invoice approval, assign all reviewers a sequence of “1”. This will allow reviewers to review and approve an invoice simultaneously.
 If you enter a reviewer group in the Default Reviewer Group field, the approval sequences default from HQ Reviewer Groups and you cannot change them.

## Optional Reviewer

The Optional Reviewer checkbox in the AP Unapproved Invoice Entry form header, Reviewers tab.
When this checkbox is selected, this reviewer is designated as optional on all applicable lines for this invoice, which allows for one of multiple optional reviewers to approve invoice lines with a given approval sequence. Changing this setting affects the setting on this reviewer for each line.
As long as more than one optional reviewer is assigned to each invoice line's approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line's approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line's approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance:

- if ALL reviewers on a sequence are set as optional, at least one must approve

- if ALL reviewers on a sequence are set as non-optional (Optional Reviewer checkbox is not selected), all must approve

- if some reviewers on a sequence are set as non-optional and some as optional, all non-optional must approve

## Approve with missing data

Approve with missing data checkbox in the AP Unapproved Invoice Entry form header, Reviewers tab.
Select this checkbox if your review process requires this reviewer to approve all applicable lines for this invoice even though some required data is still missing. This allows the reviewer to approve invoices that lack data, which allows the invoice to progress in the review process. The missing data must still be entered before posting, but can be entered at some time after this reviewer's approval.
The default value comes from the setting for this reviewer in the HQ Reviewer Group form or the HQ Reviewers form.
Changes you make to this checkbox will update every line of this invoice that the reviewer is assigned to. If instead you want to make changes for specific lines only, make the change on each of those lines.

## Memo

Memo field in the Header Reviewers tab of the AP Unapproved Invoice Entry form
Use this field to enter miscellaneous notes or information about this invoice/reviewer, up to 255 characters.
Note:Entries in this Memo field of the header record can
 only be viewed while in this form; they are not displayed in any other form. If you need
 invoice reviewers to see a note, place it in any of the following locations of this
 form:

- Notes tab of the header record

- Notes tab of the line record

- Reviewers tab of the footer, in the Memo field

If you need more space, double-click on this field to display the Notes window. The Notes window allows up to 8k of space for your notes and information.
To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box and click the right mouse button. From the shortcut menu, select the Standard Notes option, which brings up the Std Note Copy window. Enter the standard note to copy and click OK to add the note. Note will be appended to the end of existing note text (if applicable).
A spell check can be run for any notes entered in this window. Click the Spelling button in the toolbar () or select the Spelling option from the Tools or shortcut menu.
Tip: To use the Tab feature (such as to indent the first
 line of a paragraph or create columns), you will need to press Ctrl + Tab for each tab increment.

## Line

 Entry in this field is required.
 Enter a number (0-32,767) for this invoice line, or ‘N’, ‘New’, or '+' for the next available number.

## Type

The Type drop-down on the AP Unapproved Invoice Entry form, items Info tab.

Select the line type. The screen displays additional fields related to the line type.

- 1-Job – Use for expenses
 related to a JC job.

- 2-Inv – Use for expenses
 related to an Inventory location.

- 3-Exp – Use for
 miscellaneous expenses.

- 4-Equip – Use for expenses
 related to equipment usage.

- 5-EM Work Order – Use for
 expenses related to an EM work order.

- 6-PO – Use for expenses related to a purchase
 order (includes POs entered in PO Purchase Order
 Entry and SM Purchase Order Entry).Note: If you entered a PO
 number in the invoice header (PO
 field), new items automatically default this line
 type. You may override if needed.

- 7-SL – Use for expenses related to a subcontract.Note: If you entered a
 subcontract number in the invoice header
 (SL field), new items automatically
 default this line type. However, if you also
 entered a PO number in the invoice header
 (PO field), new lines automatically
 default to type 6-PO. You may override if
 needed.

- 8-SM Work Order – Use for miscellaneous
 expenses related to an SM work order.Note: Entries of this type
 will auto-generate a work completed miscellaneous
 line in the Work Completed grid of SM Work
 Orders.

## JC Co#

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the Job Cost company in which job/phase/cost type information for this invoice item will be validated, and to which the job expense will be posted.

## Job

Entry
 in this field is not required. However, if entry is made, it must be valid.
Specify the job to be charged for this invoice item.
Once the job is specified, the system checks
 the JC Jobs to see if a Reviewer has been assigned to the job. If so, and the reviewer has
 not yet been assigned to the invoice, he/she will be added once the line has been saved.

- If you enter a soft- or hard-closed job, the status displays in red to the right of the Line field. The system will only save the record if you allow posting to soft or hard-closed jobs (flags in JC Company Parameters).

- The update to AP from SL Worksheet creates invoice items for subcontracts posted to soft- or hard-closed jobs, regardless of whether you allow posting to closed jobs. Once you approve the invoice, it can be added to an AP invoice batch; however, if you do not allow posting to closed jobs, you will be unable to post the batch.

## Phase

Entry
 in this field is not required. However, if entry is made, it must be valid.
Specify the phase to which this invoice item applies.
Note:If the specified job’s Lock Phases option is checked
 (JC Jobs), must be a valid job phase (as set up in JC Job Phases).

## CT

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the Job Cost cost type for this invoice item.

## Ticket

The Ticket field on the AP Unapproved Invoice Entry form, Lines section, Info tab.
This field only displays for 1-Job lines and job-related 6-PO lines that reference a field ticket.

For Job lines: Enter the field ticket number for this unapproved invoice line or press F4 to select from a list of valid open field tickets for the specified job/contract.

For job-related PO lines: This field defaults the field ticket specified for the purchase order item and is disabled.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job lines is only useful if the job's contract/contract item has a bill type of T&M or Both.

Once you post the invoice (via AP Unapproved Invoice Posting), the system updates the Cost Detail tab in JC Field Ticket with this line's transaction information, showing a Source of AP Entry.
For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Material

The Material field on the AP Unapproved Invoice Entry form,
 items Info tab.

Entry in this field is not required unless posting an Inventory
 transaction (2-Inv).
Enter the material to which this invoice item applies.
Job, Exp, Equip, EM Work Order, and SM Work Order LinesYou can enter any material, valid (in HQ Materials) or
 non-valid (not in HQ Materials). If you enter a valid HQ material, the
 description, unit of measure, and unit cost default from HQ Materials. If a
 non-valid material, the description defaults as 'Not in Material File', the unit
 of measure defaults as LS, and the unit cost defaults as 0.00 and is disabled. You
 can override all defaults as needed. Inventory LinesYou must enter a valid stocked material; that is, the
 material must be flagged as stocked in HQ Materials and be set up for the
 specified location in IN Materials. The system defaults the purchase UM and
 description from HQ Materials, and the last unit cost from IN Location
 Materials.PO LinesThe material defaults from PO and field is disabled. Material
 description, UM, and unit cost default from PO item.
Note: If the material is set up for the vendor in PO Vendor
 Materials, the unit cost will default based on the vendor's setup, regardless of the
 line type.

## IN Co#

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the Inventory company in which material/location information for this invoice item will be validated, and to which inventory item will be posted.

## Location

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the Inventory location for which this material was purchased. Location must be set up in IN Location Setup, and material must be assigned to this location in IN Materials.

## EM Co#

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the EM company in which equipment information for this invoice item will be validated, and to which the equipment expense will be posted.

## Equipment

Entry in this field is not required. However, if entry is made, it must be valid.
Specify the equipment (from EM Equipment Master) to which this invoice item applies.
If this is a Work Order line, this field is display only, and will default the equipment assigned to this work order, if applicable.
Note:Once the equipment is specified, the system checks the EM Equipment Master to see if a Reviewer has been assigned to the equipment. If so, and the reviewer has not yet been assigned to the invoice, he/she will be added once the line has been saved.

## Comp Type

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the component type (from EM Component Types) for the equipment, if applicable.
 If this is a Work Order line, this field is display only, and will default the component type assigned to this work order, if applicable.

## Component

 Entry in this field is not required. However, if entry is made, it must be valid.
 If you entered a component type in the previous field, this field defaults the first component of this type for the indicated equipment (as defined in EM Equipment). The default may be overridden, but it must be a valid component for this equipment.
 If this is a Work Order line, this field is display only, and defaults the component assigned to this work order, if applicable.

## Cost Code

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the cost code (as defined in EM Cost Codes) to which this invoice item applies.
 If this is an Equipment line, and you entered a component for this equipment (previous field), this field defaults the cost code assigned to the component’s type in EM Component Types; may be overridden.
 If this is a Work Order line, this field defaults the cost code assigned to the specified work order item (in EM Work Order Edit).

## Cost Type

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the equipment cost type (as defined in EM Cost Types) to which this invoice item applies.

## WO

 Entry in this field is not required. However, if entry is made, it must be valid.
 Enter the work order (as set up in EM Work Orders) to which this invoice item applies.

## WO Item#

 Entry in this field is not required. However, if entry is made, it must be valid.
 Indicate the work order item to which this invoice item applies. Once you have entered the item number, the Equipment, Comp Type, Component, and Cost Code assigned to this work order item are displayed to the right of this field. The Equipment, Comp Type, and Component fields are disabled and cannot be changed. Cost Code may be overridden.

## PO

The PO field on the AP Unapproved Invoice Entry form, items Info tab.
Entry in this field is not required.
Enter the purchase order to which this invoice item applies or press F4 to select from a list of valid POs.
If you entered a PO number in the invoice header (PO field), this field defaults the specified PO. You may override if needed.
Note:

- The vendor assigned to the specified purchase order must be the same as the vendor specified in the transaction header.

- If you selected the Check Compliance On Transaction Entry, Warning
 Only checkbox for Purchase Orders in AP Company Parameters and
 the purchase order is out of compliance, you will receive a warning at this point
 stating that the "Purchase order is not in compliance".

- If the purchase order is related to an SM work
 order, the associated SM Co, SM Work Order, and Scope display below the PO Item#
 and PO Item
 Line fields. If the PO is for a job-related SM work order, the system
 will also display the JC phase and cost type assigned to the PO item. These fields
 are display only.

- If the SM work order is job-related and the job has been soft or hard-closed, the system allows you to save the record, regardless of whether you allow posting to closed jobs (flags in JC Company Parameters); however, if you do not allow posting to closed jobs, you will be unable to post the invoice in AP Unapproved Invoice Posting.

## PO Item#

Entry in this field is not required. However, if entry is made, it must be valid.
Enter the purchase order item for the invoice. Additional fields will display based on the type of purchase order item (e.g. if a job line, screen will display the JC Co, Job, Phase, and CT). Some fields may be disabled; these cannot be changed.
Note:Once you have entered the item number and item line, you can view additional information about the purchase order item by selecting the Other Info tab. This tab displays current totals for the PO item, such as the Current Units, Unit Cost, and Total Cost, and Received, Backordered, Invoiced, and Remaining amounts.

## PO Item Line

If you have distributed the PO item to
 multiple lines, enter the applicable line number. Press F4 to see a
 list of valid line numbers. If you have not distributed the PO item to multiple lines, this
 field will default automatically to 1.
If you have not already distributed the PO
 item to multiple lines, and want to, select Open PO Item Distribution from the Tasks
 drop-down  on the toolbar. When you save your
 changes, and exit the PO Item Distribution form, the PO line on this form refreshes to
 display the updated data. For more information, see [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form).
This field is not required, but if you enter a value it must be valid.

- If you clear this field, the system will display a warning, but will allow you to save. However, when the invoice is viewed in AP Unapproved Invoice Review, that form will display "Missing Information" in red, and you will be unable to post the invoice in AP Unapproved Invoice Posting until you enter a line number here.

- Once you have entered the item number and item line, you can view additional information about the purchase order item by selecting the Other Info tab. This tab displays current totals for the PO item, such as the Current Units, Unit Cost, and Total Cost, and Received, Backordered, Invoiced, and Remaining amounts.

## Rec #

The Rec # field on the AP Unapproved Invoice Entry form, Items section Info tab.

This field is only visible for items with a line Type of 6-PO.
Display only field showing the receiver number for the purchase order.
 This field only populates if all of the following are true:

- You received the purchase order via PO Initialize Receipts or PO Receipts Entry and provided a Receiver # on the receipts transaction.

- You added the purchase order to an AP Transaction Entry batch via initialization (via the AP Purchase Order Initialize form, which is accessed from AP Transaction Entry by selecting File > Initialize from PO).

- When initializing the PO, you used the Receiver # initialization option (that is, you entered the Receiver # on the Receiver # tab in AP Purchase Order Initialize).

## SL

The SL field on the AP Unapproved Invoice Entry form, items Info tab.
 Entry in this field is not required.
 Enter the subcontract to which this invoice item applies or press F4 to select from a list of valid subcontracts.
If you entered a subcontract number in the invoice header (SL field), this field defaults the specified subcontract. You may override if needed.

## SL Item

 Entry in this field is not required. However, if entry is made, it must be valid.
 Enter the subcontract item to which this invoice item applies. The item’s assigned job, phase, and cost type (as set up in SL) and the job/phase/cost type’s U/M (as set up in JC) are displayed. These fields cannot be changed.

## SMCo

The SM Co field on the AP Unapproved Invoice Entry form,
 items Info tab.
This field only displays for line type
 8-SM Work Order. It is
 disabled for PO lines associated with an SM work order.
Enter the SM company to which this invoice
 line applies. This will be the SM company in which the SM work order was set up. Press
 F4
 for a list of valid SM companies.

## SM Work Order

The SM Work Order field on the AP Unapproved Invoice Entry
 form, items Info tab.
This field only displays for line type
 8-SM Work Order. It is
 disabled for PO lines associated with an SM work order.
Enter the SM work order to which this invoice
 line applies. Press F4 for a list of valid work orders for the specified SM company.
Note: If you specify a job-related work order and the job
 associated with the work order has been soft or hard-closed, you will be allowed to save
 the record, regardless of whether or not you allow posting to closed jobs; however, if you
 do not allow posting to closed jobs (i.e. the Allow Posting to Hard-Closed Jobs and/or
 Allow Posting to
 Soft-Closed Jobs boxes are unchecked in JCCompany Parameters), you will be
 unable to post the invoice in APUnapproved Invoice Posting.

##  Scope Seq

The Scope Seq field on the AP Unapproved Invoice Entry
 form, items Info tab.
This field only displays for line type
 8-SM Work Order. It is
 disabled for PO lines associated with an SM work order.
Enter the work order scope to which this invoice
 line applies. Press F4 for a list of valid scopes for the
 specified work order.
If you specify a work order scope that is closed,
 the system will allow you to save the record. However, you must either reopen the scope
 in SM Work Orders or select an open scope before you post the invoice in AP Unapproved
 Invoice Posting.
 For job-related work orders:

- If the job is soft or hard-closed, you will be allowed to save the record;
 however, if you do not allow posting to closed jobs (that is, the Allow Posting
 to Hard-Closed Jobs and/or Allow Posting to Soft-Closed
 Jobs checkboxes are unselected in JC Company Parameters), you
 will be unable to post the invoice in AP Unapproved Invoice Posting.

- If the Costing Method is Markup and the work order scope is not
 assigned a rate template or phase (in SM Work Orders), the system will allow you
 to save the line; however, you will be unable to post the invoice (in AP
 Unapproved Invoice Posting) until the specified information is entered for the
 work order scope

## SM Cost Type

The SM Cost Type field on the AP Unapproved Invoice Entry form, Items Info tab.
This field only displays when the line type is 8-SM Work
 Order.
Enter the SM cost type that applies to this invoice line. Press F4 for a list of valid SM cost types.

Note: Although entry in this field is not initially required, if you apply
 taxes to the invoice line (that is; the Tax Amt field is not 0.00) and you do
 not enter an SM Cost Type, an error displays indicating that the SM Cost Type is
 missing and is required for proper tax distribution. The system saves the line, but
 you must specify an SM Cost Type before you can post the invoice via AP Transaction
 Entry or AP Unapproved Invoice Posting.

## JC Cost Type

The JC Cost Type field on the AP Unapproved Invoice Entry
 form, items Info tab.

This field is only displayed and enabled if the line Type is
 8-SM Work Order and the SM work order is for a job.
Enter the JC cost type (from JC Cost Types)
 for this invoice line. Initially defaults as follows:

- If you entered an SM cost type for the line, defaults the JC
 cost type assigned to the SM cost type (in SM Cost Types). Default may be overridden.

- If you did not enter an SM cost type or if you entered an SM
 cost type, but no JC cost type is assigned to the SM cost type, defaults as blank and
 must be entered manually.

The system uses this cost type, in conjunction
 with the phase specified for the work order sequence, to post the costs to Job Cost (via
 the JC Cost Detail table).
Locked Phases vs. Non-Locked PhasesIf the Phases
 on this job are locked checkbox is selected for the job in JC Jobs,
 the cost type specified here must be set up for the job/phase in JC Job Phases. If
 it is not, the system displays a warning, but allows you to save the record.
 However, you will be required to enter a valid job/phase cost type before you can
 post the invoice in AP Unapproved Invoice Posting.Tip: You can add the
 cost type to the job phase by pressing F5 from this field to
 access JC Job Phases. Once you set up the cost type and exit JC Job Phases,
 you can enter the cost type here.

If the Phases on this job are locked checkbox is not selected in JC
 Jobs, you can use any cost type defined for the phase in JC Job Phases or JC
 Phases. If the cost type is not set up for the phase, the system displays a
 warning, but allows you to save the line. However, you will be required to
 enter a valid phase cost type before you can post the invoice (via AP
 Unapproved Invoice Posting).
Note: If the work order scope specified for this invoice
 line is not assigned a phase, a message displays indicating that the phase
 is missing. You can still save the record, but you must assign a phase code
 to the work order scope before you post the invoice in AP Unapproved Invoice
 Posting.

## Description

Entry in this field is not required.
Enter the description of this invoice item, up to 30 characters. Initially defaults the header description, but may change depending on the line type entered.

- Job – If you checked the "Default Header Description to Lines on Job Type" option (AP Company Parameters), the header description will be used as the line description. If you did not check this option, the phase description will default as the line description.

- Inventory – Defaults the material description.

- Expense – Defaults the header description.

- Equipment, Work Order – Defaults the cost code description. If you selected the ‘Default header description to lines on equipment type’ checkbox in AP Company Parameters, this field defaults the value in the header Description field.

- PO & SL – Defaults the PO item description or SL item description, respectively.

If a material is specified for the line, description defaults as follows:

- Job or Expense – Defaults the material description from HQMT (HQ Materials). If an non-valid material, description will default as 'Not in material file'.

- Equipment or Work Order – Defaults the material description from EMEP (Equipment Parts), HQMT (HQ Materials), or POVM (PO Vendor Materials). If a work order may also default from EMWP (Work Order Parts). If the material exists in more than one table, it will use the description from the first table in which the material is located. For example, if the material exists in both Equipment Parts and Vendor Parts, but you select the material from Vendor Parts in the F4 lookup, it will return the description from Equipment Parts because EMEP is checked before POVM.

## Reviewer Group

The Reviewer Group field on the AP Unapproved Invoice Entry form, Info tab of Invoice Lines section.
If a group exists for the job, location, or
 equipment, that group defaults here.
You may enter a different reviewer group for this invoice line.
Press F4 for a list of active reviewer groups.
 Press F5 to access HQ Reviewer Group for reviewer-group management.
All reviewers without an assigned threshold amount display on the line Reviewers tab. If a reviewer has a threshold amount less than or equal to the amount in the Gross field for this line, they will default on the Reviewers line tab once you exit the form. For more information on setting threshold amounts, refer to HQ Reviewer Groups in Related Topics below.
Note: If you have defined rejection notification recipients for this
 group in HQ Reviewer Groups (Email Options for Rejection section), the system will send
 email notifications to the specified recipients when reviewers in this group reject this
 invoice in AP Unapproved Invoice Review. For more information, see the F1 help for the
 [Reject](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form#ID-00007706--en) checkbox in AP Unapproved Invoice Review.

### Re-Adding Reviewers to an Invoice Line

If you delete a reviewer from an invoice invoice line that was initialized via a reviewer group, you can manually add the reviewer back to the invoice line as needed.
 However, if you use the AP Unapproved Invoice Status form and plan to filter by responsible person, you cannot use the manual method to re-add reviewers to the invoice line, as it will result in the invoice being excluded from the result set when filtering by the responsible person associated with that reviewer group.
Instead, you must delete the reviewer group from the invoice line, save the record, and then reassign the reviewer group to the invoice line. This ensures that all reviewers in the group are properly initialized to the invoice line. Then when filtering by that responsible person in AP Unapproved Invoice Status, the invoice is included in the filtered results.

[](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)HQ Reviewer Groups

## GL Co#

The GL Co# field on the AP Unapproved Invoice Entry form,
 items Info tab.

This field is enabled for Expense lines only (type 3-Exp).
Specify the GL company for this invoice item. Initially defaults the GL company specified in AP Company Parameters.
For all other line types, this field defaults as follows:

- Job - Defaults the GL company assigned to
 the JC company in JC Company Parameters.

- Inventory - Defaults the GL company
 assigned to the IN Company in IN Company Parameters.

- Equip / EM Work
 Order - Defaults the GL company assigned to the EM company in EM
 Company Parameters.

- PO / SL - These
 two modules have a one-to-one relationship with AP; therefore, this field defaults
 the GL company assigned to the active AP company.

- SM Work Order - Defaults the GL company
 specified for the department assigned (in SM Departments) to the work order's service
 center.

## GL Acct

This field initially
 defaults a GL account based on the transaction line type:

- 1-Job - Defaults from the JC Departments form. If you did not
 select the Allow GL Account override
 when posting cost checkbox in the JC Company Parameters form (GL Cost
 tab), the system will disable this field. If the default is blank, the system will
 allow entry in this field; however, once the line is saved, the system disables the
 field. If you selected the Allow GL
 Account override when posting cost checkbox, the system enables this
 field and you can override the value.

- Defaults from IN Locations. If you did not select the Allow GL Account
 overrides checkbox in IN Company Parameters, the system will disable
 this field. If the default is blank, the system will allow entry in this field;
 however, once the line is saved, the system disables the field. If you selected the
 Allow GL
 Account overrides checkbox, the system enables this field and you can
 override the value.

- 3-Expense - Defaults from AP Vendors, unless a non-stocked
 material is specified, in which case, this field defaults from the Non-Stocked GL
 Account field in HQ Material Categories.

- 4-Equipment - Defaults from the EM Departments form. If you did not select the
 Allow GL Account Override checkbox in the EM Company
 Parameters form, the system will disable this field. If the default is blank, the
 system will allow entry in this field; however, once the line is saved, the system
 disables the field. If you selected the Allow GL Account
 Override checkbox, the system enables this field and you can override
 the value.

- 5-EM Work Order - Defaults from the EM Departments form. If you did not check the
 Allow GL Account Override checkbox in the EM Company
 Parameters form, the system will disable this field. If the default is blank, the
 system will allow entry in this field; however, once the line is saved, the system
 disables the field. If you checked the Allow GL Account
 Override checkbox, the system enables this field and you can override
 the value.

- 6-Purchase Order - Defaults from the purchase order. If a job PO item, defaults as
 follows:

- If the job is open and the JC Dept GL account is blank, this field defaults
 the GL account from the PO item.

- If the job is open and the JC Dept GL account is not blank, but you have
 checked the Allow GL Account override when posting
 revenue box in JC Company Parameters, this field defaults the GL
 account for the PO item. If you did not check the box, this field defaults the
 GL account from the JC department. The system will display a message warning
 that the defaulted GL account does not match the PO item's GL account.

- If the job is closed (final) and the JC Dept closed GL account is blank, the
 GL account defaults as blank. The system will display a message warning that
 the defaulted GL account does not match the PO item's GL account. If you did
 not check the Allow GL Account override when posting
 revenue box (JC Company Parameters), manual entry is required,
 as initialization cannot occur.

- If the job is closed and the JC Dept closed GL account is
 not blank, this field defaults the closed GL account from JC Departments. The
 system will display a message warning that the defaulted GL account does not
 match the PO item's GL account.

Note: For PO items referencing an
 SM work order, this field is disabled.

- 7-Subcontract - Defaults from the subcontract as follows:

- If the job is open and the JC Dept GL account is blank, this field defaults
 the GL account from the subcontract item.

- If the job is open and the JC Dept GL account is not blank, but you have
 checked the
 Allow GL Account override when posting revenue
 box in JC Company Parameters, this field defaults the GL account
 for the subcontract item. If you did not check the box, this field defaults the
 GL account from the JC department. The system will display a message warning
 that the defaulted GL account does not match the subcontract item's GL
 account.

- If the job is closed (final) and the JC Dept closed GL account is blank, the
 GL account defaults as blank. The system will display a message warning that
 the defaulted GL account does not match the subcontract item's GL account. If
 you did not check the
 Allow GL Account override when posting revenue
 box (JC Company Parameters), manual entry is required, as
 initialization cannot occur.

- If the job closed and the JC Dept closed GL account is not
 blank, this field defaults the closed GL account from JC Departments. The
 system will display a message warning that the defaulted GL account does not
 match the subcontract item's GL account.

- 8-SM Work Order - The
 GL
 Acct
 field is always disabled for this line type and will derive the Misc
 Cost account from the SM department as follows:

- If you specified a division on the work order scope and an alternate
 department is assigned to the division, the system uses the following hierarchy
 to determine the correct account to use:

1. The system looks for a cost type category/call type/cost type override
 (in SM Departments, Overrides tab) based on the SM cost type entered for
 the invoice line, the cost type category assigned to the SM cost type,
 and the call type specified for the work order scope. If one exists, it
 will use that account.

1. If no cost type category/call type/cost type override is defined, the
 system will then look for an override cost type category/call type or
 cost type category/cost type, and if found, use it.

1. If no override accounts are defined by cost type category/call type or
 cost type category/cost type, the system will use the standard account
 defined for the cost type category at the department level (SM
 Departments, Info tab).

1. If no SM cost type is specified for the invoice line, the system will
 use the standard Other account defined in SM Departments (if no material
 is entered) or the Material account defined in SM Departments.

- If no alternate department is assigned to the division or no division is
 assigned to the work order scope, the system will use the department assigned
 to the service center to determine the default account using the same process
 defined above.

## UM

The UM field on the AP Unapproved Invoice Entry form, Items section, Info tab.

Entry in this field is required if entering units and unit cost. If left blank, the Units and UC fields are disabled.
Enter a valid unit of measure for this invoice item or accept the
 default.
If you entered a material, this field defaults based on the line type
 as follows:

- Job, Inv, Exp, and SM Work Order - If you entered a valid HQ
 material or IN Material (2-Inv lines only), this field defaults the Purchase UM
 from HQ Materials (HQMT). You may override the default, but it must be a valid
 unit of measure for that material.If overrides exist for
 the specified material/vendor in PO Vendor Materials (POVM), this field
 defaults the vendor material UM matching the Purchase UM in HQMT. If no
 match is found, defaults the lowest UM for the vendor/material
 group/material.

- Equip - If the selected material exists in EM Equipment
 Parts (EMEP) for the equipment, this field defaults the UM from EMEP, if it
 matches the Purchase UM in HQ Materials; otherwise, defaults the Purchase UM
 from HQMT. If you selected a vendor material that does not
 also exist in EMEP, defaults the vendor material UM if it matches the HQMT
 Purchase UM; otherwise, defaults the lowest UM in POVM for the
 vendor/material group/material.
 If material does
 not exist in EMEP or POVM, defaults the HQMT Purchase UM.

- EM Work Order - If the selected material exists in EM Work
 Order Parts (EMWP) for the work order, defaults the UM from EMWP, regardless of
 whether it matches the HQMT Purchase UM.If you select a
 material from EM Equipment Parts that does not also exist in EMWP for the
 work order, the UM defaults from EMEP if matches the HQMT Purchase UM;
 otherwise, defaults the HQMT Purchase UM.
 If you
 select a vendor material that does not also exist in EMWP or EMEP for the
 work order, defaults the vendor material UM if it matches the HQMT Purchase
 UM; otherwise, defaults the lowest UM in POVM for the vendor/material
 group/material.
 If material does not exist in
 EMWP, EMEP, or POVM, defaults the HQMT Purchase UM.

- PO and SL - Defaults the unit of measure specified for the
 PO or SL item. This default cannot be overridden.

Note: If you enter a non-valid material (Job, Exp, Equip, EM Work
 Order, and SM Work Order lines only), the UM will defaults as LS. You can override
 this default with any valid unit of measure.

If you did not enter a material (all line types except Inventory,
 which requires entry of a material), defaults are follows:

- Job - If the Default JC Job Phase UM on job lines checkbox is selected in AP
 Company Parameters, this field defaults the UM from the cost type specified for
 invoice line (as defined in JC Job Phases). If the Default JC Job Phase UM on job
 lines checkbox is not selected, this field defaults the unit of
 measure as LS (lump sum).

- Exp, Equip, EM Work Order, and SM Work Order - Defaults as
 LS.

- PO and SL - Defaults from the purchase order item or
 subcontract item; cannot be overridden.

## Units

The Units field on the AP Unapproved Invoice Entry form, Items section, Info tab.

This field is disabled and set to 0.00 if the UM is LS (Lump Sum).
Required for non-LS units of measure.
Enter the number of units for this invoice item.
If this is a purchase order line and the
 invoiced units exceed the PO's received units, a warning displays. If the Allow Invoice to Exceed
 Received checkbox is selected in AP Company Parameters, the entry is
 allowed and you can post the batch (via AP Unapproved Invoice Posting). However, if the
 checkbox is not selected, you must correct the invoiced units in order to save the
 line.
Note: Units posted to job lines are only
 updated to JC Cost Detail (JCCD) if you selected the Update Actual Units From AP
 option for the specified job in JC Jobs. If option is no selected, units are set to
 0.00 in JCCD.

## UC

The UC field on the AP Unapproved Invoice Entry form, Items section, Info tab.

Enter the unit cost for this invoice item or accept the defaulted value.
If you specified a material for this invoice item that is set up for
 the vendor in PO Vendor Materials, the unit cost defaults based on the vendor's setup,
 regardless of line type. Otherwise, this field defaults for each line type as
 follows:
 This field initially defaults as follows:

- Job, Exp, Equip, EM Work Order, and SM Work Order - If you
 specified a material, defaults the unit cost from HQ Materials. If you did not
 specify a material, defaults as 0.00.Note: For Job lines only, the
 system only updates the unit cost to JC Cost Detail (JCCD) if you
 selected the Update Actual
 Units From AP checkbox for the job in JC Jobs. If the
 checkbox is not selected, the unit cost is set to 0.00 in JCCD.

- Inv - Defaults the Last Unit Cost defined in IN Location
 Materials.

- PO and SL - Defaults the unit cost defined on the purchase
 order or subcontract.Note: If you change the unit
 cost for a PO or SL item, a warning displays indicating that the unit
 cost is different than the PO or SL unit cost, and that committed costs
 will be reduced by units at the PO or SL unit cost. Changes are not
 updated to the related PO or SL files.

## ECM

 Entry in this field is not required.
 Specify which quantity the unit cost represents:
 E = Cost is per each unit.
 C = Cost is per 100 units.
 M = Cost is per 1000 units.

## Gross

The Gross field on the AP Unapproved Invoice Entry form,
 items Info tab.
Enter the total amount for this invoice item or accept the default
 (units x unit cost).
If the unit of measure for this item is other than LS (lump sum),
 changes to this amount will cause the unit cost to be recalculated.
Purchase Order LinesIf you enter a Gross amount for an item with 0.00 units
 and a non-LS (lump sum) unit of measure, a message displays warning you that
 entering a gross amount without units could cause problems, and that for Job
 Type items, it will cause committed costs to be improperly updated. However,
 entry is allowed.In addition, the system checks the
 invoice amount for each item and if it exceeds the current total cost of
 the PO item and/or PO, a warning displays; however, the entry is
 allowed.
If the Allow Transactions to Exceed
 Item's Current Total Cost and/or Allow Transactions to Exceed PO's
 Current Total Cost checkboxes in AP Company Parameters
 are selected, the system will not allow you to post the batch until the
 invoiced amounts are corrected.
The system
 also checks to see if the invoiced amount exceeds the PO's received
 amount and if it does, a warning is displayed. If the Allow Invoiced to Exceed
 Received checkbox is selected in AP Company Parameters,
 the entry is allowed. If the checkbox is unselected, you cannot save the
 line until you correct the invoiced amount.
Subcontract LinesThe system checks the invoiced amount for each item
 and if it exceeds the current total cost of the subcontract item or
 subcontract, a warning displays, but the entry is allowed. However, once
 the invoice is approved and added to an AP batch, if the Allow Transactions to Exceed
 Current Total Cost checkbox is not selected in AP
 Company Parameters, you will be unable to post the batch until the
 invoiced amounts are corrected.
Note: The system
 will perform another check once all items are entered and accepted.
 If the total of all items exceeds the total remaining amount
 available on the subcontract, another warning is displayed, but
 amount is allowed. This verification allows for the condition of a
 deduct item not invoiced, which could then result in an
 overpayment

SM Work Order LinesThe Gross amount is sent to the specified SM work
 order as "actual cost". If you also entered taxes and a miscellaneous
 amount (with Included checkbox selected), those amounts are included
 in the actual cost sent to SM.
Note: If the SM
 work order is job-related, the resulting actual cost is updated to
 Job Cost using the phase and JC cost type associated with this
 line.

### Amt

Specify the payable amount for this invoice item, or accept the default. If unit of measure is other than LS (lump sum), changes to this amount will cause the unit cost to be recalculated.
Purchase Order Lines
If you enter an amount and the item's units are 0.00 and the UM is not LS, the system provides a warning, but entry is allowed.
The invoiced amount for each item
 is checked to see if it exceeds the current total cost of the PO item and/or PO. If it
 does, a warning is displayed, but the entry is accepted. However, if the Allow Transactions to
 Exceed Item's Current Total Cost and/or Allow Transactions to Exceed PO's Current Total
 Cost checkboxes are selected in the AP Company Parameters form, you will be unable to
 post the batch until the invoiced amounts are corrected.
The invoiced amount will also be checked to
 see if it exceeds the PO's received amount. If it does, a warning is displayed.
If the
 Allow Invoiced
 to Exceed Received checkbox is selected in the AP Company Parameters form, the entry will
 be allowed. However, if not selected, you will be unable to save the line until the invoiced
 amount is corrected.
Subcontract Lines
The invoiced amount for each item will be checked to see if it exceeds the current total cost of the subcontract item or subcontract. If it does, a warning is displayed. If the Allow Transactions to Exceed Current Total Cost checkbox is selected in the AP Company Parameters form, the amount will be allowed. Another check will be done at the header level once all items have been entered and accepted. If the total of all items exceeds the total remaining amount available on the subcontract, another warning is displayed. Total amount will be allowed if the “Allow transactions…” checkbox is selected. This verification allows for the condition of a deduct item (subcontracts) not invoiced, which could then result in an overpayment.

## Misc Amt

The Misc Amt field on the AP Unapproved Invoice Entry form,
 items Info tab.

Enter the miscellaneous amount for this invoice item. Typically used to
 enter freight or other miscellaneous charges.
If you select the Included
 checkbox (to the right), the system includes this amount in this line’s total. However,
 this amount is not included in this line's tax, discount, or retainage calculations.
The system also excludes this amount:

- When checking the item's invoiced amount against the current total cost of the PO/PO
 Item or SL/SL Item.

- From the total committed cost in APJC (AP JC Distributions) for standing PO's where
 the unit of measure is LS and the PO is not flagged for receiving.

- When updating the Received Cost and Invoiced Cost amounts in POIT (PO Items).

- When updating the Invoiced Cost amount in SLIT (SL Items).

### SM Work Orders

For SM work order related lines, this amount is handled as
 follows:

- For PO lines (type 6-PO) referencing a purchase order item
 that is associated with an SM Work Order, this amount is included in the actual
 cost updated to the work completed purchase line (in SM Work Orders, Work
 Completed tab).If multiple work completed purchase lines
 exist that reference the same PO item, the actual cost will be allocated
 proportionately across the work completed lines.

- For SM Work Order lines (type 8-SM Work Order), this amount
 is included in the Cost UC, Cost Subtotal, Cost Rate, and Total Actual Cost
 amounts updated to the work completed line.

## Included

The Included checkbox on the AP Unapproved Invoice Entry
 form, items Info tab.

Select this checkbox to include the Misc Amt in this line's total amount.
 The Misc Amt is not included when calculating tax, discount, or retainage amounts for this
 line.
Leave this checkbox unselected to exclude the Misc
 Amt from this line's total amount.
 For all line types except Inventory and SM Work Orders, the Misc Amt is not
 charged to Job Cost, Equipment, or General Ledger. It is a memo entry only and is only useful if
 writing reports to pull this miscellaneous amount.
Inventory LinesIf you selected the Burdened Unit Cost - include AP Misc Amt
 and Tax checkbox in IN Company Parameters, the Misc amount is handled as
 follows:

- If this checkbox is selected, the Misc Amt is included in the AP
 invoice total, the Inventory and AP accounts are debited/credited with the total amount,
 and the total (including the Misc Amt) is included in the unit cost for the Inventory
 location.

- If this checkbox is not selected, the Misc Amt is excluded from the
 AP invoice total, but is included in the unit cost for the IN location. The Inventory
 account is debited with the total amount (including the Misc Amt), the AP account is
 credited with the gross amount (total less the Misc Amt), and the Misc Amt is credited to
 the location's Miscellaneous Expense account. When posting the freight vendor's invoice for
 the Misc Amt, the entry should be posted to offset the Miscellaneous Expense amount.

SM Work Order LinesInvoice items with this line type automatically generate a work
 completed line in SM Work Orders (Work Completed tab) once the batch is posted. The Misc work
 completed line is updated as follows:

- If this checkbox is selected, the Misc Amt is included in the AP
 invoice total, and the resulting Misc work completed line includes the Misc Amt in the Cost
 UC, Cost Subtotal, Cost Rate, and Total Actual Cost amounts.

- If this checkbox is not selected, the Misc Amt is excluded from the
 AP invoice total, and the resulting Misc work completed line excludes the Misc Amt from the
 Cost Rate and Total Actual Cost amounts; however, it does include the Misc Amt in the work
 completed line's Cost UC and Cost Subtotal amounts.

## Ret%

Entry in this field is not required.
Specify the percentage at which retainage is calculated for this item, or accept the default.
Note:Retainage can be entered with any line, but is typically only used with job-related transactions.

## Ret Amt

Entry in this field is not required.
If a Ret% was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount. Accept the default, or enter the retainage amount. If you change the default amount, the retainage percentage is recalculated.

- A line’s retainage amount cannot exceed the line’s gross amount. If this occurs, a warning displays, and the amount must be corrected before the line can be saved).

- Retainage is not calculated on Tax or Misc amounts. Additionally, the retainage portion of the invoice line is automatically placed on hold using the Retainage hold code specified in AP Company Parameters.

## Disc%

Entry in this field is not required.
Specify the percentage at which discounts for this invoice item will be calculated, or accept the default. Discount rate initially defaults from the Vendor’s payment terms (specified in invoice header). If the line’s type is PO or SL, the discount rate defaults from the payment terms specified for the purchase order or subcontract.

## Disc Amt

Entry in this field is not required.
If a Disc % was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount (less retainage, if any). Accept the default, or enter the discount amount. If you change the default amount, the discount percentage is recalculated.
Note:Discounts are not calculated on Misc amounts. Also, if you enter a discount amount here, a discount date must be entered in the header. If a discount date is not entered, a warning displays when you validate the batch (AP Batch Process).

If using tax discounts (flag in AP Company Parameters), the discount will be taken by subtracting this amount from the invoice's gross amount to get the tax basis.

## Tax Type

The Tax Type field on the AP Unapproved Invoice Entry form, items Info tab.

Specify the tax type for this item.

- 1-Sales – Tax amounts are payable to the vendor and are
 added to the invoice total. This tax amount is directly charged to Job Cost,
 Equipment, and GL.

- 2-Use (US only) - Tax amounts are accrued, and will be paid
 at a later date to the appropriate State or Local taxing authority. Calculated
 tax amounts do not affect the gross or net balance due to the vendor. Instead,
 the transaction's gross amount and tax amount is charged to Job Cost, Equipment,
 and GL account with an offsetting liability account as defined in HQ Tax Codes.
 Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) - This tax is paid on goods and
 services at each stage of production or distribution, and is based on the value
 added at each stage. This tax is not directly expensed; it is tracked in the GL
 and reduces the payment to a taxing authority through an Input Tax Credit (ITC).
 Use the AP Value Added Tax Report to obtain an itemization of VAT amounts. This
 is the default tax type for Australian and Canadian companies.

Note: For non-SM Work Order lines, if you
 specify a material for the invoice item and the material is non-taxable, this field
 defaults as blank, but may be overridden.

### SM Work Completed Lines

For invoice lines posted to an SM Work Order (line type 8), the
 system defaults the tax information based on the SM Cost Type entered on the invoice
 line, and the Matl Tax Override and Tax Option Override options selected on the
 associated work order scope. You may override the defaults as needed.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the AP
 vendor is not assigned a tax code and the work order scope's
 tax source (service site or service center) is not assigned
 a tax code, all tax fields default as blank, but may be
 overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase
 OnlyM - Taxable at Purchase/Markup at
 Billing
F - Full Tax at Purchase
 and Billing
If Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not TaxableB
 - Taxable at Billing Only
AllBlank
BlankP - Taxable at Purchase
 OnlyM - Taxable at Purchase/Markup at
 Billing
F - Full Tax at Purchase
 and Billing
If Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not TaxableB
 - Taxable at Billing Only
AllBlank

When you post an AP Transaction Entry batch, the system
 auto-generates a separate Misc work completed line on the specified work order (in
 SM Work Orders) for each SM Work Order invoice line. The Tax Type specified here for
 each line updates the Cost Tax
 Type field on the generated miscellaneous work completed line.
Note: For invoice lines posted to a
 Purchase Order (line type 6), if the PO item is posted to an SM Work Order, the
 AP tax information will only update the AP History tab on the SM Work Completed
 Purchase form. Only the tax information posted to the purchase order item will
 appear on the work completed purchase line.

### Intercompany Transactions

The tax type you select determines whether the selling company or the purchasing company is responsible for paying tax. The system defaults the appropriate tax rate and tax code based on the responsible company's associated tax group (HQ Tax Codes and Rates field, HQ Company Setup, Add’l Info tab).
For sales and value added tax, the system validates/defaults the tax code based on the selling company's tax group. For use tax, the system validates/defaults the tax code based on the purchasing company's tax group.

## Tax Code

The Tax Code field on the AP Unapproved Invoice Entry form, items Info tab.

If posting taxes to this item, specify a valid tax code (HQ Tax Codes), or accept the default. This field defaults as follows:

- 1-Job – The tax code default is determined by the Base Tax On field in JC Jobs. If set to J-Job, the tax code defaults from JC Jobs. If set to V-Vendor, the tax code defaults from AP Vendors. If set to O-Vendor Override, the tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code defaults from JC Jobs. You can override the default as necessary.

- 2-Inv – Defaults the tax code from IN Locations, unless the material is not taxable, in which case, defaults as blank.

- 3-Exp – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank.

- 4-Equip – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank

- 5-EM Work Order – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank

- 6-PO – Defaults the tax code from the purchase order item

- 7-SL – Defaults the tax code from the subcontract item

- 8-SM Work Order – Defaults based on work order type:

- Customer Work Order - If Tax Type is Sales or VAT, defaults the vendor tax code. If no vendor tax code exists, defaults the tax code from the work order's tax source (service site or service center). If no tax code assigned to the tax source, defaults as blank.If the Tax Type is Use, defaults the tax code from the work order's tax source (service site or service center). If no tax code assigned to the tax source, defaults as blank.

- Job Work Order - For Sales, VAT, and Use tax types, this field defaults based on the Base Tax On field in JC Jobs. See the description for Job lines above.

Committed CostsIf you specified a job (JC, PO, or SL line types) for this line and you post taxes to the line, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- if phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- if a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- if a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.

- if phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

Intercompany TransactionsFor Sales or VAT tax, the tax code defaults based on the Tax Group assigned to the AP Company. For Use tax, the tax code defaults based on the Tax Group assigned to the 'posted to' company.

## Tax Basis

The Tax Basis field on the AP Unapproved Invoice Entry form, line items Info tab.

This field is only enabled if you enter a Tax Type and Tax Code for the line.
Enter the amount of this transaction that is taxable or accept the defaulted value. Typically, the default value will be equal to the line's gross amount; however, if you are using tax discounts (the Using tax discounts checkbox is selected in AP Company Parameters), this field defaults the line's gross amount less the discount amount.
Note: If you entered an amount in the Misc Amt field, that amount is not included in the Tax Basis amount.

Note: Tax amounts posted to subcontract lines are not included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set up a subcontract to include sales tax, it is suggested that you post invoices with the tax amount included as part of the gross amount and set this field to 0.00. If the subcontract is set up without tax and sales tax applies, then gross and sales tax amounts should be entered separately on the invoice line.

## Tax Amt

The Tax Amt field on the AP Unapproved Invoice Entry form, line items Info tab.
This field defaults an amount based on the Tax Basis times the Tax Code rate; may be overridden.

### Subcontract Lines

Tax amounts posted to subcontract lines are not included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set up a subcontract to include sales tax, it is suggested that you post invoices with the tax amount included as part of the gross amount (not posted separately here). If the subcontract is set up without tax, and sales tax applies, the gross and sales tax amounts should be entered separately on the invoice line.

### SM Work Order Lines

When you process this transaction (via AP Transaction Entry or AP Unapproved Invoice Posting), the system automatically generates a work completed miscellaneous line (in SM Work Orders) for each invoice line posted to line type 8-SM Work Order. Tax information entered on these lines will populate the Cost Tax fields on the work completed line.
Note: If the value in this field is not 0.00, you must enter a value in the SM Cost Type field. If you leave the SM Cost Type blank, an error displays indicating that the SM Cost Type is missing and is required for proper tax distribution. The system saves the line, but you must specify an SM Cost Type before you can post the invoice via AP Transaction Entry or AP Unapproved Invoice Posting.

## Pay Category

This field displays only if you selected the
 Using
 Payable Category checkbox in AP Company Parameters.
Specify a valid pay category for this line. The pay
 category specified here, along with the line type (Type field), will determine the
 default pay type (next input).
Initially defaults a pay category as follows:

- If you have set up a standard or user pay category override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the company, default will be null. (In this case, the pay type will default from AP Company Parameters based on the line's type.)

The default may be overridden if you allow overrides
 to pay type (you selected the Allow Payable Type Override checkbox
 in AP Company Parameters); otherwise, input is disabled.
Purchase Order Lines (Line Type 6)
The pay category and pay type always default from the PO item, regardless of whether overrides exist in F3, VA User Profile, or AP Company Parameters. This is true even if you turn off the "Using Payable Category" flag in AP Company Parameters after you have already implemented its use. Although the pay category is not visible, its assignment will remain in effect.
If a pay category and pay type were not specified for the PO item, the pay category and pay type default based on the standard hierarchy (F3, VA User Profile, AP Company Parameters) and the PO item's line type.

## Pay Type

The Pay Type field in AP Unapproved Invoice Entry, Lines section, Info tab.
Required.
Specify the pay type for this item. If you are using pay categories (flag in AP Company Parameters), defaults the pay from this line's pay category based on the line type. The pay type used for each line type is as follows:

- Job lines - Use the Job pay type

- Inv, Exp, Equip, and EM Work Order lines - Use the Expense pay type

- PO lines - Use the pay type assigned to the PO item.

- SL lines - Use the Subcontract pay type

- SM Work Order lines - Use the SM Work Order pay type

If you allow pay type overrides (flag in AP Company Parameters), you may override the default.
 If you are using pay categories, the pay type must be either assigned to the specified pay category (in AP Pay Category) or an 'unassigned' pay type (a pay type that has not been restricted to a pay category in AP Payable Types). If you are not using pay categories, you can specify any pay type, regardless of whether the pay type is restricted to a pay category.Note: You can only enter a pay type that is not designated for retainage in AP Company Parameters or for a pay category in AP Pay Category.

## Supplier

 Entry in this field is not required.
 Indicate the supplier (from AP Vendors) for
 this item, if applicable. Note that if a supplier is entered here, payment will be made
 with a 2-party check.

## Reviewer

The Reviewer field on the Reviewer tab of the AP Unapproved Invoice form, Lines section.

Enter the reviewers' ID's. Press F4 for a list of active reviewers.
Defaults will be as follows:
This field defaults all reviewers assigned at the header level, as well as reviewers assigned to vendor.
 If this is a job line, defaults all reviewers (with a reviewer type of Invoice or Both) assigned to the specified job in JC Jobs.
 If this is an equipment-related line, defaults the reviewer specified in the Invoice Reviewer field in EM Departments. Additionally, defaults all reviewers associated with the group specified in the Invoice Reviewer Group field.
 If this is an Inventory line, defaults the reviewer specified in the Invoice Reviewer field in IN Locations. Additionally, defaults all reviewers associated with the group specified in the Invoice Reviewer Group field.
If this is a customer work order line, defaults the reviewer specified in the Reviewer field in SM Work Order. If it is a job work order, defaults according to the job.

### Re-Adding Reviewers to an Invoice Line

If you delete a reviewer from an invoice invoice line that was initialized via a reviewer group, you can manually add the reviewer back to the invoice line as needed.
 However, if you use the AP Unapproved Invoice Status form and plan to filter by responsible person, you cannot use the manual method to re-add reviewers to the invoice line, as it will result in the invoice being excluded from the result set when filtering by the responsible person associated with that reviewer group.
Instead, you must delete the reviewer group from the invoice line, save the record, and then reassign the reviewer group to the invoice line. This ensures that all reviewers in the group are properly initialized to the invoice line. Then when filtering by that responsible person in AP Unapproved Invoice Status, the invoice is included in the filtered results.

## Approval Seq

 If manually assigning reviewers to this invoice line, enter the sequence
 number (0-255) for this reviewer.
 If you assigned reviewers at the header level, all reviewers assigned at that level default to this grid. If you wish to change the sequence for a reviewer, you will need to delete the reviewer, then re-add them with the correct sequence.
 If you assigned reviewers at the job, EM
 department, and/or IN location levels (JC Jobs, EM Departments, and IN Locations), they
 will also default to this grid when the specified job, equipment, or location is referenced
 on an invoice line.
 If you assigned a reviewer group at the header and/or the line level, reviewers default to this grid with the sequences specified in HQ Reviewer Groups.
If you are using a hierarchical method of invoice approval, this sequence number should represent the order in which this reviewer is to review and approve this invoice line. For example, if this reviewer must approve this invoice line before anyone else, enter “1” as the sequence. Reviewers with sequences greater than “1” are unable to review and approve this invoice line until this reviewer has marked it as approved. If not using a hierarchical method, assign all reviewers a sequence of “1”.

## Optional Reviewer

The Optional Reviewer checkbox in the AP Unapproved Invoice Entry lines section, Reviewers tab.
When this checkbox is selected, this reviewer is designated as optional on this line, which allows for one of several reviewers to approve at a given approval sequence.
You can change this setting at the line level without affecting any other invoice lines or approval sequences. On the other hand, if the reviewer on this line also appears in the header Reviewer tab, changes to the Optional Reviewer checkbox in the header affects all lines to which this reviewer is assigned.
As long as more than one optional reviewer is assigned to each invoice line’s approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line’s approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line’s approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance.

- if ALL reviewers on a sequence are set as optional, at least one must approve

- if ALL reviewers on a sequence are set as non-optional (Optional Reviewer checkbox is not selected), all must approve

- if some reviewers on a sequence are set as non-optional and some as optional, all non-optional must approve

## Approve with missing data

Approve with missing data checkbox in the AP Unapproved Invoice Entry form footer, Reviewers tab.
Select this checkbox if your review process requires this reviewer to approve this line, even though some required data is still missing. This allows the reviewer to approve the lines that lack data, which allows the line to progress in the review process. The missing data must still be entered before posting, but can be entered at some time after this reviewer's approval.
The default value comes from the setting for this reviewer in the header. Changes you make to this checkbox will only affect this invoice line. If you wish to make changes for every line this reviewer is assigned to on this invoice, and if the reviewer is already listed in the header, make the change on the header instead.

## Memo

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Add Standard Notes
To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box and click the right mouse button. From the shortcut menu, select the Standard Notes option, which brings up the Std Note Copy window. Enter the standard note to copy and click OK to add the note. Note will be appended to the end of existing note text (if applicable).
Spelling Check
A spell check can be run for any notes entered in this window. Click the Spelling button in the toolbar () or select the Spelling option from the Tools or shortcut menu.
Tip: To use the Tab feature (such as to indent the first
 line of a paragraph or create columns), you will need to press Ctrl + Tab for each tab increment.

## Rejected

Used to indicate whether this line has been rejected; you cannot reject an invoice line here.
The system automatically selects this box when any reviewer rejects the invoice line in the AP Unapproved Invoice Review form. If the checkbox is selected, you can only access this field to clear it once the invoice line is ready for the reviewer to review it again.
Note:You must deselect this checkbox manually for all invoice lines.

## Reject Reason

 This field is display only. This field defaults the rejection reason specified by this reviewer for this invoice line in AP Unapproved Invoice Review.
