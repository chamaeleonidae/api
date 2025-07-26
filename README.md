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

**Progress: 13/27 webhook examples updated (48% complete)**

#### ✅ Updated with Realistic Data:
- `tour.started`, `tour.exited`, `tour.completed`, `tour.button.clicked`
- `survey.started`, `survey.completed`, `survey.exited`, `survey.button.clicked`
- `response.finished`
- `helpbar.search`, `helpbar.answer`, `helpbar.item.action`
- `ping` (already had good examples)

#### 🔄 Still Outstanding:
- `tour.snoozed`
- `survey.snoozed`
- `helpbar.item.error`
- `embed.*` events (started, completed, exited, button.clicked, snoozed)
- `alert.triggered`
- `demo.*` events (started, finished, reveal, form.submitted, email.added)

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

### Next Steps:
1. Continue collecting webhook payload examples for remaining event types
2. Add consistent navigation and cross-references across documentation
3. Consider adding more comprehensive API response examples
4. Complete webhook documentation when more event examples are available