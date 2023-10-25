# The Skin Deep web app

## Motivation

I own a bunch of [The Skin Deep's](https://shop.theskindeep.com/) card games, and have found them a fun and valuable tool for building and deepening various relationships in my life. The problem is that I don't carry them around with me, and I don't like having a bunch of /stuff/ stacked up around the house. Using my document scanner and [cv2](https://github.com/opencv/opencv-python)/[pytesseract](https://github.com/madmaze/pytesseract), I digitized the seven decks I own and built this app to randomize and display them.

## Source material

I'm not sharing the contents of the decks for obvious reasons (I think the product is a good one and that you should buy it from the source), so I am leaving in place custom methods I've written in separate modules to pull their contents from my [Joplin](https://github.com/laurent22/joplin) server. Anyone else will need to replace those methods to pull in data from their preferred source.

## Design

The use case is already pretty lightweight, so the main variables to consider resource-wise are number of requests and data transfer (and, since we're talking about sets of ~200 short strings as the max object size, the latter is trivial). For that reason, I have python perform the randomization and directly inject the list of card strings into a Javascript array to be traversed by the client, rather than having a single random card returned per GET. This also precludes close-proximity repeats and enables functionality like moving backwards through the deck via the left arrow key.

## Interface

Once a deck is selected, tapping/clicking the card or text will "deal" the next card in line. On clients with keyboards, the left and right keys will move the user backwards/forwards through the deck.

## Other considerations/future improvements

### Front-end

I'm not skilled in the black magic wizardry of front-end development, so the responsiveness, etc of the UI are best approximations of what someone who knows what they're doing would be able to pull off. As it is, it's good enough to satisfy my anal-retentiveness.

### Security

I'm currently hosting this app on my local network, so no security is in place. Making this public-facing would require some form of authentication to protect the source data, which would be a balancing act with the desire to keep it as light as possible. The right level of control, then - without considering deployment options - feels like simple password auth, which could use eg the [flask.session](https://flask.palletsprojects.com/en/3.0.x/api/#sessions) object. Of course this wouldn't be enough to keep anyone with the right knowledge from accessing the source data, so there's more thinking to be done about the right approach here.

### Deployment

I've thought about making this app available to my friends which, since I'm not interested in opening a random port on my server to the internet, would probably look something like one of the following:

1. Hosting on Heroku, or something similar
   - Not free anymore, and I'd want a little more control over access than a PaaS can probably give me for the reasons detailed above.
2. A VPS
   - Sufficient security control, but this app is written to be minimally resource-intensive, so even the smallest instance would probably be overkill.
3. An AWS Lambda function or equivalent, pulling the cards from object storage
   - Could be free indefinitely with the right setup
   - Would need to research access/security feasibility
     - Obviously plenty of control is possible (and keeping the source data locked down is straightforward), but app-level authentication would be an interesting problem to solve inside of a serverless function and it might make more sense to scaffold authentication out to the infrastructure layer, which could easily become clunky or just straight overkill for this app.
   - This would make flask a less sensible framework, as it's built to wait for requests rather than start up and shut down with each. At that point, using vanilla [jinja](https://jinja.palletsprojects.com/en/3.1.x/) might make more sense.