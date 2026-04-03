---
title: "AASHTOWare XML Format | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/certified-benefit-program-maintenance/aashtoware-xml-format"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/certified-benefit-program-maintenance/aashtoware-xml-format"
---

# AASHTOWare XML Format

Use Spectrum to create an XML export file that follows the AASHTOWare specifications.
Access this feature by selecting AASHTOWare XML file on the Certified Payroll Report starting screen. It contains information based on the starting screen settings and other Job Cost and Payroll setup.
AASHTOWare's Civil Rights and Labor (CRL) application is used to manage certified payrolls for these
agencies and is developed by the American Association of State Highway Transportation Officials
(AASHTO).
Use this format only if applicable.

## Requirements

It is a requirement that the union and wage code system be used to utilize the AASHTOWare format.
Note: Non-Union Pay Groups are not supported for AASHTOWare reporting.
Unions are required as the union code references the Certified craft code. Wage codes are required as
they reference the Certified labor code.

## Information Needed To Get Started

Before you begin, you will need to obtain the following from the DOT/agency:

- The Civil Rights and Labor (CRL) website link

- Your user name and password

- Your Contractor/Vendor ID code

- The Contract #

- The Project #

- The Craft and Labor codes used

- Benefit program information

If you are already submitting files using the XML Spreadsheet converter, see [Mapping the AASHTOWare System to Spectrum](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/certified-benefit-program-maintenance/mapping-the-aashtoware-system-to-spectrum).

## Certified Benefit Program Maintenance

Use this screen to map add-ons, deductions and union fringe benefits to their Program type.

1. Navigate to Payroll > Maintenance > Certified Benefit Program.

1. Select Build.

1. Enter Job state and XML format of AASHTOWare.

1. Select OK.

1. All of the various program types appear on the screen.

1. Highlight the first program type and select Edit.

1.  Enter program information on the Properties  tab.Note: Even though the DOT/agency typically requires that these fields all be completed, they are not required entry fields in Spectrum. This way you can enter the information you have, and return later if needed to enter remaining requirements.

1. On the Fringes tab, select all items to map to this program type.

1. On the Adds / Deducts tab, select all items to map to this program type.

1.  Select OK.

1. Continue assigning fringes, add-ons, and deductions to all program types.

## Union File Maintenance

By union, enter the Certified craft code. These numerical codes come from the state or agency to
which the payroll is being submitted. Enter only the code in this field, as entry of the description will
cause the XML file to error out.Note: : The AASHTOWare system provides an Excel spreadsheet option of creating the XML file. Obtain a
copy from your state and navigate to the Craft tab. The codes needed are displayed. Enter only the codes in this field; including the description in this field will result in the file being
rejected.

## Creating the AASHTOWare XML File

Within Spectrum, the Certified Payroll Report screen is used to create the XML file. Preview the report prior to creating the file and submitting it.
Select XML format – AASHTOWare and select Preview to start compiling the file. Once complete, it
downloads to your workstation.
This format does not use all of the available selections on the start screen.
 When creating the AASHTOWare format, enter the Job number, Pay period and Work
week ending date. Select whether you want to include the employee's address and full social security
number. Also indicate how fringes are paid, plus any exception information. Complete the Contact
email field in the Other XML Info button. All other start screen fields are ignored.
Per AASHTOWare's specification, the XML file can only contain one job per file. You will receive an error
message when two or more jobs are entered on the start screen.
The Other XML Info button includes the following:
Contractor IDEnter your Contractor's Vendor ID number from the state.
License typeLeave blank, as this field is not used with the AASHTOWare format.
License #Leave blank, as this field is not used with the AASHTOWare format.
Insurance #Leave blank, as this field is not used with the AASHTOWare format.
Contracting agencyLeave blank, as this field is not used with the AASHTOWare format.
Contact emailEnter the email address of the contact at your company.

## File format

The file is automatically named Job_MMDDYY.xml.
