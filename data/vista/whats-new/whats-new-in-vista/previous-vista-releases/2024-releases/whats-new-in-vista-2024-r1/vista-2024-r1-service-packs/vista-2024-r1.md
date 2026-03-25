---
title: "Vista 2024 R1.03 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/vista-2024-r1-service-packs/vista-2024-r1.03"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/vista-2024-r1-service-packs/vista-2024-r1.03"
---

# Vista 2024 R1.03

This release contains an update to scanner driver compatibility, changes to the AR Invoice - Canada report, an update to Aatrix for Alabama exempt overtime, and bug fixes that apply to all geographies.

## WIA Scanner Drivers Now Supported, in Addition to TWAIN

You can now scan documents into Vista using WIA or TWAIN drivers. Previously only TWAIN drivers were compatible. See the following articles for more information:

- [Set up Scanning Functionality](/en/vista/vista/system-tools/document-management/dm-workflow/document-scan/set-up-scanning-functionality)

- [Vista Hardware Requirements](/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-hardware-requirements)

## Tax Breakout for AR Invoice - Canada Report (CA only)

Report ID: 1242
The AR Invoice - Canada report now includes a breakout of Provincial State Tax (PST) from Goods and Services Tax (GST). The Tax field on the report shows the total tax amount (as it did previously), but you can now see the breakout of PST and GST below the totals.

## Alabama Exempt Overtime Now Included in Aatrix AUF (U.S. only)

In accordance with Alabama reporting requirements for overtime compensation, the Aatrix W-2 AUF will now include overtime wages, as reported in Box 14 (EX AL OT) of the Aatrix W-2/1099 Preparer form.

 In addition, a new Alabama Tax Exempt Wages query was added to the Accounting Work Center under the Payroll folder (Items > Payroll > Alabama Tax Exempt Wages). Once you enter the month range (for example, 01/2024 - 12/2024), the grid displays all employees within the range that have overtime wages. The amount shown in the Total Exempt Amt column should match what is reported in Box 14 (in Aatrix) and is the amount included for each employee in the Aatrix W-2 AUF file.
Note: All wages and associated Earn Codes must be set up to be subject to Alabama withholding for the calculation to be accurate (in PR Deductions/Liabilities, Basis Codes tab).

## Include Arrears Payback in PR to AP Update

You can now include arrears payback amounts for a deduction, along with the calculated amount, when sending information to AP using the PR AP Update process.
A new Include Payback in Auto Update to AP checkbox was added to the Arrears/Payback tab of the PR Deductions/Liabilities form. This checkbox is enabled only if you selected both the Automatic Update to Accounts Payable and Subject to Arrears checkboxes for the deduction.
If selected, and an employee is flagged as active for arrears in PR Employees, payback amounts for the employee will be included with the calculated deduction amount in the AP transaction generated during the PR to AP Update process. The system will generate one transaction line that includes both the deduction amount (calculated or override) and the payback or override payback amount.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
