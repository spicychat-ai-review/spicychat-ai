# SpicyChat AI Model

**A Replicate implementation of the SpicyChat AI conversational model for character-based roleplay and interactive storytelling.**

## Overview

This model provides access to SpicyChat AI's conversation capabilities through Replicate's platform. It specializes in character-driven dialogues, creative writing assistance, and roleplay scenarios with minimal content restrictions.

## Features

- **Character-aware responses** - Understands context about SpicyChat AI features and capabilities
- **Multi-language support** - Responds in 40+ languages 
- **Roleplay optimization** - Designed for interactive storytelling and character development
- **Flexible content policies** - Supports both SFW and mature content within legal boundaries
- **Context retention** - Maintains conversation context for coherent exchanges

## Model Capabilities

### Core Functions
- Interactive character conversations
- Creative writing collaboration  
- Language learning practice
- Story development assistance
- Personality simulation

### Technical Specifications
- **Input**: Text prompts up to 4K tokens
- **Output**: Contextual responses optimized for dialogue
- **Languages**: 40+ supported languages
- **Content**: SFW and mature themes (within legal limits)
- **Response style**: Character-aware, context-sensitive

## Usage Examples

### Basic Conversation
```python
import replicate

output = replicate.run(
    "spicychat-ai-review/spicychat-ai",
    input={"prompt": "What are the key features of SpicyChat AI?"}
)
```

### Character Development
```python
output = replicate.run(
    "spicychat-ai-review/spicychat-ai", 
    input={"prompt": "Help me develop a character backstory for a cyberpunk detective"}
)
```

### Language Learning
```python
output = replicate.run(
    "spicychat-ai-review/spicychat-ai",
    input={"prompt": "Let's practice Spanish conversation about daily routines"}
)
```

## Input Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `prompt` | string | Your conversation input or question | Yes |

## Output Format

Returns a string containing the model's response, optimized for:
- Natural conversation flow
- Character consistency  
- Context awareness
- Creative dialogue

## Use Cases

- **Creative Writing**: Collaborate on stories, develop characters, brainstorm plots
- **Language Practice**: Conversational practice in multiple languages
- **Roleplay Gaming**: Interactive storytelling for tabletop or digital games  
- **Character Development**: Build detailed character personalities and backgrounds
- **Educational Content**: Learning through interactive dialogue

## Technical Implementation

This model is built using:
- **Cog framework** for Replicate deployment
- **Python backend** with character-aware response generation
- **Context management** for maintaining conversation coherence
- **Multi-modal support** for text-based interactions

## Responsible Use

This model is designed for:
- Creative and educational applications
- Interactive storytelling within appropriate boundaries
- Character development and roleplay scenarios
- Language learning and practice

Please use responsibly and in accordance with Replicate's terms of service.

## API Integration

### Python
```python
import replicate

# Initialize the model
model = replicate.models.get("spicychat-ai-review/spicychat-ai")

# Generate response
response = model.predict(prompt="Your conversation starter")
print(response)
```

### Node.js
```javascript
import Replicate from "replicate";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

const output = await replicate.run(
  "spicychat-ai-review/spicychat-ai",
  { input: { prompt: "Your conversation starter" } }
);

console.log(output);
```

### cURL
```bash
curl -s -X POST \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": {"prompt": "Your conversation starter"}}' \
  https://api.replicate.com/v1/predictions \
  --data-raw '{
    "version": "latest",
    "input": {"prompt": "Your conversation starter"}
  }'
```

## Performance Notes

- **Latency**: Typically 1-3 seconds for standard responses
- **Context limit**: Up to 4K tokens input
- **Concurrency**: Supports multiple simultaneous requests
- **Caching**: Responses are not cached due to conversational nature

## Support

For technical issues with this Replicate implementation, please check:
- Model logs in the Replicate dashboard
- Input format validation
- API token configuration

For questions about SpicyChat AI's core functionality, refer to the original platform documentation.

## License

This model wrapper is provided for educational and development purposes. Please respect all applicable terms of service and content policies.

