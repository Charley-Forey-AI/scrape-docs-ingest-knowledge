---
title: "Imports Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/administration/imports-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/administration/imports-features"
---

# Imports Features

Vista 2025.6 delivers on user-requested Imports enhancements, fixes, and other improvements.

## Update to SMAgreementService Import

In support of the [Tax Handling](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features#concept-k1quaafr1002--en__SMTaxHandlingRN) feature included in Vista 2024 R1, the SMAgreementService (SM Service) import was updated to include the following field.
IdentifierColumnDescription
147MatlTaxOptionTax Option Override

 Upon installation of this release, all existing import templates using the SMAgreementService import form will be updated to include the new identifier.
When importing agreement service data, if a value exists for the MatlTaxOption column, the validation process checks to make sure it is set to N, P, B, M, or F. If it is not, an error displays and you will need to correct the imported value accordingly.

## Quotation Marks Supported in Import Files

Vista now supports the use of single quotes ( ' ), double quotes (
 " ), and grave accents ( ` ) in import files, regardless of the file format you use.
 For more details about import files, see [About Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
