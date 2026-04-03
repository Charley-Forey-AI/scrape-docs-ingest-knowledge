---
title: "Cost Transaction Report - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/cost-transaction-report/cost-transaction-report---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/cost-transaction-report/cost-transaction-report---cost-center-information"
---

# Cost Transaction Report - Cost Center Information

If the cost center feature is enabled in the
 Enterprise Installation screen, the Cost Transaction
 Report screen includes the Cost group field. When a cost
 group or cost center is specified, the report shows only jobs assigned to cost centers in that
 group (based on the cost center recorded in the Jobs > Edit window).

- When your scheme includes override settings for job entries in Cost
 Center Scheme Maintenance, this report will validate the cost
 center assigned to transaction detail lines based on these overrides. The override
 cost center(s) supersede the cost center list defined for the scheme in general.
 Spectrum will compare the cost center assigned in the entry screen detail with job
 override cost centers in your assigned scheme; if the cost center is not included,
 then the transaction entry line will not be shown. Operator override scheme
 settings for Employee
 and Equipment are not
 applicable for this report and update.

- When you specify a cost center on the Cost Transaction
 Report screen, Spectrum verifies that you have permission to access
 that cost center before allowing you to proceed.

- When printing and updating job cost transactions, Spectrum includes a transaction only if you have permission to access the transaction's debit cost center. Spectrum compares the debit cost center assigned to the transaction with cost centers in your assigned scheme; if the cost center is not included, then that entry will not be processed.

- During the update, Spectrum determines whether both cost centers specified on
 each transaction line are assigned to the same cost center. If the cost centers
 differ, then the software will create balancing debit and credit entries for cost
 center inter-posting; cost center inter-posting account information is defined in
 the Job Cost Installation screen. When cost centers are
 used and the Enterprise Installation Allow G/L account overrides by cost centercheckbox is selected,
 Spectrum assigns inter-posting amounts to multiple G/L accounts by cost center
 based on a list of override G/L accounts in Job Cost
 Installation.
