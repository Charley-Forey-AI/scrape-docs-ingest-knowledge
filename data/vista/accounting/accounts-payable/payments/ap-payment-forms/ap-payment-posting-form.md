---
title: "AP Payment Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form"
---

# AP Payment Posting Form

Use the AP Payment Posting form to pay invoice transactions. This process is done in a batch and includes multiple steps, all of which can be done from this form.
There are multiple ways you can add invoices to a payment batch:

- Using the initialization feature in the AP Initialize Payments form.

- Using the Initialize New Payment feature in the AP Payment Posting form.

- Manually using the AP Payment Posting form.

- From a payment workfile in the AP Payment Workfile form.

Best practice is to use a separate batch for each pay method since the process for completing each method is inherently different.
Important: The exception to this recommendation is if you are using ePayments (U.S. only), which is able to processes all originally assigned pay methods at once. When you generate the ePayments data file, you are given the option to change the pay method originally assigned to N-ePayments.

You can use this form to process all of your AP invoices. Payment options include:

- computer checks

- manual checks

- EFTsNote: For United States users, EFT transactions can also include International ACH Transactions (IATs). For more information, see [Set up Vendors for International Electronic Payments (United States)](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-up-vendors-for-international-electronic-payments-united-states)

- voided payments

- imported payments (transactions that were imported from a third-party application using import templates. For more information, see [Standard Import Templates](/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates)).

You cannot add invoices to the batch if they are on hold, unapproved, prepaid, or in a separate batch of any type.

Related tasks

- [Add Multiple Invoices to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-multiple-invoices-to-a-payment-batch)

- [Add a Single Invoice to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-a-single-invoice-to-a-payment-batch)

- [Add Invoices to a Payment Batch Manually](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-payment-batch-manually)

- [Add Invoices to a Batch Using AP Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-batch-using-ap-payment-workfile)

- [Post and Process Payments](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/post-and-process-payments#ID-00004ae6--en__ID-00004ae6)

- [Void Unposted Payment Records](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-unposted-payment-records#task-192--en__task-192)

Related information

- [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form)

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

- [AP Credit Service Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-credit-service-download-form)

- [AP EFT Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form)

- [AP Initialize Payments Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-initialize-payments-form)

- [AP Payment Preview Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-preview-form)

- [VA Audit Log Viewer Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/va-audit-log-viewer-form)

## Field Definitions: AP Payment Posting Form

The following is a list of field descriptions for the AP Payment Posting form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

### Seq#

Enter the existing sequence to work on, or enter N,
 New or  +  to add a new sequence.
 The system assigns the next available sequence number.

### Pay Method

 The Pay Method field in the AP Payment Posting form, header Info tab.

If you added invoices automatically, this field defaults from the Pay Method field in one of these forms:

- AP Transaction Entry

- AP Unapproved Invoice Entry

- AP Recurring Invoices

Select the payment method to use for this transaction.

- N-ePayments (U.S. only) - You are not required to select the N-ePayments method before paying invoices because at the moment you generate the ePayments file, you are given the option to change the pay method originally assigned. For details, see the field help for [Payment Methods](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-000063380001--en) in the AP ePayments Export form.

- C-Check

- E-EFT - Only select this method if you have entered bank routing information for this payee in the AP Vendors form (Routing Transit # and Bank Account # fields, Payment Method tab).If you do not have this information set up, the system will display a warning and you will not be able to process the payment

- S-Credit Service - Only select this method if you have taken these steps in the AP Company Parameters form:

- Selected either 1-Comdata or 2-EFS from the Credit Service drop-down (Payment Services tab)

- Entered information in the required fields of either the Comdata or EFS section (Payment Services tab)

- Entered information in the CM Co# (Subledgers tab) and CM Acct # (Payment Services tab) fields

If no payment method is assigned, the system displays a warning and will not allow you to process the payment.
Note: Once a CM Ref# is assigned to a payment transaction (whether manually or automatically), this field is disabled. If you need to change the payment method, you must first clear the CM Ref# for the applicable transaction.

Related information

- [About Invoice Payment Batches](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches)

### CM Acct

The CM Acct field on the AP Payment Posting form, header Info tab.
This field is enabled only when the Pay Method is C-Check and the Check Type is M-Manual.
Enter the CM bank account for paying this
 invoice.
For all other payment types, this field automatically populates with the CM Acct # specified on the invoice (in AP Transaction Entry, AP Unapproved Invoice Entry, or AP Recurring Invoices) or during initialization (in AP Initialize Payments) if no CM Acct is specified on the invoice.

### Check Type

The Check Type drop-down on the AP Payment Posting form, header Info
 tab.
For payments made by check only, indicate the type
 of check used to pay this transaction.

- C-Computer– check generated by computer

- M-Manual– check paid manually

Note: There are two additional options available from this field:
 P-Prepaid and I-Import. However, you cannot manually select
 either one. Both indicate that the transaction has already been
 paid either through the AP Prepaid Process form or via the
 third-party application you are importing data from (via the AP
 Payment or AP Payment Textura import templates).
Note: If you do not want the manual check amount to be reduced by
 a displayed discount amount, you can use the AP Payment Control Detail program to change
 the discount amount before you record the payment in AP Payment Posting.
Note: The system clears this field automatically when you change the Pay
 Method to something other than 'C-Check'.

### CM Ref#

The CM Ref# field on the AP Payment Posting form, header Info tab.

For manual checks only, enter the CM reference number (check number) for this transaction. Up to 10 digits are allowed, including any leading zeros.
For computer-generated checks, EFT transactions, ePayments, or Credit Service transactions, this field is disabled and populates automatically when running the related program (AP Check Print, AP EFT Download, AP ePayments Export, or AP Credit Service Download, respectively) based on the CM Ref# assigned in those forms.
Note: Once a CM Ref# is assigned to a transaction, the system disables the Pay Method field. If you need to change the Pay Method, you must first clear the CM Ref# for the applicable transaction.

### CM Seq#

The CM Seq# field on the AP Payment Posting form, header Info tab.

This field is enabled only if the Pay Method is C-Check and the Check Type is M-Manual.
Displays the CM reference sequence number for this
 transaction. For all payment types, this field defaults to 0.
For manual checks, you may override this value as needed.

### EFT Seq#

This field displays the sequence number of the
 EFT transaction. This number is assigned by the system when the EFT Download program is
 run.

### Paid Date

The system enables this field when you select
 M-Manual from the Check Type field.
Enter the date this transaction was paid. This field defaults the current date if the current month and year match the batch month and year. If they do not match, this field defaults as blank.
Note: If you enter a date that is not the same month and
 year as the batch month, the system displays a warning, but you can still post the
 payment.

### Vendor

 Vendor field in the AP Payment Posting form
 Enter the vendor to be paid. Press F4 to see a
 list of vendors.
Note: If you selected S-Credit Service from the Pay Method
 drop-down, and you are using Comdata as your credit service provider (you selected
 Comdata from the Credit Service drop-down in AP Company
 Parameters form, Payment Services tab), you must enter an email address in the Payment Service Email field in the AP
 Vendors form (Payment Method tab) in order to add the vendor here.

### Name

Initially defaults the name of the vendor
 specified in the Vendor field. This value may be overridden if necessary. This is
 particularly useful when printing checks for temporary vendors using the same vendor
 number.

### Supplier

If this is a two-party check, enter the second party (from AP Vendors)
 to be paid by this check. Press F4 to see a list of vendors.

### Add'l Info

Defaults the additional information specified for this vendor in AP
 Vendors, up to 60 characters allowed; may be overridden. Information entered here is
 included when printing checks for this vendor (e.g. Attention line, Garnishment Case #,
 etc.).

### Address

Enter the
 vendor's payment address information in the following fields (or accept the default).
 Overriding the defaults for these fields may be useful when printing checks for vendors using
 the same vendor number.

- Address - This field initially defaults the payment address specified for
 the selected vendor in AP Vendors, up to 60 characters.

- City -
 This field initially defaults the payment city for the selected vendor in AP Vendors, up
 to 30 characters.

- State
 - This field initially defaults the payment state for the selected vendor in AP Vendors.
 If you override the default, you must enter a valid state. The system validates the state
 based on the Default Country field in HQ Company Setup for the active company. If the
 state is not valid, the system will display an error but will allow entry.

- Zip
 Code - This field initially defaults the payment zip/postal code

- Country - This field defaults the payment country specified for the vendor
 in AP Vendors. If you override the default, enter the 2-character country code. Entry in
 this field is required when the address exists outside the Default Country
 specified in HQ Company Parameters for the active company. The country must be valid for
 the specified state (e.g., state, province, territory, etc.) as defined in HQ States.

### Month

 Enter the expense month of the transaction to be added to the payment batch.

### AP Trans

 Enter the transaction to be added into the payment batch. Use F4 to display a list of available AP transactions.

## Initialize New Payment

 The Initialize New Payment section of the AP Payment
 Posting form allows you to add a single invoice to a payment batch. This section includes
 the Month and APTrans fields. It also includes the
 CM Acct is
 missing on the transaction... field when you attempt to add an invoice
 without an associated CM account number.The
 following instructions detail how to add single invoices to a batch using the Initialize
 New Payment section of AP Payment Posting.

1. Enter a new sequence number
 in the Seq
 # field or enter N, New, or
 + to have the system
 generate the next available sequence number.

1. Enter the invoice expense
 month in the Month field in the Initialize New Payment section.

1. Enter the AP transaction
 number in the AP Trans field. Press F4 to see a list of invoices
 associated with the specified month.

1. Click Initialize.

 The system adds the invoice to the batch.If an invoice is
 missing a CM account, the system displays a warning dialog box. Close the dialog and
 enter a CM account in the CM Acct is missing on the
 transaction... field. Click Re-validate and then click Initialize
 to add the invoice to the batch.
If you are adding an invoice with a payment
 method of credit service, the system will not add the invoice if the CM account does not
 match the CM Acct field (AP Company Parameters form, Payment
 Services tab). Additionally, invoices with a payment method of credit service will not
 be added if you did not enter the required credit service provider information in the AP
 Company Parameters form (Comdata or EFS sections of the Payment Services
 tab).
Invoices with payment method of either check or EFT that reference the
 credit service CM account number (CM Acct field, AP Company
 Parameters form, Payment Services tab) will not be added to the batch.
If the
 invoice is associated with a subcontract or purchase order, the system will check for
 compliance. If the invoice is “out of compliance,” a warning displays. To add the
 transaction, click Initialize and the system adds the invoice to
 the payment batch. For more information on tracking compliance in AP, see [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking).
