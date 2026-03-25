---
title: "Use Notifier Queries for Workflow Notifications | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/use-notifier-queries-for-workflow-notifications"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/use-notifier-queries-for-workflow-notifications"
---

# Use Notifier Queries for Workflow Notifications

You can use Notifier queries to send notifications when using the review/approval workflow process for purchase orders, pending purchase orders, and subcontracts.

1. In WF Notifier Job Manager, set up the following Notifier jobs:

1. Set up a job for sending email notifications to approvers when purchase orders, pending purchase orders, and/or subcontracts are submitted for review approval. Associate the job with the PMDocumentApprovalList query.

1. Set up a job for sending email notifications to submitters when purchase orders, pending purchase orders, and/or subcontracts are approved, rejected, or still waiting for review. Associate this job with the PMReviewedDocumentList query.

For more information about setting up Notifier jobs, see [Set up a Notifier Job](/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job).

1. If you want to suppress the system's standard review/approval notifications, select the Using Review Workflow Notifier Queries checkbox in PM Company Parameters (Info tab).If you leave this checkbox unselected, reviewers and submitters will receive notifications via the Notifier jobs you set up, as well as the system's standard review/approval notifications.

Reviewers/approvers will now receive notifications via the applicable Notifier job listing all purchase orders and subcontract that they have been assigned to review and approve, and submitters will receive notifications for all purchase orders and subcontracts that they submitted that have been approved, rejected, or are still waiting for review.Note: Email notifications will exclude purchase orders, pending purchase orders, and subcontracts from the list of documents once they are interfaced.
