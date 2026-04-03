---
title: "Using Locations and Entities on OSHA Forms | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-and-entities-on-osha-forms"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-and-entities-on-osha-forms"
---

# Using Locations and Entities on OSHA Forms

The Department of Labor requires employers to maintain a separate OSHA 300 Log for each establishment that is expected to be in operation for one year or longer. This includes jobs and projects that are expected to last more than one year.
OSHA Establishment Maintenance
Here, Locations and OSHA Establishments are used to define the appropriate OSHA log. Map the 'Location' field to the appropriate OSHA Establishment. The OSHA report will use the OSHA Establishment information instead of the information from the Company Installation screen.
For backwards compatibility, a <BLANK> Establishment code is assumed to be the "main company." The main company reports will use the company name and address found on the Company Installation screen.

- ESTABLISHMENTS: Map Locations to OSHA Establishments to define the appropriate OSHA log.

- ENTITIES: Create Entity-specific OSHA Establishments to manage your various entities.

## Logging OSHA Incidents by Location

Use the 'Location' field to tag the incident to the proper OSHA Establishment. This information will be used when compiling the OSHA forms later.

## Calculating the Average Number of Employees and Hours

Spectrum can be used to calculate the average number of employees and hours worked last year.

1.  Navigate to Admin  >  Installation  >  Human Resources – Reporting tab.

1.  Click the Calculate button and enter the pay period year. When OSHA Establishments have been defined, the system will calculate the totals by OSHA establishment and display them in a confirmation window.

1. Click Continue to accept these results.
For those organizations that manually calculate the average number of employees and hours, enter the appropriate information in the OSHA section of the screen.
Note: About the Calculations: All checks in the specified calendar year are
 reviewed on an employee-by-employee basis. This calculation is based on the total
 checks for the employee divided by total checks expected for the employee for the
 year. If an employee is weekly, you'd expect 52 checks; if that employee only has
 13 checks for the year (based on a different pay period end date), then they would
 count as .25 of an employee. Similarly, if an employee works the entire year, they
 are calculated as one employee; if they work half a year, they are calculated as
 half an employee, and so on. All employees (including partial) are then added up
 to get the average employees during the year. The total is then rounded up to the
 nearest whole number.

## OSHA Forms

When running the OSHA Reports, the user will be prompted to assign an OSHA Establishment code for reporting purposes. When an Establishment code is entered on the OSHA Forms start screen, it will use the establishment's name, address and other key information on the forms.
Note: Note that the Entity prompt only
 appears when Entities are enabled.
Why didn't we just use the existing 'Location' field without OSHA Establishments?
OSHA defines establishments as those in operation over one year. As these 'Locations' will come and go, it was decided that the OSHA Classification option gave users more control of how these would be managed.
