---
title: "Ownership Cost Journal/Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/ownership-cost-journal/ownership-cost-journalupdate---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/ownership-cost-journal/ownership-cost-journalupdate---cost-center-information"
---

# Ownership Cost Journal/Update - Cost Center Information

If cost centers are being used in the current company, when
 printing the Depreciation, License and Insurance Journal, Spectrum includes the equipment only
 if your operator has permission to access the equipment.
During the update, Spectrum compares the cost center assigned to the equipment with cost
 centers in your operator's assigned cost center scheme, and if the cost center is not
 included, then that equipment is not shown on the report and is not updated.
The report includes the cost center for both the debit and credit entries of each transaction. When creating G/L entries during the update, Spectrum will determine whether both cost centers assigned to each transaction line of the invoice are assigned to the same cost center. If there are two different cost centers, then Spectrum will create balancing debit and credit entries for cost center inter-posting; cost center inter-posting account information is defined in the Equipment Control Installation.
The Ownership Cost Journal update will looks at the Equipment Control Type table to get the proper G/L accounts to use – if needed, you can set up overrides by having multiple equipment types. When your operator's scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this report validates the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with equipment override cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then the transaction entry line will not be shown.
Even though the operator may not have authorization to access a G/L account assigned to a DLI transaction, the transaction update is performed.
