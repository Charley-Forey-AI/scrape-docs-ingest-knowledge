---
title: "Manual Credit Card Check Register - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/manual-credit-card-check-register/manual-credit-card-check-register---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/manual-credit-card-check-register/manual-credit-card-check-register---cost-center-information"
---

# Manual Credit Card Check Register - Cost Center Information

If cost centers are being used, Spectrum verifies your operator has permission to access the vendor before including credit card payments on the Manual Credit Card Payment Listing. Spectrum compares the vendor's list of shared cost centers with cost centers in your assigned cost center scheme, and if there are no common cost centers, then credit card payments for that vendor are not selected.
The Manual Credit Card Payment Listing will include transactions only if you have permission to access the cost center associated with the credit card. The cost center used for comparison purposes with your allowed codes is the payment transaction cost center associated with the credit card account.
At the Cash G/L account code field (when Cash Management is not present), Spectrum allows entry of a G/L account code only if you have permission to assign that code. Spectrum compares the G/L account's list of shared cost centers with cost centers in your assigned cost center scheme, and if there are no common cost centers, then that G/L account cannot be assigned.
During the update, when the Enterprise Installation option for Allow G/L account overrides by cost center is selected, Spectrum assigns discount taken amounts to multiple General Ledger accounts, by cost center based on a list of override G/L accounts in Accounts Payable Installation.
