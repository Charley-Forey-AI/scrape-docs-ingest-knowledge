---
title: "SM Technicians Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form"
---

# SM Technicians Form

Use the SM Technicians form to set up the technicians that
 will perform service work for your company.
Technicians set up here must first be set up in PR Employees; this association ensures that labor hours entered for a technician on a work order are properly updated to Payroll.
 You can link a technician to an employee from any Payroll company. However, technician lists are not shared across SM companies. Therefore, if you have a PR employee that performs service work for multiple SM companies, you must set up a technician record in each of the applicable SM companies and associate them with that PR employee.
The Work Schedule tab allows you to set up the technician's work schedule. Dispatchers can use the work schedule to identify the times that a technician is available for scheduling on a work order.

## Rate

The rate you assign to each technician represents the anticipated labor cost rate for service work performed by the technician. This rate will generally include the base rate for the employee (as defined in PR Employee) plus burden; in other words, the total expected payroll cost (per hour) incurred each time the technician performs service work. This allows you to estimate the labor costs for work completed on a work order, long before payroll is actually cut. However, the system will only use this rate if the pay type specified when entering work completed labor on a work order uses a Cost Method of 0-Multiplier. The system will multiply the technician's rate by the factor defined for the pay type to derive the Cost Rate for the labor line. For example, if the technician's pay rate is $35.00 and the factor is 1.50, the calculated Cost Rate for the work completed labor line will be $52.50 (35.00 x 1.5). If the pay type uses a Cost Method of 1-Dollar Rate, the system overrides the technician's rate with the rate defined for the pay type (in SM Pay Types).

## Default Material Location

The IN Co and IN
 Location fields allow you to specify the location from which the
 technician generally pulls materials when performing service work. This might
 typically be the service truck (if you set up your service trucks as locations in IN
 Locations), but can also be a service center warehouse or any other location used to
 provide materials for service work. This information will then default automatically
 for work completed inventory lines (type 4-Inventory) entered for the technician on
 a work order.

Click the following links for more information about this form.
[Set Up a Service Technician](/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician)
[Set up Technician Work Schedules](/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician/set-up-technician-work-schedules)
