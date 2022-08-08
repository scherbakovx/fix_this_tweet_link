import re
from typing import Optional

def replace_twitter_link(text: str) -> Optional[str]:
    all_twitter_links = re.findall(r"(https?:\/\/twitter.com[^ ]*)", text)
    if all_twitter_links:
        first_twitter_link = all_twitter_links[0]
        new_twitter_link = first_twitter_link.replace("twitter.com", "vxtwitter.com")
        return new_twitter_link

    return None
