# cs361-project
Quarter long project for CS 361 Software Engineering I

As of this moment the plan is for the project to be a RPG party maker. The idea is to create a party of a maximum of people made up of various classes such as fighter, mage, healer, etc. The party maker will be able to cycle through different weapon or spell systems and give the stats of these choices. At the end you will be able to see the average stats of the party you made to see how balanced or unbalanced it is and what you need to work on. I also plan to incorporate a name randomizer to help naming your party members.

Also provided is a microservice for my partner's project that provides a random currency for his currency converter. 

A. Requesting Data

    This will be done locally. To request data from the microservice you would place the below code into your program. 
    
    socket.send_string("Hello")
    
    Right now it is set up to just send the message "Hello" to the server. The server will wait to receive this message before sending anything back.
    
B. Receiving Data

    The server receives the "Hello" message and sends a random currency name and value back. The below code will need to be added to receive the data back.
    
    json_response = socket.recv_string()
    response = json.loads(json_response)
    
    Once you have the response in "response" you can access the value name like the below.
    
    response['value'] and response['name']

    For example, the value would be "HWK" and the name would be "Hong Kong Dollar (HKD)"

C. UML Diagram

![image](https://github.com/njbrunette/cs361-project/assets/89284172/4dc5eb0f-fd73-425a-b761-e514a184a8ea)

    
