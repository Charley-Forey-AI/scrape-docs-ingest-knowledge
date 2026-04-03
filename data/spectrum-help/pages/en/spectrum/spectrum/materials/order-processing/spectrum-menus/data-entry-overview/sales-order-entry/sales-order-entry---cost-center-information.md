---
title: "Sales Order Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---cost-center-information"
---

# Sales Order Entry - Cost Center Information

If cost centers are being used, the Order
 Entry screen includes a  Cost
 center field. Spectrum
 verifies that the cost center is authorized for the specified customer. Spectrum compares the Order Entry cost center
 with the list of cost centers for the customer; if the cost center is not listed, then the
 entry is not allowed. Spectrum also
 compares the entry with the entry with cost centers in the operator's assigned scheme; if the
 order's cost center is not present, then the cost center is disallowed.
When the Enterprise Installation > Allow G/L account overrides by cost
 center checkbox is selected, Spectrum will assign the Accounts Receivable Trade G/L account
 based on a list of override G/L accounts in the Order Processing Installation > A/R Trade Override window. The header cost center is used to determine the override G/L
 account.
Spectrum will validate that the cost center is valid for the A/R G/L account when the G/L account code is changed.
In the Order Entry, Spectrum will validate that the warehouse entered has an active cost center assigned to it. If not, entry of that warehouse will not be allowed.
During Order Confirmation, the cost center specified on the main screen is transferred to Invoice Entry as the confirmation invoice is created.
