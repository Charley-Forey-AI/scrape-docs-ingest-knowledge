---
title: "About Security Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-security-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-security-groups"
---

# About Security Groups

You can implement data level security for Job Cost contracts to control who has access to which contracts/jobs.
If you are implementing data level security at the contract level, you can assign security groups to each contract you set up in the JC Contracts form. This can be very useful if you regularly set up new contracts, as it allows you to easily designate who will have access to the job without having to set it up in [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form).
To implement this feature, in VA Data Security Setup, you must:

- select the Secure Datatype option for the 'bContract' datatype

- designate a Default Security Group

- select the In Use flag for the JCCM (JC Contracts) table, as well as for any other tables to which you want contract level security assigned

- regenerate views to activate data level security for the specified views/tables

Once you complete the security, the Security Grp field on the JC Contracts form (Info tab) is enabled, allowing you to designate the security group who will have access to information about the selected contract.

Note: It is important to note that in addition to the security group specified for a contract, access to information about this contract is automatically granted to the Default Security Group you specified in VA Data Security Setup. In addition, access may be granted to additional groups in VA Data Security Access. For more information, see [Assign Security to Secured
 Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-security-to-secured-datatypes).
