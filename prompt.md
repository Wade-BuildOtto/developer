a meteorjs based application that uses blazejs templates and bootstrap ui elements.
the app will have a staff login that will all them to interact with customers via a
chat window. the chat entries be run thru twillio's sms api. the customers phone number
will be used as the point of reference. navigation will use iron router to manage page views

### login
- username and password with a signin button centered on the screen 
- once logged in goes to chat page

### Chat
- a right side bar with a scrolled list of active chats sorted by most recent
- the chats will be identified with the users phone number
- the main chat window will be scrollable with the most recent items added to the bottom
- the users chats will be in a grey card on the left and the staffs responses in blue on the right