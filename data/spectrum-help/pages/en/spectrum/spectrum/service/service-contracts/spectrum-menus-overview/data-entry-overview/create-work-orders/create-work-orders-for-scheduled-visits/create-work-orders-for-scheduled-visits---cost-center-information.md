---
title: "Create Work Orders for Scheduled Visits - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/create-work-orders/create-work-orders-for-scheduled-visits/create-work-orders-for-scheduled-visits---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/create-work-orders/create-work-orders-for-scheduled-visits/create-work-orders-for-scheduled-visits---cost-center-information"
---

# Create Work Orders for Scheduled Visits - Cost Center Information

If cost centers are being used, the software will assign a
 cost center to the work order header.
The software will first read the cost center from the Service Contract Header Table and
 assign this contract, and if not available, the update will assign the cost center from
 the Site Table. If the Operator does not have authorization for the assigned cost
 center, the register/update will not include that contract. Operator scheme overrides
 are not applicable.
If cost centers are on the Work Order Type, Spectrum looks to see if the Work Order header has a cost center assigned to it. When there is no cost center on the Work Order Type, Spectrum will look to the service contract for a cost center. When there is no cost center on the service contract, Spectrum will use the cost center assigned to the site.
