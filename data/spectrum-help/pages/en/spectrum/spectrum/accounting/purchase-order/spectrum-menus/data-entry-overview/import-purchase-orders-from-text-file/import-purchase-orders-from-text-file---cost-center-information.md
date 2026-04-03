---
title: "Import Purchase Orders from Text File - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/import-purchase-orders-from-text-file---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/import-purchase-orders-from-text-file---cost-center-information"
---

# Import Purchase Orders from Text File - Cost Center Information

If the cost center feature is enabled in the Enterprise
 Installation page for the current company, Spectrum verifies that the operator has permission
 for the cost center.
The system runs through several operator-specific validations for the header and detail
 records. It is recommended that only full-security cost center users perform the import.
 If the cost center feature is not enabled in the Enterprise Installation page, then the
 cost center field in the file layout detail will be ignored.
If it is a direct job cost entry, direct equipment cost entry, direct work order cost entry, or non-direct cost entry, then the cost center must be allowed for the G/L account assigned to the detail line. For a non-direct cost entry, the cost center must be valid for the vendor assigned to the purchase order.
