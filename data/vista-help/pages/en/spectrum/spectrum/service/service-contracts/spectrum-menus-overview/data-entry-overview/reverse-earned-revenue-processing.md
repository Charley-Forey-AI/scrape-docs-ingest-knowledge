---
title: "Reverse Earned Revenue Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/reverse-earned-revenue-processing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/reverse-earned-revenue-processing"
---

# Reverse Earned Revenue Processing

Use the Reverse Earned Revenue Processing screen to undo
 G/L entries originally generated using Service Contract Earned Revenue.
From the Site Map, select
 Service Contracts > Data Entry > Reverse Earned Revenue.
This feature will only select records that were originally created using Service Contract Earned Revenue, ignoring any history records that were generated during Reverse Earned Revenue Processing, or related to an 'As billed' transaction. This feature will also automatically deselect any history records that have already been reversed.
If the billing source for the contract is from Service Contract, the contract will be included in the batch. If the billing source for the contract is from Work Order, then that contract will be skipped during the report compilation and update.
Once the Reverse Earned Revenue Register has been previewed or printed,
 the software will determine if the 'Post to G/L' flag in General Ledger > Installation is selected. If selected, the amounts from the Reverse Earned Revenue
 Register will update in summary to General Ledger and added to the earned revenue history
 table as of the specified reverse G/L date. If it is not selected, the update will not
 write to the G/L tables.

Related information

- [Reverse Earned Revenue Register](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/reverse-earned-revenue-processing/reverse-earned-revenue-register)
