---
title: "Company Installation - Print Options Tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/installation/company-installation---properties-tab/company-installation---print-options-tab"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/installation/company-installation---properties-tab/company-installation---print-options-tab"
---

# Company Installation - Print Options Tab

Entries made here will serve as the default print options for the current company, unless operator overrides exist.
Important: Each Spectrum company requires a different entry in the User ID field because each Spectrum company uses a different SQL Server user for access to the database. Without the proper User ID, Crystal Reports will not return any data.
Fields/ButtonsDescriptions
User IDCrystal-Link User IDs will be maintained in the SQL Server database. Spectrum will auto-create the User ID in the form: <Company Code>+REPORTS+<4-digit number>.
If you wish to change the User ID, click the Reset button to use the next available User ID defined for this company in the database.

Company logoIf you would like to include your company logo on your Crystal Reports, enter the image file name here. Up to 30 characters are allowed. Once you enter a file name, the software will check to see if this file already exists in the server Crystal Reports directory.
If not, a warning message displays and you simply have to click the Upload button to copy the file to the proper location.
Multi-company users can specify the company logo image file that will display on all customer forms that reference this file.

Related information

- [Adding a Company Logo File to Report Headers](/en/spectrum/spectrum/system-administration/installation/adding-a-company-logo-file-to-report-headers)

- [Customize Reports with Your Company Logo File](/en/spectrum/spectrum/getting-started/reports--printing-overview/customize-reports-with-your-company-logo-file)
