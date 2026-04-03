---
title: "Enter Equipment Meter Reading - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/enter-equipment-meter-reading---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/enter-equipment-meter-reading---cost-center-information"
---

# Enter Equipment Meter Reading - Cost Center Information

If cost centers are being used in the current company, when
 recording meter readings for a piece of equipment in Enter Equipment Meter Reading, Spectrum
 allows entries for the equipment only if you have permission to access the equipment.
As you request each piece of equipment, Spectrum compares the cost center assigned to the
 equipment with cost centers in your operator's assigned cost center scheme, and if the cost
 center is not included, then entries for that equipment will not be allowed. This
 protection is also included for the Replace Meter, Meter Readings, and New Base Meter
 Reading windows.
When your operator's scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with equipment override cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then the transaction entry line is not allowed.
For multi-company meter transactions, cost center validation is performed based on settings in the destination company. When cost centers are being used in the destination company, the cost center designated for the equipment code on the transaction line must be authorized for your operator in the other company. When cost centers are not being used in the destination company, then the applicable cost center validation will not occur for that transaction line.
