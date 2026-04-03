---
title: "Sales Tax Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/sales-tax-code-maintenance/sales-tax-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/sales-tax-code-maintenance/sales-tax-code-maintenance---field-descriptions"
---

# Sales Tax Code Maintenance - Field Descriptions

The New Sales Tax Code window is used to set up sales tax codes for use during Invoice Entry. Sales tax codes may be up to 15 alpha-numeric characters long. There will be at least one code for each municipality for which the company must collect and forward sales tax revenues. If some sales are made that do not require tax, one or more non-taxable sales tax codes will be used in the Customers screen to establish a default sales tax code that will then appear in Invoice Entry. At that time, a different sales tax code may be recorded, if appropriate.
If it is not necessary to track sales tax information, simply enter a single sales tax code and then use that code for every customer.
Field
Description

Sales tax code
Enter a unique code (up to 15 alpha-numeric digits) to identify this sales tax jurisdiction. Companies working in many tax jurisdictions may wish to use the state tax codes in this field.
Sales tax codes will be used throughout Spectrum. A tax code will be entered in every customer, indicating the amount of sales tax that will typically be charged to that customer. A tax code can also be entered in every job, indicating the amount of sales tax that will typically be charged on that job. This entry sets up defaults; when invoices are created, the defaults can be overwritten as needed.
Note: Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding scheme should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, '1', '10', '100' will appear before '2', '20', '200'. Instead, codes should be set up '001', '010', and so forth. If more than 1000 codes are anticipated, instead enter '0001', '0002', and so forth.

Description
Enter the description for this sales tax code.

Properties

Online tax code
Select this checkbox to use the Avatax online tax service to calculate sales tax.

Current tax rate
Enter the percentage tax rate for this jurisdiction. For example, a tax percent of six and a half would be entered as 6.5. If there is no sales tax for this type of sale, enter 0 (zero).
If the Online tax code checkbox is selected, this field will be set to 0.0000% as online tax service rates will apply.

G/L account code
Enter the General Ledger account code for "sales tax payable" for this tax code. A lookup window is available for viewing valid General Ledger account codes. If the G/L status code you select has a status of Not used, you cannot proceed using this code. If the G/L status code you select has a status of Inactive, a warning will display.
Cost Center Information
If the cost center feature is enabled in the Enterprise Installation screen, when adding or changing a sales tax code Spectrum will allow entry of a G/L account code only if the operator entering the G/L account has permission to assign that code. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that G/L account cannot be assigned. Once a G/L account code has been assigned to a sales tax code (by an authorized operator), then that G/L account will be used by all operators when processing involves that tax code.

Tax on freight?
Select the checkbox if sales tax is to be calculated on freight. Clear the checkbox if sales tax is not to be calculated on freight. This field is only relevant if the Order Processing or Materials Management module is installed.

Financials

Total sales / Total tax
These figures are accumulated balances of transactions updated since the last period end clear was executed.

Tax rate revision

Next tax rate
The next tax rate displays in this field.
To edit the upcoming tax rate, click the Rates button to open the [Rate History](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/rate-history) window.

Effective as of
The date that the next tax rate goes into effect displays.
To edit the upcoming tax rate's effective date, click the Rates button.

Comments
A comment about the upcoming tax rate displays. The text in this field does not display on the Sales Tax Code Listing.
To edit the upcoming tax rate's comment, click the Rates button.
