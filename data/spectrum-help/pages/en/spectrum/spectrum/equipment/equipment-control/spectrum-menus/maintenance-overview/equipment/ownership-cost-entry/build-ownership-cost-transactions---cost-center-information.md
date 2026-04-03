---
title: "Build Ownership Cost Transactions - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/build-ownership-cost-transactions---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/build-ownership-cost-transactions---cost-center-information"
---

# Build Ownership Cost Transactions - Cost Center Information

If cost centers are being used in the current company, then
 when calculating depreciation, license, and insurance costs in Build Ownership Cost
 Transactions, Spectrum includes the equipment only if your operator has permission to access
 the equipment.
During the update, Spectrum compares the cost center assigned to the equipment with cost
 centers in your operator's assigned cost center scheme, and if the cost center is not
 included, then calculations for that equipment are not performed.
When your operator's cost center scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this update validates the cost center assigned to the equipment code based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the Equipment Maintenance screen with equipment override cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then the transaction entry line will not be created.
When you do not have authorization to access equipment assigned to a DLI transaction, then that transaction entry is not created. Likewise, when the warning appears to alert you that Unposted records already exist for these selections and will be deleted, the update will only delete equipment records that you have permission to access.
