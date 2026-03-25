---
title: "Print Two-Party Computer-Generated Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/checks/about-two-party-ap-checks/print-two-party-computer-generated-checks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/checks/about-two-party-ap-checks/print-two-party-computer-generated-checks"
---

# Print Two-Party Computer-Generated Checks

Use the AP Check Print form to print computer-generated,
 two-party checks.
You can issue checks to two payees—the vendor and a second
 vendor or supplier to the vendor. A two-party check (also known as a joint check) is generally
 used on the transaction to ensure payment to a supplier by a particular subcontractor. For
 example, if you have not received a signed Waiver of Right To Lien form back from a
 subcontractor’s supplier, you can issue a two-party check to the subcontractor to ensure the
 supplier receives payment from the sub.To print computer-generated two-party checks.

1. Create the supplier record in
 the AP Vendors form.Note: You can create suppliers as either a regular or a
 supplier vendor type. To set them up as a supplier, select the Supplier
 option from the Vendor Type field in the AP Vendors form.

1. Set up the transaction (AP
 Transaction Entry, AP Recurring Invoices, AP Unapproved Invoice Entry) and assign the
 supplier to each line on the transaction that comprises the two-party check (Supplier
 field). If you do not assign the supplier here, you can assign the supplier later in the process in the AP Payment
 Posting form or AP Payment Control Detail form (accessed from the AP Payment Workfile form).Note: If only part of the subcontractor’s check should
 be two-party, use the AP Payment Control Detail form to split the transaction into parts and
 assign the supplier to the portion requiring a two-party check. For more information,
 see [Creating Partial Payments](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form).

1. Set up the information requested
 in the AP Payment Posting form. Select C-Computer from the Check Type
 drop-down. If you have not previously assigned a supplier, you can do it here.

1. Select Tasks > Print Checks to access the AP Check Print form.

1. Set up the parameters requested
 and click Print
 Checks.The system prints the check with the
 supplier’s name just below the subcontractor’s name. If you are paying the subcontractor
 for other transactions that do not have an assigned supplier, the system prints a separate
 check to the subcontractor for the total of those transactions. For more information, see
 [Printing AP Checks](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form).

1. Once the checks finish printing,
 process the batch.
