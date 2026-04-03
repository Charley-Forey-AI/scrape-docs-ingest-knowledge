---
title: "Purchase Order Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---cost-center-information"
---

# Purchase Order Entry - Cost Center Information

If the cost center feature is enabled, the Cost center row will appear on the grid and
 only purchase orders you are allowed to access will display on this page.
This is determined by comparing the cost center assigned to the purchase order with cost
 centers in your scheme, and if the purchase order cost center is not present, then the
 purchase order will not be displayed.
Spectrum also verifies that the operator has security authorization to the cost center assigned to the work order in the Work Order Header Table. If the Work Order module is present, then at the Work order field, Spectrum will compare the cost center assigned to the work order with cost centers in your assigned scheme, and if the cost center is not present, then purchase order entry for that work order will not be allowed.
All items on order for the purchase order will displays on the page, regardless of operator cost center security. When adding or editing a detail line, the Operator can only assign or change a cost center they have authorization to. However, when deleting a detail row, any cost center can be deleted regardless of Operator authorization.
If a purchase order is issued for a work order that has a different cost center from the associated site ID, the work order cost center will be used instead.
