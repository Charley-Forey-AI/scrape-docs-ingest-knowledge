---
title: "Worker's Compensation Limit Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/workers-compensation-limit-hierarchy"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/workers-compensation-limit-hierarchy"
---

# Worker's Compensation Limit Hierarchy

The software calculates the Worker's Compensation Limit by
 looking to the Limit method for the
 specified Worker's compensation code + State to determine the start date for the limit
 calculation.
For more information, see [Worker's Compensation Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance).

- If the Limit method = None – no limit (the system calculates worker's comp on every time card line based on the rate of that code+state)

- If the Limit method = Pay period – the system calculates the worker's comp limit from previous time cards in the current pay cycle

- If the Limit method = Annual - the system reads the MM/DD of the 'Policy start date'

- If the Limit method = Quarterly - the system reads the MM/DD of the 'Policy start date' and determines the most recent quarterly policy start date by comparing the policy start date and the 'Check date'. If the quarterly MM/DD is greater than or equal to the MM/DD of the 'Check date' for this pay cycle, then the system looks for checks dated since that MM/DD in the prior year, inclusive.

- If the Limit method = Monthly - the system reads the DD of the 'Policy start date' , if the DD is greater than or equal to the DD of the Check date for this pay cycle, the system looks for checks dated since that DD in the prior month, inclusive.

- For Regular and Manual Checks: For each time card line, the system calculates the worker's compensation based on the applicable 'limit settings' when a rate '$100 code has been assigned to the time card line.
