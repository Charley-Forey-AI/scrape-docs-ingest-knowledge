---
title: "Field Definitions: HQ State Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/company-setup/hq-state-compliance-form/field-definitions-hq-state-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/company-setup/hq-state-compliance-form/field-definitions-hq-state-compliance-form"
---

# Field Definitions: HQ State Compliance Form

The following is a list of field descriptions for the HQ State Compliance form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Country

The Country field on the HQ State Compliance form.
Enter the country for which you are setting up state compliance requirements or press F4 to select from a list of valid countries (as defined in HQ Countries).

## State

The State field on the HQ State Compliance form.
Enter the state for which you are setting up compliance requirements or press F4 to select from a list of valid states for the specified country (as defined in HQ States).

## Effective Date

The Effective Date field on the HQ State Compliance form.
Enter the date on which the compliance requirements defined for the specified country and state are effective.
The system will apply these requirements to timecards entered on or after this date. Timecards with a date prior to this date will use the previous effective date rules. If no previous rules exist, no state compliance check will occur.

## Min Wage

The Min Wage field on the HQ State Compliance form.
Enter the minimum wage for covered, nonexempt employees for the specified country/state. This may or may not differ from the current federal minimum wage.
Note: Many states have a minimum wage that is higher than the federal minimum wage. If an employee is subject to both federal and state minimum wage laws, they are entitled to the higher of the two rates.

## OT Requirement

The OT Requirement field on the HQ State Compliance form.
Select the applicable OT Requirement type for the specified country/state.

- F - Federal - Select this option to follow the Federal overtime rules (defined by the Fair Labor Standards Act).

- S - State - Select this option to follow overtime rules based on OT schedules defined in PR Overtime Schedule (for the active PR company). Once selected, the OT Schedule field is enabled.

## OT Schedule

The OT Schedule field on the HQ State Compliance form.
Enabled if the OT Requirement field is set to S-State.
Enter the OT schedule to use for this country/state or press F4 to select from a list of valid overtime schedules.
Note: Although the HQ State Compliance requirements are shared by all companies, overtime schedules are defined by Payroll company. Therefore, when you press F4, the list of overtime schedules will differ depending on the active HQ company. For example, if the active HQ Company is Company #2, the F4 list will show overtime schedules for Payroll Company #2.

## Required

The Required checkbox on the HQ State Compliance form.
Select this checkbox if this country/state has meal break requirements. Once selected, remaining fields in the Meal Break Requirements section are enabled.
Leave unselected if there are no meal break requirements for this country/state.

## Meal Break Hrs Requirement

The Meal Break Hrs Requirement field on the HQ State Compliance form.
Enabled when the Required checkbox is selected.
Enter the number of hours an employee must work to be entitled to a meal break.

## Meal Break Length (Hrs)

The Meal Break Length (Hrs) field on the HQ State Compliance form.
Enter the length of time required for meal breaks, in hours. For example, enter 1.00 for one hour or .50 for half an hour (30 minutes).

## Meal Break Penalty

The Meal Break Penalty checkbox on the HQ State Compliance form.
Select this checkbox if the specified country/state imposes penalties on employers who fail to provide required meal breaks.
Leave this checkbox unselected if this country/state does not impose penalties on employers for meal break violations.

## Meal Break Penalty Hrs

The Meal Break Penalty Hrs field on the HQ State Compliance form.
Enabled and required when the Meal Break Penalty checkbox is selected.
Enter the meal break penalty in hours. For example, enter 1.00 for one hour or .50 for half an hour (30 minutes).

## Fed Form Accepted

The Fed Form Accepted checkbox on the HQ State Compliance form.
Select this checkbox if the specified country/state accepts the federal withholding form for calculating state tax withholding.
Leave this checkbox unselected if the specified country/state does not allow the federal withholding form for state tax calculations.
Note: Some states require that employees fill out a state-specific withholding form due to federal tax laws being different from the state's, making the federal withholding form less suitable for calculating state tax withholding.

## State Form

The State Form field on the HQ State Compliance form.
Enter the specified state's withholding certificate form (W-4).

## Supplemental Wage Rate

The Supplemental Wage Rate field on the HQ State Compliance form.
Enter the supplemental wage rate for income tax withholding for the specified country/state. This rate applies to supplemental wages such as bonuses, commissions, back pay, etc., when paid separately from regular wages.
Note: The supplemental wage rate specified here is in addition to the federal supplemental withholding rate for supplemental wages.

## Notes

The Notes tab on the HQ State Compliance form.
Enter any miscellaneous notes about this country, state, and effective date. The space allowance is virtually unlimited.
Note: If you access this field from the grid tab and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
