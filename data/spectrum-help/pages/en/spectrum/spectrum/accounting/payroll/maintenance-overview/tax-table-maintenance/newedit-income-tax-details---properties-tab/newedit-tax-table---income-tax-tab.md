---
title: "New/Edit Tax Table - Income Tax tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---income-tax-tab"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---income-tax-tab"
---

# New/Edit Tax Table - Income Tax tab

The tax table code displays in the header of this window.
The list box portion of the screen displays the filing statuses for the specified tax code.
Fields/Buttons
Descriptions

Description
Type a description of the tax table being entered, for example, "United
 States" or "California".

Tax ID number
Enter the employer tax identification number for this income tax jurisdiction. Up to 20 characters are allowed.

G/L liability account
The G/L account entered must be a non-direct G/L account. Use the drop-down arrow to select an account. No entry is required if the account status is Not Used.
Note: Cost center validation only occurs when the G/L account is being
 changed.

W-2 state abbreviation
-or-
 Province abbreviation
Payroll W-2 Processing requires use of a two-character state code for paper and electronic filing, per IRS specifications--enter this code here. During the 'Build W-2' Update, the Abbreviated W-2 State Code' is recorded in W-2 Processing for the employee's W-2 Form.
Note: In cases where multiple Tax Codes are present in Spectrum for the same
 jurisdiction, and values need to be aggregated on the employee W-2, the
 Payroll Manager may assign the same 'state code' to both codes.

Aatrix tax type
If you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to the Spectrum G/L account code for income tax in this field.
Note: Aatrix eFiling is only available to hosted customers.

Electronic filing #
If the selected tax code is filed electronically, enter the electronic filing # in this field.

Business number code?
This checkbox is only enabled when the Allow non-US payroll processing? checkbox is selected in the Payroll Installation - Defaults screen. This field is provided to accommodate different tax calculation amounts, such as the Basic Exemption amount that is part of the Canadian Pension Plan.

Country
This field is only enabled when the Allow non-US payroll processing? checkbox is selected in the Payroll Installation - Defaults screen and the Business number code checkbox is selected in the current screen. Use the drop-down list to select Canada or Other.

JurisdictionSelect the jurisdiction for the tax table code: County, Local, State/Province or Unassigned. Specifying a jurisdiction here
 will allow you to filter search results by jurisdiction on the Search Tax
 Codes window.
Note: If the selected tax table is federal, or the Business number code checkbox is
 selected, this field will be disabled.

Extra pay period this year?
Select this checkbox if your federal payroll tax requires you to include an extra pay period for the current year to properly calculate payroll tax deductions.
Note: This field will be hidden for non-federal tax codes.

New
Edit
Delete buttons
View the New/Edit Income Tax Details window. The information that displays in the columns of the list box default from entries made in this sub-window.

- The software automatically creates 'Married' and 'Single' filing status records when a new tax code is created, but it does NOT automatically create Head of Household or Other filing statuses.

- Click the Employees tab to see which employees are currently assigned to the selected filing status. If cost centers are being used, it might appear as if the filing status is not in use. However, this operator would still be disallowed from deleting the filing status because one or more active employees that are assigned to prohibited cost centers exist.

List box column descriptions

Filing status
When adding a new tax table, the software automatically creates 'Married' and 'Single' filing status records, but it does NOT automatically create Head of Household or Other filing statuses.

Calculation type
The Income tax calculation for this tax table displays in this column:

- Graduated tax table

- Percentage

Tax details
The Tax percentage or Graduated tax table bracket amounts for this tax table will display in this column.
Note: This window will support up to 50 graduated tax table
 rows.

Standard deduction
This field displays 'Yes' or blank for each filing status based on the Standard deductions setting in the New/Edit Income Tax Details window.

Tax credit
This field displays 'Yes' or blank for each filing status based on the Tax credit setting.

Tax exemption
This field displays 'Yes' or blank for each filing status based on the Tax exemptions setting.

Deduct other taxes
This field displays 'Yes' of blank for each filing status based on settings in the Deduct other taxes tab.

Tax basis
The tax base for the selected tax table will display in this column:

- Gross earnings

- Federal income tax

- State income tax.

If there is no income tax calculation for this tax table, the tax basis is 'None'.
