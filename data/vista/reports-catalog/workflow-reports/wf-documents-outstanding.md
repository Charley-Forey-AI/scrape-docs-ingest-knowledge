---
title: "WF Documents Outstanding | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/workflow-reports/wf-documents-outstanding"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/workflow-reports/wf-documents-outstanding"
---

# WF Documents Outstanding

You can use the WF Documents Outstanding report by selecting Workflow > Reports > WF Documents Outstanding.
Summary:
The WF Documents Outstanding report returns approval process details and status for documents that have been submitted for approval but have not yet finished the entire process. From the document status of 'No Activity' (document submitted for approval, but no activity has occurred in any step) to 'Approved-Unprocessed' the report will display details regarding each step for each item in the submitted document.
Display\Parameter Restrictions:
Since this is a WF report and WF is not bound by company, the Company report parameter is blank by default. Also, the report is able to see steps where all or some of the members are optional approvers. If the step has all optional approvers, the step is still required and the report will just flag the first pending approver as the next member scheduled to approve the document. If the step has a mix of optional and required members then the report will flag the next required member as the next approver.
Data Sources:

- HQ Roles List

- WF Approval Process Details

- Workflow Documents My Initiated Outstanding (PM Work Center Inquiry)

- Workflow Documents All Outstanding (PM Work Center Inquiry)

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Initiated By
Click the Field Lookup
 button or press F4 to select the initiated by
 person or leave blank for all.

Next to Approve
Click the Field Lookup
 button or press F4 to select the next to
 approve person or leave blank for all.

Process Used
Click the Field Lookup
 button or press F4 to select the process used
 or leave blank for all.

Show (N)o Activity, (P)atrial, (R)ejected, or (A)ll Statuses
Enter N, P, R, or A.
