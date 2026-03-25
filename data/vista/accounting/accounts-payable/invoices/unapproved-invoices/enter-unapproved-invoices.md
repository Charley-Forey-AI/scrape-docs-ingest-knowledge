---
title: "Enter Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/enter-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/enter-unapproved-invoices"
---

# Enter Unapproved Invoices

Use the AP Unapproved Invoice Entry form to enter invoice records that need to pass through an approval process before they are posted.
Entering unapproved invoices is done in the same manner as regular AP invoices (that is, those entered using the AP Transaction Entry form), except that certain missing or incomplete data is permissible. However, data must be valid if entered, such as job numbers, purchase orders, subcontract numbers, and so forth.
If you have data to enter that is normally validated (such as a PO or Subcontract #), but has not yet been entered in the system, use F5 to access the setup form and enter the data. If you cannot currently enter the data, consider using the Description field to note and explain the data, so that you can enter it properly later.
For more information about the fields on this form, see the F1 Help.

1. In the Month field, enter the invoice month.Tip: Regardless of the month you enter here, you have the option of posting invoices, once approved, to any open period.

1. In the Seq # field, enter N , or + to enter the next available sequence number.

1. In the Vendor field, enter the vendor number. Press F4 to select from a list.Note: If you have set the system to check for compliance when entering invoices (you selected the Don't add vendor to payment batch if "out of compliance" checkbox in the AP Company Parameters form (Invoice Options tab) and the vendor you have entered is out of compliance, a warning displays in red above the header. You can continue to enter the record, however; this rule will be enforced when attempting to post, once the invoice is fully approved.

1. Complete the remaining fields as necessary. These include: AP Reference, Reviewer Group, Description, Invoice Date, Discount Date, Due Date, and Inv Total. For more information, see the F1 Help.Note: If you want the system to apply a group's reviewers to all invoice lines, enter a reviewer group in the Reviewer Group field.

1. If you need to prevent this transaction from being paid until you [release the hold code](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/about-placing-invoicestransactions-on-hold), select the Payment Overrides tab and enter a hold code for the invoice in the Hold Code field.

1. To group this invoice together with other invoices, select the Payment Overrides tab and enter a pay control code or accept the default in the Pay Control field.

1. Select the pay method for this invoice from the Pay Method drop-down. Instructions on how to include EFT addenda info for posting are included in [Posting Approved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices).

- N-ePayments - only select this option if you meet the setup requirements as described in [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

- C-Check

- E-EFT

- S-Credit Service

Instructions on how to include EFT addenda info for posting are included in [Posting Approved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices).
Note: If you select E-EFT and the invoice will require [addenda information](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00006e4a--en) before payment, you can still allow the invoice to go through the approval workflow. However, after it's approved and ready to post, you will need to use the AP Transaction Entry form to add the addenda information. To do so, follow the instructions in [Posting Approved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices), but stop after you successfully added the invoice to a batch by selecting Update (and before you select Post). Close the form, go to the AP Transaction Entry form, locate and open the batch you have just created, select the Addenda Info tab, and add the required information. Post this batch as normal. If you do not have bank routing information set up in AP Vendors (Payment Method tab) for the specified vendor, the system displays a warning, but allows you to save the record.

Note: You should select S-Credit Service only if:

- You have selected either 1-Comdata or 2-EFS from the Credit Service drop-down in the AP Company Parameters form (Payment Services tab);

- You have entered information in either the fields in the Comdata or EFS sections of the AP Company Parameters form (Payment Services tab); and

- You have entered information in the CM Co# (Subledgers tab) and CM Acct fields (AP Company Parameters form, Payment Services tab).

- If using Comdata: You have entered an email address for the vendor for receiving remittance information from Comdata in the Payment Service Email field in the AP Vendors form (Payment Method tab).
If you select S-Credit Service and you do not have the above information set up, the system displays a warning but allows you to save the record.

1. If you want to include this invoice in 1099 totals when posted, fill in the information in the 1099 Info section of the form. For more information, see [1099 Processing](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s).

1. Check the Include in 1099 Totals box. The system enables the Type and Box # fields.

1. Enter the 1099 type in the Type field or press F4 to select from a list of types.

1. In the Box # field, press F4 to select from a list of valid boxes on the 1099 form that will be used to accumulate and print 1099 amounts.

1. Enter the cash management account or accept the default for paying this invoice in the CM Acct field.

1. Select the Separate Payment checkbox if this invoice/transaction is to be paid separately from other invoices/transactions for the associated vendor.

1. [Override the vendor's address](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices) on the Address Override Info tab, if necessary.

1. Reviewers assigned to the invoice on the Reviewers tab (header level) will default to each invoice line. For more information, see [Assigning Reviewers to Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices/assign-reviewers-to-unapproved-invoices).

1. Add detail lines to the invoice. For more information, see [Entering Accounts Payable Invoice Lines](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s.).

1. Add additional reviewers to invoice lines on the Reviewers tab (line level). For more information, see [Assigning Reviewers to Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices/assign-reviewers-to-unapproved-invoices).

1. If you want to mark the invoice as ready to review and release it into the approval workflow, select the Change Status button, or, if using the grid, select 1 - Ready in the Invoice Status column drop down list.

Once you enter the invoices and mark them as ready to review, assigned reviewers with applicable approval sequences can view them in the AP Unapproved Invoice Review form.
