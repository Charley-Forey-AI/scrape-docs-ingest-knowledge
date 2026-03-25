---
title: "Field Definitions: HR Resource Salary History Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/talent-and-performance/about-the-hr-resource-salary-history-form/field-definitions-hr-resource-salary-history-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/talent-and-performance/about-the-hr-resource-salary-history-form/field-definitions-hr-resource-salary-history-form"
---

# Field Definitions: HR Resource Salary History Form

The following is a list of field descriptions for the HR
 Resource Salary History form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Resource #

 Disabled if this form was accessed
 from HR Resources.
 Specify the resource (HR Resources) for which
 this salary history event is being entered.

##  Effective Date

 Enter the date of this salary/position adjustment. If there is existing salary history for the resource, this field defaults to the last (most recent) salary history date. Press F4 for list of all salary history dates for this resource.

##  Salary/Hourly

Salary - Select this option if this resource works on a salary basis.
Hourly - Select this option if this resource works on an hourly basis.

##  Old Salary/Rate

 Display only, the resource’s current salary/rate as of the Effective Date.

##  New Salary/Rate

 If not using the Calculate option (below), enter the new salary or hourly rate for this resource. Based on this amount and the old salary/rate, a total percent increase is calculated and displayed to the right of this field.
 If using the Calculate option, leave this field blank. The new salary/rate will be calculated based on values entered in the Salary Reasons grid.

##  Position

 Defaults the
 position code assigned to this employee in HR Resources, or as null (blank) if no position
 code is assigned. If you are not changing this employee’s position, no entry is needed.
 Otherwise, enter the new position code (from HR Position Codes) for this employee.
Note: If you change this employee’s position code (or set it
 to ‘null’), upon saving the record, the system will display a message asking if you want to
 “Update Position Code in HR Resources”. Click Yes to update the new position to HR
 Resources. If you click No, no update will occur; however, you can update the position code
 manually in HR Resources.

##  Next Salary Review Date

 Indicate the date of the next salary review for this employee.

##  Calculate?

 Check this box to have the new salary/rate calculated for you based on sequences in the grid.When checked, for each entry in the grid, you specify the applicable reason code and percent increase, and the new salary/rate is calculated for you. If multiple sequences are entered, the new salary/rate is recalculated after each entry, and will include all previous sequences. The Total Pct Increase field to the right of the New Salary/Rate field will display the total percent increase of all sequences.
Note: When checked, the New Salary/Rate field cannot be changed. (An amount can be entered, but the entry will not be saved.)
 Leave this box unchecked to manually enter the new salary or hourly rate. The Total Pct Increase will be calculated based on the new salary/rate and the old salary/rate. Entries can still be made in the grid to indicate the reason for the increase, but any percent increase specified for a sequence will not affect the new salary/rate or total percent increase.
This option determines whether you will
 manually enter the new salary/rate for the employee, or have the system calculate it for
 you. If this option is unchecked, you must enter a value in the New Salary/Rate field (Info
 tab). The 'Total Pct Increase' automatically reflects the appropriate rate increase based
 on the new salary and old salary values. You can then add entries in the grid to identify
 how the new salary/rate was determined. For example, if the total percent increase is 10%,
 the first entry in the grid will default 10.00%. If you change the percent, say to 7.00%,
 then add another item, the new entry will default a percent of 3.00.
Note: When using this method, the New Salary/Rate and Total
 Pct Increase values are not updated by the values entered in the grid. This will cause a
 discrepancy if the total percent of the items does not equal the Total Pct Increase. In
 this case, you can either correct the values in the grid or check the Calculate option to
 have the grid values update the New Salary/Rate and Total Pct Increase.
If you check the Calculate button, you can
 bypass the New Salary/Rate input and instead add entries in the grid to determine the new
 salary/rate. You can add as many entries in the grid as necessary, each with its own reason
 code and rate increase. Once all entries have been added, the system will calculate the new
 salary/rate based on the total of all entries in the grid and update the Total Pct Increase
 value accordingly.

##  Seq

 Display only, the system-assigned sequence number for each reason code entered in this grid.

##  Reason Code

 Enter a valid reason code (HR Codes, Type N)
 to identify the reason for this salary and/or position adjustment.

##  % Increase

 Indicate the percentage by which this employee’s salary will be increased for this reason code.
Note: If you are using the Calculate option, the percentage entered here is used to calculate the New Salary/Rate and the Total Pct Increase. If not using the Calculate option, the percentage entered here is informational only and will not affect the New Salary/Rate or the Total Pct Increase.
