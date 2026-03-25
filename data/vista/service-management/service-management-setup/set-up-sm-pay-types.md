---
title: "Set Up SM Pay Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-sm-pay-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-sm-pay-types"
---

# Set Up SM Pay Types

Set up pay types in SM Pay Types.

1. From the Programs menu
 of Service Management, double-click on the SM Pay Types icon. This opens the SM
 Pay Types form.

1. In the
 Pay
 Type
 field, enter a pay type code to represent the pay level you are
 setting up (e.g. REG, OT, DT, HOL, etc.).

1. Enter a description of
 the pay type in the
 Description
 field.

1. Select the cost method
 (0-Multiplier or 1-Dollar Rate) from the
 Cost
 Method
 drop-down. The cost method determines how the system will derive
 the cost rate for work completed labor entries (in SM Work Orders).

1. If you selected the
 0-Multiplier cost method, use the
 Factor
 field to specify the multiplier for the cost method (i.e. 1.00
 for regular time, 1.5 for time and one/half, 2.00 for double-time, etc.).Note: The system multiplies this value by the
 technician's pay rate to determine the
 Cost Rate
 for work completed labor entries (in SM Work Orders).
If you selected the 1-Dollar
 Rate cost method, use the
 Rate/Amount
 field to enter the override pay rate.
Note: The amount entered in this field will be used instead
 of the technician's standard pay rate (defined in SM Technicians).

1. In the Earnings
 Code field, enter earnings code to use as the default when
 entering timesheets or timecards (in PR My Timesheet or PR Timecard Entry,
 respectively) that reference this pay type.Note: You must enter a valid timesheet
 earnings code (you checked the Include in Remote Timesheet
 Entry box in PR Earnings Codes). Press F4 for a list of valid timesheet earnings codes.

1. Check the
 Active
 box to activate the pay type.Note: Inactive pay types will not display in
 F4 lookups, nor can they be referenced when entering work completed labor on
 a work order (in SM Work Orders).
