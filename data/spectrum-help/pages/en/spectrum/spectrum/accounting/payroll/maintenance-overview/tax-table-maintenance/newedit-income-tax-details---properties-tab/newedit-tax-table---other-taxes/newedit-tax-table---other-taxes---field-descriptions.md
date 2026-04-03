---
title: "New/Edit Tax Table - Other Taxes - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes/newedit-tax-table---other-taxes---field-descriptions"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes/newedit-tax-table---other-taxes---field-descriptions"
---

# New/Edit Tax Table - Other Taxes - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Note: Aatrix eFiling is available only to hosted customers.

Fields/ButtonsDescriptions
 Exempt this tax code from unemployment and SDI/EI calculations? (State and province Tax tables only)When selected, all fields on this tab are disabled.
 Unemployment
 Other

Employer G/L liabilityFor the state tables, enter the General Ledger account code for the employer unemployment insurance. The account entered must be a non-direct cost account. No entry is allowed if the account status is Not Used.
Tax rateEnter a rate between 0% and 99.9999%.
Annual startEnter a value between 0 and 999,999.99 at which the tax assessment begins.
Annual limitEnter a value between 0 and 999,999.99 after which no tax assessment is made.
Limit basis (States and provinces only)For County and Local jurisdictions, this option controls whether the check calculation uses all County (or Local) 'subject to' unemployment earnings or the current jurisdiction only. While the label says 'This state only', it applies to 'This county only' (or 'This local only') depending upon what field it is assigned to in Time Card Entry.
Aatrix tax type (States and provinces only)If you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to your G/L account code for the employer unemployment insurance in this field.
 Entity Override buttonDisplays only if 'Entity tracking' is enabled in Enterprise Installation and this company is operating in the US and this is not the US tax code.
Select to open the Entity-Specific Unemployment Rates window and enter the entity-specific employee and employer tax (SUTA) rates there.

 SUTA tax ID numberIf applicable, enter your SUTA tax ID number in this field.
 Other tax ID numberIf applicable, enter a relevant tax ID number in this field.
 Disability insurance
These fields display when the selected tax table is not 'US' but does pertain to a U.S. state.

Employee G/L liabilityEnter the General Ledger account code for the employee portion of the state disability insurance. The account entered must be a non-direct cost account. No entry is allowed if the account status is set to Not Used.
Employer G/L liabilityEnter the General Ledger account code for the employer portion of the state disability insurance. The account entered must be a non-direct cost account. No entry is allowed if the account status is Not Used.
Limit basisSelect to apply the limit to the specified tax code or all states.
Limit method Select whether the limit is an annual one or is per pay period.
Aatrix employee tax typeIf you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to your G/L account code for the employee portion of the state disability insurance in this field.
Aatrix employer tax typeIf you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to your G/L account code for the employer portion of the state disability insurance in this field.
Employee / Employer calculations, tax rates, and limitsSelect the calculation type from the available drop-down list and then enter the respective tax rate, starting amount, and limit.
Entering a "0" in the tax rate field is the same as selecting 'None' in the calculation field.

 Entity Override buttonDisplays only if 'Entity tracking' is enabled in Enterprise Installation and this company is operating in the US and this is not the US tax code.
Select to open the Entity-Specific Disability Rates window and enter the entity-specific employee and employer tax rates there.

 Social Security and Medicare
These fields display only when the selected tax table is 'US'.

Employee G/L liabilityEnter the General Ledger account code for the employee portion of FICA. The account entered must be a non-direct cost account. No entry is required if the account status is Not Used.
Employer G/L liabilityEnter the General Ledger account code for the employer portion of FICA. The account entered must be a non-direct cost account. No entry is required if the account status is Not Used.
Social security rateEnter the Social Security tax rate.
Annual startLeave blank.
Annual limitEnter the limit specific to the tax year.
Medicare rateEnter the percent to be used in calculating the Medicare assessment.
Total rate (over threshold)Enter the percent to be used in calculating the additional employee Medicare withholding when income exceeds the threshold amount.
Annual limitEnter the earnings level after which no Medicare assessment is to be made, if one applies.
The field names and meanings in this section differ depending on the tax table in question:

- Disability insurance - For province tax codes, this section is for employment insurance (EI) withholdings and company matches.

- Pension Plan - If the Federal checkbox is selected and the Country field is set to Canada in the Income Tax tab, this section is for Canada Pension Plan (CPP) withholdings and company matches.

Employee G/L liabilityEnter the General Ledger account code for the employee portion of the CPP or EI.
The account entered must be a non-direct cost account. No entry is required if the account status is Not Used.

Employer G/L liabilityEnter the General Ledger account code for the employer portion of the CPP or EI.
The account entered must be a non-direct cost account. No entry is required if the account status is Not Used.

Limit basis (EI only)Select to apply the limit to the specified tax code or to all provinces.
Limit method (EI only)Select whether the limit is an annual one or is per pay period.
Aatrix employee tax typeEnter the tax type for the employee contributions.
Aatrix employer tax typeEnter the tax type for the employer contributions.
Basic exemption (CPP only)Enter the annual basic exemption amount to be used in determining the CPP 'Subject to' wages during check calculation.
Employee First TierChoose the calculation method and enter the employee tax rate and starting and stopping amounts.
Employee Second Tier (CPP only)Enter the rate and limits specific to this tier.
Appears only when the selected tax table is CN and is enabled only when the employee first tier calculation method is Percentage.
The calculation method and starting amount correspond to your choices for the the first tier.

Employer First TierChoose the calculation method and enter the employer tax rate and starting and stopping amounts.
Employer Second Tier (CPP only)Enter the rate and limits specific to this tier.
Appears only when the selected tax table is CN and is enabled only when the employer first tier calculation method is Percentage.
The calculation method and starting amount correspond to your choices for the the first tier.
