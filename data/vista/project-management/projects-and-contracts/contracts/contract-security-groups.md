---
title: "Contract Security Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/contract-security-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/contract-security-groups"
---

# Contract Security Groups

If you are implementing data level security at the contract
 level, you have the option to assign security groups to each contract you set up in this
 program.
This can be very useful if you regularly set
 up new contracts, as it allows you to easily designate who will have access to the job
 without having to go to VA Data Security and set it up.
To implement this feature, in VA Data
 Security Setup, you must have:

- checked the Secure Datatype option for
 the 'bContract' datatype.

- designated a Default Security Group.


- check the In Use flag for the JCCM (JC
 Contracts) table, as well as for any other tables to which you want contract
 level security assigned.

- regenerated views to activate data
 level security for the specified views/tables.

This enables the Security
 Grp input on this form, allowing you to designate the security group who
 will have access to information about this contract.
Note: It is important to note that in addition to the
 security group specified on this form, access to information about this project is
 automatically granted to the Default Security Group you specified in VA Data Security
 Setup. In addition, access may be granted to additional groups in VA Data Security
 Access.
