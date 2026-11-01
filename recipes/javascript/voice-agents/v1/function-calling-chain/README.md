# Multi-Turn Function Calling Chain (Voice Agents v1)

Chain multiple dependent function calls across conversation turns in a voice agent session.

## What it does

Demonstrates a sequential function-calling workflow where each tool result feeds into the next call. The agent processes a customer return request through four dependent steps:

1. **lookup_customer** — find the customer record by name
2. **get_orders** — retrieve order history using the customer ID from step 1
3. **check_return_eligibility** — verify the order is within the return window
4. **initiate_return** — create the return and generate a shipping label

Each `FunctionCallRequest` arrives from the LLM when it needs external data. Your code executes the function, sends the result back via `sendFunctionCallResponse()`, and the LLM uses that result to decide the next step. This pattern enables multi-step workflows like customer service, booking systems, and data lookup assistants.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | `Array<Object>` | Array of function definitions available to the LLM |
| `think.prompt` | `string` | Instructs the LLM on the order of function calls |
| `FunctionCallRequest.functions` | `Array` | Functions the LLM wants to call |
| `FunctionCallRequest.functions[].id` | `string` | Unique ID to match response to request |
| `sendFunctionCallResponse()` | method | Send function result back so the LLM can continue the chain |

## Example output

```
Connection opened
Agent ready — sending return request
[user] I'm Jane Smith and I want to return the headphones I bought recently.
Step 1: lookup_customer({"name": "Jane Smith"})
  → {"customer_id": "C-1234", "name": "Jane Smith", "email": "jane@example.com"}
Step 2: get_orders({"customer_id": "C-1234"})
  → {"orders": [{"order_id": "ORD-5678", "item": "Wireless Headphones", "date": "2026-10-15", "total": "$89.99"}]}
Step 3: check_return_eligibility({"order_id": "ORD-5678"})
  → {"eligible": true, "return_window_days": 30, "days_remaining": 16}
Step 4: initiate_return({"order_id": "ORD-5678", "reason": "customer request"})
  → {"return_id": "RET-9012", "status": "approved", "label_url": "https://example.com/label/RET-9012"}

Chain complete: 4 function calls executed
```

## Prerequisites

- Node.js 20+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `npm install`

## Run

```bash
node example.js
```

## Test

```bash
node --test example.test.js
```
