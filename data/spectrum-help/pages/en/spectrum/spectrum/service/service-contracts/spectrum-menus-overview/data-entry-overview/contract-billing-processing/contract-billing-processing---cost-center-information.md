---
title: "Contract Billing Processing - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-billing-processing/contract-billing-processing---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-billing-processing/contract-billing-processing---cost-center-information"
---

# Contract Billing Processing - Cost Center Information

If cost centers are being used, the software will assign a
 cost center to the Accounts Receivable invoice header and each detail line.
The software will first read the cost center from the Service Contract Header Table and
 assign this contract, and if not available, the update will assign the cost center from
 the Site Table. If you do not have authorization for the assigned cost center, the
 register/update will not include that contract.
If the 'Use entity-specific numbering?' installation option is selected for this company, entity-specific invoice numbers used for Accounts Receivable invoices will read for the cost center to be assigned to the new invoice. If the cost center is assigned to the 'main company entity' (blank), then get the 'Next invoice number' from Accounts Receivable Installation. If an entity is associated with the cost center, then read the new Entity Invoice Number Table for the 'Next invoice number' to be assigned to invoices in that entity.
