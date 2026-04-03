---
title: "Consolidation Company | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/consolidated-financials/consolidation-company"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/consolidated-financials/consolidation-company"
---

# Consolidation Company

Spectrum has the capability of producing financial reports that consolidate the financial information from several companies/divisions. Four conditions must exist in order to set up the consolidation company:

- The General Ledger must be the only installed module for the consolidation company.

- The fiscal calendars of all companies/divisions being consolidated must be the same (for example, all must be July through June, or all must be January through December).

- The Chart of Accounts for all companies/division must be similar (the mask set up in the General Ledger Installation screen must be the same length for all companies; account codes may be different, so long as the mask length is the same).

- The fiscal calendar for the consolidation company must have already been set up.

Each period end, after all activity has been recorded in the operating companies, perform the Consolidated Financials Update in the Print Financials Reports screen in General Ledger Reports. During this update, Summary G/L information from each of the operating companies is compiled in the consolidation company. Use the Monthly Activity Balance File Report and Transaction Journal to review records. Perform adjusting Journal entries as needed, then print financial reports.
Tip: When a consolidated financials company is used, journal
 entries recorded in the consolidated company are removed each time the consolidation update
 is performed. To "save" journal entries that should not be overwritten each month, set up
 another Spectrum company with the same chart of accounts and fiscal calendar, then do the
 consolidating journal entries in that company. Be sure to include this company code in the
 consolidated company's Consolidated Financials Control list, and be sure to perform the
 Opening Forward Balance Update in the journal entry company.

Related information

- [Set Up a Consolidation Company](/en/spectrum/spectrum/accounting/general-ledger/procedures-overview/set-up-a-consolidation-company)
