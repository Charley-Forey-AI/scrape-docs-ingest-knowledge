---
title: "Update T+M Billings - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-tm-billings/update-tm-billings---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-tm-billings/update-tm-billings---cost-center-information"
---

# Update T+M Billings - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, all billings will be shown regardless of cost center security setup for the operator. Spectrum will determine the cost center for each billing by looking first at the A/R contract. If the contract does not have a cost center, then the job cost center will be used. If there is no valid cost center for a billing, then the screen will give a warning and will clear the Select checkbox if the user selects the Select checkbox.
When the user selects the Select checkbox for a billing, Spectrum will also determine the A/R trade G/L account that will be assigned to the invoice header; note that the override G/L account may apply. If the header cost center (from the contract or the job) is not valid for this G/L account, then an error will display and the Select checkbox will be cleared.
The update will use this cost center (from the contract or the job) on the A/R invoice header. The cost center will not display on the Update T+M Billings to Invoice Entry.
The update creates a detail line for each summarized cost type, add-on, and fee line. Spectrum will calculate the cost center for each detail line from the phase override; if no phase override exists, Spectrum will use the contract/job cost center. Spectrum will create one detail line for each unique cost type and cost center. It will also create a detail line for each add-on and fee, using the header cost center for those lines.
Spectrum will verify that the assigned cost center is allowed for the G/L account associated with that detail line. If a mismatch would be created, then selection of that billing will not be permitted in he Update T+M Billings to Invoice Entry starting screen.
When the Allow G/L account overrides by cost center checkbox on the Enterprise Installation screen is selected, Spectrum will use the override G/L account for the invoice, if one exists for the Default A/R trade G/L account in the Accounts Receivable Installation screen.
If the 'Use entity-specific numbering?' installation option is selected for this company, entity-specific invoice numbers used for Accounts Receivable invoices will read for the cost center to be assigned to the new invoice. If the cost center is assigned to the 'main company entity' (blank), then get the 'Next invoice number' from Accounts Receivable Installation. If an entity is associated with the cost center, then read the new Entity Invoice Number Table for the 'Next invoice number' to be assigned to invoices in that entity.
Update T+M Billings - VAT processing information
If the 'Utilize value added tax (VAT) tracking?' checkbox is selected in General Ledger Installation, this update includes VAT tax on the new customer invoice when a VAT code is present on the billing.
The invoice amount shown on the report after the update includes the total VAT amount.
