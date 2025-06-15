# Usage Examples - Enhanced QR Code MCP Server

## Basic QR Code Generation

### Simple Text QR Code
```json
{
  "content": "Hello from Enhanced QR Code MCP!",
  "output_directory": "./qr_output/",
  "filename": "hello_world",
  "errorCorrectionLevel": "M",
  "size": 5
}
```

**Result:**
- `hello_world.png` - QR code image
- `hello_world_metadata.json` - Metadata file
- Chat display (if enabled)

### Website URL QR Code
```json
{
  "content": "https://github.com/myownipgit/enhanced-qrcode-mcp",
  "output_directory": "./qr_output/",
  "filename": "github_repo",
  "errorCorrectionLevel": "H",
  "size": 6,
  "border": 6
}
```

## Business Card QR Codes

### Single Contact Card
```json
{
  "content": "BEGIN:VCARD\nVERSION:3.0\nFN:John Doe\nORG:Acme Corporation\nTITLE:Software Engineer\nTEL:+1-555-123-4567\nEMAIL:john.doe@acme.com\nURL:https://johndoe.dev\nEND:VCARD",
  "output_directory": "./business_cards/",
  "filename": "john_doe_contact",
  "errorCorrectionLevel": "H",
  "size": 7
}
```

### Batch Business Cards
```json
{
  "qr_codes": [
    {
      "id": "john_doe",
      "content": "BEGIN:VCARD\nVERSION:3.0\nFN:John Doe\nORG:Acme Corp\nTEL:555-0123\nEMAIL:john@acme.com\nEND:VCARD",
      "type": "vcard"
    },
    {
      "id": "jane_smith",
      "content": "BEGIN:VCARD\nVERSION:3.0\nFN:Jane Smith\nORG:Acme Corp\nTEL:555-0124\nEMAIL:jane@acme.com\nEND:VCARD",
      "type": "vcard"
    },
    {
      "id": "bob_johnson",
      "content": "BEGIN:VCARD\nVERSION:3.0\nFN:Bob Johnson\nORG:Acme Corp\nTEL:555-0125\nEMAIL:bob@acme.com\nEND:VCARD",
      "type": "vcard"
    }
  ],
  "output_directory": "./business_cards/",
  "errorCorrectionLevel": "H",
  "size": 6
}
```

## Event Management

### Event Ticket QR Code
```json
{
  "content": "EVENT:Tech Conference 2025\nDATE:2025-07-15\nTIME:09:00\nVENUE:Convention Center\nTICKET:VIP-001\nSEAT:Row A, Seat 12\nACCESS:VIP Lounge, All Sessions",
  "output_directory": "./event_tickets/",
  "filename": "ticket_vip_001",
  "errorCorrectionLevel": "H",
  "size": 8
}
```

### Batch Event Tickets
```json
{
  "qr_codes": [
    {
      "id": "vip_001",
      "content": "TICKET:VIP-001|EVENT:Tech Conf 2025|SEAT:A-12|ACCESS:VIP",
      "type": "ticket"
    },
    {
      "id": "regular_002",
      "content": "TICKET:REG-002|EVENT:Tech Conf 2025|SEAT:B-24|ACCESS:General",
      "type": "ticket"
    },
    {
      "id": "student_003",
      "content": "TICKET:STU-003|EVENT:Tech Conf 2025|SEAT:C-15|ACCESS:Student",
      "type": "ticket"
    }
  ],
  "output_directory": "./event_tickets/",
  "errorCorrectionLevel": "H",
  "size": 7
}
```

## WiFi Access QR Codes

### Single WiFi Network
```json
{
  "content": "WIFI:T:WPA;S:ConferenceWiFi;P:TechConf2025!;H:false;",
  "output_directory": "./wifi_access/",
  "filename": "conference_wifi",
  "errorCorrectionLevel": "Q",
  "size": 6
}
```

### Multiple WiFi Networks
```json
{
  "qr_codes": [
    {
      "id": "lobby_wifi",
      "content": "WIFI:T:WPA;S:Lobby_Guest;P:Welcome123;H:false;",
      "type": "wifi"
    },
    {
      "id": "conference_wifi",
      "content": "WIFI:T:WPA;S:Conference_Net;P:Event2025;H:false;",
      "type": "wifi"
    },
    {
      "id": "vip_wifi",
      "content": "WIFI:T:WPA;S:VIP_Access;P:VIPOnly2025;H:false;",
      "type": "wifi"
    }
  ],
  "output_directory": "./wifi_access/",
  "errorCorrectionLevel": "Q",
  "size": 5
}
```

## Marketing Campaign QR Codes

### Product Information
```json
{
  "content": "https://example.com/products/laptop-pro?utm_source=qr&utm_campaign=summer2025&utm_medium=print",
  "output_directory": "./marketing/products/",
  "filename": "laptop_pro_qr",
  "errorCorrectionLevel": "H",
  "size": 6
}
```

### Social Media Links
```json
{
  "qr_codes": [
    {
      "id": "instagram",
      "content": "https://instagram.com/acmecorp",
      "type": "social"
    },
    {
      "id": "linkedin",
      "content": "https://linkedin.com/company/acmecorp",
      "type": "social"
    },
    {
      "id": "twitter",
      "content": "https://twitter.com/acmecorp",
      "type": "social"
    }
  ],
  "output_directory": "./marketing/social/",
  "errorCorrectionLevel": "M",
  "size": 5
}
```

## Error Correction Level Guidelines

- **L (7% recovery)**: Indoor use, clean environments
- **M (15% recovery)**: Standard use, moderate durability needed
- **Q (25% recovery)**: Industrial environments, potential damage
- **H (30% recovery)**: Outdoor use, high damage potential

## Size Guidelines

- **Size 1-3**: Small labels, business cards
- **Size 4-6**: Standard posters, flyers
- **Size 7-10**: Large displays, banners
- **Size 11-20**: Very large displays, outdoor signage

## Directory Organization Tips

```
project/
├── qr_output/
│   ├── business_cards/
│   ├── event_tickets/
│   ├── wifi_access/
│   ├── marketing/
│   │   ├── products/
│   │   └── social/
│   └── inventory/
│       └── assets/
```

This organization makes it easy to manage different types of QR codes and their associated metadata files.