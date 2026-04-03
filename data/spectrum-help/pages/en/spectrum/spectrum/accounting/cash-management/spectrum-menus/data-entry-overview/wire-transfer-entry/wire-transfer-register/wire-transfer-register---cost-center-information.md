---
title: "Wire Transfer Register - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-register/wire-transfer-register---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-register/wire-transfer-register---cost-center-information"
---

# Wire Transfer Register - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the Wire Transfer Register provides the cost center assigned to each check. This is the cost center recorded in the heading portion of Wire Transfer Entry. The Report also shows the cost centers assigned to each detail distribution line.
Spectrum will determine whether all distribution lines of the invoice are
 assigned to the same cost center as in the direct check header. If there are multiple
 cost centers, then Spectrum will create balancing debit and credit entries for cost
 center inter-posting; cost center inter-posting account information is defined in the
 Cash Management Installation screen. When cost centers are used and the Allow G/L
 account overrides by cost center checkbox is selected on the Enterprise Installation
 screen, Spectrum will assign inter-posting amounts to multiple General Ledger accounts
 by cost center based on a list of override G/L accounts in the Cash Management Installation > Inter-posting Overrides window.
When updating to the General Ledger for multi-company entries, the software will read the company code of the distribution line and then determine if that company code has been assigned a particular inter-company G/L account.
For multi-company entries, the software will read the company code of the distribution line, and then determine if that company code has been assigned a particular inter-company G/L account. For entries in the bank account company, the Cash Management Installation setup of the bank account company is used, and for the entries to the company referenced in the distribution, the Cash Management Installation setup of that other company is applied. Inter-post entries are not applicable for these transaction lines.
