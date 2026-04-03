---
title: "Transaction Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/transaction-update/transaction-update---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/transaction-update/transaction-update---cost-center-information"
---

# Transaction Update - Cost Center Information

When creating G/L entries during the update, Spectrum
 determines whether both cost centers assigned to each transaction line of the invoice are
 assigned to the same cost center.
If there are two different cost centers, then Spectrum
 creates balancing debit and credit entries for cost center inter-posting (cost center
 inter-posting account information is defined in the Equipment Control Installation). When
 cost centers are used and the Enterprise Installation Allow G/L account overrides by cost
 center checkbox is selected, Spectrum assigns inter-posting amounts to multiple General
 Ledger accounts, by cost center, based on a list of override G/L accounts in the
 Inter-posting Overrides window in Equipment Control Installation.For
 multi-company transactions, the inter-company entries are processed through the
 applicable cost center inter-posting accounts. When cost centers are used in the
 destination company, then the inter-posting and inter-company accounts specified in that
 company's Equipment Control Installation are recorded. When overrides are set up,
 Spectrum automatically substitutes the designated G/L account specified in Equipment
 Control Installation as an override for lines referencing the cost center with the
 override account. You are not required to possess cost center authorization to write to
 this override G/L account in order to update.
