---
title: "Contract Renewal Management | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-renewal-management"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-renewal-management"
---

# Contract Renewal Management

Use the Contract Renewal Management screen to automate the
 renewal process for a range of contracts expiring within a specified date range.
From the Site Map, select
 Service Contracts > Data Entry > Renewal Management.
The Contract Administrator can specify a default 'Contract price' escalation percent, and whether to set the status of new contracts to 'Proposed'.
The update will renew contracts based on settings in the interactive grid. Scheduled billing dates and scheduled visits will be generated from the past contract, incremented based on the length of the particular contract. For example, these dates will be set to the following year for year-long contracts.
When this screen is first accessed, the Build List of Expiring Contracts window will open to specify which contracts appear on this screen, and any new contract defaults. Click the OK button and Spectrum will calculate a new contract price, new start date, and new end date to display in the grid. Spectrum will also look at the old contract # to determine if a new contract # can default. The contract # will increment the last numeric by 1 and then test whether it already exists in the Service Contract Master Table for the current site. If that contract # already exists, the new contract # will be left blank. A warning message will display in the header to indicate contracts missing a 'new contract #' that will not be updated.
