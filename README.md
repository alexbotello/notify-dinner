# notify-dinner
A microservice that sends me push notifications on what's for dinner today

I'm very lazy. I also happen to hate the question, "What's for dinner today?"
I don't want hear about it OR spend precious brain cycles having to think about it

Behold! I will innovate to perpertrate this laziness.

Pushing to this repository will automatically trigger a docker image build and push to Google Container Registry and automatically deploy to Cloud Run. Cloud Scheduler will trigger the microservice once a day to tell me what the hell I'm eating tonight.