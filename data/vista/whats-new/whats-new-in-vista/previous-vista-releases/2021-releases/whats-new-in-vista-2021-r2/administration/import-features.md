---
title: "Import Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/administration/import-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/administration/import-features"
---

# Import Features

Vista 2021 R2 delivers on user-requested Imports enhancements, fixes, and other improvements.

##  Fields Added to the PR Employees Import

In conjunction with the new gender fields added to the PR Employees form, the PR Employees import (PREmpl) now includes the following new identifiers:

- GenderIdentity (Identifier #610)

- GenderIdentityOther (Identifier #620)

For information about the gender identity information added in PR Employees, see the [Payroll](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/hr-and-payroll/payroll-features) release notes.
To allow importing other pertinent employee information, the following fields were also added to the PREmpl import:

- Email1095CYN (Identifier #540)

-  EmailT4YN (Identifier #545)

- EmailW2YN (Identifier #535)

- GeographicCode (Identifier #560)

- JobKeeperFinishFN (Identifier #580)

-  JobKeeperStartFN (Identifier #570)

-  JobKeeperTierLevel (Identifier #590)

- PRUpdateAPVMYN (Identifier #173)

- StatusIndianYN (Identifier #372)​

##  Added Shortcut Buttons to IM Imports

You can now access the IM Template, IM Upload, and IM Work Edit forms from the IM Imports form. To enable this functionality, added the following shortcut buttons to the IM Imports form:

- Open Template - Opens the IM Template form, with focus on the import template from the last executed import.

- Open Work Edit - Opens the IM Work Edit form, with focus on the work edit file from the last executed import.

- Open IM Upload - Opens the IM Upload form, with focus on the last executed import.

## Added Tekla Import Templates

To support the import of Tekla data, there are now three new import templates in IM Templates:

- TeklaJCAdj (PS Tekla Job Cost Adjustment)

- TeklaPO (PS - Tekla Purchase Order)

- TeklaPORec (PS - Tekla PO Receipts Import)

With these imports, you can now import Tekla data files, edit the data records as needed, and then upload the data into Vista. All three imports are 'batch' imports, meaning that when you upload the data to Vista, the system generates a batch in the related form. For example, the TeklaJCAdj import will generate a JC Cost Adjustments batch. You can then access the batch via the JC Cost Adjustments form, edit the entries as needed, and then process the batch.
You can learn more by watching the following videos on the Tekla import templates:
[Tekla Job Cost Import Adjustment](/en/vista/vista/videos/costs-and-contracts/tekla-job-cost-import-adjustment)
[Export a Tekla PO for Importing to Vista](/en/vista/vista/videos/costs-and-contracts/export-a-tekla-po-for-importing-to-vista)
[Import Tekla PO Files to Vista](/en/vista/vista/videos/costs-and-contracts/import-tekla-po-files-to-vista)

## SM Customer Import Supports Agreement Invoice Delivery Options

In conjunction with the new agreement invoice delivery options added in SM Customers, the SM Customers (SMCustomer) import now includes these new fields.
The new fields are as follows:

- AgreementUseWorkOrderSettingsYN (Identifier #360)

- AgreementReportID (Identifier #370)

- AgreementDeliveryTo (Identifier #380)

- AgreementDeliveryMethod (Identifier #390)

- AgreementBillingEmail (Identifier #400)

- AgreementBillingName (Identifier #410)

- AgreementBillingAddress1 (Identifier #420)

- AgreementBillingAddress2 (Identifier #430)

- AgreementBillingCity (Identifier #440)

- AgreementBillingState (Identifier #450)

- AgreementBillingPostalCode (Identifier #460)

- AgreementBillingCountry (Identifier #470)

In addition, increased the work order BilliingEmail identifier (#120) to 255 characters to allow for multiple email addresses.

## Support "As Cost Incurred" Revenue in SM Imports

The SMWorkOrder and SMAgreement imports now support 'as cost incurred' revenue. The following fields were added to these imports as follows:

- SMAgreement (SM Agreements)

- RevenueRecognition (Identifier 100)

- CostRevenueMargin (Identifier 105)

- SMWorkOrder (SM Work Orders)

- RevenueRecognition (Identifier 280)

- Margin (Identifier 290)

The RevenueRecognition column for both imports defaults to Use Viewpoint Default. If this value is blank in the import data file, the system populates the column in IM Work Edit based on how you set the Recognize Revenue as Costs Incurred checkbox in SM Company Parameters. If selected, the system defaults a value of C (As Costs Incurred). If not selected, the system defaults a value of B (As Billed).
A value is required in the Margin column for both work orders and agreements when the Recognize Revenue as Costs Incurred checkbox is selected in SM Company Parameters and when the pricing method is Flat Price (for work order scopes) or Time of Service, Flat Rate (for agreement services).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
