---
title: "SMAgreementService | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smagreementservice"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smagreementservice"
---

# SMAgreementService

If the Post Revenue to Service Center or Division Dept. checkbox is selected for a record in the import file, the Service Center value is required for that record.

If there is no value in the data file, the system defaults a value based on how you set the User Default Value, Override Import Value, and Use Viewpoint Default options for the Service Center identifier in the Template Detail. If you did not provide a value in the User Default field and you did not select the Use Viewpoint Default checkbox, the system will automatically default the service center from the Default Service Center field for the service site in SM Service Sites.
When importing agreement service records, the system will automatically set the TaxTypeOverride value equal to the Matl Tax Override value specified (in SM Call Types) for the call type associated with the agreement service, regardless of the default behavior you defined in IM Template Detail for the TaxTypeOverride identifier. You cannot override the defaulted value in IM Work Edit, nor can you edit the value once it is uploaded to SM Service. The system restricts the value allowed for the tax type override because of how call types are grouped for budgets on agreement services.
It will also check the MatlTaxOption (Tax Option Override) value to ensure it is set to one of the following:

- N (Not Taxable)

- P (Taxable at Purchase Only)

- B (Taxable at Billing Only)

- M (Taxable at Purchase/Markup at Billing)

- F (Full Tax at Purchase and Billing)

 If it is not, an error displays and you must correct the imported value accordingly.
