---
title: "Void Wire Transfers Register - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/void-wire-transfer-entry/void-wire-transfers-register/void-wire-transfers-register---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/void-wire-transfer-entry/void-wire-transfers-register/void-wire-transfers-register---cost-center-information"
---

# Void Wire Transfers Register - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the Void Wire Transfer Register includes a column displaying the cost center assigned to each void transaction.
Spectrum will determine whether all distribution lines of the invoice are
 assigned to the same cost center as in the direct check header. If there are multiple
 cost centers, then Spectrum will create balancing debit and credit entries for cost
 center inter-posting; cost center inter-posting account information is defined in the
 Cash Management Installation screen. When cost centers are used and the Allow G/L
 account overrides by cost center is selected on the Enterprise Installation screen,
 Spectrum will assign inter-posting amounts to multiple General Ledger account by cost
 center based on a list of override G/L accounts in the Cash Management > Inter-posting Overrides window.
The Void Wire Transfers Register updates to General Ledger (in both companies) using the inter-company setup instead of the inter-post setup when voiding a multi-company wire. In the unusual case where the installation setup has changed since the wire was first updated, the inter-company G/L account specified in the installation at the time the wire is voided will be applied rather than the original inter-company G/L account.
