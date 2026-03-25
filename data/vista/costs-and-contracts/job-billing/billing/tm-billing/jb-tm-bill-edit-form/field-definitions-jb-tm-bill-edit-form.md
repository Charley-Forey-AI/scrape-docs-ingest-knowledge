---
title: "Field Definitions: JB T&M Bill Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form/field-definitions-jb-tm-bill-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form/field-definitions-jb-tm-bill-edit-form"
---

# Field Definitions: JB T&M Bill Edit Form

The following is a list of field descriptions for the JB
 T&M Bill Edit form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Bill Month

 Enter the bill month for the invoices to review, edit, or add.

##  Bill Number

 Specify the bill number of the invoice to review/edit. Press F4 for a list of valid bill numbers. If adding a new billing, enter “N” or "New" to have the system assign the next sequential bill number.

- If you specify a billing in a closed month, a warning displays (in blue) at the top of the form. You can make changes to 'closed-month' billings; however, you cannot add or delete billings in a closed month.

- If you specify/add a billing, and future billings exist for that contract/customer, a warning displays (in red) at the top of the form.

##  Invoice

 This field defaults as follows:

- If the Auto Sequence Invoice # option (JB Company Parameters) is not checked, this field defaults as blank and you must enter the invoice number manually. Up to 10 characters allowed.

- If the Auto Sequence Invoice # option is checked, but you did not elect to have invoice numbers assigned during initialization, this field defaults as blank and you must enter the invoice number manually.

- If the Auto Sequence Invoice # option is checked and you elected to have invoice numbers assigned during initialization, this field defaults the billing’s assigned invoice number. If you are manually entering a new billing, this field defaults the next available sequential invoice number.

Note: All billings must have an invoice number in order to be interfaced.

##  Contract

 If you initialized billings, this field defaults to the contract for the
 billing and is disabled.
 If entering this billing manually, specify
 the contract (JC Contracts) for this billing. Once you save the record, this field is
 disabled.
Closed Contracts
 Regardless of whether you are changing an existing billing or manually adding a new billing, if the billing's contract has been soft or hard closed (indicated in red to right of contract), the ‘Allow Posting to Soft-Closed Jobs’ and ‘Allow Posting to Hard-Closed Jobs’ options in JC Company Parameters determine how the billing is handled.

- If you allow posting to hard and/or soft-closed jobs, the contract's description reads, "Contract is closed." However, you will be able to save the record.

- If you do not allow posting to soft or hard-closed jobs, in addition to the contract description indicating the contract is closed, you will receive the following message: the following message:

 You will be unable to save the record.
Note: You can specify to allow posting soft-closed jobs, but not hard-closed jobs, in which case the conditions indicated above will apply accordingly; that is, you will be able to save billings posted to soft-closed jobs, but will not be able to save billings posted to hard-closed jobs.

##  Customer

 Defaults the customer assigned to the specified contract (JC Contracts);
 may be overridden.
 If no customer is assigned to the contract, enter the customer to assign to this contract for this billing.

##  Template

 Specify the T&M Template (defined in JB T&M Template Setup) to use for this billing. This template determines the definition and layout of the billing, including which fields are available when entering or editing lines.
Note: Once lines exist for the billing, this template cannot change.

##  Application #

 Specify a number (0-32,767) to identify this billing. This field automatically defaults a system-assigned sequential number based on the number of billings for the contract. If a previous billing does not exist for this contract, defaults to “1.”

##  Invoice Desc

 Enter a description for this invoice, up to 30 characters. Initially defaults the ‘Description to Use’ specified during initialization. If no description specified at time of initialization, defaults the description as follows:

- If bill type is ‘T&M’ (i.e. all items on the contract are ‘T&M’), defaults description from the Customer Reference specified for the contract in JB Contract Info. If no Customer Reference specified, defaults the description as 'JB T&M'.

- If bill type is ‘Both’ (i.e. one or more items on the contract are ‘Both’), defaults the invoice description as “JB App # XX” (where XX represents the billing application number).

- For non-contract billings, defaults the invoice description as “JB T&M.”

 When interfacing this billing, the description updates to the Description column in ARTH (Transaction Header).

##  Status

 Indicate the status of this invoice. The following options are available when invoicing non-interfaced billings.

- A-Active – Invoices initially default this status when creating a billing.

- N-Never Interfaced – Select this status if this billing will never be interfaced. This option is typically used when a contract item requires both a Progress and T&M billing (defined in JC Contract Items), but only one billing is interfaced to prevent a duplicate billing in AR.

 These options are available once when invoicing and interfacing a billing.

- C-Change – Defaults to this status automatically when changing a previously interfaced billing.

- D-Delete – Select this option to delete a previously interfaced invoice. You can only delete billings in an open month.

- I-Interfaced – Interfaced invoices automatically default this status.

##  Process Group

 This field is optional and defines the processing group for this contract billing. If the contract has a defined processing group (JB Contract Info), the processing group defaults here.
Note: You do not have to process billings by group; process each one separately, if desired.

##  Receivable Type

 Specify the receivable type for this billing. Initially defaults the receivable type specified for the contract (in JB Contract Info). If the contract does not have a specified receivable type, this field defaults the receivable type specified for the contract’s customer in AR Customers (or AR Company Parameters if the customer does not have a receivable type).
 The receivable type determines which GL accounts receive an update during the interface.

##  Restrict by Item Bill Group

 Check this box to restrict the initialization of contract items by bill
 group. Only contract items with a bill group (assigned in JC Contracts) matching the one
 specified below (Item Bill Group) will initialize.
 Leave this box unchecked to initialize all contract items to this billing, regardless of bill group.

##  Item Bill Group

 Specify the bill group, up to 20 characters, to restrict item
 initialization with. All contract items assigned this bill group (in JC Contracts) will
 initialize to the billing.
 The system does not validate this field; you can enter either a valid or non-valid bill group. If you specify a valid bill group (one that has been set up in JB Bill Groups), provide a single description that applies to all items on the invoice matching this bill group.

##  Override GL Rev Account

 Check this box to override the revenue account (specified for the contract’s assigned department) for this billing.

##  Override GL Revenue Acct

 Enter the GL account for revenue posting.

##  Invoice Date

 This field defaults to the invoice date specified during initialization.
 If entered manually, defaults to the current date. The system allows overrides to this field.

##  Payment Terms

 If applicable, specify the payment terms for this contract. Initially
 defaults the payment terms specified for the contract in JC Contracts. If the contract does
 not have specified payment terms, this field defaults the payment terms specified for the
 customer in AR Customers. The system allows overrides to this field.

##  Due Date

 Defaults a due date based on the payment terms. If payment terms do not exist, the due date is the same as the invoice date. The system allows overrides to this field.

##  Discount Date

 Initially defaults a discount date based on the payment terms. If payment terms do not exist, this date defaults as blank. The system allows overrides to this field.

##  From Date

 Specify the beginning date of the bill period. This field is optional and informational only.

##  To Date

 Specify the ending date of the bill period. This field is optional and informational only.

##  Address

 Defaults the override address specified for this contract in JB Contract Info or, if no override address specified, the billing address defined for the customer in AR Customers. If no billing address is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## City

Defaults the override city specified for this contract in JB Contract Info or, if no override city specified, the billing city defined for the customer in AR Customers. If no billing city is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## State

Defaults the override state specified for this contract in JB Contract Info or, if no override state specified, the billing state defined for the customer in AR Customers. If no billing state is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Zip

 Defaults the override zip code specified for this contract in JB Contract Info or, if no override zip code specified, the billing zip code defined for the customer in AR Customers. If no billing zip code is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Country

Defaults the override state specified for this contract in JB Contract Info or, if no override state specified, the billing state defined for the customer in AR Customers. If no billing state is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Add'l Address

 Defaults the override additional address specified for this contract in JB Contract Info or, if no override address specified, the billing additional address defined for the customer in AR Customers. If no billing additional address is defined for the customer (or a customer is not specified for the contract), this field defaults as null. You may override if necessary.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## JB Reviewer Group

The JB Reviewer Group field on the JB T&M Bill Edit form,
 Info tab.
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in JB Company Parameters.
 Enter the reviewer group for this T&M billing. Must be a reviewer group
 set up in the HQ Reviewer Groups form with a Reviewer Group Type of 3-Job Billing. Initially defaults the
 reviewer group assigned to the contract (via the JB Contract Info form).
Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

Related concepts

- [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form)

Related tasks

- [Create Reviewer Groups for Job Billing Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-job-billing-invoices)

## Assigned To

The Assigned To field on the JB T&M Bill Edit form, Info
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

The Ready for Review checkbox on the JB T&M Bill Edit
 form, Info tab.

Select this checkbox when this T&M billing is ready to review. Once selected, the display fields to the right populate with the current User ID and Date.

Clear this checkbox if this T&M billing is not ready to review or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Draft Approved

The Draft Approved checkbox on the JB T&M Bill Edit form,
 Info tab.
Select this checkbox if the draft bill is approved. Once selected, the
 display fields to the right populate with the current User ID and Date.

Clear this checkbox if the draft bill is not approved or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Sent to Customers

The Sent to Customers checkbox on the JB T&M Bill Edit
 form, Info tab.
 Select this checkbox if the draft billing has been sent to the customer.
 Once selected, the display fields to the right populate with the current User ID and
 Date.
Clear this checkbox if the draft version of the billing has not been sent to the customer or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Approved for Billing

The Approved for Billing checkbox on the JB T&M Bill Edit
 form, Info tab.
 Select this checkbox when this T&M bill is approved for billing.
Clear this checkbox if this T&M bill is not approved or if you are not tracking the review process for billings.
Note: If you are tracking the review process for billings (that is, the Use Review and Approval Workflow checkbox is selected in the JB Company Parameters form), the Review Level defined for the associated contract (in the JC Contract Master form) determines what level of the review process is required before you can interface the billing. For example, if you set the review level to 3-Sent to Customer, you can only interface this bill if you select either the Sent to Customers or Approved for Billing checkbox.

Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

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

Seq field on the Delivery tab of the JB T&M Bill Edit form.

This field displays the system-assigned ID for this delivery event.Note: This is not an editable field.

## Date Sent

The Date Sent field on the Delivery tab of the JB T&M Bill Edit form.
This field displays the date an invoice was sent.Note: This is not an
 editable field.

## Delivery

The Delivery field on the Delivery tab of the JB Progress Billings and JB T&M Bill Edit forms.

This field displays the delivery method used to deliver the selected Job Billing invoice (E-Email or P-Print).Note: This is not an editable field.

## Delivery Status

Delivery Status field on the Delivery tab of the JB T&M Bill Edit form.

This field displays the status of the invoice delivery event (D-Delivered or F-Failed).Note: This is not an editable field.

## Recipient

The Recipient field on the Delivery tab of the JB T&M Bill Edit form.

This field displays the name of the person who received the invoice.Note: This is not an editable field.

## Email

The Email field on the Delivery tab of the JB T&M Bill Edit form.

This field applies to recipients with an E-Email delivery method.
This field displays the recipient's email address (that is, where the invoice was sent via email).Note: This is not an editable field.

## Address

The Address fields on the Delivery tab of the JB Progress Billings and JB T&M Bill Edit forms.

This field applies to recipients with a P-Print delivery method.
This field displays the recipient's mailing address (Address, Add'l Address, City, State, Zip, and Country).Note: This is not an editable field.
