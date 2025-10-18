# Project Status Report
_Assignment: VS Code Remote_

### Progress:
1. My biggest progress so far has been inplementing a junction table for the many-many relationship in my application. 
    - Previously: I didn't have a junction table between Users <--> Feeds. This violated principles of database data normalization because this many to many relationship needs it's own table. If I were to store these relationships in just the Users || just the Feeds Table – then I would have serious issues maintaining a single source of truth for the many-many relationship and adding the data would create inconsistencies in either Users or the feeds table. 
    - Currently: I have a juntion table that uses a composite primary key (PK = Several FK's: which are attributes from the users and feeds tables.)


### Blockers: 
1. I'm used to creating Front End Applications but not fullstack applications. Learning how to sync a backend application to a front end (and securely) will be a really good challenge for me. I'm considering purchasing a domain for this application so I can get the full experience of provisioning a server, setting up an nginx web server, hosting the front end and backends, and setting up an auth system too..?

_What I'm comfortable with:_ 
- FE Development
- Privisioning VPS
- Proxy Servers with Nginx
- CRUD on the FE

_What I'm less comfortable with:_
- BE development
- Auth systems
- connecting the FE to BE

### Risks: 
1. Over complicating the assignment given the time constraints that I am working with. I will try to mitigate this by completing the assignment as required and if I have time outside of this – then I go hog WiLd with publishing to the internet. 

2. Trying to over engineer: As always, less = more;

3. If I don't follow principles of 12 Factor apps & TDD I will likely add more time to building the application than necessary.

4. Writing python logic that doesn't adhere to my data model. 