---
title: "Frequently Asked Questions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/frequently-asked-questions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/frequently-asked-questions"
---

# Frequently Asked Questions

The Frequently Asked Questions section provides quick access to a list of frequently asked questions related to the Info-Link module.

## I've created my Info-Link query. Why am I not getting any data or only some of my
 data?

Typically this is due to an error in the link properties. Microsoft
 Excel, Access and Seagate Crystal Reports all use a linking wizard that attempts to
 automatically establish links between tables you are using in your query/report. These
 are very fallible and often link columns that should not be connected. In both Excel and
 Access, the links are represented as lines drawn between the tables attached to specific
 columns in those tables. Seagate Crystal Reports also displays them similarly, however
 you need to open Seagate Crystal Reports > Database > Visual Linking Expert to see them. Often, there will be extraneous links that can and should be
 deleted.
There are two options for solving unwanted link issues:
- Delete the extra links.
--OR--
- Modify the properties of the links.

- In Excel and Access, right-click on the link.

- In Crystal, click the link and then click
 Options to access the join properties.
If you need additional assistance with these settings, contact
 either Microsoft or Seagate. Additionally, the Help files in Microsoft Excel,
 Access and Crystal Reports offer useful information regarding link properties and
 issues.

## I'm trying to design a report/query. Where does Spectrum keep the data?

There are two primary ways to find where the data is located in Spectrum.
Option One

- On the Site Map, go to Info-Link > Table Directory Inquiry.

- In the Module field, enter the two-digit
 module abbreviation.

- In the Search table name field, enter
 the partial table name. Leave this field blank to view the system default of
 ALL.

- Double-click on the table name you are searching for to view
 the linked column variables.

- Click the Listing button to display
 printing options.

Option Two

- On the Site Map, click Info-Link > Function/Table Cross Reference Report.

- Enter the function name, or press F4 to
 use the Search Spectrum
 Functions window to locate the screen by Module and Category.

- Select the Include related functions checkbox.

- Click the Preview button to view the
 report on your screen.
If neither of these options works, you may call Viewpoint
 Customer Support (1-800-352-8939) for assistance. Please remember that we can
 assist you in finding the data you are looking for, but cannot assist you in
 designing the report you are working on.
