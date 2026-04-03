---
title: "Scale Ticket Journal - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal/scale-ticket-journal---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal/scale-ticket-journal---cost-center-information"
---

# Scale Ticket Journal - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, Spectrum will populate the Cost center fields as required in the destination records.
Inventory job requisitions, transfers, receipts, and mixes will not require any change. The warehouse from the plant is associated with these records, and the inventory module will automatically use the cost center from the warehouse (and job / phase) for these transactions.
For Accounts Receivable invoices, Spectrum will check the customer contract. Spectrum will first check the customer and customer job from the ticket, and will use the cost center assigned to that customer contract, if applicable. If no cost center there, Spectrum will look at the default customer contract (blank customer job) and use that cost center, if applicable. Otherwise, Spectrum will use the cost center from the plant's warehouse. This cost center will be assigned on the invoice header and on each invoice detail line.
If posting to Order Processing invoices, the same hierarchy is used to find the cost center that will be assigned to the Order Processing invoice header. No cost center assignment is needed for the Order Processing detail lines because the cost center associated with the warehouse is used.
For customer sales tickets, the Scale Ticket Journal for Sales Invoices displays the cost center assigned to each ticket.
For customer sales tickets, when the cost center to be assigned to the invoice header is not allowed for the customer, then the ticket will appear on the exception report and will not be updated.
If the 'Use entity-specific numbering?' installation option is selected for this company, entity-specific invoice numbers used for Accounts Receivable invoices will read for the cost center to be assigned to the new invoice. If the cost center is assigned to the 'main company entity' (blank), then get the 'Next invoice number' from Accounts Receivable Installation. If an entity is associated with the cost center, then read the new Entity Invoice Number Table for the 'Next invoice number' to be assigned to invoices in that entity.
