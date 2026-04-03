---
title: "Reclassify Job Cost History: Transaction Type EQ - Equipment - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/reclassify-job-cost-history-transaction-type-eq---equipment/reclassify-job-cost-history-transaction-type-eq---equipment---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/reclassify-job-cost-history-transaction-type-eq---equipment/reclassify-job-cost-history-transaction-type-eq---equipment---cost-center-information"
---

# Reclassify Job Cost History: Transaction Type EQ - Equipment - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, Debit and Creditcost center fields display beneath the Debit and Credit fields. The Debit cost center code defaults from the Job Cost Transaction Entry screen, and no entry is allowed. In the Credit cost center field, enter the credit cost center code, click the drop-down arrow, or press F4 or double-click on this field to select from a list of available cost centers.
For EQ transaction type entries, Spectrum allows you to edit a transaction for a piece of equipment only if you have permission to access that equipment's information. Spectrum compares the equipment's cost center with cost centers in your assigned scheme; if the cost center is not present, then transaction entry for that piece of equipment is disallowed. Validation also occurs if you attempt to assign a disallowed piece of equipment to a transaction line.
The credit cost center displays based on the cost center of the equipment code. No changes are permitted.
When your cost center scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with equipment override cost centers in your assigned scheme; if the cost center is not included, then the transaction entry line will not be allowed.
