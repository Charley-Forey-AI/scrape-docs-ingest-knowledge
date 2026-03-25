---
title: "Use This Code for \"All Invoice\" Compliance | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form/field-definitions-hq-compliance-codes-form/use-this-code-for-all-invoice-compliance"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form/field-definitions-hq-compliance-codes-form/use-this-code-for-all-invoice-compliance"
---

# Use This Code for "All Invoice" Compliance

The Use This Code for "All Invoice" Compliance checkbox on the HQ Compliance Codes form.
Select this box to use this compliance code for 'all invoice' vendor compliance checking. If you have specified to 'check vendor compliance on transaction entry' (flag in AP Company Parameters), vendors assigned 'all invoice' compliance codes (in AP Vendor Compliance) will be checked for compliance when entering transactions in AP.
Note: It is recommended that you select this option for compliance codes that will be used on non-PO/SL invoices only, and that you use separate codes for PO and SL compliance. If you select this option for a compliance code and then assign the code to a vendor (in AP Vendor Compliance), it will not be added to existing POs or SLs.
Leave this box unselected if this compliance code will be used to verify compliance for purchase order and subcontract invoices only.
Note: This option also affects the AP Payment Preview with Compliance report. If selected for a compliance code, non PO/SL transactions will only be reported as 'out of compliance' on the report.
