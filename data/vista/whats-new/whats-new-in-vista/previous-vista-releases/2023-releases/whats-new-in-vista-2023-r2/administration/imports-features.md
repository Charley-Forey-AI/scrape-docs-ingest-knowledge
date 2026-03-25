---
title: "Imports Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/administration/imports-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/administration/imports-features"
---

# Imports Features

Vista 2023 R2 delivers on user-requested Imports enhancements, fixes, and other improvements.

## Update to the APEntry Import

When importing AP invoices with one or more lines posted to SM Work Orders (Line Type 8), the import process will now validate the SM Cost Type value for those lines as follows:

- If the line's Tax Amount <> 0.00, an SM Cost Type must be supplied. If the SM Cost Type is blank, an error is produced and you must correct the error (in IM Work Edit) before you can upload the transaction into an AP Transaction Entry batch.

- If the line's Tax Amount = 0.00, an SM Cost Type value is not required.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
