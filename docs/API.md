# HXAI API Reference

## Authentication Endpoints

### POST /api/auth/register
Register a new user.

**Request:**
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "full_name": "John Doe"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "username": "username",
    "full_name": "John Doe",
    "is_active": true,
    "is_verified": false,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

### POST /api/auth/login
Login a user.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password"
}
```

**Response:**
Same as register endpoint.

## Memory Endpoints

### POST /api/memory/
Create a new memory.

### GET /api/memory/
List user memories.

### GET /api/memory/{memory_id}
Get a specific memory.

### PUT /api/memory/{memory_id}
Update a memory.

### DELETE /api/memory/{memory_id}
Delete a memory.

## Context Endpoints

### POST /api/context/
Create or update context.

### GET /api/context/
Get current context.

### PUT /api/context/
Update context.

## Sessions Endpoints

### POST /api/sessions/
Create a new session.

### GET /api/sessions/
List user sessions.

### GET /api/sessions/{session_id}
Get a specific session.

### PUT /api/sessions/{session_id}
Update a session.

### DELETE /api/sessions/{session_id}
Delete a session.
