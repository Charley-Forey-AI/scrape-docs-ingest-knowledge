---
title: "Import Equipment Costs from Text File - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-equipment-costs-from-text-file/import-equipment-costs-from-text-file---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-equipment-costs-from-text-file/import-equipment-costs-from-text-file---cost-center-information"
---

# Import Equipment Costs from Text File - Cost Center Information

If cost centers are being used in the current company,
 validation will take place while importing equipment cost transactions.
Spectrum will allow the Operator to import a transaction for a piece of equipment only
 if the Operator has permission to access that equipment in the specified company.
 Spectrum will compare the equipment's cost center with cost centers in the Operator's
 assigned cost center scheme, and if the cost center is not present, the import of
 transactions for that piece of equipment will be disallowed and the records will be sent
 to the Import Equipment Cost Error Listing.
The Debit cost center will be assigned automatically, and the Credit cost center will be assigned from the import file if specified of automatically assigned the cost center associated with the equipment. Spectrum will verify the Operator is allowed to access the assigned Debit G/L and the Credit G/L accounts by comparing the list of shared cost centers with the cost centers in the Operator's assigned cost center scheme. If there are no common cost centers, the transaction will be sent to the Import Equipment Cost Error Listing.
