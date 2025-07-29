# Chameleon API Docs

A description of the routing and endpoints available on the Chameleon API

The documentation can be viewed locally by running any webserver in the `docs` directory.

For example, the following command will start a WEBrick server available on http://localhost:8000:

```
ruby -run -e httpd docs -p 8000
```

## Recent Documentation Improvements

### Webhook Documentation Enhancement (2025-07-26)

The webhook documentation has been significantly improved with comprehensive, realistic examples:

**Progress: 22/27 webhook examples updated (81% complete)**

#### ✅ Updated with Realistic Data:
- `tour.started`, `tour.exited`, `tour.completed`, `tour.button.clicked`
- `survey.started`, `survey.completed`, `survey.exited`, `survey.button.clicked`
- `response.finished`
- `helpbar.search`, `helpbar.answer`, `helpbar.item.action`
- `embed.started`, `embed.completed`, `embed.exited`, `embed.button.clicked`, `embed.snoozed`
- `demo.started`, `demo.finished`, `demo.reveal`, `demo.form.submitted`, `demo.email.added`
- `ping` (already had good examples)

#### 🔄 Still Outstanding:
- `tour.snoozed`
- `survey.snoozed`
- `helpbar.item.error`
- `alert.triggered`

#### Key Improvements Made:
1. **Privacy Protection**: Replaced real user data with fictional but realistic examples
2. **Field Variety**: Demonstrated different options across examples:
   - Multiple browsers (Chrome, Firefox, Safari, Edge, Opera)
   - Various device types (desktop, mobile, tablet)
   - International users (different languages, timezones)
   - Diverse roles (developer, designer, marketer, etc.)
   - Different plan types (free, startup, professional, business, enterprise)
3. **Complete Field Coverage**: Filled in previously missing/null fields with appropriate dummy data
4. **Educational Value**: Examples now show real-world use cases and different user personas

#### API Documentation Improvements:
- Enhanced examples in `profiles.md`, `companies.md`, `tours.md`, `surveys.md`
- Added comprehensive field examples showing different user states
- Updated with realistic but fictional data throughout
- Improved consistency in formatting and structure

### Testing Setup:
- Webhook testing performed using Pipedream endpoint
- Real webhook payloads captured and used as basis for improved examples
- Authentication testing completed with actual API responses

### Example Data Guidelines:
To ensure consistency across all documentation examples, follow these established patterns:

#### **ID Format Standards:**
- **Webhook IDs**: `5f3c4232c712de665632****` (24-character hex)
- **User IDs**: `5f3c4232c712de665632****` (matches webhook pattern)
- **Company IDs**: `5f3c4232c712de665632****` (matches webhook pattern)
- **UIDs**: Descriptive strings like `user_12345`, `embed_user_789`, `trial_user_456`

#### **Date/Time Standards:**
- **Year**: Use 2024 dates consistently
- **Format**: ISO 8601 format (`2024-MM-DDTHH:mm:ss.sssZ`)
- **Progression**: Earlier dates for `created_at`, later dates for `updated_at` and `sent_at`

#### **User Data Standards:**
- **Email Format**: `firstname.lastname@company.tld` 
- **Name Format**: `FirstName LastName` (proper case)
- **Company Domains**: Use realistic but fictional domains (`.io`, `.co`, `.com`)
- **Examples**: 
  - `sarah.johnson@techstartup.io`
  - `jennifer.clark@creativecorp.io`
  - `miguel.santos@startuptech.es`

#### **Privacy & Realism:**
- **Never use real user data** from production systems
- **Create diverse personas** with different:
  - Roles (developer, designer, product_manager, etc.)
  - Company sizes (1, 5, 12, 25, 50+)
  - Plans (free, startup, professional, business, enterprise)
  - Browsers (chrome, firefox, safari, edge, opera)
  - Locations/timezones (international diversity)
- **Maintain consistency** within related examples (same user across lifecycle events)

#### **Technical Standards:**
- **Browser Info**: Use realistic version numbers and OS combinations
- **Percentages**: Use varied values (15.88, 42.87, 72.45, 85.42, etc.)
- **Session Counts**: Realistic progression (3, 8, 15, 47, etc.)
- **Feature Flags**: Descriptive arrays like `["new_dashboard", "analytics_beta"]`

#### **Content Standards:**
- **Experience Names**: Descriptive and realistic (`"Dashboard Onboarding Tour"`)
- **Descriptions**: Clear, actionable copy that reflects real use cases
- **Button Text**: Common patterns (`"Next"`, `"Get Started"`, `"Try Demo"`)
- **URLs**: Use `app.chameleon.io` for dashboard links, realistic domains for external links

### Stylistic Improvements Analysis (2025-07-29)

Comprehensive evaluation of developer documentation completed to identify remaining improvement opportunities:

#### **Already Addressed in Recent PRs (2025-07-26):**
✅ **Enhanced API Examples**: Comprehensive, realistic data across profiles.md, companies.md, tours.md, surveys.md  
✅ **Privacy Protection**: Replaced real customer data with fictional examples  
✅ **Structural Consistency**: Fixed URL inconsistencies, standardized HTTP status headers  
✅ **Modern JavaScript**: Updated examples to ES6+ syntax  
✅ **Comprehensive Webhook Examples**: 22/27 complete with diverse user personas  
✅ **Complete Field Coverage**: Filled in previously missing/null fields  
✅ **Data Consistency Guidelines**: Established example data standards (above)

#### **Remaining Stylistic Improvement Opportunities:**

**Phase 1 (High Impact, Low Effort):**
1. **Navigation Enhancement**: Add breadcrumb navigation and "Back to Overview" links to all API pages
2. **Visual Callouts**: Add warning/tip/best practice boxes for important information
3. **Complete cURL Examples**: Add working cURL examples to remaining endpoints
4. **Cross-Reference Links**: Standardize anchor link formats across documentation

**Phase 2 (Medium Impact, Medium Effort):**  
5. **Troubleshooting Sections**: Add flowcharts for common issues (delivery not showing, webhook not firing)
6. **Quick Start Guide**: Create 5-minute getting started tutorial linking concepts together
7. **Schema Table Enhancement**: Add "Required" column and example values to all schema tables
8. **Error Response Standardization**: Consistent error table format with resolution guidance

**Phase 3 (High Impact, High Effort):**
9. **Interactive API Explorer**: Consider tools like Swagger/OpenAPI for hands-on testing
10. **Multi-language SDK Examples**: Add examples beyond cURL and JavaScript
11. **Video Tutorials**: For complex workflows like webhook setup and delivery troubleshooting

#### **Key Finding:**
Recent PRs have already addressed the major consistency and example quality issues. Remaining improvements focus on navigation, visual hierarchy, and developer onboarding rather than fundamental content quality.

### Next Steps:
1. Complete remaining 4 webhook examples (`tour.snoozed`, `survey.snoozed`, `helpbar.item.error`, `alert.triggered`)
2. Implement Phase 1 stylistic improvements (navigation, callouts, cURL examples)  
3. Consider Phase 2 improvements based on developer feedback and usage patterns
4. Monitor developer documentation usage to prioritize Phase 3 enhancements