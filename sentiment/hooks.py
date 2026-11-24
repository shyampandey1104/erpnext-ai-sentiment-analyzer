# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "sentiment"
app_title = "Erpnext Ai Sentiment Analyzer"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Ai Sentiment Analyzer - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/sentiment/css/sentiment.bundle.css"
app_include_js = "/assets/sentiment/js/sentiment.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Ai Sentiment Analyzer Entry": {
        "validate": "sentiment.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "sentiment.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "sentiment.tasks.hourly_sync"
    ],
    "daily": [
        "sentiment.tasks.daily_reconciliation"
    ],
    "weekly": [
        "sentiment.tasks.weekly_digest"
    ]
}
