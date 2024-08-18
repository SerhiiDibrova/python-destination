package main

import os
from linkedin_scraper import LinkedInScraper
from lang_chain_handler import LangChainHandler
from port_forwarder import PortForwarder

def main():
    scraper = LinkedInScraper()
    handler = LangChainHandler()
    forwarder = PortForwarder()

    while True:
        profile_data = scraper.scrape_linked_in_profile()
        response = handler.generate_response(profile_data)
        forwarder.forward_ports(response)

if __name__ == "__main__":
    main()