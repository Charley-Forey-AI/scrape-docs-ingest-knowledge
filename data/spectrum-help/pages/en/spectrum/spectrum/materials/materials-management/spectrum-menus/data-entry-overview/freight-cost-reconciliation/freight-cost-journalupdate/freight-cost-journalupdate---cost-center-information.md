---
title: "Freight Cost Journal/Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/freight-cost-journalupdate/freight-cost-journalupdate---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/freight-cost-journalupdate/freight-cost-journalupdate---cost-center-information"
---

# Freight Cost Journal/Update - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the Cost center field will display below the invoice Date field only if cost centers are enabled for that company. Entry in the Cost center field is required.
The original cost center from the ticket (from the warehouse for receipts and transfers, from the job / phase for job requisitions, or from the customer contract / warehouse for sales) posts on each detail line. The update will group tickets onto the same invoice detail line only if the General Ledger account and cost center match. The freight charge and variance amount will both use this cost center on the detail lines created.
Based on the cost centers assigned to the vendor and the operator's cost center security settings, if only a single cost center is valid then it will default (only if no cost center has been assigned for the invoice.) The cost center entered must be valid for the operator, for the vendor, and for the A/P trade G/L account (in the Accounts Payable Installation screen).
