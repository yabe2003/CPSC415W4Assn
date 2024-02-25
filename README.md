### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8080.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)

### Learning, Decision, Sources

I had a lot of difficulty with the whole assignmnet, but through the help of the O'Reilly readings as well as the help option in the Docker dashboard has helped me work my way through.
The most difficult idea I had to understand was the concept of Dockerfile, Containers, and Images. I thought I understood it when we went over in class a few times, but as I started off to work on this assignment from scratch I had to use the help function on Docker Dashboard as well as ChatGPT to help me understand the general concepts as well as the details that entailed in completing the assignment.
I seem to have just misunderstood a lot about creating my application so what I did was I had Chat help me step-by-step as it created examples which included explanations to help me walk my way to complete the application.
