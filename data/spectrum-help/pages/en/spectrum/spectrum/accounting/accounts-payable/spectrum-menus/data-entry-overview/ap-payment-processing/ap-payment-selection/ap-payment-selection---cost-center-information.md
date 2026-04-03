---
title: "A/P Payment Selection - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/ap-payment-selection---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/ap-payment-selection---cost-center-information"
---

# A/P Payment Selection - Cost Center Information

If a cost center has not already been assigned, you will be prompted to enter one when you open this screen. At the Invoice field, the Open A/P Items window only displays invoices and credit memos assigned to the same cost center as the one assigned to invoices in the current processing group. Likewise, when adding invoices and credit memos in this screen, you can only add ones that are assigned to the same cost center as the one at the top of the screen. For backward compatibility, invoices and credit memos that do not have an assigned cost center in the invoice header can be selected in any check run (similar functionality exists for the Deselect, Take Discount, Zero Discount, and Hold buttons).
When performing payment selection, Spectrum selects (or deselects) invoices only if your operator has permission to access the vendor and invoice. Spectrum compares the vendor's list of shared cost centers with cost centers in your assigned cost center scheme, and if there are no common cost centers, then invoices for that vendor are not selected. Spectrum also compares the cost center assigned in the invoice with cost centers in the your assigned cost center scheme, and if the invoice cost center is not included, then the invoice is not selected.
The Payment Selections window includes an option for a specific cost center. When a cost center is specified, then Spectrum includes only invoices assigned to that cost center. If you attempt to include a disallowed invoice, Spectrum will provide an alert message stating "Some items will not appear due to cost center security."
The windows accessed with the Deselect, Take discount, Zero discount and Hold buttons also provide cost center selections and will verify authorization for both the vendor and invoice before processing.
Inter-post accounts: This screen allows you to process Accounts Payable payments from across multiple cost centers (and multiple entities) in the same processing group. Payment Selection includes security that assures a valid payment inter-post G/L account is present before allowing selection of invoices that have a different assigned cost center than the designated 'payment cost center' for the current processing group.
