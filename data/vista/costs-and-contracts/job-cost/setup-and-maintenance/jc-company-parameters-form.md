---
title: "JC Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form"
---

# JC Company Parameters Form

Use the JC Company Parameters form to set up the various control options for job cost processing in a company.
You must define the company setup options before you begin processing in Job Cost.
It is important that you take time to understand the effects of all choices for each set-up question. The options you select will affect how the programs work, and how other modules such as Payroll and Accounts Payable interact with Job Cost. It is suggested that this Company Setup program be restricted so only the system administrator has access to it.

- Audit Options - The Audit Options section on the Info tab controls whether
 adding, changing, or deleting information in selected forms will be recorded in
 the HQ Master Audit table. For more information, see [Audit Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form/field-definitions-jc-company-parameters-form#ID-00016f5b--en).

- Track changes to the form - The HQ Master Audit (HQMA) table contains a list of
 changes to records in the application. For example, if you change a setting on a
 company parameters form, a new entry is created in the HQMA table so that there
 is a record of the change. For more information, see [About Viewing the Master Audit Log.](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log)

- Interface Options - The GL Cost, GL Revenue, GL Close, and Material tab are used to set the interface levels for each Job Cost company, as well as specify the journal to update. For more information, see [About the GL Interface Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-gl-interface-options#concept-5868--en__concept-5868).

- Forecast Options - The Forecast tab allows you to distribute contract revenue
 and costs over the life of a job. For more information, see [Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options).

- Changing Settings after Startup - Once the control options have been defined for
 a Job Cost company in JC Company Parameters, it is rare that you should ever
 need to make changes to these setup options. Because changing an option may
 affect processing or stored information, changes should be made carefully. If
 you want to change an option but are unsure of its effect on existing data in
 the system, contact Viewpoint.Note: When
 setting up a company, the entry of invalid data in certain fields will cause
 a warning; however, entries will be allowed and you will be able to save the
 record. This primarily applies to (but is not limited to) required data such
 as the 'interface to' companies and journals, since it is sometimes
 necessary to set up the company information before you can set up the data
 being requested

- Workflow - This tab only applies if you have the Workflow module and use the [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) feature. Use this tab to define which workflows
 should be used for the specified company. The workflow processes set up here will
 override the workflow processes set up using the Workflow tab on the HQ Company Setup form. You can also set this
 up using the Assigned Companies tab on the WF Workflow Process form.
