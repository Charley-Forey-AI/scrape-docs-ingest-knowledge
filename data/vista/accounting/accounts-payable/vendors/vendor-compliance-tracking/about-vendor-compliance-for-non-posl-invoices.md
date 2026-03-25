---
title: "About Vendor Compliance for Non-PO/SL Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices"
---

# About Vendor Compliance for Non-PO/SL Invoices

With Vista, you have the ability to track compliance for invoices that are
 not associated with purchase orders and/or subcontracts.
If you track compliance for non-PO/SL invoices, there
 are two options in AP Company Parameters that need to be set in order to implement this
 feature:

- Check compliance on transaction entry, warn only – select this
 option if you want the system to check vendor compliance when posting non-PO and
 SL invoices. If selected, and you are entering a non-PO/SL invoice for which the
 vendor is out of compliance, a warning displays, but the entry is allowed. If you do
 not select this option, the system does not check invoices for vendor compliance.

- Don't add Vendor to Paym't batch if “out of compliance” –
select this option if you do not want “out of compliance” non-PO/SL
 transactions initialized into a payment batch. If not selected, the payment initialization
 process includes out-of-compliance invoices.

Note: Setting these options is only part of the setup required for implementing
 compliance checking for non-PO/SL transactions. You must also make sure to appropriately
 flag each compliance code you want verified in the HQ Compliance Codes form.

Related information

- [HQ Compliance Codes Form](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form)

- [About Compliance Tracking Setup for Non PO/SL Invoices](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices/about-compliance-tracking-setup-for-non-posl-invoices)
