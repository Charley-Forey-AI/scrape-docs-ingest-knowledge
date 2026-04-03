---
title: "Using Locations on the EEO Report | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-on-the-eeo-report"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/using-locations-on-the-eeo-report"
---

# Using Locations on the EEO Report

The EEO Employment Report is compiled by 'establishment' when the company has multiple locations.

- ESTABLISHMENTS: Spectrum uses Locations to track establishments for OSHA reporting.

- ENTITIES: Use a combination of Locations and Entity File Maintenance to define your entities.

## Enable Reporting by Establishment

To enable reporting by establishments, select the 'Report by location' checkbox on Human Resources Installation > Reporting tab.
Report by location?
Selecting this checkbox tells the system to create one of the 'Multiple Establishment' versions of the EEO and Veterans report. It will determine the type of report based on the way you set up Locations.
Important: Always select the 'Report by location' checkbox when Entities are enabled.

## Entity File Maintenance

Define the appropriate information on the EEO Veteran Reporting tab in Entity File Maintenance. Information entered here will be used on reporting for this entity instead of what is found on Human Resources Installation.

## Location Maintenance

Use Location Maintenance to store the address of each location. This information will be used on the EEO report instead of that found on Company Installation.
OSHA establishment
Use this field to assign this location to an OSHA establishment code.

Headquarters for veteran reporting
This checkbox is only applicable for companies that have flagged the Human Resources Installation screen to 'Report by location'. For Multiple Establishments, the Veterans report will use this flag to determine whether or not this location is a headquarters or a hiring location.

## Job Openings

Use the Location field to assign the job opening to a specific establishment for EEO reporting.
COST CENTERS: The cost center in Job Openings is used when the EEO report is run for Applicants. Cost center security also restricts operator access to keep users out of disallowed job openings. In the event that the job opening does not have a cost center, it will be available for everyone to select it.

## Applicant Main Properties

The Location field here can be used to record where the application was received. It is not used for EEO Employment reporting.
COST CENTERS: All job openings that the applicant has applied to will display, but cost center security will prevent a user from editing or removing a job opening that they are not authorized for.

## EEO Employment Report

When the HR Installation > Reporting screen is set to report by location, the EEO Employment report will change and print by Establishment (aka locations). When Entities are enabled, the report will also provide entity-specific information.
Note: Note that the 'Entity' prompt only appears when Entities are enabled.

## Report Compilation

The employee format of the report supports both entity and location tracking. The employee version of the report will compile first for entity filtering and then by locational grouping.

- Entity filtering only occurs when entities are enabled. Filtering is accomplished by reading the 'Entity' column in the Payment History Table while the update reads for employees that were paid within the date range.

- Location filtering only occurs when the 'Report by location' checkbox is selected on Human Resources Installation. Filtering is accomplished using the 'Location' column in the Employee Master Table.

Having identified the employees to include on the report, the system then calculates statistical information on them as described below.

## Entity + Location + EEO Classification + Race + Gender

Employees and applicants without an EEO classification are not included in the report.
The applicant version of the report compiles information in the same manner. It first compiles by entity and then by location.

- Entity filtering only includes job openings assigned a cost center that belongs to that entity code.

- Location filtering uses the job openings assigned location code.

Having identified the job openings to include on the report, the system then calculates statistical information on the applicants who have applied for these openings.
Important: Even though there is both 'EEO' and 'Location' codes in the Applicant screen, they are not used as the reporting location. Instead the 'EEO' and 'Location' codes of the job opening are used. This means that one applicant who has applied for multiple openings would be counted twice in the consolidated totals. This only applies to the applicant version of the report.
