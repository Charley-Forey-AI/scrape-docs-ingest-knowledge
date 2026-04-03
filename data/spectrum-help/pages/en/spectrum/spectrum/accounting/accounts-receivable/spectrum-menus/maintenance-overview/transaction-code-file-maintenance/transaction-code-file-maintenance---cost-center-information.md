---
title: "Transaction Code File Maintenance - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/transaction-code-file-maintenance/transaction-code-file-maintenance---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/transaction-code-file-maintenance/transaction-code-file-maintenance---cost-center-information"
---

# Transaction Code File Maintenance - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when adding or changing a transaction code Spectrum will allow entry of G/L account codes only if the operator entering the G/L account has permission to assign the codes. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that G/L account cannot be assigned.
Once a G/L account code has been assigned to a transaction code (by an authorized operator), then that G/L account will be used by all operators for processing that involves that transaction code.
Spectrum also verifies cost center authorization when a Cash Management bank account is assigned. Spectrum compares the bank account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that bank account cannot be assigned.
When an authorized bank account is entered, Spectrum also verifies that the operator has authorization for the G/L account associated with the bank account (because Spectrum automatically resets the G/L account for this transaction code when the new bank account is assigned. If the operator does not have permission for this G/L account, then that bank account will be disallowed.
Once a G/L account and/or bank account code has been assigned to a transaction code (by an authorized operator), then that account will be used by all operators for processing involving that transaction code.
