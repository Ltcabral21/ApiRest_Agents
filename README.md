
RestAPI With OpenAI Agents 🤖                                                                                                                      
Base URL:
The API is available at the following address:
Local: http://127.0.0.1:3000
Local Network: http://<your-ip>:3000
1. Create an Agent
Endpoint: POST /agents
This endpoint allows you to create a new agent with a name and personality.
Request Body:
{
  "name": "HelperBot",     // Name of the agent
  "personality": "friendly" // Personality of the agent (optional, default is "neutral")
}
Response:
{
 "message": "Agent 'HelperBot' created successfully."
}
Status 400:   When the agent name is not provided or if the name already exists.
{
"error": "Agent name is required."
}
2. Chat with an Agent
Endpoint: POST /agents/<name>/chat
This endpoint allows the user to send a message to the agent and receive a response based on the OpenAI model.
Request Body:
{
 "message": "Hello, how are you?"
 }
Response:
{
 "reply": "Hello! I am a friendly assistant. How can I help you today?"
 }
Status 400: When the user message is not provided.
{ 
"error": "Message is required."
 }
Status 404: When the agent with the specified name does not exist.
{
 "error": "Agent 'HelperBot' does not exist."
 }
3. List All Agents
Endpoint: GET /agents
This endpoint allows you to list all created agents.
Response:
Status 200: Returns a list of agents
[ 
"HelperBot", 
"AssistantBot" 
]
4. Delete an Agent
Endpoint: DELETE /agents/<name>
This endpoint allows you to delete an agent by name.
Response:
Status 200: When the agent is successfully deleted.
{
 "message": "Agent 'HelperBot' deleted successfully." 
}
Status 404: When the agent with the specified name does not exist.
{ 
"error": "Agent 'HelperBot' does not exist."
 }
Example Full Flow:
Create an Agent:
POST /agents 
Body:
 {
"name": "HelperBot", 
"personality": "friendly"
}
Send a Message to the Agent:
POST /agents/HelperBot/chat 
Body:
 {
"message": "Hello, how are you?"
}
Get answer from agent:
{ 
"reply": "Hello! I am a friendly assistant. How can I help you today?"
 }
List All Agents:
GET /agents
Delete an Agent:
DELETE /agents/HelperBot
by Lucas Cabral
