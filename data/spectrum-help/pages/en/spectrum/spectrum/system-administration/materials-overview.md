---
title: "Materials Overview | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/materials-overview"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/materials-overview"
---

# Materials Overview

Spectrum allows you to import Trade Service pricing files into Spectrum in order to maintain a current inventory database of materials. This material price list can then be updated as needed.

## Step 1: Link Trade Service and Spectrum

Once your System Administrator has set up your system to work with Trade
 Service Pro, the [Trade Service Link Update Manager](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data/trade-service-link-update-manager)
 feature is available and must be run on your server (in the case where this is not
 possible, for example, if your server is hosted, please contact Spectrum Support). [Trade Service Link Update Manager](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data/trade-service-link-update-manager) is an external
 application that can be used by subscribers to Trade Service to update inventory prices
 in other applications. Spectrum provides the link update utility so you can call
 Spectrum and update the inventory price and cost.

## Step 2: Trade Service Updates the Spectrum Database

The Trade Service program updates the Spectrum database by a three-step
 process (only the first step requires user interaction).

1. First, Spectrum is called, and creates an ASCII file, EDPLIST, which lists the EDP numbers in the inventory master file.

1. Second, a Trade Service program, SV_PFMS.EXE, then creates a TRADE.DAT file,
 based on the EDPLIST file. (No user action required. If you have a valid trade.dat
 file you can import via the function [Import Trade Service Data](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data), otherwise Trade Service Imports are done through [Data
 Exchange](/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx).)

1. Third, Spectrum is entered again and updates the database with the information in TRADE.DAT. (No user action required.)

## Step 3: (Optional) Change Item Codes

After the update, if you have the Inventory Control module, you can use the
 you are free to use the [Change Item Codes](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/utilities-overview/change-item-codes) utility in order to rename the code to something that is
 easier to remember instead of the long Trade Service designation. The data in the EDP
 field remains the same so that next item there's an import, the system will find that
 item as a match and update it.

## Additional Information

For users without the Inventory Control module, it will be necessary to do some preliminary setup in order to use the Trade Service features.

1. First, the Inventory Control checkbox in the Site Map > System Administration > Installation > Company > Modules tab should be selected to allow access to the inventory items.

1. Second, in the Site Map > System Administration > Installation > Inventory Control > Properties tab, the Default warehouse should be set. Items
 will be added to this warehouse during the import process. Most users specify
 warehouse A or 1, but any single letter or number would acceptable.

1. Also set the Site Map > System Administration > Installation > Inventory Control > Properties tab's Default costing method and the
 G/L Codes tab's default G/L account codes, as these will be
 used to build the category file.

Related information

- [Trade Service Link Update Manager](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data/trade-service-link-update-manager)

- [Import Trade Service Data](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data)

- [Import Item Prices from Text File](/en/spectrum/spectrum/system-administration/materials-overview/import-item-prices-from-text-file)
