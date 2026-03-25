---
title: "Import Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/administration/import-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/administration/import-features"
---

# Import Features

Vista 2024 R1 delivers on user-requested Imports enhancements, fixes, and other improvements.

## Update to the SL Subcontract Entry (SLEntry) Import

When importing subcontracts, the import process now handles Tax Code and Tax Type defaults tax code defaults as follows:

-  If the Use default tax code for subcontracts checkbox in JC Jobs is selected for the job specified on the subcontract, the system uses the Base Tax On drop-down in JC Jobs to determine the tax code and tax type defaults as follows:

- If the Base Tax On drop-down is set to J-Job, the system uses the tax code specified for the job (in JC Jobs) and sets the Tax Type to 1 (Sales). If the job's tax code is a VAT code, the Tax Type is set to 3 (VAT).If no tax code is specified for the job, the tax code and tax type are left blank.

- If the Base Tax On drop-down is set to V-Vendor, the system uses the tax code specified for the vendor (in AP Vendors) and sets the Tax Type to 1 (Sales). If the vendor's tax code is a VAT code, the Tax Type is set to 3 (VAT). If no tax code is specified for the vendor, the subcontract's tax code and tax type are left blank.

- If the Base Tax On drop-down is set to O-Vendor Override, the system uses the tax code specified for the vendor (in AP Vendors) and sets the Tax Type to 1 (Sales). If the vendor's tax code is a VAT code, the Tax Type is set to 3 (VAT). If no tax code is specified for the vendor, but a tax code is specified for the job, the system uses the job's tax code and sets the Tax Type to 1 (Sales). If the job's tax code is a VAT code, the Tax Type is set to 3 (VAT).
 If no tax code is specified for the vendor or the job, the Tax Code and Tax Type are left blank.

- If the Use default tax code for subcontracts checkbox in JC Jobs is not selected for the job specified on the subcontract, the Tax Type and Tax Code are left blank.

## Update to the PO Purchase Order Entry (POEntry) Import

When importing purchase orders with one or more lines posted to SM Work Orders (Line Type 6), the import process will now validate the SM Cost Type value for those lines as follows:

- If the line's Tax Rate <> 0.00, and the SM Cost Type is blank, an error is produced. You can upload the import data into a PO batch, but you must enter an SM cost type for each applicable line before you can process the batch.

- If the line's Tax Rate = 0.00, an SM Cost Type value is not required.

## Add PO/SL Fields to AP Unapproved Invoice Import

In support of the PO and SL fields added (in a previous release) to the AP Unapproved Invoice Entry header, the APUnapprInv (AP Unapproved Invoice Entry) import was updated to include new PO and SL identifiers:

- PO (Identifier #210)

- SL (Identifier #215)

Upon installation of this release, all existing import templates using the APUnapprInvoice import form will be updated to include the two new identifiers.

## Updated Default Routine for PR Craft Class (PRCraftClass) Import

The PRCraftClass import form now has a new Viewpoint Routine titled "vspIMViewpointDefaultsPRCC" for applying default values to specific fields. This routine replaces the "bspIMViewpointDefaults" routine, which is no longer in use.

## Updated SM Imports for SM Tax Enhancement

The SMWorkOrderScope and SMWorkCompletedMisc imports now include new tax fields in support of the new fields added in SM Work Orders for the [SM Tax Handling](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features#concept-k1quaafr1002--en__SMTaxHandlingRN) enhancement included in this release.
The new fields added are as follows:
SM Work Completed Misc (SMWorkCompletedMisc) ImportColumn NameIdentifier
CostTaxType (Cost Tax Type)108
CostTaxCode (Cost Tax Code)111
CostTaxAmount (Cost Tax Amount)114
CostTaxBasis (Cost Tax Basis)117

SM Work Order Scope (SMWorkOrderScope) ImportColumn NameIdentifier
MatlTaxOption (Material Tax Option)143
TaxType (Billing Tax Type)162
TaxCode (Billing Tax Code)163

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
