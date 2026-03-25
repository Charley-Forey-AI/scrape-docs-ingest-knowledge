---
title: "Field Definitions: AP Payment Workfile Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form/field-definitions-ap-payment-workfile-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form/field-definitions-ap-payment-workfile-form"
---

# Field Definitions: AP Payment Workfile Form

The following is a list of field descriptions for the AP Payment Workfile form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Acct To Use If Not Assigned In The Transaction

 Optional.
 Specify the CM account to use for transactions with no CM account assigned. During initialization, the system will automatically assign this CM account to any transaction without a CM account.

## Restrict by CM Account

 Check this box to restrict initialization based on CM account. CM account is specified to the right.
 Do not check this box if not restricting initialization based on CM account.

## CM Acct

 Enabled only when the Restrict by CM Account box is checked.
 Specify the CM account by which to restrict initialization. Only transactions with this CM account meeting all other restriction criteria will be initialized into the payment work file.

## Vendor

 Optional.
 Specify the vendor by which to restrict initialization. Only transactions posted to this vendor and meeting all other restriction criteria will be initialized into the payment work file.

## AP Ref#

The AP Ref# field on the AP Payment Workfile form, Payment Selection Criteria section.
 Optional.
 Specify the AP reference number by which to restrict initialization. Only transactions posted to this reference number and meeting all other restriction criteria will be initialized into the payment work file.

## JCCo

 If restricting by Job, you must enter the JC company. Otherwise, entry is optional.
 Specify the JC company by which to restrict initialization. Only transactions posted to this JC company and meeting all other restriction criteria will be initialized into the payment work file.

## Job

 Optional.
 Specify the job by which to restrict initialization. Only transactions posted to this job and meeting all other restriction criteria will be initialized into the payment work file.

## Restrict By Payment Control

 Check this box to restrict initialization based on payment control number.
 Do not check this box if not restricting initialization based on payment control number.

## Payment Control

 Specify the payment control number by which to restrict initialization. Only transactions with this payment control number and meeting all other restriction criteria will be initialized into the payment work file.

## Restrict By Payable Type

Select this check box to restrict initialization by payable type. Then use the selection box to the right of this field to specify which payable types to restrict by. Only those transactions posted to the selected payable types and meeting all other restriction criteria will be initialized into the payment work file.
Do not select this checkbox if not restricting initialization by payable type. Note: The list of payable types excludes any payable types designated for retainage in AP Company Parameters or for a pay category in AP Pay Category.


## Include On Hold Transactions

Select this checkbox to include hold codes (non-retainage only) when initializing the
 payment work file.
Clear this checkbox to exclude "on hold" transactions when initializing the payment work
 file.
Note: To release retainage for payable transactions, you must use AP Release Retainage; you
 cannot release retainage holds using this form. For more information, see Release
 Retainage for AP Invoices.

## Check to Pay if Out of Compliance

Default is No (unchecked), but can be overridden.
This option sets the default for the Pay option in the AP Payment Workfile header grid. When this option is checked, out of compliance transactions are initialized as checked to pay. However, functionality is determined by how the “Don’t Add to Payment Batch if Out of Compliance” option is set in AP Company Parameters. For example, if a user checks this flag, but the AP Company Parameters setting is set to “not add out of compliance transactions” to a payment batch, then the initialization does not check these transactions to be paid and the user will not be able to manually check the “to pay” column.
The following table illustrates how the two options work together. Note that the setting in the AP Payment Workfile header grid determines whether a transaction occurs.
AP Payment Workfile
AP Company Parameters
AP Payment Workfile Grid
Can User Change the AP Payment Workfile Grid?

Yes, pay if out of compliance (checked)
No, don't pay out of compliance (checked)
No, don't pay (unchecked)
No

Yes, pay if out of compliance (checked)
Yes, pay if out of compliance (unchecked)
Yes, pay (checked)
Yes

No, don't pay if out of compliance (unchecked)
No, don't pay if out of compliance (checked)
No, don't pay (unchecked)
No

No, don't pay if out of compliance (unchecked)
Yes, pay if out of compliance (unchecked)
No, don't pay (unchecked)
Yes

## Separate Payment Per Job

The Separate payment per job checkbox on the AP Payment Workfile form.
 Select this checkbox to print a separate check (in AP Payment Posting) for each unique job. When you create the payment batch, the system groups all job transactions together by vendor and job, and prints a separate check for each unique combination.
 Leave this checkbox unselected to print a single check per vendor.

## Separate Payment Per Subcontract

The Separate payment per subcontract checkbox on the AP Payment Workfile form.
 Select this checkbox to print a separate check (in AP Payment Posting) for each subcontract. When you create the payment batch, the system groups all subcontract transactions together by vendor and subcontract, and prints a separate check for each unique combination.
 Leave this checkbox unselected to print a single check per vendor.

## Exclude Vendors with Credit

 Check this box to exclude vendors with a credit balance.
 When you check this box, if the sum total of all the vendor’s transactions is zero, or have a negative balance (credit), the system does not add the transactions to the batch. If you do not check this box, the system initializes both positive and negative transactions into the workfile, but only adds transactions greater than zero into the payment batch.

## Open Retainage only

The Open Retainage only checkbox on the AP Payment Workfile form.

Select this checkbox to include only open retainage transactions in the payment workfile. The transaction grids display only those transactions/lines for which you have released retainage in AP Release Retainage. If a transaction includes multiple lines, retainage and non-retainage, only the lines for released retainage will display.
If you leave this checkbox unselected, the grid includes all lines for a transaction; however, lines with unreleased retainage will default with the Pay checkbox unselected.
For more information about adding open retainage to a payment workfile, see [Create a Released Retainage Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile).

## Payment Methods

For each payment method, select the checkbox to include invoices to be paid by that payment method.
If you do not select the checkbox for a payment method, invoices with that payment method are excluded.
Note: By default, when you open the form, the Check and EFT checkboxes are selected. When processing invoices that have a credit/payment service payment method, use a separate payment batch from invoices paid by check or EFT.

## Include Transactions Due As Of

Specify the due date to use as a cutoff date when determining which transactions to initialize into the work file. All transactions with a due date equal to or less than this date will be initialized into the payment work file. All transactions with a due date later than this date will be skipped.
If left blank, all transactions meeting other selection criteria will be initialized, regardless of due date.

## If Available, Use Discount Date

Check this box if you want the discount date
 to be compared to the date you entered in the Include Transactions Due As Of field when
 selecting transactions to add to the payment work file. All transactions with a discount
 date equal to or less than the cutoff date will be initialized into the payment workfile.
 All transactions with a discount date later than the cutoff date will be skipped. If a
 transaction does not have a discount date indicated, the transaction’s due date will be
 used.
Do not check this box if you do not want to compare a transaction’s discount date to the cutoff date when selecting transactions to add to the payment batch. The due date will be used instead.
Note:If this option is checked and you enter a date in the Cancel if Discount Date is Prior To field, it will affect how discounts are handled. For more information, see [Adding Invoices with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).

## Include Discounted Transactions Only

 Check this box to initialize only those transactions with a discount. When checked, if any line on a transaction has a discount, all lines for the transaction will be initialized into the batch.
 Do not check this box if all transactions should be initialized, whether or not a discount is taken.

## Take All Discounts

Only select this checkbox if you want offered discounts to be taken.
This field is disabled if either of the following checkboxes are selected in the AP Company Parameters form:

- PayTypes/Discounts/ICR tab: Post Discounts
 Offered to GL and Net Amounts to Subledgers

- Invoice Options tab: Using tax
 discount

Note: Offered discounts will automatically be taken and
 cannot be changed.

## Cancel if Discount Date is prior To

Cancel if Discount Date is prior to field in the AP Payment Workfile form
For those transactions offering discounts, enter the discount date to use when determining whether the discount may be taken or not. Discounts will be taken for all transactions with a discount date equal to or greater than this date. If the discount date specified for a payable transaction is prior to this date, the discount will not be taken.
If you specify a date here and you have also
 selected the If
 available, use Discount Date checkbox, it will affect how canceled
 discounts are handled. For more information, see [Adding Invoices with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).
This field is disabled if either of the following checkboxes are selected in the AP Company Parameters form:

- PayTypes/Discounts/ICR tab: Post Discounts
 Offered to GL and Net Amounts to Subledgers

- Invoice Options tab: Using tax
 discount

## Initialize To Be Paid

Check this box to mark initialized transactions as ready for payment. During initialization, the system checks the Pay box for each transaction/line that initializes into the work file, as long as:

- the transaction's due date is equal to or less than the date you indicated in the Cutoff Date fields.

- the transaction is in compliance or, if out-of-compliance, you did not check the ‘Don’t add Vendor to Payments Batch if out of compliance’ boxes in AP Company Parameters (for Invoices, Subcontracts or Purchase Orders).

Do not check this box if you do not want initialized transactions to be marked as ready for payment.

## Mth

 If adding transactions manually, specify the month in which the transaction you want to add to the payment work file was posted.
 If transactions were initialized into payment work file, this will be the transactions posted month. Month cannot be changed.

## Trans

 If adding transactions manually, specify the transaction to add to the payment work file. Press F4 for a list of valid transactions for the vendor and month.
 If transactions were initialized into payment work file, this will be the number assigned to the transaction. Number cannot be changed.

## Vendor

 If adding transactions manually, specify the vendor assigned to the transaction you want added to the payment work file. Press F4 for a list of valid vendors.
 If transactions were initialized into payment work file, this will be the vendor assigned to the transaction. Vendor cannot be changed.

## Disc Date

Defaults the discount date for this transaction based on assigned payment terms (if applicable). May be overridden.

## Due Date

Defaults the due date for this transaction based on assigned payment terms. May be overridden.
Note:If you want changes to the due date to be updated to the detail lines for this transaction, you must be in 'Change' mode (i.e. save the header transaction, then make the change). If you change the due date while in 'Add' mode, it will not be updated to the detail lines.

## Release Hold Code

The Release Hold Code checkbox on the AP Payment Workfile form, Transactions
 grid.
Select this checkbox to release the hold code associated with this transaction. When you
 remove the hold code from the transaction, the system removes the same hold code from all
 associated line items and clears the On Hold checkbox for this
 transaction. This box remains checked until you refresh the screen.
If you select this checkbox and there is more than one hold code associated with the
 transaction, the system displays the AP Payment Control Detail form. You must then use that
 form to release hold codes.
Note: You cannot use this feature to release retainage; you must release retainage using AP
 Release Retainage. If you select this checkbox and the transaction only has a retainage
 hold, a message displays indicating you must use the AP Release Retainage to release
 retention. For transactions with multiple holds, you can use AP Payment Detail to
 release only the non-retainage holds.For information about releasing retainage, see
 [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Pay

The Pay checkbox on the AP Payment Workfile form, transaction header grid.
Select this box if this transaction is ready to be paid. When creating a payment batch (the Create Payment Batch button is clicked), this transaction will be removed from the payment work file and added to the payment batch.
Do not select this box if this transaction is not ready to be paid. When creating a payment batch (the Create Payment Batch button is clicked), this transaction will be removed from the work file, but will not be added to the payment batch.
Note:If you checked the “Initialize to be Paid” option when initializing the payment work file, this box will automatically be checked for each transaction. However, if a transaction is 'out of compliance' (line highlighted in red) and the "Don't Add to Payments Batch if Out of Compliance" option is checked for Subcontracts and/or Purchase Orders (in AP Company Parameters), this flag will be left unchecked for that transaction. You will need to manually set this flag to Y (checked) if you want to include the transaction when initializing the payment batch.

Additionally, if a transaction is marked for payment, but will result in a negative payment, it will not be added to the payment batch when initialized. Instead 'negative payment' transactions will remain in the payment work file.

## Net Pay Amount

Display only.
This will be the net payment amount for this transaction. Payment amount will be determined by the payment amounts specified for each line/sequence that have been marked as paid for this transaction (in Payment Work file Detail).
Note:If a transaction is marked for payment, but will result in a negative payment, it will not be added to the payment batch when initialized. Instead 'negative payment' transactions will remain in the payment work file.

## Pay Control

 Defaults pay control number assigned to transaction, if applicable. May be overridden.

## Pay Method

The Pay Method field in the AP Payment Workfile form's grid.

This field's default value comes from the payment method assigned to the transaction record. You may change it to one of the following:

- N-ePayments

- C-Check

- E-EFT

- S-Credit Service

N-ePayments (U.S. only)If you intend to use this pay method, you're not required to select it here because at the moment you generate the ePayments file (via AP ePayment Export), you are given the option to change the pay method originally assigned. For details, see [Payment Methods](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-000063380001--en).
E-EFTIf you change the selection to E-EFT, you must also specify the necessary bank account information in the AP Vendors form (Payment Method tab, EFT Info section). If you have not specified bank account information, the system displays an error but allows you to save the record.
 For more information about setting vendor payment methods, see [Set the Vendor's Payment Method: U.S. and Canada](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-the-vendors-payment-method-u.s.-and-canada).
S-Credit ServiceYou can change the selection to S-Credit Service if you have specified the necessary credit service information in the AP Company Parameters form (Payment Services tab). This information includes the credit service provider (Comdata or EFS), credit service CM account number, and any other necessary credit service information. If you have not specified credit service information, the system displays an error but allows you to save the record.
 For more information about setting up credit service information, see [Set up Credit Services with Comdata](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata).
When you select S-Credit Service, the system updates the CM Acct field with the account you specified for the credit service in the AP Vendors form (CM Acct field, Payment Services tab).
 If you change this field from S-Credit Service to either C-Check or E-EFT, the system updates the CM Acct field to use the correct account based on one of the following:

- AP Transaction Entry

- A batch posted from MS Haul Payment Worksheet or MS Material Payment Worksheet

- The CM Acct to use if not assigned in the transaction field located above the workfile grid.

Note: If you are using Comdata as your credit service provider, the system checks to see if you specified a credit service email for the vendor in the AP Vendors form (Payment Service Email field, Payment Method tab). If you have not specified an email address, the system displays a warning, but allows you to save the record.

## CM Acct

For invoices with a payment method of check or EFT, the default value in this field comes from one of the following:

- AP Transaction Entry form

- Batch posted from MS Haul Payment Worksheet or MS Material Payment Worksheet

- From the CM Acct to use if not assigned in the
 transaction field on this form

For invoices with a payment method of credit
 service, this field defaults from the CM Acct # field in the AP Company
 Parameters form (Payment Services tab).
Accept the default value or enter a different valid CM account for the invoice.
If you change the Pay Method
 field for this invoice, the system will update this field based on the default information
 above.
Note:If you have specified a credit service CM account in the AP Company Parameters form, and you are paying this vendor with a different method (either check or EFT), the system will display a warning if you enter the credit service CM account. You will be allowed to save the record, however.

## Supplier

 If this is a two-party check, indicate the supplier (from AP Vendors) to be paid by this
 transaction. The supplier entered here will be assigned to each detail line associated with
 this transaction.

## Separate Pay

The Separate Pay checkbox on the AP Payment Workfile form, transaction header grid.

This checkbox is enabled for N-Viewpoint, C-Check, and E-EFT pay methods only.
Select this checkbox if paying this transaction separately. When initializing payments in AP Payment Posting, the system will generate a separate payment for this transaction.
Note: If you are generating separate payments per job or subcontract and this option is selected, this transaction is paid separately from all other transactions for a subcontract or job.
Leave this checkbox unselected if not paying this transaction separately. When payments are initialized, the system will group this transaction together with other transactions having the same vendor on a single invoice.
This option defaults to the setting selected for the Separate Payment checkbox in AP Transaction Entry; updating this option updates the option in AP Transaction Entry and vice versa.

## Address Seq#

Specify the payment address sequence to use for this transaction. Must be a valid address sequence defined for the vendor in AP Additional Addresses, and must be an address sequence flagged as 'Payment' or 'Both'.
Note:If you previously entered an override address (below), entering an address sequence in this field will cause the 'Override Payment Address' checkbox to be cleared, and the override address to be replaced with the address defined for this address sequence.

## Override Payment Address

Check this box if you want to override the standard name and/or address specified for this transaction's vendor. When initializing the payment batch, a separate check will be printed for this transaction.
Do not check this box if you do not want to override the payment address for this vendor.
Note:This checkbox is only for use when entering an override payment address (below). If you check this box, then enter an Address Seq (above), this box will automatically be cleared.

## Name

The Name field on the AP Payment Workfile form, Address Override tab.
Enabled only if the Override payment address checkbox is selected.
Enter an override name here (up to 80 characters). When printing checks, the system will print a separate check for this transaction.
If you leave this field blank, the vendor's name as defined in AP Vendors is used.
Note: If you enter a value in the Address Seq # field after entering a value in this field, the system overrides the name you entered with the vendor's name from AP Vendors and disables this field.

## Add'l Info

Enter additional information, up to 60 characters, to be printed on the check paying this transaction (e.g. Attention line, Garnishment Case #, etc.).
Note:If you elect to use the 'Address Seq' option (above), this field will be disabled and will automatically default the 'Add'l Address' specified for the address sequence (in AP Additional Addresses). If you previously entered override info, it will be replaced with the additional address specified for the address sequence.

## Address

If the Override Payment Address option is checked, enter the override address, up to 60 characters. Entry here will result in a separate check printing for this transaction.
Note:If you elect to use the 'Address Seq' option (above), this field will be disabled and will automatically default the address specified for the address sequence (in AP Additional Addresses). If you previously entered an override address, it will be replaced with the address specified for the address sequence.

## City

If the Override Payment Address option is checked, enter the override city, up to 30 characters. Entry here will result in a separate check printing for this transaction.
Note:If you elect to use the 'Address Seq' option (above), this field will be disabled and will automatically default the city specified for the address sequence (in AP Additional Addresses). If you previously entered an override address, entry in this field will be replaced with the city specified for the address sequence.

## State

If the Override Payment Address option is checked, enter the override state. Entry here will result in a separate check printing for this transaction.
Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

## Zip

If the Override Payment Address option is checked, enter the override zip code, up to 12 characters. Entry here will result in a separate check printing for this transaction.
Note:If you elect to use the 'Address Seq' option (above), this field will be disabled and will automatically default the zip code specified for the address sequence (in AP Additional Addresses). If you previously entered an override address, entry in this field will be replaced with the zip code specified for the address sequence.

## Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

## Line

If transactions were added to the work file through initialization, all lines that met the selection criteria will display in this grid. Lines can be deleted or added, but the line number cannot be changed. If adding a line, press F4 for a list of valid lines for the specified transaction.
Note:You cannot add new lines to a transaction, you can only add existing lines that are not already in the grid.

## Seq

If transactions were added to the work file through initialization, all sequences for the line that met the selection criteria will display in this grid. Sequences can be deleted or added, but the sequence number cannot be changed. If adding a sequence, press F4 for a list of valid sequences for this line.
Note:You cannot add new sequences to a line, you can only add existing sequences that are not already in the grid.

## Pay

The Pay checkbox on the AP Payment Workfile form, transaction detail grid.
Select this box if this line/sequence is ready to be paid. When creating a payment batch (the Create Payment Batch button is clicked), this line/sequence will be removed from the payment work file and added to the payment batch.
Do not check this box if this line/sequence is not ready to be paid. When creating a payment batch (the Create Payment Batch button is clicked), this line/sequence will be removed from the work file, but will not be added to the payment batch.
Note: If you selected the Initialize to be paid checkbox when initializing the payment work file, this check is automatically selected for each line/sequence in the grid. However, if a transaction is 'out of compliance' (line highlighted in red in payment work file grid) and the Don't add to Payments batch if "out of compliance" checkbox is selected for Subcontracts and/or Purchase Orders (in AP Company Parameters), this checkbox is left unselected for each line/sequence for that transaction. You will need to manually select this checkbox for each applicable line/sequence you want included when initializing the payment batch.

## Discount Offered

 Defaults the discount offered for this line/sequence, if applicable. May be overridden manually or using the Discount option in AP Payment Control Detail (the Additional Payment Control Functions option in File menu). If using the Discount option in AP Payment Control Detail, the discount amount will be proportionately distributed to the transaction’s lines, based on each line’s amount.

## Discount Taken

Defaults from the discount offered for the sequence, if applicable. May be overridden manually or using the Discount option in AP Payment Control Detail (the Additional Payment Control Functions option in File menu). If using the Discount option in AP Payment Control Detail, the discount taken will be proportionately distributed to the transaction’s lines, based on each line’s amount.
Note:If the "Using Tax Discounts" and/or "Post Discounts Offered to GL and Net Amounts to Subledgers" options are set to Y (checked), this field will be disabled.

## Due Date

Defaults the due date assigned at the header level in AP Transaction Entry, or overridden at the header level in AP Payment Workfile. May be overridden. If this date is greater than the 'cut-off date' specified when initializing transactions to the work file, and you specified to flag transactions as ready to be paid, this box will be left unchecked.
Note:Changes made to this due date will be updated to the APWD (Work file Detail) and APTD (Transaction Detail) tables—they do not affect the due date specified at the header level. This date will be used as the default due date when this detail line is added to the payment batch, or if the transaction is pulled back into a payment work file.

## Supplier

 Defaults the supplier assigned to the transaction line in originating program or in AP Payment Workfile, if applicable. May be overridden manually or using the Supplier option in AP Payment Control Detail (the Additional Payment Control Functions option in File menu). If using the Supplier option in AP Payment Control Detail, the Supplier will be assigned to all lines on the transaction.

## Release Hold Code

The Release Hold Code checkbox on the AP Payment Workfile form, Lines grid.
Select this checkbox to release the hold code associated with this line item. When you
 remove the hold code from th is line, the system clears the On Hold
 checkbox.
If you select this checkbox and there is more than one hold code associated with the line,
 the system displays the AP Payment Control Detail form. You must then use that form to
 release hold codes.
Note: You cannot use this feature to release retainage; you must release retainage using
 AP Release Retainage. If you select this checkbox and line item has only a retainage
 hold, a message displays indicating you must use the AP Release Retainage to release
 retention. For lines with multiple holds, you can use AP Payment Detail to release only
 the non-retainage holds.For information about releasing retainage, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).
