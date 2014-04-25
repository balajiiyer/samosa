Samosa
========

Samosa helps you build leaderboards for various fitness devices, allowing you to compete with your friends.

Currently it supports:

    * Jawbone Up
    * Fitbit

Feature revisions could include -

    * Garmin Vivofit
    * Polar Loop
    * Argus Lifetrak
    * Nike Plus

Features
--------

- Easy to use API
- Support for many popular devices

Samosa Components
------------------

Samosa Bot
-----------

Samosa bot is resposible for collecting activities and stats from different APIs and storing it in Redis. The bot runs every 30 mins. (Configurable)


API
---

**1. Add user details to Samosa**

Typical details include the type of product they are using, and credentials that would help pull data on user's behalf from device provider's API ::


    POST  /user

    Content-Type: application/json

        {
        "name" : "Balaji Iyer",
        "device" : {fitbit,vivofit,up,nikeplus,argus},
        "credentials" : apikey, {username, password}, customer secret
        }



**2. Get leaderboard** ::

    GET /leaderboard

    [
        {
            "user": "sriram",
            "rank": 1,
            "data": { "steps":100, "calories": 200, "distance": 2.8 },
            "rankingmetric": "steps"
        },
        {
            "user": "balaji",
            "rank": 2,
            "data": { "steps":80, "calories": 200, "distance": 2.8 },
            "rankingmetric": "steps"
        }
    ]

    By default, users will be ranked by steps, however the default ranking can be changed by passing a 'rankby' parameter.

    GET /leaderboard?rankby={steps,calories,distance}


**3. Get stats on a specific user** ::

    GET /stats?user={username}

    {
        "user": "sriram",
        "rank": 1,
        "data": { "steps":100, "calories": 200, "distance": 2.8 },
        "rankingmetric": "steps"
    }

UI
---

Samosa prints a leaderboard by making an AJAX request to the API. Check ui/leaderboard.html for the source.


Contribute
----------

- Issue Tracker: github.com/balajiiyer/samosa/issues
- Source Code: github.com/balajiiyer/samosa

Support
-------

If you are having issues, please let us know using the github Issue Tracker.

License
-------

The project is licensed under the Apache license.
