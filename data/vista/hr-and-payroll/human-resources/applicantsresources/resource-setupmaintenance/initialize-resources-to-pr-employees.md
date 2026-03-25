---
title: "Initialize Resources to PR Employees | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/initialize-resources-to-pr-employees"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/initialize-resources-to-pr-employees"
---

# Initialize Resources to PR Employees

If you are using the Human Resource module (HR), you can
 initialize resources set up in HR Resources into PR Employees using HR Initialize PR Employees.
 You can initialize all eligible resources or a specific range of resources, and specify to
 initialize only Active resources or both Active and Inactive resources.
Before you initialize
 resources to PR Employees, you must make sure they are set up appropriately in
 HR Resources. Certain fields require entry in order for the update to PR to occur, even
 if the data is not required to set up the resource. For each resource you plan to initialize
 to HR, make sure you have entered values in the following fields:Field

Located on Tab

Field

Located on Tab

Race

Info

Class

Payroll Info

PR Co #

Payroll Info

Ins Code

Payroll Info

SSN #

Payroll Info

Earn Code

Payroll Info

PR Group

Payroll Info

Unemp State

Payroll Info

Department

Payroll Info

Ins State

Payroll Info

Craft

Payroll Info

Local Code

Payroll Info

1. From the Main Menu, use the
 Company drop-down to select the HR company from which to initialize
 resources.

1. Open HR Initialize PR Employees.


1. In the Update
 Direction field, select Update HR to PR.

1. In the PR Co# field,
 enter the PR company to which you are initializing resources or press F4 to select
 from a list of valid PR companies.

1. If you want to initialize all HR
 resources to PR Employees, select the Initialize All checkbox.If you want to initialize a specific range
 of resources, deselect the Initialize All checkbox.

1. If you want to initialize only
 "active" HR resources, select the Exclude inactive employees check
 box.If you want to initialize both "active" and
 "inactive" resources, leave the Exclude inactive employees checkbox
 unselected.

1. If you elected to initialize a
 range of resources (Initialize All checkbox is not
 selected), use the Beginning Employee # and Ending Employee # fields to enter the
 range of resources to initialize.

1. Click
 Update Grid
 . The grid will populate with resources based on selection criteria. The
 Ready
 checkbox will be selected for each resource that is ready for initialization.
Note: If the Ready checkbox is not selected for a
 resource, the Error Message column will indicate what information is missing. If you are
 not prepared to correct the errors at this time, you can clear those resources from the
 grid by clicking the Clear button. A message displays asking if you want to clear only
 those entries that are not ready. Click Yes to clear the grid of only those
 resources with the Ready checkbox unselected. Click
 No
 to clear all resources from the grid.

1. If you do not want to initialize
 a resource flagged as Ready, deselect the Ready checkbox for that resource.

1. Click Initialize. During the initialization process, the
 system will try to assign the employee number using the same number as the HR Resource.
 If the system determines that the number already exists for another employee, it will
 assign the next sequential number based on the highest existing employee number. For
 example, if you initialize Resource #100 to PR and Employee #100 already exists in PR,
 and the highest existing employee number in PR is 850, the system will assign the 851 as
 the employee number.
Once you have initialized resources to PR,
 the grid is cleared of the initialized resources. You can repeat the process if
 needed.
