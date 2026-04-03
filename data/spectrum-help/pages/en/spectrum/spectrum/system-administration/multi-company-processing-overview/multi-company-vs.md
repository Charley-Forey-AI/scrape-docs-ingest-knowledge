---
title: "Multi-Company vs. Departments | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-vs.-departments"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-vs.-departments"
---

# Multi-Company vs. Departments

Spectrum provides the capability of tracking the accounting records of multiple companies.
The multi-company feature allows a business to record revenue and expenses in separate companies, while combining that information on a single report whenever financial statements are printed. This feature also allows one company to issue checks while the expenses for those checks are charged to a separate company.
Careful consideration should be given, however, to the reasons behind using the multi-company feature. It is sometimes possible to achieve the same results through a departmentalized general ledger. You can record, track, and report multiple profit centers using either separate companies or departmental logic within a single company. There are advantages to both methods.

## Multi-Company

Financial statements for multiple companies can be reported as one company by using the "consolidated" financial statements feature. Even though a business's profit centers are not different fiscal entities, setting them up in separate companies could simplify transaction entry by having the desired GL accounts automatically default in each company. For example, the vendor expense and contract revenue account numbers can be defaulted for a specific company's direct job expense and revenue accounts; these accounts then default during transaction entry of AP invoices, Payroll departments, and Accounts Receivable invoices.
This method might not work well if there are several profit centers within a single job and it is necessary to have all the job's history available on one report. For example, if a job had expenses for both profit center #1 and profit center #2, setting up different companies would prevent all of the job's information for reporting on one report; the job's information would be in at least two separate companies.
Note: There may be a question as to which company records the
 revenue. This would effect the Contract Status Report for monthly entry of over/under
 billings.

## Departmentalized General Ledger

Setting up General Ledger Departments to define the different profit centers/divisions of a company works well for recording entries in a true fiscal entity (for example, a single company with a unique Federal ID number).
When setting up a job, it is possible to specify the division/department to which all of the job's expenses and revenue will be charged. This serves as a control to make sure that your staff enters the correct expense or revenue account. For example, suppose that the direct material account number is 515, and is preceded by either 01 or 02 to define the profit center, and that job #100 is set up as a division 01 job. In this example, entering an A/P invoice distributed to 02-515 would produce a warning that this account number does not match the job's division. The user would then realize the necessity of changing the account number for distribution of the invoice to 01-515.
Note: Users might not wish to enter general ledger accounts during transaction
 entries.

Related information

- [Multi-Company Setup](/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-setup)
