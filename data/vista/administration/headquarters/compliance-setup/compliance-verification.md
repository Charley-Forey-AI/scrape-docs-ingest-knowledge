---
title: "Compliance Verification | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/compliance-setup/compliance-verification"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/compliance-setup/compliance-verification"
---

# Compliance Verification

To implement compliance verification, you will need to check the Use This Code to Verify Compliance option for each compliance code you set up (HQ Compliance Codes).

Any compliance code with the Use This Code to Verify Compliance checkbox selected that has been assigned to a subcontract or purchase order, will be reviewed when the transaction is entered (option in AP Company Parameters) or considered for payment to ensure it is in compliance.
If you are also tracking vendor compliance for non-PO/SL invoices (that is, a vendor is assigned one or more 'all invoice' compliance codes), the system will first check compliance for the vendor at the header level, then check compliance at the line level for all PO and SL lines.
If you leave the Use This Code to Verify Compliance checkbox unselected, compliance will be informational only, and no verification will occur. (Note: This option controls a default on the individual compliance codes at the vendor, purchase order, and/or subcontract level. It may be overridden for each record at any time in the process.)
[HQ Compliance Codes Form](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form)
[AP Vendor Compliance Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-compliance-form)
[PO Compliance Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form)
[SL Compliance Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form)
