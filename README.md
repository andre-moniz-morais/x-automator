# X (former Twitter) automator
A code that runs every day at 8am, 12pm, 4pm and 8pm.

## Concept
It will create posts everyday at the same hours.
Initially it will send me an email with the post's content for me to publish.

## Steps
1. The script will decide if asks chatgpt for a theme or if it goes to google news rss to get the latest news.
    1. If it uses chatgpt, then it must ask for an interesting topic of AI, Apple, Samsung, Xiaomi, Phones, Computers or technology in general.
    2. If it uses google news rss, it must collect all the news about technology in the last 24h and choose the most interesting one.
2. With the topic chosen, the script will ask gpt for about 7 threaded posts for X related with that topic. Each post cant have more than 280 chars.
3. The script must select two images about the topic in the internet, by requesting the urls for the two images to chat gpt.
4. The script send me the email with all the posts.
