# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "sentiment"
app_title = "Erpnext Ai Sentiment Analyzer"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Ai Sentiment Analyzer for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/sentiment/css/sentiment.bundle.css"
app_include_js = "/assets/sentiment/js/sentiment.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "sentiment.engine.on_document_submit",
        "on_cancel": "sentiment.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "sentiment.engine.daily_scheduled_sync"
    ]
}
