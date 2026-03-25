---
title: "Set Up Crafts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-crafts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-crafts"
---

# Set Up Crafts

You can use the PR Crafts form to set up crafts.
When setting up a craft you will create a craft code, and specify any related add-on earnings, deductions (including pre-tax), liabilities, and any holidays that apply to the craft. Craft codes define work types or unions. For union contractors, one craft should represent one union for reporting purposes. Non-union contractors may also use the craft and class tables for setting up standard pay rates by work type, particularly if doing prevailing wage work.
Information entered at this level applies to all standard and template classes for the craft, unless specifically overridden. For more information, see [Crafts, Classes, and Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates).
The following instructions detail how to set up crafts.

1. Open the PR Crafts form.


1. In the Craft field, enter a code that will uniquely identify this
 union or type of work.

1. In the Description field, enter a description for the craft.

1. In the address fields, enter the address information for the craft/union.

1. In the Vendor field, enter the vendor that will be used for creating
 AP transactions for this craft's deductions and liabilities. Typically, this
 field is used by union contractors.Leave this field blank to use
 the vendor assigned to this craft's deductions and liabilities in PR
 Deductions/Liabilities.
Note: If the deduction/liability code is not
 set for automatic updates to AP, it is not included in the interface to AP,
 regardless of the vendor. For more information, see [Setting Automatic Accounts Payable Updates for D/L
 Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-automatic-accounts-payable-updates-for-dl-codes).

1. In the Effective
 Date field, enter the date that new rates for add-on earnings
 and deductions/liabilities become effective. Timecards posted to dates before
 this date use the old rates, while those posted on or after this date will use
 the new rate.

1. The Report
 Type field is optional. You can use this field to enter a code
 that could be used in a report as a restriction to group together like crafts
 that use the same report format. For example, you might have multiple carpenter
 unions that all use the same format. Each carpenter craft could be set with CARP
 in the Report Type field. A report that was formatted to match the
 carpenter format could be set up with a restriction to only print for crafts
 with CARP as the report type.

1. In the OT
 Schedule field, enter the overtime schedule to use to determine
 the daily overtime rules for this craft or press F4
 to select from a list of overtime schedules. This schedule will be used for
 employees who have craft set up as their overtime option in PR Employees
 (Overtime field, Add'l Info tab). Leave this field blank if daily
 overtime is not required by the craft.

1. [Set up a holiday week overtime override for the craft, if necessary](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-holiday-week-overtime-by-craft).

1. For Australia users: If
 you pay a weekly minimum for superannuation for this craft, enter the amount in
 the Superannuation Weekly Minimum field. For more information, see
 [Setting Weekly Minimums for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-weekly-minimums-for-superannuation).


1. For New York users: In
 the CHAMP Trade Seq# field (Add'l Info tab), enter the trade
 sequence number for this craft. A list of valid trade sequence numbers can be
 found in the "CHAMP-CM Equal Opportunity Management Software" requirements.


This is a required field for NY DOT electronic
 filing. Other states may also require this information; check your state's
 requirements to determine if entry in this field is necessary.

1. [Assign add-on earnings to the craft](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft).

1. [Assign deductions and liabilities to the craft](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft).

1. [Set capped codes and limits for prevailing wage work, as necessary](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

1. [Set up any holidays that are paid for the craft](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-holidays).

1. [Add classes to the craft](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes).

1. [Add templates to the craft, as necessary](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-templates).

Related information

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [PR Overtime Schedule Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form)
