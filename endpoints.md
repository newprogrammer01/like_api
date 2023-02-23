# Endpoints

## Add image

### Request

```bash

curl -X POST \
  /api/addImage \
  -H 'Content-Type: application/json' \
  -d '{
    "image_id": "1",
    "message_id": "1",
    
}'
```

### Response

```json
{
    "status": "ok"
}
```