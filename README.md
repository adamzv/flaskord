# [flaskord](https://flaskord.herokuapp.com)
Simple Slack/Discord clone based on [cs50w](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) ["Flack" project](https://docs.cs50.net/web/2018/x/projects/2/project2.html) using Flask and Vue.js. The project had 7 requirements:

## Result
![image](https://user-images.githubusercontent.com/31664842/54117167-87bc7e00-43f0-11e9-9037-84a62f05f387.png)

## Project requirements
1. The web application should ask first time visitors to type in their display name,
2. Any user should be able to create a new channel,
3. Every user should be able to see all available channels and after selecting one, the user should be able to see message view,
4. User should be able to see a maximum of 100 messages per channel (storing messages in server side memory),
5. User should be able to send text messages to others in the channel. All users should then see the new message appear in the channel without reloading the page,
6. After returning to the web page, application should remember what channel the user was on previously,
7. Add a personal touch to the web application. In my case I used Vue.js with Bulma for my frontend.

## Built with
* Flask - a Python microframework,
* Vue.js - a JavaScript framework for building single-page applications
* Bulma - CSS framework (alternative to Bootstrap)
* Socket.io - JavaScript library for real-time communication
