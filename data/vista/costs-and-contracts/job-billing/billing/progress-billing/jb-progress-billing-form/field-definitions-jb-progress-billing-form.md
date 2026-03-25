---
title: "Field Definitions: JB Progress Billing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form/field-definitions-jb-progress-billing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form/field-definitions-jb-progress-billing-form"
---

# Field Definitions: JB Progress Billing Form

The following is a list of field descriptions for the JB
 Progress Billing form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Bill Month

 Enter the bill month of the invoices to review, edit, or add.

##  Bill Number

 Enter the bill number of the invoice to review/edit. Press F4 for a list of valid bill numbers. If you are adding a new billing, enter “N” or “New”, and the system assigns the next sequential bill number when the record is saved.

- If you specify a billing in a closed month, a warning is displayed (in blue) at the top of the form. You can make changes to 'closed-month' billings; however, you cannot add or delete billings in a closed month.

- If you specify/add a billing and future billings exist for that contract/customer, a warning is displayed (in red) at the top of the form.

##  Invoice

 This field defaults as follows:

- If the Auto Sequence Invoice # option (JB Company Parameters) is not checked, this field defaults as blank and you must enter the invoice number manually. Up to 10 characters allowed.

- If the Auto Sequence Invoice # option is checked, but you did not elect to have invoice numbers assigned during initialization, this field defaults as blank and you must enter the invoice number manually.

- If the Auto Sequence Invoice # option is checked and you elected to have invoice numbers assigned during initialization, this field defaults the billing’s assigned invoice number. If you are manually entering a new billing, this field defaults the next available sequential invoice number.

Note: All billings must have an invoice number in order to be interfaced.

##  Contract

 If you initialized billings, this field defaults to the contract for the billing and is disabled.
 If entering this billing manually, specify
 the contract (JC Contracts) for this billing. Once you save the record, this field is
 disabled.
Closed Contracts
 Regardless of whether you are changing an existing billing or manually adding a new billing, if the billing's contract has been soft or hard closed (indicated in red to right of contract), the ‘Allow Posting to Soft-Closed Jobs’ and ‘Allow Posting to Hard-Closed Jobs’ options in JC Company Parameters determine how the billing is handled.

- If you allow posting to hard and/or soft-closed jobs, the contract's description reads, "Contract is closed”, but save is allowed.

- If you do not allow posting to soft or hard-closed jobs, in addition to the contract description indicating the contract is closed, you will receive the following message:

 Contract is soft-closed (or hard-closed). Billing not allowed.
 You will be able to save the billing, but you will be unable to enter any item values. This allows adding a bill header for the purpose of releasing retainage. Once you have released retainage and interfaced the billing, you will be unable to change information on the bill header.

##  Customer

 Defaults the customer assigned to the specified contract (JC Contracts);
 may be overridden.
 If a customer is not assigned to the contract, enter the customer to assign to this contract for this billing.

##  Application #

 Defaults a sequential number, assigned by the system based on the number of billings for this contract. If a previous billings does not exist for this contract, the field defaults to 1; may be overridden, but value must be between 0 – 32,767.

##  Invoice Desc

 Enter a description for this invoice, up to 30 characters. Initially defaults as JB App # XX (where XX represents the billing application number). Once this billing is interfaced, this description is updated to the Description column in ARTH (Transaction Header).

## Status

These options are available when billings are invoiced, but not yet interfaced.

- A-Active – Invoices initially default this status when a billing is first created.

- N-Never Interfaced – Select this status if this billing will never be interfaced. This option is typically used when a contract item requires both a Progress and T&M billing (defined in JC Contract Items), but only one billing is interfaced to prevent a duplicate billing in AR.

These options are available once a billing has been invoiced and interfaced.

- C-Change – Defaults to this status automatically when changes are made to Item or Change Order detail for a billing that has been previously interfaced. If changes are made to the Invoice, Due, or Discount Dates or the Payment Terms (header), this field must be changed to this status manually. Only billings with this status will update AR when re-interfaced.

- D-Delete – Select this option to delete a previously interfaced invoice. Only billings in an open month can be deleted. (Note: If you set a billing to this status and change orders exist for the billing, a message displays stating that the billing cannot be deleted until change orders are removed. Remove the change order by using JB Progress Bill Change Orders. When finished, reset this field to Delete.)

- I-Interfaced – Invoices that have been interfaced will automatically default this status.

##  Process Group

 This optional field defines the processing group for this contract billing. If a processing group was defined for the contract (JB Contract Info), the processing group defaults here.
Note: Even though a billing may be assigned a processing group, it does not have to be processed by group. It can be processed separately, if desired.

##  Receivable Type

 Defaults the receivable type specified for the contract (in JB Contract Info). If a receivable type is not specified for the contract, this field defaults the receivable type specified for the contract’s customer in AR Customers or AR Company Parameters (if a receivable type is not specified for the customer). The receivable type specified here determines which GL accounts will be updated when this billing is interfaced. This field may be overridden.

##  Restrict by Item Bill Group

 Check this box to restrict the initialization of contract items to this
 billing by bill group. When checked, only contract items with a bill group (assigned in JC
 Contracts) matching the one specified below (Item Bill Group) will be initialized.
 Leave this box unchecked if you want all contract items to be initialized to this billing, regardless of bill group.

##  Item Bill Group

 Specify the bill group, up to 20 characters, by which to restrict item
 initialization. All contract items assigned a bill group (in JC Contracts) matching this
 bill group will be initialized to the billing.

##  Invoice Date

 If billing was initialized, defaults the invoice date specified during initialization. If billing is entered manually, defaults current date. This field may be overridden.

##  Pay Terms

 If applicable, enter the payment terms for this contract. Initially
 defaults the payment terms specified for the contract in JC Contracts. If payment terms are
 not specified for the contract, defaults the payment terms specified for the customer in AR
 Customers. This field may be overridden.

##  Due Date

 Defaults due date based on payment terms. If payment terms are not specified, the due date will be the same as the invoice date. This field may be overridden.

##  Discount Date

 Initially defaults a discount date based on payment terms. If payment terms are not specified, defaults to null (blank). This field may be overridden.

##  From Date

 Specify the beginning date of the bill period for this bill. This field is optional and informational only.

##  To Date

 Specify the ending date of the bill period for this billing. This field is optional and informational only.

##  Address

 Defaults the override address specified for this contract in JB Contract Info or, if no override address specified, the billing address defined for the customer in AR Customers. If no billing address is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  City

 Defaults the override city specified for this contract in JB Contract Info or, if no override city specified, the billing city defined for the customer in AR Customers. If no billing city is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## State

Defaults the override state specified for this contract in JB Contract Info or, if no override state specified, the billing state defined for the customer in AR Customers. If no billing state is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
NOTES: The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Zip

 Defaults the override zip code specified for this contract in JB Contract Info or, if no override zip code specified, the billing zip code defined for the customer in AR Customers. If no billing zip code is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Country

Defaults the override country specified for this contract in JB Contract Info or, if no override country specified, the billing country defined for the customer in AR Customers. If no billing country is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
NOTES: Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Add'l Address

 Defaults the override additional address specified for this contract in JB Contract Info or, if no override address specified, the billing additional address defined for the customer in AR Customers. If no billing additional address is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Certified

 This field will only display if you have checked the Certify Progress Billing Claims box in JB Company Parameters.
 Check this box to certify this billing. When you check this box, the system ‘locks’ the Claimed Units and Claimed Amounts fields (Items tab) and will no longer update them with changes to This Bill WC Units and This Bill WC Amounts fields. This allows you to keep historical data in the event that you need to change the value in the This Bill WC Amount field. In addition, the Certify Date field is enabled.
 Leave this box unchecked if this billing is not certified.

##  Claim Date

 This field will only display if you have checked the Certify Progress Billing Claims box in JB Company Parameters.
 Enter the claim date for this billing. Initially defaults current date. Once you have marked this billing as ‘certified’, this field is disabled and cannot be changed.

##  Certify Date

 This field will only display when you have checked the Certify Progress Billing Claims box in JB Company Parameters, and is enabled once you check the Certified box.
 Enter the date this billing was certified. Initially defaults the current date.

## JB Reviewer Group

The JB Reviewer Group field on the JB Progress Billing form,
 Info tab.
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in JB Company Parameters.
If you are using the web-based Financial Controls application, this field interacts with the Financial Controls review process.
 Enter the reviewer group for this progress billing. Must be a reviewer group
 set up in HQ Reviewer Groups with a Reviewer Group Type of 3-Job Billing. Initially defaults the
 reviewer group assigned to the contract (in JC Contracts, JB Contract Info, or PM Contracts).
Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

Related information

- [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form)

## Assigned To

The Assigned To field on the JB Progress Billing form, Info
 tab.
When you create a new bill, the Assigned To field automatically
 populates with your username as the owner of the bill.
The Assigned
 To user can change or delete the bill.
If additional Bill Control Options are enabled in JB Company
 Parameters:

- Other users may have permissions to change or delete bills
 assigned to you.

- Even if you are assigned to a particular bill, you may not
 have permissions to change or delete the bill if the JB month has closed.

Note: For existing bills, if someone
 initializes or edits the bill, the Assigned To field defaults
 to the Created By user. For bills where Created
 By is blank, Assigned To populates with the
 user who saves the record.

## Ready for Review

The Ready for Review checkbox on the JB Progress Billing
 form, Info tab.
If you are using the web-based Financial Controls
 application, this checkbox interacts with the Financial Controls review process.
 Select this checkbox when this progress billing is ready to review. Once
 selected, the display fields to the right populate with the current User ID and
 Date.
Clear this checkbox if this billing is not ready to review or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Draft Approved

The Draft Approved checkbox on the JB Progress Billing form,
 Info tab.
If you are using the web-based Financial Controls application, this checkbox
 interacts with the Financial Controls review process.
 Select this checkbox if the draft bill is approved. Once selected, the
 display fields to the right populate with the current User ID and Date.
Clear this checkbox if the draft bill is not approved or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Sent to Customers

The Sent to Customers checkbox on the JB Progress Billing
 form, Info tab.
If you are using the web-based Financial Controls application, this checkbox
 interacts with the Financial Controls review process.
 Select this checkbox if the draft billing has been sent to the customer.
 Once selected, the display fields to the right populate with the current User ID and
 Date.
Clear this checkbox if the draft version of the billing has not been sent to the customer or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Approved for Billing

The Approved for Billing checkbox on the JB Progress Billing
 form, Info tab.
If you are using the web-based Financial Controls application, this checkbox interacts with the Financial Controls review process.
Select this checkbox when this progress bill is approved for billing.
Clear this checkbox if this progress bill is not approved or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Notes

Use this field to enter any miscellaneous notes about this progress bill item. The space allowance is virtually unlimited.
Note: Notes entered here apply only to the progress bill item; they do not apply to the contract item associated with this bill item. Contract item notes should be entered on the Item SM/Tax tab or in JC Contract Items/PM Contract Items.
Add Standard Notes
To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box and click the right mouse button. From the shortcut menu, select the Standard Notes option, which brings up the Std Note Copy window. Enter the standard note to copy and click OK to add the note. Note will be appended to the end of existing note text (if applicable).
Spelling Check
You can run a spell check for any notes entered in this window. Click the Spelling button in the toolbar () or select the Spelling option from the Tools or shortcut menu.
Tip: To use the Tab feature (such as to indent the first line of a paragraph or create columns), you will need to press Ctrl + Tab for each tab increment.

##  Item

 This column initially defaults all items on the contract initialized to
 this billing. Items can only be deleted if the selected item does not exist on another
 billing for the contract. Items may be added to a billing, but they must exist on the
 contract (JC Contracts) prior to addition here.
Note: If the contract for this billing is closed (indicated in red above the grid), you can only add items or make changes to existing items if the Post to Closed Jobs checkbox in JC Company Parameters is selected. A warning displays upon saving the line, but the save is allowed. If the checkbox is not selected, the warning displays and the line is not saved.

##  Std Item

 Displays the standard item code assigned this contract item in JC
 Contracts, if applicable.

##  Description

 Initially defaults the Bill Description specified for this contract item
 in JC Contracts. If a bill description does not exist, defaults the contract item’s
 description, which may be overridden (up to 60 characters allowed). Changes to the default
 description do not affect the bill description (or contract item description) in JC
 Contracts.

##  Unit Price

 Defaults the unit price specified for this contract item in JC Contracts
 (Items); may be overridden.

##  Contract Units

 This field defaults the current number of units for this contract item.
 This value is the sum of the original contract units specified for this item in JC
 Contracts (Items) and all approved change orders associated with this item. The value may
 be overridden if necessary, but only if the Allow Changes to Previous and Contract Amounts
 checkbox in JB Company Parameters is selected.

##  Contract Amount

 This field defaults the current total for this contract item. This value
 is the sum of the original contract total specified for this item in JC Contracts and the
 total of all approved change orders associated with this item. The value may be overridden
 if necessary, but only if the Allow Changes to Previous and Contract Amounts checkbox in
 JB Company Parameters is selected.

## Previous Units

This field defaults the total of previous units for this contract item, and is the sum of the last billing’s 'previous' and 'this invoice' units.
 You may only override this value if the
  Allow Changes
 to Previous and Contract Amounts box is checked in JB Company
 Parameters.
Note: If you change this value, the Previous Amount and %
 Complete values will be updated to reflect the change.
Warning: If you have checked the Automatic Update of Prev
 Billed and ChgOrder Amounts on Future Bills box in JB Company Parameters, it
 is highly recommended that you do NOT change this value, as it may cause inaccuracies when
 previous amounts are updated for future billings.

## % Complete

Enter the total percent of work completed on this item through this billing. The system automatically calculates the current billing amounts (This Bill Units, This Bill Amt) and to-date amounts (To Date Units, To Date Amt). If the value entered exceeds 100% for the item, a warning displays, but entry is allowed. (Note: This warning displays when there are current contract amounts or units, depending on the unit of measure; no warning displays if the contract is for zero units or dollars.)

- To have the system calculate the percent complete
 for you, leave this field blank and enter a value in the This Bill
 Units field instead.

- If you change the Previous Amount or Previous Units,
 the percent complete will be updated to reflect the change.

##  This Bill WC Units

 This field defaults an amount based on previous units and to-date units (To Date Units – Previous Units). This value may be overridden, but that will cause To Date Units to be recalculated.
 If you did not enter percent complete, enter the number of work complete units to bill on this invoice. The % Complete and To Date Units will automatically calculate.

##  This Bill WC Amount

 Defaults an amount based on Unit Price and This Bill Units. Overriding this value will cause the This Bill WC Units to be recalculated.

##  To Date Units

 If you entered a percent complete value (in % Complete field), this field defaults “to-date” units based on the previous units billed and the percentage completed through this billing. This value may be overridden, but will cause % Complete to recalculate.
 If you did not enter a percent complete, enter the total units to-date completed on this item through this billing and % Complete will automatically calculate.

##  To Date Amount

 This field defaults an amount based on To Date Units and Unit Price. This value may be overridden, but will cause % Complete and To Date Units to recalculate.

##  Units Claimed

 This field is used for tracking claimed units.
 Enter the number of units claimed for this billing. Initially defaults from the This Bill WC Units field. Once you certify this bill (by checking the Certified box on the Info tab), this field will no longer be updated by changes to the This Bill WC Units field.
Note: In order for this field to display in the grid, you must check the Show in Grid box for this field’s sequence (#175 – Claim Units) in the Field Properties (F3) form (System Overrides or User Overrides tab).

##  Amount Claimed

 This field is used for tracking claimed amounts.
 Enter the amount claimed for this billing. Initially defaults from This Bill WC Amount + This Bill SM Amount fields. Once you certify this bill (by checking the Certified box on the Info tab), this field will no longer be updated by changes to the This Bill WC Amount or This Bill SM Amount fields.
Note: In order for this field to display in the grid, you must check the Show in Grid box for this field’s sequence (#180 – Claim Amount) in the Field Properties (F3) form (System Overrides or User Overrides tab).

##  Reason Code

 Enter a valid reason code to explain the reason for item billing amount changes. Press F4 for a list of valid reason codes.
Note: In order for this field to display in the grid, you must check the Show in Grid box for this field’s sequence (#185 – Reason Code) in the Field Properties (F3) form (System Overrides or User Overrides tab).

##  Retainage %

 This field defaults retainage percent specified for the contract item (in JC Contract Items). This field may be overridden.
Note: If you enter retainage at the contract level (JB Progress Bill Retg Totals), any percentage entered here will be overridden and must be re-entered.

##  Retainage

 Defaults an amount based on the retainage percent and the current billing amount; may be overridden.
Note: If you enter retainage at the contract level (JB Progress Bill Retg Totals), any amount entered here will be overridden, and must be re-entered.

## Previous Amount

This field defaults the total of previous amounts for this contract item, and is the sum of the last billing’s “previous” and “this invoice” amounts.
 You may only override this value if the
  Allow Changes
 to Previous and Contract Amounts box is checked in JB Company
 Parameters.
Note: If you change this value, the % Complete will be
 updated to reflect the change. If you have checked the Automatic Update of Prev Billed and ChgOrder Amounts
 on Future Bills box in JB Company Parameters, it is highly recommended that
 you do NOT change this value, as it may cause inaccuracies when previous amounts are
 updated for future billings.

## Seq

The Seq field on the Recipients tab of the JB Progress Billing and JB T&M Bill Edit forms.

For the default recipient, this field defaults the system-assigned sequence number and cannot be changed.
If adding a new recipient, enter N or +; the system will automatically assign the next sequential number.

## Delivery

The Delivery Method drop-down on the Recipients tab of the JB Progress Billing and JB T&M Bill Edit forms.

Required.
For default recipients, this field defaults the delivery method specified for the recipient in JC Contract Recipients Detail. May be edited as needed.
Note: Changing the delivery method for a default recipient here does not update the recipient's delivery method in JC Contract Recipients Detail.

Indicate the delivery method for the selected recipient.

- P-Print — Select this option to print invoices for delivery via postal mail. Requires that you enter a mailing address in the address fields.

- E-Email — Select this option to deliver invoices via email. Requires that you enter an email address in the Email field.

## Name

The Name field on the Recipients tab of the JB Progress Billing and JB T&M Bill Edit forms.

Required.
For default recipients, this field defaults the name specified for the recipient in JC Contract Recipients Detail. May be edited as needed.
Note: Changing the name for a default recipient here does not update the recipient's name in JC Contract Recipients Detail.

Enter the name of the individual or company to whom you will be mailing or emailing this invoice.

## Email

The Email field on the Recipients tab of the JB Progress Billing and JB T&M Bill Edit forms.
Required if the Delivery field is set to E - Email.
For default recipients, this field defaults the email address specified for the recipient in JC Contract Recipients Detail. May be edited as needed.
Note: Changing the email address for a default recipient here does not update the recipient's email address in JC Contract Recipients Detail.

Enter the email address to use for this recipient.
 You can enter multiple email addresses if applicable; however, you must separate them with a semicolon (for example, janed@email.com; jane_doe@coemail.com). The system will send an email to each address specified here.

## Address

The Address fields on the Recipients tab of the JB Progress Billing and JB T&M Bill Edit forms.

Required if the Delivery field is set to P - Print.
For default recipients, this field defaults the address information defined for the recipient in JC Contract Recipients Detail form. May be edited as needed.
Note: Changing the address for a default recipient here does not update the recipient's address in JC Contract Recipients Detail.

Enter the delivery address to use for this recipient:

- Address - Enter the street address.

- Add'l Address - Enter additional address information for this recipient (for example, suite number, apartment, etc.). If the recipient receives their mail at a P.O. Box, then you might enter the P.O. Box in the Address field above, and use this field to enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

## Seq

Seq field on the Delivery tab of the JB Progress Billing form.

This field displays the system-assigned ID for this delivery event.Note: This is not an editable field.

## Date Sent

The Date Sent field on the Delivery tab of the JB Progress Billing form.
This field displays the date an invoice was sent.Note: This is not an
 editable field.

## Delivery

The Delivery field on the Delivery tab of the JB Progress Billings and JB T&M Bill Edit forms.

This field displays the delivery method used to deliver the selected Job Billing invoice (E-Email or P-Print).Note: This is not an editable field.

## Delivery Status

Delivery Status field on the Delivery tab of the JB Progress Billing form.

This field displays the status of the invoice delivery event (D-Delivered or F-Failed).Note: This is not an editable field.

## Recipient

The Recipient field on the Delivery tab of the JB Progress Billing form.

This field displays the name of the person who received the invoice.Note: This is
 not an editable field.

## Email

The Email field on the Delivery tab of the JB Progress Billing form.

This field applies to recipients with an E-Email delivery method.
This field displays the recipient's email address (that is, where the invoice was sent via email).Note: This is not an
 editable field.

## Address

The Address fields on the Delivery tab of the JB Progress Billings and JB T&M Bill Edit forms.

This field applies to recipients with a P-Print delivery method.
This field displays the recipient's mailing address (Address, Add'l Address, City, State, Zip, and Country).Note: This is not an editable field.

## Notes

Use this tab to enter any miscellaneous notes about this progress billing. The space allowance is virtually unlimited.
Add Standard Notes
To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box and click the right mouse button. From the shortcut menu, select the Standard Notes option, which brings up the Std Note Copy window. Enter the standard note to copy and click OK to add the note. Note will be appended to the end of existing note text (if applicable).
Spelling Check
You can run a spell check for any notes entered in this window. Click the Spelling button in the toolbar () or select the Spelling option from the Tools or shortcut menu.
Tip: To use the Tab feature (such as to indent the first line of a paragraph or create columns), you will need to press Ctrl + Tab for each tab increment.
