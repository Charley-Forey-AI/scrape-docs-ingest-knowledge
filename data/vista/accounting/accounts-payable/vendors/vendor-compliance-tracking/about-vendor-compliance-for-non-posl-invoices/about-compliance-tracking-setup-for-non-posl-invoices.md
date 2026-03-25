---
title: "About Compliance Tracking Setup for Non PO/SL Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices/about-compliance-tracking-setup-for-non-posl-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices/about-compliance-tracking-setup-for-non-posl-invoices"
---

# About Compliance Tracking Setup for Non PO/SL Invoices

There are setup options in both Accounts Payable and Headquarter that you should consider before tracking vendor compliance on non-purchase order and non-subcontract related invoices.
In the AP Company Parameters form:

- Check Vendor Compliance on Trans Entry, Warn Only – This checkbox should be selected if you are tracking vendor compliance when posting non-PO and SL invoices. If you enter an invoice for which the vendor is out-of-compliance, a warning is displayed, but the entry will be allowed. If you leave this checkbox cleared, invoices are not checked for vendor compliance.

- Don't Add Vendor to Paym't Batch if out of Compliance – This checkbox should be selected if you do not want non-PO or SL transactions initialized to a payment batch when the vendor is out of compliance. If you leave this checkbox cleared, out-of-compliance invoices can be initialized into payment batches.

In the HQ Compliance Codes form:

- Use this Code to Verify Compliance – Select this checkbox for every compliance code that you want verified when checking compliance. If not selected, compliance is not checked for that code.

- Use this Code for 'All Invoice' Compliance – Select this checkbox if you want the compliance code to check compliance on all non-PO/SL invoices. If you leave this checkbox unselected, compliance is checked for purchase orders and subcontracts only.

## Compliance Check During Invoice Entry

Typically, when you add a compliance code for a vendor (in the AP Vendor Compliance form), the system checks for purchase orders and subcontracts assigned to the vendor. If purchase orders and/or subcontracts exist for the vendor, the AP Update PO/SL Compliance window displays, allowing you to update the codes to all purchase orders and/or subcontracts for that vendor. However, if you add/delete a compliance code flagged for 'all invoice' compliance, this window does not display, regardless of whether there are existing purchase orders and/or subcontracts for the vendor.
Once you have implemented this feature, each time you enter a non-PO/SL transaction (in AP Transaction Entry, AP Unapproved Invoice Entry, AP Payment Posting, or MS Haul Payment Worksheet) that is not in compliance, you will receive a warning message; however, the entry will be allowed.

## Compliance Check on Payments

If you specify to exclude 'out of compliance' vendors in payment batches (flag in AP Company Parameters, Invoices tab), the payment initialization process excludes 'out of compliance' vendors for non-PO/SL invoices. However compliance checks for purchase orders and subcontracts override vendor compliance checking. In other words, if a transaction passes the 'all invoice' check, but its PO or SL lines are not in compliance, the transaction will not be added to the payment batch. Likewise, if an 'all invoice' check shows 'out of compliance', but the PO/SL lines are in compliance, transactions will be added to the batch.

Select the following links for more information about compliance tracking.
[Initial Setup for Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/initial-setup-for-compliance-tracking)
[Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking)
[Compliance Maintenance](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/compliance-maintenance)
