---
title: "SM Labor Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-codes-form"
---

# SM Labor Codes Form

Use the SM Labor Codes form to set up labor codes that
 identify repairs or resolutions that commonly occur when performing service work.

When capturing labor on a work order, you can assign labor codes to the work completed labor entries to identify what repairs or resolutions occurred.
Some examples of labor codes might be:

- Pipe repair

- Preparation work

- Installation

- Inspection

- Maintenance

## JC Cost Type

 If you will be using labor codes when capturing labor costs on job work orders, you have the option to assign a default JC cost type. When you assign the labor code to a work completed labor line, the JC Cost Type defaults in automatically. The system uses this cost type and the phase specified on the work order sequence to post costs to Job Cost (via the JC Cost Detail table).

- JC cost types are only used when capturing work completed labor on job work orders. If you add the labor code to a customer work order, the cost type is ignored.

- You can assign any phase to a work scope; however, when adding work completed labor lines to a job work order, the following applies:

- If the job is locked—that is, you selected the Phases on this job
 are locked checkbox in JC Jobs)—the cost
 type must be set up in JC Job Phases for the phase specified
 on the work order sequence. Otherwise, the system displays a
 warning and will not allow you to save the work completed
 record until you specify a valid job/phase cost type.

- If the job is not locked, the cost type must be set up in JC Job Phases or JC
 Phases for the phase specified on the work order sequence;
 otherwise, the system displays a warning and will not allow
 you to save the work completed record until you specify a
 valid phase cost type.

Click the link below for more information about using this form.
[Set Up a Labor Code](/en/vista/vista/service-management/service-management-setup/set-up-a-labor-code#task-6993--en__task-6993)
