---
title: "Purchase Order Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/purchase-order-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/purchase-order-features"
---

# Purchase Order Features

Vista 2023 R1 delivers on user-requested Purchase Order enhancements, fixes, and other improvements.

## Updated Tax Code Defaults for SM Purchase Orders

When entering SM Work Order lines on a purchase order item (in PO Purchase Order Entry), the tax type and tax code now default as follows:

- Tax Type - If the material entered for the purchase order item is taxable and the service center has a tax code defined, the Tax Type defaults as Sales (U.S. companies) or VAT (Canadian and Australian companies). If the material is not taxable or if no tax code is defined for the service center, the Tax Type defaults as blank.

- Tax Code - If the material is taxable and a tax type of Sales or VAT is specified for the purchase order item, the tax code defaults from the service center assigned to the specified SM work order. If no tax code is defined for the service center, the system defaults the tax code defined for the work order's service site. If no tax code is specified for the service center or service site, the tax code defaults as blank. Previously, the tax code defaulted from the vendor specified on the purchase order.

For job work orders, the tax code defaults the job tax code, the vendor tax code, or the vendor override tax code, depending on how you set the Base Tax On flag for the job in JC Jobs.
For additional information about tax types and tax codes, see the [Tax Type](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-00030cc1--en) and [Tax Code](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-00030cdb--en) F1 Help.
This functionality was also implemented for purchase orders entered in SM Purchase Order Entry. For more information, see the [Service Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/service-management/service-management-features) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
