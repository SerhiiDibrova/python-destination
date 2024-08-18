package linkedin_scraper

import os
from third_parties.linkedin import LinkedIn

class LinkedInScraper:
    def __init__(self, config):
        self.config = config
        self.api = LinkedIn(config['linkedin_api_key'], config['linkedin_api_secret'])

    def fetch_user_profiles(self, user_ids):
        profiles = []
        for user_id in user_ids:
            try:
                profile = self.api.get_profile(user_id)
                profiles.append(profile)
            except Exception as e:
                print(f"Error fetching profile for {user_id}: {str(e)}")
        return profiles

    def extract_relevant_info(self, profiles):
        relevant_info = []
        for profile in profiles:
            info = {
                'first_name': profile['firstName'],
                'last_name': profile['lastName'],
                'headline': profile['headline'],
                'location': profile['location']['name']
            }
            relevant_info.append(info)
        return relevant_info