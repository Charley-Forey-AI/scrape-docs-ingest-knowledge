---
title: "Import Trade Service Data | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data"
---

# Import Trade Service Data

This screen is used to transfer information from Trade
 Service into the Spectrum database.
When items are imported into Spectrum, the import uses the category file
 to determine whether an item mask is specified. If so, then new item is created in Spectrum
 using the next available item code for that category. If no mask is indicated, then it will
 add the item using the EDP number as the new item code. This update screen uses this
 method, instead of always using the EDP number as the new item code.
In order to successfully import the Trade Services data, be sure the
 Spectrum data directory is specified in the [Trade Service Link Update Manager](/en/spectrum/spectrum/system-administration/materials-overview/import-trade-service-data/trade-service-link-update-manager) screen before proceeding.
