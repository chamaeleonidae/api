# Bulk Tagging

Bulk tagging is helpful to update your account with a new tagging system or daily/weekly correctness checks for tags

Tags can be used for organization, Alerts, Rate limiting, and more which means having the right tags helps your team and your end-users

> These examples are in Ruby, which you can run with `irb` in the terminal or claude can help translate them


```ruby
require 'csv'
api_key = YOUR_API_KEY # from https://app.chameleon.io/settings/tokens
```

### Example: List all the Tag IDs and names

```ruby
response = JSON.parse(`curl 'https://api.chameleon.io/v3/edit/tags?limit=500' -H 'X-Account-Secret: #{api_key}'`.chomp)
tags = response['tags']
puts "Found #{tags.size} tag#{tags.size == 1 ? '' : 's'}:"

puts CSV.generate_line(['Tag ID', 'Tag name'])
tags.each do |tag|
  puts CSV.generate_line([tag['id'], tag['name']])
end; nil
```

### Example: Tag four Tours with exactly these three tags each

- A Tour, Microsurvey, and Embeddable are all `model_type=Campaign`
- Use `tag_names` to remove any current tags and add exactly the tag_names tags

```ruby
tag_names = ['Onboarding', 'Onboarding 2029-02', 'Company size bucket: Medium'] # Examples
tour_updates = [
  { model_type: 'Campaign', model_id: TOUR_01_ID, tag_names: tag_names },
  { model_type: 'Campaign', model_id: TOUR_02_ID, tag_names: tag_names },
  { model_type: 'Campaign', model_id: TOUR_09_ID, tag_names: tag_names },
  { model_type: 'Campaign', model_id: TOUR_11_ID, tag_names: tag_names },
]

body = { updates: tour_updates }.to_json
response = JSON.parse(`curl -X POST 'https://api.chameleon.io/edit/v3/tags/bulk' -H 'X-Account-Secret: #{api_key}' -H 'Content-Type: application/json' --data '#{body}'`.chomp)

if response['code'] # code is presented back with error states
  puts "Updating encountered an error code=#{response['code']}, messages=#{response['messages'].join(', ')}"
else
  puts "Tags applied successfully"
end
```


### Example: Tag one Tour and one Launcher

- Use `tag_name` with a `+` to add the tag and `-` to remove a tag

```ruby
mixed_updates = [
  { model_type: 'Campaign', model_id: TOUR_01_ID, tag_name: '+Onboarding 2029-02' },
  { model_type: 'List', model_id: LAUNCHER_01_ID, tag_name: '-Self-serve' },
  { model_type: 'List', model_id: LAUNCHER_01_ID, tag_name: '+Onboarding 2029-02' },
  { model_type: 'List', model_id: LAUNCHER_01_ID, tag_name: '+Self-serve Onboarding' },
]

body = { updates: mixed_updates }.to_json
response = JSON.parse(`curl -X POST 'https://api.chameleon.io/edit/v3/tags/bulk' -H 'X-Account-Secret: #{api_key}' -H 'Content-Type: application/json' --data '#{body}'`.chomp)

if response['code']
  puts "Updating encountered an error: #{response['messages'].join(', ')}"
else
  puts "Tags applied successfully"
end
```

