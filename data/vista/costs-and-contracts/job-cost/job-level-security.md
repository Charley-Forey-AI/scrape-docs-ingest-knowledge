---
title: "Job Level Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/job-level-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/job-level-security"
---

# Job Level Security

If you are implementing data level security at the job level,
 you have the option to assign security groups to each job you set up in JC Jobs.

This can be very useful if you regularly set up new jobs, as it allows you to easily designate who will have access to the job without having to go to VA Data Security and set it up.
To implement this feature, in VA Data Security Setup:

- Check the Secure Datatype box for the
 'bJob' datatype.

- Designate a Default Security Group.

- Check the In Use flag for the JCJM (JC
 Jobs) table, as well as for any other tables to which you want job level
 security assigned.

- Regenerate views to activate data level security for the specified views/tables.

This enables the Security
 Grp input on the Jobs form, allowing you to designate the security group
 who will have access to information about the specified job.
Note: It is important to note that in addition to the security
 group specified in JC Jobs, access to information about the selected job will also be
 granted to the Default Security Group you specified in VA Data Security Setup, as well
 as to any other security groups that have been granted access in VA Data Security
 Access. 
[](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)VA Data Security Setup
