---
title: "Using Locations and Establishments in Vets Reporting | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-and-establishments-in-vets-reporting"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-and-establishments-in-vets-reporting"
---

# Using Locations and Establishments in Vets Reporting

The Veterans report (Vets-4212 form) is compiled 'by establishment' when the company has multiple locations. When the 'Multiple locations' is enabled, the report will provide information about employees at the hiring location as well as at headquarters. It also supports multiple entities and their hiring locations as well.
Checkboxes on the Veterans report are dependent on the following setup:
 Single EstablishmentIs marked when the 'Report by location' checkbox is not selected on Human Resources Installation.
Multiple Establishment – HeadquartersThis option is selected when both the 'Report by location' and 'Headquarters for EEO veteran reporting' options are selected.
Multiple Establishment – Hiring LocationThis option is selected when both the 'Report by location' is selected and 'Headquarters for EEO veteran reporting' is not selected.

- ESTABLISHMENTS: Spectrum uses Locations to track establishments for Veterans reporting purposes.

- ENTITIES: Use a combination of Locations and Entity File Maintenance.

## Enable Reporting by Establishment

 To enable reporting by establishments, select the Report by location checkbox on Human Resources Installation > Reporting tab.
 As the company's contractual relationship with the Federal Government may vary from year to year (as well as by entity), this information is only used as a default. The type of organization will default from here on the Veterans report start screen, but can be overridden as needed.
Report by location?
Selecting this checkbox tells the system to create the 'Multiple Establishment' versions of the Veterans report. It will determine the type of report based on the way you set up Locations.
Important: Always select the Report by location checkbox when Entities are enabled.

## Entity File Maintenance

Define the appropriate information on the EEO Veteran Reporting tab in Entity File Maintenance. Information entered here will be used instead of what is on Human Resources Installation.

## Location Maintenance

Use Location Maintenance to store the address of each location.
OSHA establishmentUse this field to assign this location to an OSHA establishment code.
Headquarters for veteran reporting?This checkbox is only applicable for companies that have flagged the Human Resources Installation screen to Report by location. For Multiple Establishments, the Veterans report will use this flag to determine whether or not this location is a headquarters or a hiring location.

## Veteran Employment Report

Note: The Entity prompt only appears when Entities are enabled.
In earlier versions, the start screen had sections to indicate the parent company and hiring locations. There also was a number of permanent employees field. These have been removed as the system will calculate these values accordingly.

## Report Compilation

The report will identify entity-specific employees and location-specific employees using payment history for the year as well as employee's veteran settings.

- Entity filtering only occurs when entities are enabled. Filtering is accomplished by reading the 'Entity' column in the Payment History Table while the update reads for employees that were paid within the date range.

- Location filtering only occurs when the 'Report by location' checkbox is selected on Human Resources Installation. Filtering is accomplished using the 'Location' column in the Employee Master Table.

Having identified the employees to include on the report, the system then calculates the maximum and minimum number of employees by entity and by location.
Next, it reads the employee's hire date to determine whether or not to tally them for both 'All Employees' and the 'New Hires' columns or just the 'All Employees' column.
Once it knows the columns to place the employee, it then uses their EEO code to determine their applicable row.
