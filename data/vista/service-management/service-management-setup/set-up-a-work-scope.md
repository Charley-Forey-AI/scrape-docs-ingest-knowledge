---
title: "Set up a Work Scope | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-a-work-scope"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-a-work-scope"
---

# Set up a Work Scope

Work scopes allow you identify common problems reported by customers, maintenance work, or services you provide, such as installations, or other small jobs.
 You will set up work scopes using the SM Work Scopes form.
The following instructions detail how to set up work scopes:

1. From the Programs menu of Service Management, launch the SM Work Scopes form.

1. In the Work Scope field, enter a name or code to represent the scope of work you are setting up.

1. Enter a description of the work scope in the Description field.

1. In the Priority field, enter High, Med, or Low to represent the priority of this work scope. You can also select the priority via the F4 lookup.

1. Use the Details field to enter information about the work scope (e.g. special needs, directions, measurements, etc.).

1. In the Default Phase field, enter the phase to use as the default when adding this work scope to a job work order (in SM Work Orders). Note: Assigning a phase here does not prevent you from using the work scope on a customer work order. The system will only default the phase for job work orders.

1. Save the record.

1. [Set up split revenue entries](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue).

1. Select the Prevent Scope Auto Close when Billing checkbox to prevent the currently selected scope from automatically being closed when billing.Note: Selecting this checkbox overrides the Auto Close Work Order on Final Bill checkbox in SM Company Parameters. The system will not auto-close any fully-billed work order scope that is assigned this work scope. You will need to close the work order scope manually.

Once you set up a work scope here, you can assign it to a quote sequence (in SM Work Order Quotes) or a work order sequence (in SM Work Orders).
