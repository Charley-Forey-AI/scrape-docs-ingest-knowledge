---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/service-management/service-management-features"
---

# Service Management Features

Vista 2023 R1 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Updated Tax Code Defaults for SM Purchase Orders

When entering purchase orders for an SM work order (in SM Purchase Order Entry), the tax type and tax code now default as follows:

- Tax Type - If the material entered for the purchase order item is taxable and the service center has a tax code defined, the Tax Type defaults as Sales (U.S. companies) or VAT (Canadian and Australian companies). If the material is not taxable or if no tax code is defined for the service center, the Tax Type defaults as blank.

- Tax Code - If the material is taxable and a tax type of Sales or VAT is specified for the purchase order item, tax code defaults from the service center. If no tax code is defined for the service center, the system defaults the tax code defined for the work order's service site. If no tax code is specified for the service center or service site, the tax code defaults as blank. Previously, the tax code defaulted based on the Tax Source defined for the work order scope. The Tax Source is now only used to default tax codes for work completed line.

For job work orders, the tax code defaults the job tax code, the vendor tax code, or the vendor override tax code, depending on how you set the Base Tax On flag for the job in JC Jobs.
For additional information about tax types and tax codes, see the [Tax Type](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046861--en) and [Tax Code](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046877--en) F1 Help.
This functionality was also updated for SM purchase orders entered in [PO Purchase Order Entry](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/purchase-order-features). For more information, see the Purchase Order release notes.

## Changed Use of Man Hours to Person Hours

To support a more generic language, the following fields were retitled to use person hours:
In SM Serviceable Items, Agreements tab:

- The Avg Man Hours field was changed to Avg Person Hours

- The Man Hours field was changed to Person Hours

In SM Class Maintenance (Info tab)

- The Average Man Hours field was changed to Average Person Hours

## Added Agreement and Term Notes to Work Order Summary Info

You now have the ability to view Agreement and Term notes in the Summary Info panel of the SM Work Orders form.
Previously, when hovering over or clicking the Agreements link in the Notes section of the Summary Info panel, you could only see an agreement's revision notes. With this release, the pop-up window will now show agreement notes, term notes, and/or revision notes, each as a separate section in the pop-up window or the Agreement Notes form (accessed by clicking the Agreements link) for easier viewing.
Note: Agreement, term, and revision notes are entered on the Agreement Notes, Term Notes, and Revision Notes tabs in SM Agreements (respectively).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
