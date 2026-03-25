---
title: "Remove, Cancel, or Complete Work Order Process Runs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/remove-cancel-or-complete-work-order-process-runs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/remove-cancel-or-complete-work-order-process-runs"
---

# Remove, Cancel, or Complete Work Order Process Runs

You can remove or cancel work order process runs or continue incomplete process runs using the SM Generate Work Order Summary Form.
A process run is created when you select to generate one or more preventative maintenance work orders using the SM Generate PM Work Orders form. Using the SM Generate Work Order Summary form, you can clear completed work order processes, cancel processes that have been requested or are being processed, or continue processes that were interrupted due to a power outage or system shutdown.

- To remove a single process run:

1. From the grid, select the completed or incomplete process to remove.

1. Click Remove Selected.The system removes the selected process run from the grid

- To remove all completed process runs:

1. Click Remove All Completed.The system removes the selected process run from the grid

- To cancel a process run that is in 'requested' or 'processing' status:

1. From the grid, select the process to cancel.

1. Click Cancel Selected Process.If the status is Requested, the system cancels the selected process run and makes the agreement service(s) available for selection in SM Generate PM Work Orders. If the status is Processing, the system cancels the process run, but leaves work orders already created intact. Only work orders not yet processed are made available again in SM Generate PM Work Order. The WO Generated column in the grid indicates how many work orders were generated before the process was canceled.

- To complete a process run that was interrupted due to a power or system failure:

1. From the grid, select the incomplete process to remove.This will be a process that does not have a Status of "Complete" and does not have errors.

1. Click the Continue Selected Process buttonThe system completes the process run.

- For process runs that were not completed due to errors encountered during work order generation:

1. From the grid, select the incomplete process to remove.This will be a process that does not have a Status of "Complete" and has errors listed in the Errors section (below the grid).

1. Click the Remove Selected button.

1. Correct the errors as applicable.

1. Run the SM Generate PM Work Orders for the selected service.

Related information

- [SM Generate Work Order Summary Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-work-order-summary-form)

- [SM Generate PM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form)
