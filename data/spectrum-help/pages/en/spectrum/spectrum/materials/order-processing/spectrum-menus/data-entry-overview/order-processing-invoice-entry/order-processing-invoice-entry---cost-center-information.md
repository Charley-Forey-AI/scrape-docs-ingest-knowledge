---
title: "Order Processing Invoice Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---cost-center-information"
---

# Order Processing Invoice Entry - Cost Center Information

If cost centers are being used, the Invoice Entry screen
 includes a Cost center
 field.
Spectrum verifies that the cost
 center is authorized for the specified customer. Spectrum compares the Invoice Entry cost center with the list of
 cost centers for the customer; if the cost center is not listed, then the entry is not
 allowed. Spectrum also compares the
 entry with cost centers in the operator's assigned scheme; if the order's cost center is
 not present, then the cost center is disallowed.
When the Enterprise Installation Allow G/L account overrides by cost center checkbox is selected,
 Spectrum will assign the Accounts
 Receivable Trade G/L account based on a list of override G/L accounts in the
 A/R Trade Override window in Order Processing
 Installation. The header cost center is used to determine the override
 G/L account.
Spectrum will validate that the cost center is valid for the A/R G/L account when adding or changing the G/L account code.
In the Invoice Entry > Properties window and in the Details window on each line,
 Spectrum will validate that the
 warehouse entered has an active cost center assigned to it. If not, entry of that
 warehouse will not be allowed.
When reversing an invoice, Spectrum will create a credit memo with the same cost center that
 was assigned on the main Invoice Entry screen.
