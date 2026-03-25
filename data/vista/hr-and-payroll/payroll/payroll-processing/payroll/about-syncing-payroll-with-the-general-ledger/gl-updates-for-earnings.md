---
title: "GL Updates for Earnings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/gl-updates-for-earnings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/gl-updates-for-earnings"
---

# GL Updates for Earnings

Payroll and Job Cost department files contain the General
 Ledger accounts to which payroll costs will be posted.
 Additionally, if using the Equipment
 Management module, the EM department file will be used for mechanics in the same manner
 that Job Cost is used for time posted to a job.

Non-Job Payroll Posting
The Payroll department file is always used when the timecard entry is
 not posted to a job or a piece of equipment. The Payroll departments (set up in the PR
 Departments) define the GL accounts to be debited for payroll costs. Each employee is
 assigned a payroll department code in the PR Employees form. If you need to post an
 employee’s time to another GL code, the department may be overridden in the Payroll
 posting form. Each earnings code is set up in PR Earnings Codes with an Earnings Type.
 The earnings types are assigned GL codes in PR Departments.
Payroll Earnings Posted to Jobs and Equipment
For payroll timecard entries posted to jobs or equipment, you can
 choose to have the JC Department or EM Department used for payroll rather than the PR
 Department. To set up either option, enter the JC or EM GL account in the JC Fixed Rate
 GL Account or EM Fixed Rate GL Account fields in PR Departments.
When using these options, the following path is followed to determine the GL account to
 which the direct payroll earnings are debited:

- The earnings codes are assigned to a JC cost type (typically Labor) and an
 earnings type in PR Earnings Codes. The labor cost type for mechanics is set up
 in EM Company Parameters.

- General Ledger accounts are assigned by cost type in the JC and EM Department
 forms.

- Overrides by earnings type are set up in JC Departments. As an example, you
 might want all earnings to go to the labor cost type, but Subsistence to go to a
 separate GL account.

- Overrides by cost code are set up in EM Departments and will be used for
 mechanics’ payroll, as well as other costs.

If you leave these fields blank, timecard lines that have a job or mechanic entries
 assigned will result in an error when you do the Ledger Update.
