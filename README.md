
# **RestAPI With OpenAI Agents 🤖**

An API built with Flask to manage and interact with customizable AI agents powered by OpenAI's GPT models. The system supports creating agents, chatting with them, listing available agents, and deleting agents.

---

## **Base URL**
The API is accessible via the following addresses:
- **Local:** `http://127.0.0.1:3000`
- **Local Network:** `http://<your-ip>:3000`

---

## **Endpoints**

### **1. Create an Agent**
- **Endpoint:** `POST /agents`
- **Description:** This endpoint allows you to create a new agent with a name and personality.

#### **Request Body:**
```json
{
  "name": "HelperBot",     
  "personality": "friendly" 
}
```
- `name`: Name of the agent (required).
- `personality`: Personality of the agent (optional, default is `"neutral"`).

#### **Response:**
```json
{
  "message": "Agent 'HelperBot' created successfully."
}
```

- **Error (400):** When the agent name is not provided or already exists.
```json
{
  "error": "Agent name is required."
}
```

---

### **2. Chat with an Agent**
- **Endpoint:** `POST /agents/<name>/chat`
- **Description:** Send a message to an agent and receive a response based on the OpenAI model.

#### **Request Body:**
```json
{
  "message": "Hello, how are you?"
}
```

#### **Response:**
```json
{
  "reply": "Hello! I am a friendly assistant. How can I help you today?"
}
```

- **Error (400):** When the message is not provided.
```json
{
  "error": "Message is required."
}
```
- **Error (404):** When the agent does not exist.
```json
{
  "error": "Agent 'HelperBot' does not exist."
}
```

---

### **3. List All Agents**
- **Endpoint:** `GET /agents`
- **Description:** Lists all created agents.

#### **Response:**
```json
[
  "HelperBot",
  "AssistantBot"
]
```

---

### **4. Delete an Agent**
- **Endpoint:** `DELETE /agents/<name>`
- **Description:** Deletes an agent by name.

#### **Response:**
```json
{
  "message": "Agent 'HelperBot' deleted successfully."
}
```

- **Error (404):** When the agent does not exist.
```json
{
  "error": "Agent 'HelperBot' does not exist."
}
```

---

## **Example Full Flow**

1. **Create an Agent:**
   - **Request:**
     ```bash
     POST /agents
     ```
   - **Body:**
     ```json
     {
       "name": "HelperBot",
       "personality": "friendly"
     }
     ```

2. **Chat with the Agent:**
   - **Request:**
     ```bash
     POST /agents/HelperBot/chat
     ```
   - **Body:**
     ```json
     {
       "message": "Hello, how are you?"
     }
     ```

3. **List All Agents:**
   - **Request:**
     ```bash
     GET /agents
     ```

4. **Delete an Agent:**
   - **Request:**
     ```bash
     DELETE /agents/HelperBot
     ```

---

## **Author**
Developed by Lucas Cabral.

