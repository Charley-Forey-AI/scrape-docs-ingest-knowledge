---
title: "Set Up a Service Technician | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician"
---

# Set Up a Service Technician

You will use the SM Technicians form to set up the technicians that will perform service work for your company.
Use the following steps to set up a service technician.

1. From the Programs menu of Service Management, launch the SM Technicians form.

1. Enter a technician in the Technician field using one of the following options:

1. Enter a technician name or number.

1. Press F4 to select an employee from PR Employees. Then select the All Employees radio button, choose an employee from the list, and click OK. The Technician field defaults the employee's sort name from PR Employees. In addition, the system defaults the PR Co and Employee from PR Employees.

1. Enter the payroll company to which the technician is associated in the PR Co field.Skip this step if you used Step 2b to enter the technician.

1. In the Employee field, enter or select the employee from the PR Co specified above that identifies the technician you are setting up.Skip this step if you used Step 2b to enter the technician.
Note: If you select an "inactive" employee, the system will allow you to save the record. However, you must activate the employee (in PR) before you can post transactions to the technician.

1. In the Rate field, enter the default labor rate for the technician. This rate will be used in labor cost calculations on work completed labor entries that reference this technician in SM Work Orders (Work Completed tab).Note: This rate is only used when the pay type specified for work completed labor lines (entered in SM Work Orders) has a Cost Method of 0-Multiplier. The system multiplies this rate by the factor specified for the pay type (in SM Pay Types) to derive the Cost Rate for the labor line.
 If the pay type Cost Method is 1-Dollar Rate, the system overrides the rate defined for the technician with the rate defined for the pay type (in SM Pay Types).

1. In the IN Co and IN Location fields, enter the IN company and location from which this technician pulls materials when performing service work (e.g. truck, warehouse, etc.). Press F4 for a list of valid IN companies and/or locations.

1. Check the Active box to activate the technician. Technician will be available for selection in any field that prompts for technician.Leave this box unchecked if technician is not currently active.

1. Save the record.

1. [Set up the technician's work schedule](/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician/set-up-technician-work-schedules).
