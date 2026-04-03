---
title: "New Equipment Statistic | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/equipment-statistics/new-equipment-statistic"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/equipment-statistics/new-equipment-statistic"
---

# New Equipment Statistic

Use this window to add or edit the statistics associated
 with the specified equipment.
When statistics are set up for the equipment type, then only statistics from that list will
 be valid for the equipment (and the Search Statistics window will only display statistical
 codes specified for the equipment).
The instructions and result format default from the [Statistic Code File Maintenance](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/statistic-code-file-maintenance) screen (or the Equipment Type File Maintenance screen) and no changes to these fields are allowed in this window.
When the statistic being added is a tire-specific statistic code, the Component and Sequence fields do not display, and a [Tire Statistics Entry](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/equipment-statistics/tire-statistics-entry) window opens automatically at the Test/reading entry field . (For tire statistics shown in the Edit Equipment Statistic window, the tire code and description display instead of the component code and description, and you will need to press F4 at the Test/reading entry field to open the Tire Statistics Entry window.)
Fields
Descriptions

Instructions
The instructions on how to obtain the statistic test result display.

Result format
Select the result format that you want to associate with this statistic code. The fields that display in the Validation section will depend on the selection you make here.

Component
Select a component code for this equipment from the available drop-down list. The associated component description will then display. (In the Edit and View windows, the Component code, description, and Sequence code will display.)

Sequence
The next available sequence number defaults automatically after a component has been entered.

Event

Test/reading entry
This field varies by result format. Entry is required in this field, but numeric and percentage fields will allow zero as a valid entry.

> Result format
Valid entry

Pass/Fail
Select either P or F from the available drop-down list.

Numeric
Enter a positive or negative value.

Percentage
Enter a positive or negative value.

Alpha
Enter test describing the test reading. If this field is set up to be validated, then you may select from a list of available codes.

Date
Enter any date. If this field is set up to be validated, then you will must select a date within the current minimum/maximum date range as set up in [E/C Processing Date Change](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/ec-processing-date-change)

When the statistic being added is a tire-specific statistic code, a [Tire Statistics Entry](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/equipment-statistics/tire-statistics-entry) window opens automatically.

Examination date
This field defaults to the current Equipment Control processing date, but you may enter a different date if necessary (and the minimum/maximum processing date range will not restrict entry).

Examiner
Select the person who performed the statistic test reading from the available drop-down list. The examiner can be both an employee and vendor. In the new window, the examiner will default from the previous entry (made during the same session).

Comments
Enter any comments relating to this statistical event that might be helpful to other operators.

Evaluation

Test finding
This field is set automatically by the software to Pass, Fail, or blank, based on the Result format and Test/reading entry fields.

> Result format
Test finding answer

Pass/Fail
Set equal to the user entry in the Test/reading entry field.

Numeric
Set to Fail if the Test/reading entry is outside the minimum/maximum range, set to Pass if within the range, and set to blank if no range is specified.

Percentage
Set to Fail if the Test/reading entry is outside the minimum/maximum range, set to Pass if within the range, and set to blank if no range is specified.

Alpha
Set to Fail if the validated alpha code is assigned a test result of Fail, and set to Pass if the code is assigned a test result of Pass.

Date
Set to Fail if the date is outside the minimum/maximum range, set to Pass if within the range, and set to blank if no range is specified.

Test result details
This field is generated automatically based on the statistic code setup; no changes are allowed.

Norm
This field displays only when a Norm, Minimum norm, or Maximum norm is set up; no changes are allowed.

Resolution
This field works in conjunction with the Reviewed checkbox and only displays if the Test finding = Fail. Use this field to enter any notes regarding the evaluation and resolution of the failed test. This field is only accessible to operators with security access to the Review Statistical Findings screen.
