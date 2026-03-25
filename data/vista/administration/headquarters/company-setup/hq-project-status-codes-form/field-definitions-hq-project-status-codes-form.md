---
title: "Field Definitions: HQ Project Status Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/company-setup/hq-project-status-codes-form/field-definitions-hq-project-status-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/company-setup/hq-project-status-codes-form/field-definitions-hq-project-status-codes-form"
---

# Field Definitions: HQ Project Status Codes Form

The following is a list of field descriptions for the HQ
 Project Status Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project Status Code

Enter a code, up to 10 characters, that identifies the status of a potential project. The following is a list of suggested project status codes:

- Active

- Awarded

- Active Construction

- Closed

- Completed

- In Negotiation

- Not Awarded

## Description

Enter a description for this project status code, up to 60 characters.

## Status Order

The Status Order field on the HQ Project Status Code form allows you to specify a numerical order by which
 to sort project status codes and effectively, potential projects.
Enter a status order number (0-2,147,483,647) for this project status code. If you use this feature, any F4 lookup of
 project status codes will display the status codes by their status order.
The PC Potential Projects form will
 also use the status order to sort potential projects. Although the sort function applies
 to both the Info and Grid tabs, you may find it most useful when using the Grid tab. For
 example, say you use status orders of '1', '2', and '3'. When you access the potential
 projects grid, all projects assigned a status code with a status order of '1' will be
 listed first in the grid, followed by projects with a status order of '2', then '3'. If
 you assign the same status order to status codes that represent a specific stage in the
 life of a potential project, this will allow you to easily see all potential projects
 for a specific status. If you do not want project status codes and potential projects
 sorted by status order, leave this field blank. Project status codes and potential
 projects will be sorted in standard numerical/alphabetic order.

## Active Lookup

The Active Lookup field on the HQ Project Status Codes from determines whether the selected status code is included in project status lookups.
Check this box if this project status code is active and will be included in project status code lookups.
You might typically uncheck this box for status codes that you no longer use, but do not want removed from the system. If you uncheck this box, it only excludes the status codes from F4 lookups; it does not prevent you from using the code.
Note:Setting a project status code to inactive does not prevent its use when setting up potential projects in PC Potential Projects.
