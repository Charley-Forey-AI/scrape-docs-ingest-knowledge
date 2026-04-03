---
title: "Build Ownership Cost Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/build-ownership-cost-transactions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/build-ownership-cost-transactions"
---

# Build Ownership Cost Transactions

The Build Ownership Cost Transactions screen is used to
 calculate the depreciation, license, and insurance costs on equipment based on information
 recorded in the Equipment File Maintenance > Financials window.
Entry is allowed to specify the equipment and fiscal period desired.
To exclude accruals of Depreciation/License/Insurance for sold or retired equipment, the status selection may be used to request only active equipment. If depreciation was already calculated on pieces of equipment that you do not want included, these entries will need to be deleted in the Ownership Costs screen.
If you plan to calculate and update the License and Insurance in
 Equipment Control along with the depreciation coming over from Fixed Assets, you will need to make certain
 that you do NOT select the Depreciation transaction type in this screen (which creates the
 depreciation amount in Equipment Control) if you have already run the update from Fixed
 Assets.
The following reflects the typical procedure used to pass depreciation data from the Fixed Assets module to Equipment Control:

- Access the Fixed Assets module and process the depreciation calculations using Calculate Depreciation Update. Process the depreciation through Update Depreciation to Master and Fixed Assets G/L Summary Update.

- Continue the monthly processing in Equipment Control using Ownership Cost Entrythrough Ownership Cost G/L Register.
It is not necessary, however, to calculate DLI as the first step in the process, as the year and period may be recorded on the Depreciation License & Insurance Entry screen and on the Ownership Cost Journal screen.

Related information

- [Build Ownership Cost Transactions - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/build-ownership-cost-transactions---cost-center-information)

- [Ownership Cost Journal](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/ownership-cost-journal)

- [Ownership Cost G/L Register](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/ownership-cost-entry/ownership-cost-gl-register)
