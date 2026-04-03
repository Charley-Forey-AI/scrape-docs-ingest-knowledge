---
title: "Import Item Prices from Text File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/materials-overview/import-item-prices-from-text-file"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/materials-overview/import-item-prices-from-text-file"
---

# Import Item Prices from Text File

This update reads a standard comma-delimited text-only
 (ASCII) file and if the DCI code matches a Spectrum EDP# , then the price from the text file
 will be updated to Spectrum.
The user may select to copy the Book Price, Price 1, or Price 2 into the
 Spectrum Standard Cost, or any List Price (1-5). This function will process the EDP part
 number field in the import file with or without quotes bracketing the field, and it will
 retain spaces in the field. If a match is made, then the Spectrum item price or cost will
 be updated. If no match is made, then that line of the import file will be skipped.
Important: Unit of measure fields in the text file must have
 quotation marks around them.
