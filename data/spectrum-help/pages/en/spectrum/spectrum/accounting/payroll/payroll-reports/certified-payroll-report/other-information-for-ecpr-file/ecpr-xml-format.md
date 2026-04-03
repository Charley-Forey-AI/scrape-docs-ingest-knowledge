---
title: "eCPR XML Format | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/payroll-reports/certified-payroll-report/other-information-for-ecpr-file/ecpr-xml-format"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/payroll-reports/certified-payroll-report/other-information-for-ecpr-file/ecpr-xml-format"
---

# eCPR XML Format

Use Spectrum to create an XML export file that follows the 'eCPR' specifications for the State of
California Department of Industrial Relations.
This feature is accessed by selecting the new 'eCPR XML
file' option on the Certified Payroll Report starting screen, and contains information based on the
starting screen settings and other Job Cost and Payroll setup.
In the event that no work was performed for the week, California requires that a "statement of noncompliance" be filed. Clients should complete this statement using the iForm at the California DIR
website. This same iForm can be used to make corrections to previously submitted forms as well.

## Requirements

1. The union / wage code system be used to utilize the eCPR format. This functionality does not
work with the Non-Union Pay Groups.

1. Obtain a PWCR (Public Works Contractor Registration) number from the California Department
of Industrial Relations (DIR).

## Information Needed To Get Started

1. The DIR Project ID# for the project.

1. Your PWCR (Public Works Contractor Registration) number.

More information is available at the DIR website.

## Certified Benefit Program Maintenance

Use this screen to map add-ons, deductions and union fringe benefits to their respective 'Program type'.

1. Navigate to Payroll > Maintenance > Certified Benefit Program.

1. Select Build to begin.

1. Enter California for Job state eCPR for the XML format.

1. Select OK.

1. All of the various program types for eCPR will default on the screen.

1. Highlight the first program type and select Edit.

1. As this is the eCPR format, skip the 'Properties' tab in the Edit Benefit Program window.

1. On the Fringes tab, select all items to map to this program type.

1. On the 'Adds / Deducts' tab, select all items to map to this program type.

1. Select OK.

1. Continue assigning fringes, add-ons and deductions to all program types.

## Job Payroll Setup

Navigate to Job Payroll Setup and enter the Work state of California. Note: : The Work state entered here must be the same as was used as the Job state when
defining the Certified Benefit Program above. It is the state code that links this job to the correct benefit
program.

## Creating the eCPR XML File

Spectrum uses the Certified Payroll Report screen to create the XML file. Preview the report prior to creating the file and submitting it.
Select Preview to start compiling the file. Once complete, it downloads to your workstation.
This format does not use all of the available selections on the start screen. Only these fields are pertinent:

- Other XML Info

- Job number

- Pay period

- Work week ending date

- XML format – eCPR

Per California's specification, the eCPR file can only contain one job per file.
