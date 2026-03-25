---
title: "Initializing Employees to HR From PR | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/initializing-employees-to-hr-from-pr"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/initializing-employees-to-hr-from-pr"
---

# Initializing Employees to HR From PR

If you are using the Human Resource module (HR), you can
 initialize employees set up in PR Employees into HR Resources using
 HR Initialize PR Employees.
You can initialize all eligible employees
 or a specific range of employees, and specify to initialize only Active employees or
 both Active and Inactive employees.
To initialize employees to
 HR Resources:

1. Open HR Initialize PR
 Employees.

1. In the Update
 Direction field, select Update PR to HR.

1. In the
 PR
 Co#
 field, enter the PR company from which to initialize employees or
 press
 F4
 to select from a list of valid PR companies.

1. If you want to initialize
 all PR employees to HR Resources, select the Initialize All checkbox.If you want to initialize a specific
 range of employees, deselect the Initialize All checkbox.

1. If you want to initialize
 only "active" PR employees, select the
 Exclude
 inactive employees
 checkbox.If you want to initialize both
 "active" and "inactive" employees, leave the
 Exclude
 inactive employees
 checkbox unselected.

1. If you elected to initialize a range of employees (
 Initialize All
 checkbox is not selected), use the
 Beginning Employee #
 and
 Ending Employee #
 fields to enter the range of employees to initialize.

1. Click
 Update Grid
 . The grid will populate with employees based on selection criteria. The
 Ready
 checkbox will be selected for each employee that is ready for initialization. Those not flagged as "ready" will be skipped during initialization.
Note: With the exception of the Name, SSN#, and PR Group fields,
 most of the fields required in PR Employees are not required in HR Resources.
 Therefore, if the Ready checkbox is not selected
 for an employee, it will generally be because an employee already exists in HR
 that has the same social security number, sort name, and/or first name/last name
 combination (the Error Message column will indicate the reason). If they are not
 the same person, you will need to correct the information for the applicable
 employee and/or resource before you proceed with initializing them to HR.

1. If you do not want to initialize an employee flagged as Ready, deselect the
 Ready
 checkbox for that employee.

1. Click
 Initialize. During the initialization process,
 the system will try to assign the resource number using the same number as the PR
 Employee. If the system determines that the resource number already exists for
 another employee, it will assign the next sequential number based on the highest
 existing resource number. For example, if you initialize Employee #100 to HR and
 Resource #100 already exists in HR, and the highest existing resource number in HR
 is 850, the system will assign the 851 as the resource number.
Once you have initialized employees
 to HR, the grid is cleared of the initialized employee. You can repeat the process
 if needed.
