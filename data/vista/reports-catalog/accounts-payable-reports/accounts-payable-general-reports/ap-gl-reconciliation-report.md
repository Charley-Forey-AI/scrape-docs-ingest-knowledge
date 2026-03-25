---
title: "AP GL Reconciliation Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/accounts-payable-reports/accounts-payable-general-reports/ap-gl-reconciliation-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/accounts-payable-reports/accounts-payable-general-reports/ap-gl-reconciliation-report"
---

# AP GL Reconciliation Report

Use the AP GL Reconciliation report as a tool for reconciling differences between payables accounts in the GL and the AP module for a given company and month.
Drill-down capabilities allow you to compare batch-level information, see detail from the GL batch, access attachments associated with a batch, and see current AP data for a batch.
 The
Direct GL Entries section only appears if there are transactions to a Payable account from a non-AP module. This includes transactions that may or may not have been entered as part of fixing a reconciliation problem; as such this section may show entries that are expected.
The

AP Clear section shows only if the cleared invoices for a month do not net zero, and includes a list of invoices that were part of AP Clear batches.
The

Account Activity section shows all of the GL Accounts associated with pay types that had activity in the month in GL, AP, or both. Due to the nature of the AP data structure with regard to changes and deletes, there may be some false-positives in the batch-level detail on the AP side. If they net to zero for the month, it's ok.
Report ParametersDescription
GLCoEnter the GL company or press F4 to select from a list of valid GL companies.
MonthEnter the month to reconcile.
