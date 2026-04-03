---
title: "Journal Entry Activity Report - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/journal-entry-activity-report/journal-entry-activity-report---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/journal-entry-activity-report/journal-entry-activity-report---cost-center-information"
---

# Journal Entry Activity Report - Cost Center Information

If your company is using cost centers, the Cost group field displays. When you specify a cost center, the report will show only journal entries assigned to cost centers in that group (based on the cost center recorded in the heading portion of the Journal Entry screen).
This report displays the cost centers associated with each journal entry, including the cost center assigned to each line. Spectrum determines whether all lines for the journal entry are assigned to the same cost center; if there are multiple cost centers, then Spectrum will create balancing debit and credit entries for cost center inter-posting, which is defined in General Ledger Installation. When cost centers are used and the Enterprise Installation option for Allow G/L account overrides by cost center is selected, Spectrum will assign inter-posting amounts to multiple General Ledger accounts by cost center and based on a list of override G/L accounts in General Ledger Installation.
For all formats of the report, Spectrum will include the journal entries on the report only if your operator has permission to access the cost center assigned in the header of the journal entry. Spectrum compares the cost center assigned to the journal entry with cost centers in the operator's assigned scheme, and if the journal entry cost center is not included, then that entry is not shown on the report.
If Entity tracking is enabled, Spectrum will re-classify inter-post lines to entity inter-post G/L accounts. The report will show the debits and credits to be posted to G/L based on any inter-entity transactions in the Journal Entry, and then the update writes the applicable inter-post amounts to the designated entity-specific G/L accounts.
