---
title: "New/Edit Union - Properties tab - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---properties-tab/newedit-union---properties-tab---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---properties-tab/newedit-union---properties-tab---field-descriptions"
---

# New/Edit Union - Properties tab - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Union code
Enter a union code or select an existing one from the available drop-down arrow. Up to 10 characters are allowed.

Description
Enter a description of the union code. If you are editing an existing union code, entry is not allowed.

Craft
Enter the craft for this union code (for example, Carpentry, Masonry, Landscaper, and so forth).

Certified craft code
This field is applicable for those using the AASHTOWare XML electronic
 reporting feature. Data from this field will be written to the XML File.

Status
Select the Union status: Active or Inactive. Based on this setting, alerts will display throughout Spectrum when an operator enters an Inactive union code. No message will appear if the code was previously entered, and in all cases the operator is allowed to continue entry.

Deductions and add-ons

Deduction code
If there was some change in rate or calculation on the contract (as of a new effective date), enter a union deduction code. Up to 10 characters are allowed.

Description
Enter a description for the deduction code (for example, Vacation).

Method
Select the calculation method from the drop-down list of valid options. Click the corresponding button for additional information on the calculation methods.
 If the method is a 'user-defined formula', the formula code will be provided along with a search window to look up formula codes. For user-defined methods, click the User-Defined button to record user-defined variables.

Formula
Use this field to enter the user-defined formula code for deductions. A search window is available for selecting valid codes. This field is available only if 'User-defined' is selected in the corresponding 'Method' field.

Rate
Enter the new deduction rate that will take effect on the date of the scheduled rate adjustment. A search window is available only if the deduction method is User defined.
When this rate is set to zero, the system looks at the Employee Deduction/Add-on Maintenance screen to see if there are any employee-designated rates.

Effective date
Enter the date on which the rate change should automatically go into effect.

Include in gross pay?
Select this checkbox if you want to include the deduction amount in the employee's gross pay. Typically, this checkbox is not selected. It is selected under certain contractual arrangements where union dues, for example, must be paid to the employee in the form of additional gross pay, taxed, then deducted and forwarded to the union. This checkbox cannot be selected for add-ons, pay types SA, 1, 2, or 3, or for "fixed" method deductions.
This field is used in conjunction with the window at regular rate in the Union File Maintenance - [New/Edit Union - Rates tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---rates-tab) and the Wage Code File Maintenance - Properties tab.
After entering the add-on or deduction here, such as $1.00 per hour, the operator must open the window at regular rate in the union or wage screens to complete the process. There, the base rate is recorded. The system will automatically add the deduction amount to arrive at the full rate. For example, if the base rate is $15.00, the full rate in our example would be $16.00. Response in the Gross pay checkbox is irrelevant if rates are not stored in these screens.
Using the Gross pay feature to increase the base rate to full rate is not normally used when the calculation method is "percent of gross." This is because the effective percentages are different when added and subtracted. For example, when the base rate of $15 is increased by 10%, the full pay is $16.50. When a 10% deduction is applied, $1.65 will be subtracted rather than $1.50. For percentage method calculations, it is therefore recommended that the 'gross pay' feature not be used. Instead, enter the desired percentage deduction from the full rate in this screen, and record the full rate in the Union File Maintenance - [New/Edit Union - Rates tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---rates-tab) and the Wage Code File Maintenance - Properties tab.

Override G/L account
Use this field to enter an Override G/L account for a deduction. This lets you define a G/L account for union-specific deductions and makes it easier to reconcile G/L payable accounts. If cost centers are being used in the current company, the Override G/L account that you enter must also be allowed for the particular deduction code.

Benefit Tier Overrides
If at least one benefit code has been defined for this union and the Include in gross pay option is not selected, click this button to add any benefit tier overrides for this deduction/add-on.
The Tier-Specific Override Rates window will display all [New/Edit Union - Benefit Tiers tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---benefit-tiers-tab) setup for this union code.

- Select an Override status--No override, Not applicable, or Tier-specific rate.

- If Tier-specific rate is selected, specify the override rate to apply during check calculation. If the override rate is zero (blank), the employee-specific rate from recurring deductions/add-ons will be applied instead.
Note: Overrides do not exist for inactive
 deductions/add-ons.
