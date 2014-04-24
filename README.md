Samosa
======

Leaderboard for all Fitness Tracking Devices


Samosa currently supports {fitbit, vivofit, Jawbone Up, Nikeplus, Argus Lifetrak}

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

Get stats on a specific user

GET /stats?user={username}

UI
======

Samosa prints a leaderboard using HTML / CSS / 
