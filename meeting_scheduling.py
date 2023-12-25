```python
# Import necessary libraries
import requests
import json

class MeetingScheduling:
    def __init__(self):
        self.scheduling_tools = ['Calendly.com', 'Cal.com']

    def connect_to_scheduling_tool(self, tool_name, api_key):
        if tool_name not in self.scheduling_tools:
            raise ValueError(f"Unsupported scheduling tool. Supported tools are {self.scheduling_tools}")

        self.tool_name = tool_name
        self.api_key = api_key

    def schedule_meeting(self, prospect_info, meeting_info):
        if self.tool_name == 'Calendly.com':
            return self.schedule_calendly_meeting(prospect_info, meeting_info)
        elif self.tool_name == 'Cal.com':
            return self.schedule_cal_meeting(prospect_info, meeting_info)

    def schedule_calendly_meeting(self, prospect_info, meeting_info):
        # Calendly API integration code goes here
        # This is a placeholder and should be replaced with actual API calls
        # Refer to Calendly API documentation for correct implementation
        print(f"Scheduling meeting on Calendly for {prospect_info['name']}")

    def schedule_cal_meeting(self, prospect_info, meeting_info):
        # Cal.com API integration code goes here
        # This is a placeholder and should be replaced with actual API calls
        # Refer to Cal.com API documentation for correct implementation
        print(f"Scheduling meeting on Cal.com for {prospect_info['name']}")

if __name__ == "__main__":
    meeting_scheduler = MeetingScheduling()
    meeting_scheduler.connect_to_scheduling_tool('Calendly.com', 'your_api_key_here')
    prospect_info = {'name': 'John Doe', 'email': 'johndoe@example.com'}
    meeting_info = {'date': '2022-01-01', 'time': '10:00'}
    meeting_scheduler.schedule_meeting(prospect_info, meeting_info)
```
