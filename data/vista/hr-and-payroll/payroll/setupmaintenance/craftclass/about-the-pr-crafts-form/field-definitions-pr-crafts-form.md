---
title: "Field Definitions: PR Crafts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form/field-definitions-pr-crafts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form/field-definitions-pr-crafts-form"
---

# Field Definitions: PR Crafts Form

The following is a list of field descriptions for the PR
 Crafts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Craft

 Enter a code, up to 10 characters, that will uniquely identify this union or type of work.
 Crafts define work types or unions. For union contractors, one craft should represent one union for reporting purposes. Non-union contractors may also use the craft and class tables for setting up standard pay rates by work type, particularly if doing prevailing wage work.

##  Description

 Enter a description of this craft, up to 30 characters.

## Address

Enter the address information for this craft. You will typically only do this when the craft represents a union for reporting.

- Address

- City

- State - This must be a valid state
 as defined in HQ States. The system validates the state based on the default country
 specified in HQ Company Setup for the active company. If you enter an invalid state
 an error will display, but the system will allow entry. You must then enter a valid
 country for this state in the Country field.

- Zip Code/Postal Code

- Country - You must enter a country
 in this field when the address exists outside of the default country specified in HQ
 Company Parameters for the active company. The country must be valid for the state
 (province, territory, etc.) you specified in the State field.

Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). The system will then default the approximate location of the specified country and address. If a country is not specified, the system attempts to locate the address based on the default country specified in HQ Company Setup.

## Vendor

Enter the vendor (from AP Vendors) that will
 be used for creating AP transactions for this craft/union’s deductions and liabilities;
 typically used by union contractors. Vendor specified here may be overridden for individual
 deductions and liabilities in the Dedns/Liabs tab.
If no vendor is specified here, the vendor assigned (in PR Deductions/Liabilities) to each deduction/liability set up for this craft will be used.
Note: If a deduction/liability code’s 'Automatic Update to Accounts Payable' option is not checked (PR Deductions/Liabilities), it is not included in the interface to AP, regardless of the vendor.

## Effective Date

Enter the date on which new rates for add-on earnings and deductions/liabilities (specified on the Dedns/Liabs tab) become effective. Timecards posted to dates before this date use the old rates, and those posted on or after this date use the new rate. This applies to all classes within the craft. Effective date may be overridden by template in PR Craft Templates.
Old rates can be updated automatically with
 the new rates by selecting the Move New Rates to Old option on the File menu. The old rates
 for all classes on the craft will be replaced with their new rate; new rates are not
 affected by this update. Rates are typically moved whenever the Effective Date is changed.

##  Report Type

 Optional; not used by the standard forms.
 This field might be used to identify a Crystal Report that will be formatted for this union; informational only.
 It might also be used to enter a code that could be used in a Crystal Report as a restriction to group together like unions that use the same report format. For instance, you might have multiple Carpenters’ unions that all use the same format. Each carpenter’s craft could be set up with “CARP” as the Report Type. A Crystal Report that was formatted to match the Carpenters’ format could be set up with a restriction to only print for crafts with “CARP” as the Report Type.

##  OT Schedule

 Enter the overtime schedule (from PR Overtime
 Schedule) that will be used to determine the daily overtime “rules” for this craft. Leave
 blank if daily overtime is not required by this craft. This schedule would be used for
 employees who have C-Craft selected as their Overtime option in PR Employees.

## Add'l Info: CHAMP Trade Seq#

Enter the trade sequence number for this craft. A list of valid trade sequence numbers can be found in the “Champ-CM Equal Opportunity Management Software” requirements.
Note: This is a required field for NY DOT electronic filing. Other states may also require this information; check your state’s requirements to determine if this information is needed.

## Add'l Info: RPP Number

The system displays this field for Canadian companies only.
Enter the Registered Pension Plan for this
 craft. When generating T4s, the system will use this number. If you do not enter a number
 here, the system will use the number from the RPP Number field in PR Canada T4.

##  Capped Codes: Seq

 Enter a sequence number to control the order in which earnings and/or liabilities are reduced to keep the total wages plus benefits within a capped limit. The full amount of the preceding code must be reduced before the next code is affected.
 For more information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

##  Capped Codes: Type

Select the capped code type: E-Earnings or
 L-Liability.
For more information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

## Capped Codes: Earn/Liab Code

Enter the earnings or liability code that is to be capped. The entry must be either an add-on earnings or a liability code that is already set up for the craft, and its method must be rate per hour. If the hourly rate earned exceeds the capped limit in PR Craft Classes, then these earnings or liability codes are reduced.
Note: Employee-based liabilities (those with a calculation category of 'Any' or 'Employee' that are flagged as employee-based in PR Employee Dedns/Liabs) should not be set up here; only craft-based codes are reduced based on the capped amount.
 For more information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

##  Capped Basis: Type

Select the capped basis code type: E-Earnings or
 L-Liability.
For more information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

## Earn/Liab Code

Earn/Liab Code field on the PR Crafts form,
 Capped Basis tab.
If the Type is E-Earnings, enter a valid
 earnings code or press F4 to select from a list of valid
 earnings codes. Earnings code must have a method of H-Rate per hour (in PR Earnings
 Codes).
If the Type is L-Liability, enter a valid
 liability code or press F4 to select from a list of valid
 liability codes. Liability code must have a method of H-Rate per hour or A-Amount AND a
 calculation category of C-Craft, E-Employee, or A-Any (in PR Deductions/Liabilities).

Related information

- [Set Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits)

- [Set Up Crafts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-crafts)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

## Earn Code

Earn Code field on the PR Crafts form,
 Allowance Earnings tab.
Enter the earnings code for this allowance or press F4 to select from a list of valid earnings codes.
Tip: You should specify an earnings code that is specific to the allowance you enter. The system does not report based on allowances, but on earnings. Therefore, if you use a generic earnings code for each allowance, the system will only display a lump sum amount for earnings and you will be unable to tell which allowances contributed to the amount (PR Employee Pay Seq Control, Earnings Code tab, for example).
