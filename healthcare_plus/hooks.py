# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "healthcare_plus"
app_title = "Healthcare Plus"
app_publisher = "Ivan Ray Altomera"
app_description = "Healthcare module with a plus!"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "irayspacii@gmail.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Patient-healthix_sb",
                    "Patient-healthix_patient_id",
                    "Patient-insurance_code",
                    "Patient-insurance_provider",
                    "Patient-insurance_details",
                    "Patient-insurance_scheme_name",
                    "Patient-insurance_scheme_code",
                    "Payment Entry-patient",
                    "Payment Entry-hp_insurance_provider",
                    "Payment Entry-hp_insurance_coverage",
                    "Payment Entry-hp_insurance_section",
                    "Sales Invoice-hix_billed_by",
                    "Sales Invoice-party_type",
                    "Patient-patient_number",
                    "Patient-nhif_number",
                    "Patient-member_number"
                ]
            ]
        ]
    }
]



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/healthcare_plus/css/healthcare_plus.css"
# app_include_js = "/assets/healthcare_plus/js/healthcare_plus.js"

# include js, css files in header of web template
# web_include_css = "/assets/healthcare_plus/css/healthcare_plus.css"
# web_include_js = "/assets/healthcare_plus/js/healthcare_plus.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Payment Entry": "public/js/payment_entry.js",
    # "Sales Invoice": "public/js/sales_invoice.js"
}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "healthcare_plus.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "healthcare_plus.install.before_install"
# after_install = "healthcare_plus.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "healthcare_plus.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
    "Payment Entry": {
        "on_submit": 'healthcare_plus.utils.generate_sales_invoice',
        "validate": 'healthcare_plus.utils.set_rate_to_settings'
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"healthcare_plus.tasks.all"
# 	],
# 	"daily": [
# 		"healthcare_plus.tasks.daily"
# 	],
# 	"hourly": [
# 		"healthcare_plus.tasks.hourly"
# 	],
# 	"weekly": [
# 		"healthcare_plus.tasks.weekly"
# 	]
# 	"monthly": [
# 		"healthcare_plus.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "healthcare_plus.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "healthcare_plus.event.get_events"
# }

