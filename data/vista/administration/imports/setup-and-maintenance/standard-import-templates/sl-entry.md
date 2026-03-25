---
title: "SL Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/sl-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/sl-entry"
---

# SL Entry

Additional Information about the SL Entry template.
The imported data inserts new subcontracts and items, as well as new items for existing open subcontracts, via SL Entry batch.Note: The imported data will not update existing SL Items. Manual edits must be made for these changes.

## Tax Code/Tax Type Defaults

When importing subcontracts (including subcontracts imported from ProjectSight), the system defaults a tax code and tax type for subcontracts based on the following:

-  If the Use default tax code for subcontracts checkbox in JC Jobs is selected for the job specified on the subcontract, the system uses the Base Tax On drop-down in JC Jobs to determine the tax code and tax type defaults as follows:

- If the Base Tax On drop-down is set to J-Job, the system uses the tax code specified for the job (in JC Jobs) and sets the Tax Type to 1 (Sales). If the job's tax code is a VAT code, the Tax Type is set to 3 (VAT).If no tax code is specified for the job, the tax code and tax type are left blank.

- If the Base Tax On drop-down is set to V-Vendor, the system uses the tax code specified for the vendor (in AP Vendors) and sets the Tax Type to 1 (Sales). If the vendor's tax code is a VAT code, the Tax Type is set to 3 (VAT). If no tax code is specified for the vendor, the subcontract's tax code and tax type are left blank.

- If the Base Tax On drop-down is set to O-Vendor Override, the system uses the tax code specified for the vendor (in AP Vendors) and sets the Tax Type to 1 (Sales). If the vendor's tax code is a VAT code, the Tax Type is set to 3 (VAT). If no tax code is specified for the vendor, but a tax code is specified for the job, the system uses the job's tax code and sets the Tax Type to 1 (Sales). If the job's tax code is a VAT code, the Tax Type is set to 3 (VAT).
 If no tax code is specified for the vendor or the job, the Tax Code and Tax Type are left blank.

- If the Use default tax code for subcontracts checkbox in JC Jobs is not selected for the job specified on the subcontract, the Tax Type and Tax Code are left blank.

## ProjectSight

You can import data for Vista Subcontracts from ProjectSight.
