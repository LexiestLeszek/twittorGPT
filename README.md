# twittorGPT
TwittorGPT is a tool that uses GPP4ALL model to generate tweets and then uses JS frontend Twitter API to post them.
It uses tweety (https://github.com/mahrtayyab/tweety) library.

register.py automatically registers your account, but catcha solving is not yet done.

# Main workflow:

# step 1

Use img.py download image from thispersondoesnotexist. register.py automatically registers your account, but catcha solving is not yet done.

# step 2
Create .env variable with credentials from your twitter account:
``
USERNAME=
PASSWORD=
``

# step 2
run: ``python3 twittorGPT.py``

# Customisation
The main idea is that language model writes a tweet based on the set of topics and suggestions. That way you can manage the overall theme of your tweets.

# This app is made for educational purposes and author (developer) does not bear any responsibility for its usage by others
