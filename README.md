Samosa
======

Leaderboard for all Fitness Tracking Devices


Samosa currently supports {fitbit, Jawbone Up }

In future it might support { vivofit,Nikeplus, Argus Lifetrak}

Samosa Bot
======

Samosa bot is resposible for collecting activities and stats from different APIs and storing it in Redis. The bot runs every 30 mins. (Configurable)


API
======

Add your details to Samosa
    
    POST  /user
    
    Content-Type: application/json
    
    {
      "Name" : "Balaji Iyer",
      "Product" : {fitbit,vivofit,up,nikeplus,argus},
      "credentials" : apikey, {username, password}, customer secret
    }



Get stats on all users
    
    GET /stats
    
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
    
    GET /stats?rankby={steps,calories,distance}

Get stats on a specific user
    
    GET /stats?user={username}
    
    {
        "user": "sriram",
        "rank": 1,
        "data": { "steps":100, "calories": 200, "distance": 2.8 },
        "rankingmetric": "steps"
    }
    
UI
======

Samosa prints a leaderboard by making an AJAX request to the API
