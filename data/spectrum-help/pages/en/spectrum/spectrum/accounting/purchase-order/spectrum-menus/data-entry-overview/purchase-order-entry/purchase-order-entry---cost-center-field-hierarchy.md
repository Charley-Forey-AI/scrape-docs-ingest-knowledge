---
title: "Purchase Order Entry - Cost Center Field Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---cost-center-field-hierarchy"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---cost-center-field-hierarchy"
---

# Purchase Order Entry - Cost Center Field Hierarchy

If the cost center feature is enabled in the Enterprise
 Installation page, a Cost center
 field will display.
When adding a new purchase order, Spectrum first validates the selected vendor code (if it
 is not blank or not set up in the vendor file) by comparing the vendor's list of shared
 cost centers with the cost centers in your assigned scheme. If there are no common cost
 centers, purchase order entry for that vendor will not be allowed. The Cost center field default may be edited
 for all purchase orders, so that you can use this code when selecting invoices for
 payment.
The following hierarchy is used when determining the cost center code that will initially default into the Cost center field:

- If the Operator has access to more than one cost center, the first
 cost center entered in this screen should automatically default in subsequent purchase
 order entries.

- Use the operator cost center if only one cost center is defined for
 the operator.

- Use the vendor cost center if only one cost center is defined for
 the vendor. If the operator changes the work order in this window,
 the software will adjust the cost center assigned to the distribution line based on
 the cost center in the Work Order Header Table. Entry of the new work order will be
 disallowed if the operator does not have permission for the new cost center. For
 'Direct work order cost' entries the Cost center field will be display-only.
When
 your scheme includes override settings for Warehouse entries in Cost Center
 Scheme Maintenance, Spectrum will validate the cost center assigned to the proposed
 purchase order based on these overrides. The override cost center(s) supersede the
 cost center list defined for the scheme in general. Spectrum will compare the cost
 center assigned in the entry page with the Warehouse override cost centers in
 your scheme, and if the cost center is not included, then the warehouse will not be
 allowed.
When you are in Change mode, Spectrum will validate
 that you have security to perform the operation using the appropriate override, which
 depends on the job or work order site address used in the purchase order. If you try
 to change or delete a line, Spectrum will validate that you have security to perform
 the operation using the appropriate override based on the G/L work-in-progress
 flag.
All items on-order for the purchase order will appear
 on the page, regardless of your operator cost center security.
