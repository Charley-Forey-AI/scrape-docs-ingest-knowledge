---
title: "PM Copy Project Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-form"
---

# PM Copy Project Form

Use this form to use an existing project to create a new one. This can save you time if you need to create a new project and a similar one already exists.
Once you specify a source project from the active
 company, you must then enter information about the destination project and contract.
 Initially, the contract and its description will default from the new project and
 description; however, you can enter any contract number and description desired. You
 also have the option to assign an existing contract to the job, as long as the contract
 is open or pending. Note: If you are using data level security for jobs and/or
 contracts, the destination job and contract will inherit the security groups
 assigned to the source project and contract. You may override these assignments in
 the related programs. See Related Topics below for information about Security Groups
 at the project and/or contract level.

Once the copy process is complete, a message displays telling you the job was
 successfully copied. If an error occurred during the copy process, a message displays
 with information about the error. A second message is then displayed informing you that
 the copy was not completed.

## Data Groups

The ‘Groups’ section is an informational display showing the vendor, customer, tax,
 phase, and material groups for the source and destination companies.
If the source and destination companies
 differ, chances are the data groups will also differ. This can create problems when
 copying data that relies on the specific data groups for valid information. For
 example, if the phase groups differ, then phases being copied from the source
 project may not exist in the destination company. For this reason, the system does
 not specific tables and the data within those tables when certain data groups
 differ. The following describes what information is not copied when the source and
 destination data groups differ:
Group
Data Not Copied

Vendor
Vendor, firm, firm
 contact, or project firms

Customer
Affects only the
 customer assigned to destination contract. If you do not specify
 a customer for the new contract, and the customer assigned to
 the existing contract does not exist in destination company, the
 customer will not be copied to the new contract.

Tax
All data in
 tax-related fields

Phase
Phase and cost type
 information, which includes project markups, job phases, cost
 type headers, subcontract detail, material detail and change
 order detail.

Material
Material code - only
 applies when copying material detail. Material detail records
 are copied without their associated material codes.

Note: If the PR companies differ between the source
 and destination PM companies, PR-related data in the project master table is not
 copied.

## Information to Copy

The Copy Amounts section allows you to specify whether to copy all amounts (original
 and current estimates) or to copy the original estimates only. You can also specify
 to not copy any of the amounts to the new project.
The Additional Information to Copy
 section provides options for copying project-related detail, such as subcontract
 detail, material detail, project firms, and change order detail. If data groups
 differ between source and destination companies, some of these options will be
 grayed out.
Once you specify what data to copy and
 select Copy, the system copies information from the source project (in PM Projects)
 to the new project, and sets up the new contract in PM Contracts. User-defined memos
 existing for the source contract/contract items, project, project phases and/or cost
 type detail are also be copied to the new project. Remaining information as
 specified in the Additional Information to Copy section is also copied. Note:

- If phases are locked for the source project, they will also be locked
 for the destination project.

- With the exception of the PR State Code, the payroll information defined
 for the source project (PR Info tab in PM Projects) will not be copied
 to the new project. You must set that information up manually.

- If you do not select to copy contract item retainage, the new contract
 items will default the retainage percent defined for the contract during
 the copy process.

Related concepts

- [Contract Security Groups](/en/vista/vista/project-management/projects-and-contracts/contracts/contract-security-groups)

Related tasks

- [Set up Job Level Security](/en/vista/vista/project-management/projects-and-contracts/projects/set-up-job-level-security)
