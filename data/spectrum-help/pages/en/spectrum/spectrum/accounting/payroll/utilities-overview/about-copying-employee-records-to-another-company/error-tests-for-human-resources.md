---
title: "Error Tests for Human Resources | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/error-tests-for-human-resources"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/error-tests-for-human-resources"
---

# Error Tests for Human Resources

Spectrum performs the following tests to find errors
 associated with Human Resources setup when the "HR" module is present.
If any errors are found, they will display on the [Copy Employee Listing - Human Resources Exceptions](/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/copy-employee-listing---human-resources-exceptions) report.

- Verify that this employee's driver's license class code is not an invalid code in the destination company

- Verify that this employee's location is not an invalid location code in the destination company

- Verify there are all forms currently assigned to this employee that are present in the destination company

- Verify there are all training/certification codes currently assigned to this employee that are present in the destination company

- Verify there are all drug and alcohol test codes currently assigned to this employee that are present in the destination company

- Verify there are civil/legal/other activities codes currently assigned to this employee that are present in the destination company

- Verify there are all insurance codes currently assigned to this employee that are present in the destination company

- Verify that all insurance type codes associated with insurance codes assigned this employee that are present in the destination company

-  Verify that all insurance scheme codes associated with insurance codes assigned this employee that are present in the destination company

- Verify that any claim type codes associated with Safety/OSHA incidents for this employee are present in the destination company

- Verify that any claim status codes associated with Safety/OSHA incidents for this employee are present in the destination company

- Verify that any injury type codes associated with Safety/OSHA incidents for this employee are present in the destination company

-  Verify that any body part codes associated with Safety/OSHA incidents for this employee are present in the destination company

- Verify that any injury cause codes associated with Safety/OSHA incidents for this employee are present in the destination company

- Verify that no company-specific Incident user-defined fields have been assigned data in Safety/OSHA incidents for this employee

- Verify there are no tracking items currently 'checked out' to this employee in
 the current company (in Human Resources > Item Management)

- Verify that this employee is not a member of an 'active' crew in the current
 company (in Human Resources > Crew Assignment)

- Verify that this employee is not in-progress for 'termination' in the current
 company (in Human Resources > Termination)

Validation is NOT performed to evaluate whether the employee's job title
 is valid in the destination company. Instead, employees are always copied regardless of
 title. After completing the update, the Administrator can use the Human Resources > Utilities > Build Job Titles update to conveniently expand the list of valid job titles in the
 destination company.
