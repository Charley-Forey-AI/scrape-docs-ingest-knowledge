---
title: "Enter Accounts Payable Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices"
---

# Enter Accounts Payable Invoices

Use the AP Transaction Entry form to enter accounts payable invoices.
For more information about fields on the form, see the F1 Help.

1. Open the AP Transaction Entry form.This is batch form, so the AP Batch Selection form opens. Once you open an existing batch or create a new one, the AP Transaction Entry form displays.

1. Enter New, N, or + in the Seq # field and tab off. The next available sequence number defaults in the field.Tip: You can also add previously posted invoices to the batch by selecting File  > Add Transaction.

1. Enter the vendor number in the Vendor field. Press F4 for a list of vendors.Tip: You can also enter the sort name (Sort Name field, AP Vendors form) for the vendor in this field and tab off to have the vendor default in this field.
Note: If you have set the system to check for compliance when entering invoices (you selected the Don't add vendor to payment batch if "out of compliance" checkbox in the AP Company Parameters form, Invoice Options tab), a warning displays in red above the header once you enter a vendor in the Vendor field. You can continue to enter the record, however.

1. Enter the invoice number in the AP Reference field.

1. Enter a description for the invoice in the Description field.

1. Enter the invoice date in the Invoice Date field. The Due Date and Disc Date fields default based on the payment terms assigned to the vendor (Payment Terms field, AP Vendors form).

1. Accept the defaults in the Due Date and Disc Date fields or override as necessary.

1. Enter the invoice total in the Invoice Total field.Note: The amounts for each of the lines on this invoice must total this amount; if they do not, the system will not allow you to save the transaction record.

1. If you need to prevent this transaction from being paid until you [release the hold code](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/about-placing-invoicestransactions-on-hold), select the Payment Overrides tab and enter a hold code in the Hold Code field.

1. If you need to group this invoice together with other invoices, enter a pay control code in the Pay Control field.

1. From the Pay Method drop-down, select one of the following payment methods or accept the value defaulted from the AP Vendors:

- N-Viewpoint ePayments (U.S. only) - You should only select this method if you meet the setup requirements. For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

- C-Check

- E-EFT - If you select this method and you have not set up bank routing information for the specified vendor in AP Vendors (Payment Method tab), the system displays a warning, but allows you to save the entry. Additionally, the system enables the Addenda drop-down on the Addenda Info tab, allowing you to include tax payments, child support, or invoice detail with your payments. For details, see [Addenda](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00006e4a--en).

- S-Credit Service - You should only select this method if you have set up the appropriate information in AP Company Parameters (Payment Services tab) and AP Vendors (Payment Method tab). For more information, see [Set up Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-card-payments).

1. Enter the cash management account for paying this invoice in the CM Acct field or accept the default.

1. Check the Separate Payment box if this invoice/transaction is to be paid separately from other invoices/transactions for the associated vendor.

1. If this is a prepaid transaction, enter information in the Prepaid section.

1. If you want to include this invoice in 1099 totals, fill in the information in the 1099 Info section of the form. For more information, see [1099 Processing ](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s).

1. Check the Include in 1099 Totals box. The system enables the Type and Box # fields.

1. Enter the 1099 type in the Type field or press F4 for a list of types.

1. In the Box # field, press F4 to select from a list of valid boxes on the 1099 form where 1099 amounts will accumulate and print for this vendor.

1. [Override the vendor's address](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices) on the Address Override Info tab, if necessary.

1. Save the record as normal.

1. [Add detail lines to the invoice](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s.).You can now create additional invoice entries or process the batch.
Note: Job, Purchase Order, Subcontract, and SM Work Order invoices may not post to closed jobs, depending on the settings of the Allow Posting to Soft-Closed Jobs and Allow Posting to Hard-Closed Jobs checkboxes in the JC Company Parameters form:

- If the appropriate checkbox is not selected, the system displays a warning when you try to post an invoice referencing the closed job and prevents you from continuing.

- If the appropriate checkbox is selected, the system displays a warning, but allows you to continue.

For more information on posting to closed jobs, see [Closing Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract).
