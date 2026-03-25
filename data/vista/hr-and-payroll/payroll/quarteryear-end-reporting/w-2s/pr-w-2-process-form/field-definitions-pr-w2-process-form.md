---
title: "Field Definitions: PR W2 Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-w-2-process-form/field-definitions-pr-w2-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-w-2-process-form/field-definitions-pr-w2-process-form"
---

# Field Definitions: PR W2 Process Form

The following is a list of field descriptions for the PR W2
 Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Tax Year

Enter the tax year to initialize in YYYY format. If the current month is between, or includes, January and November, the field defaults the prior tax year. If the current month is December, the field defaults the current tax year.

## EIN #

If initializing a new W-2 run, this field defaults to the Federal Tax ID number defined for this company in HQ Company Setup; you can override this value if necessary. Note that all non-numeric characters, such as hyphens, are omitted.

## User ID #

Enter the personal identification number for this employer, as provided by the Social Security Administration. This field allows up to eight digits.
For tax years 2005 and later, this ID number is truncated to 8 characters and 9 spaces.

## Company Name

If initializing a new W-2 run, this field defaults the name of the current company as defined in HQ Company Setup. You may override this field if necessary.

## Location Address

If initializing a new W-2 run, this field
 defaults the address specified for this company in HQ Company Setup (Add'l Address
 field). You can override this field if necessary.

## Delivery Address

If initializing a new W-2 run, this field defaults the mailing address specified for this company in HQ Company Setup. You can override this default if necessary.

## City

If initializing a new W-2 run, this field defaults the city specified for this company in HQ Company Setup. You can override this default if necessary.

## State

If initializing a new W-2 run, this field defaults the state specified for this company in HQ Company Setup. You can override this default if necessary.
Enter a valid state (as defined in HQ States).
 The system validates the state based on the Default Country specified in HQ Company Setup
 for the active company. If the state is not valid, an error displays, but entry is allowed.
 You must then enter a valid country for this state in the Country field
 in HQ Company Setup.

## Zip

If initializing a new W-2 run, this field defaults the zip code specified for this company in HQ Company Setup. You can override this default if necessary.

## Zip Ext

Enter the 4-digit zip code extension.

## Contact Name

Enter the name of the individual for the SSA to contact regarding W-2s. This field allows a maximum of 27 characters. When filing electronically, the contact name is required.

## Phone

Enter the phone number for the individual that the SSA would contact regarding W-2s. This field allows a maximum of 15 characters. When filing W-2s electronically, the phone number is required.

## Phone Ext

Enter the phone extension for the individual that the SSA would contact regarding W-2s. This field allows a maximum of 5 characters.

## Fax

Enter the fax number of the individual that the SSA would contact regarding W-2s.

## Email

Enter the email address of the individual that the SSA would contact regarding W-2s. This is a required field.

## Third Party Sick Pay Indicator

Check this box if you are a third-party sick pay provider.

## NAICS Code

NAICS Code field on the PR W-2 Process form
For Maryland payroll only.
This value is pulled from the PR Company Parameters form when creating a new tax year. You may override this code with another up to 6 numbers long.

## Options To Initialize Retirement Plan Box

checkbox For All Employees – Select this
 option to check the Retirement Plan box in PR W-2 Employee Edit for all employees.
Only Check For Employees With Retirement Plan
 – Select this option to check the Retirement Plan box in PR W-2 Employee
 Information for all employees whose Retirement Plan box is checked in PR
 Employees.
checkbox For None Of The Employees – Select
 this option is selected to leave the Retirement Plan box in PR W-2 Employee
 Information unchecked for all employees.

## Resubmittal

The Resubmittal checkbox on the PR W-2 Process form, Info tab.

Note: Beginning December 2021, Aatrix is required for W-2 reporting. Resubmitted W-2s must be handled directly in Aatrix (using the History button in PR Aatrix - W2 Print and eFile). Therefore, this checkbox is no longer used and is disabled. However, to preserve historical data, this field remains visible.

Display only, indicating whether this W-2 file was resubmitted (selected).

## WFID

The WFID field on the PR W-2 Process form, Info tab.

Note: Beginning December 2021, Aatrix is required for W-2 reporting. Resubmitted W-2 must be handled directly in Aatrix (using the History button in PR Aatrix - W2 Print and eFile). Therefore, this field is no longer used and is disabled. However, to preserve historical data, this field remains visible.

This field only displays a value if the Resubmitted checkbox is selected.
Display only, the 6-character WFID (Wage File Identifier) code from the notice sent by the Social Security Administration.

## Contact Title

For the state of Maryland only. This field requires entry.
Enter the title of the individual authorized to certify this report.

## Total Tax Reported

For the state of Maryland only. This is a required field.
Enter the total tax reported on all MW506s.

## Total Tax Withheld

For the state of Maryland only. This is a required field.
Enter the total state/local tax withheld for all Maryland employees.

## Total Credits

For the states of Maryland and Missouri only.
If you are a tax-exempt organization, enter the total eligible business tax credits as indicated on Form 500CR.
Note: If you file W-2s for both Maryland and Missouri, you will need
 to enter the appropriate amount for one state (for example, Maryland), and process the
 W-2s. You will then need to change the value here as applicable for the other state
 (Missouri) and process those W-2s.

## Tax Due Amount

For the state of Maryland only.
Enter the total employer tax amount due.

## Balance Due

For the state of Maryland only.
Enter the employer balance due amount.

## Overpayment

For the state of Maryland only.
Enter the employer overpayment amount.

## Overpayment Credit

For the state of Maryland only.
Enter the employer overpayment amount that you wish to be applied as credit.

## Overpayment Refund

For the state of Maryland only.
Enter the employer overpayment amount that you wish to have refunded.

## Gross Payroll

For the state of Maryland only.
Enter the total amount of wages reported for all Maryland employees.

## Federal Information: Item

Select each of the
 earnings/deduction/liability items you want initialized for federal W-2s. Press F4 to display
 the list of standard reporting items.
Note: Viewpoint provides a list of standard reporting items each tax year, as defined by the Social Security Administration. Select only those items that apply to your company. If you run this form before the reporting items are updated for the new tax year, use the codes from the prior year and make sure that you re-initialize using the correct codes once they are updated. For a list of the current reporting items and the W-2 boxes in which they are printed, see [IRS Reporting Items](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/about-setting-federal-information-for-w-2-processing/irs-reporting-items).

## Federal Information: Type

Enter the E/D/L type for each item. Types are as follows:

- E-Earnings

- D-Deduction

- L-Liability

## Federal Information: Code

Enter the earnings, deduction, or liability code for this item, or press F4 for a list of codes. This code, in conjunction with the Type, determines where to get the amount for this item.

## Federal Information: Description

This field defaults the description for the earnings, deduction, or liability code from PR Earnings Codes or PR Deductions/Liabilities. You may override the default as necessary.

## State/Local Information: Initialize

This box defaults as checked for each state/local in the grid.
Uncheck this box if you do not want this state/local to be included in W-2 processing.

## State Box 14 Information: Line

The Line field on the PR W-2 Process form, State Box 14 Information tab.

Enter a line number to add a new state-specific record for Box 14 reporting on state W-2s.

## State Box 14 Information: State

The State field on the PR W-2 Process form, State Box 14 Information tab.

Specify the state for which you are reporting miscellaneous state information (Box 14) on the state W-2.

## State Box 14 Information: EDL Type

The EDL Type field on the PR W-2 Process form, State Box 14 Information tab.

Enter the E/D/L type for this miscellaneous description. Types are as follows:

- E-Earnings

- D-Deduction

- L-Liability

## State Box 14 Information: Code

The Code field on the PR W-2 Process form, State Box 14 Information tab.
Enter the earnings, deduction, or liability code (from PR Earnings Codes or PR Deductions/Liabilities) for this miscellaneous description.

## State Box 14 Information: Description

The Description field on the PR W-2 Process form, State Box 14 Information tab.

Use this 20-character field to enter descriptions for the Box 14 of the State/Local W-2s when you want to report state-specific deductions, such as CA SDI and AK ESC.
The system defaults the description for the code that you specified in the Code field:

- If you selected E-Earnings, the description defaults from the Description field in PR Earnings Codes.

- If you selected either D-Deductions or L-Liability, the description defaults from the Description field in PR Deductions/Liabilities. You can override the default as necessary.

## Misc Description 1-4

Use these fields to enter miscellaneous descriptions, up to 20 characters each, that print in Box 14 of the Federal W-2. Box 14 can be used to report any other information you want to give to your employees, but is not required by the Federal government. Some examples include union dues, health insurance premiums deducted, moving expenses paid, and education assistance programs.
Note:(for New Jersey users reporting FMLA information) If a private FMLA plan, enter the plan number of the insurance carrier. If a state-provided FMLA plan, leave the field blank.

##  Personal Identification Number

 Use this field when filing MMREF-1 only.
 Enter the personal identification number for this employer, as provided by the Social Security Administration. Up to eight digits allowed.
 For tax years 2005 and later, the PIN is truncated to 8 characters and 9 spaces.
