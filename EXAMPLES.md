# Enhanced QR Code MCP Server - Usage Examples

This document provides comprehensive examples of how to use the Enhanced QR Code MCP Server (Python implementation).

## Current Implementation Features

### Generate and Save QR Code (Core Feature)

#### Basic QR code generation with automatic PNG file saving
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://example.com",
    "output_directory": "./qr_codes/",
    "filename": "example_website",
    "errorCorrectionLevel": "M",
    "size": 5,
    "border": 4,
    "include_metadata": true,
    "display_in_chat": true
  }
}
```

**Output:**
- `example_website.png` - QR code image file
- `example_website_metadata.json` - Generation metadata
- Chat display (if enabled)

#### High-quality QR code for print production
```json
{
  "tool": "generate_and_save_qrcode", 
  "arguments": {
    "content": "https://mycompany.com/product",
    "output_directory": "./print_ready/",
    "filename": "product_qr_high_res",
    "errorCorrectionLevel": "H",
    "size": 10,
    "border": 6,
    "include_metadata": true
  }
}
```

### Batch QR Code Generation

#### Generate multiple QR codes for different products
```json
{
  "tool": "batch_generate_qrcodes",
  "arguments": {
    "qr_codes": [
      {
        "id": "product_a",
        "content": "https://shop.example.com/product-a",
        "type": "url"
      },
      {
        "id": "product_b", 
        "content": "https://shop.example.com/product-b",
        "type": "url"
      },
      {
        "id": "contact_support",
        "content": "BEGIN:VCARD\nVERSION:3.0\nFN:Support Team\nORG:Example Corp\nTEL:555-0123\nEMAIL:support@example.com\nEND:VCARD",
        "type": "vcard"
      }
    ],
    "output_directory": "./marketing_campaign/",
    "size": 6,
    "errorCorrectionLevel": "H"
  }
}
```

**Output:**
- `qr_product_a.png`
- `qr_product_b.png` 
- `qr_contact_support.png`
- Individual metadata files
- `batch_manifest_YYYYMMDD_HHMMSS.json`

### List Generated QR Codes

#### View all QR codes in a directory
```json
{
  "tool": "list_generated_qrcodes",
  "arguments": {
    "directory": "./qr_codes/"
  }
}
```

## Specialized Content Examples

### Contact Information (vCard)
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "BEGIN:VCARD\nVERSION:3.0\nFN:John Smith\nORG:Tech Corp\nTITLE:Software Engineer\nTEL:+1-555-123-4567\nEMAIL:john.smith@techcorp.com\nURL:https://johnsmith.dev\nADR:;;123 Tech Street;San Francisco;CA;94105;USA\nEND:VCARD",
    "filename": "john_smith_contact",
    "errorCorrectionLevel": "H",
    "size": 6
  }
}
```

### WiFi Network Credentials
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "WIFI:T:WPA2;S:OfficeNetwork;P:SecurePassword123;H:false;;",
    "filename": "office_wifi",
    "errorCorrectionLevel": "M",
    "size": 5
  }
}
```

### Calendar Event
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "BEGIN:VEVENT\nSUMMARY:Team Meeting\nDTSTART:20250620T100000Z\nDTEND:20250620T110000Z\nDESCRIPTION:Weekly team sync and planning session\nLOCATION:Conference Room A\nEND:VEVENT",
    "filename": "team_meeting_event",
    "errorCorrectionLevel": "M",
    "size": 5
  }
}
```

## Business Use Cases

### Marketing Campaign QR Codes
```json
{
  "tool": "batch_generate_qrcodes",
  "arguments": {
    "qr_codes": [
      {
        "id": "summer_promo_instagram",
        "content": "https://campaign.mycompany.com/summer2025?utm_source=qr&utm_medium=instagram&utm_campaign=summer",
        "type": "url"
      },
      {
        "id": "summer_promo_flyer",
        "content": "https://campaign.mycompany.com/summer2025?utm_source=qr&utm_medium=print&utm_campaign=summer",
        "type": "url"
      },
      {
        "id": "summer_promo_email",
        "content": "https://campaign.mycompany.com/summer2025?utm_source=qr&utm_medium=email&utm_campaign=summer", 
        "type": "url"
      }
    ],
    "output_directory": "./marketing/summer_2025/",
    "size": 7,
    "errorCorrectionLevel": "H"
  }
}
```

### Restaurant Menu QR Code
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://restaurant.com/digital-menu",
    "filename": "restaurant_menu_table_1",
    "output_directory": "./restaurant_qr_codes/",
    "errorCorrectionLevel": "M",
    "size": 6,
    "border": 5
  }
}
```

### Event Registration System
```json
{
  "tool": "batch_generate_qrcodes",
  "arguments": {
    "qr_codes": [
      {
        "id": "registration_booth_a",
        "content": "https://conference.com/register?booth=A&source=qr",
        "type": "url"
      },
      {
        "id": "registration_booth_b", 
        "content": "https://conference.com/register?booth=B&source=qr",
        "type": "url"
      },
      {
        "id": "info_desk",
        "content": "https://conference.com/info?source=qr",
        "type": "url"
      }
    ],
    "output_directory": "./conference_2025/",
    "size": 8,
    "errorCorrectionLevel": "H"
  }
}
```

## Error Correction Level Guidelines

### L (Low) - ~7% damage recovery
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://example.com",
    "errorCorrectionLevel": "L",
    "size": 5
  }
}
```
**Use for:** Clean indoor environments, digital displays

### M (Medium) - ~15% damage recovery (Default)
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://example.com",
    "errorCorrectionLevel": "M",
    "size": 5
  }
}
```
**Use for:** Standard business cards, flyers, general use

### Q (Quartile) - ~25% damage recovery
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://example.com",
    "errorCorrectionLevel": "Q", 
    "size": 6
  }
}
```
**Use for:** Industrial environments, outdoor applications

### H (High) - ~30% damage recovery
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://example.com",
    "errorCorrectionLevel": "H",
    "size": 7
  }
}
```
**Use for:** Outdoor signage, damaged surfaces, logos overlay

## File Management Examples

### Organized Output Structure
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://mycompany.com/products",
    "output_directory": "./qr_codes/company/products/",
    "filename": "main_product_catalog",
    "size": 6,
    "include_metadata": true
  }
}
```

**Creates:**
```
qr_codes/
└── company/
    └── products/
        ├── main_product_catalog.png
        └── main_product_catalog_metadata.json
```

### Batch with Custom Directory Structure
```json
{
  "tool": "batch_generate_qrcodes",
  "arguments": {
    "qr_codes": [
      {
        "id": "table_01",
        "content": "https://restaurant.com/menu?table=01",
        "type": "url"
      },
      {
        "id": "table_02",
        "content": "https://restaurant.com/menu?table=02", 
        "type": "url"
      }
    ],
    "output_directory": "./restaurant/table_qr_codes/",
    "size": 5
  }
}
```

## Production Workflow Examples

### Print Production Workflow
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://conference.com/schedule",
    "output_directory": "./print_production/conference_materials/",
    "filename": "conference_schedule_high_res",
    "errorCorrectionLevel": "H",
    "size": 12,
    "border": 8,
    "include_metadata": true,
    "display_in_chat": false
  }
}
```

### Web Asset Generation
```json
{
  "tool": "batch_generate_qrcodes",
  "arguments": {
    "qr_codes": [
      {
        "id": "website_home",
        "content": "https://mysite.com",
        "type": "url"
      },
      {
        "id": "website_contact",
        "content": "https://mysite.com/contact",
        "type": "url"
      },
      {
        "id": "website_products",
        "content": "https://mysite.com/products",
        "type": "url"
      }
    ],
    "output_directory": "./web_assets/qr_codes/",
    "size": 4,
    "errorCorrectionLevel": "M"
  }
}
```

## Advanced Configuration Examples

### Maximum Quality Settings
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://important-announcement.com",
    "filename": "critical_announcement",
    "errorCorrectionLevel": "H",
    "size": 15,
    "border": 10,
    "include_metadata": true
  }
}
```

### Minimal Size for Digital Use
```json
{
  "tool": "generate_and_save_qrcode",
  "arguments": {
    "content": "https://app.example.com/download",
    "filename": "app_download_small",
    "errorCorrectionLevel": "L",
    "size": 3,
    "border": 2
  }
}
```

## MCP Client Configuration

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "enhanced-qrcode": {
      "command": "python3",
      "args": ["/path/to/enhanced-qrcode-mcp/src/enhanced_qrcode_server.py"],
      "env": {},
      "description": "Enhanced QR code generator with automatic PNG file saving"
    }
  }
}
```

### Environment Variables (Optional)
```bash
# Set default output directory
export QR_OUTPUT_DIR="./my_qr_codes/"

# Set default error correction level
export QR_DEFAULT_ERROR_CORRECTION="M"

# Set default size
export QR_DEFAULT_SIZE="5"
```

## Best Practices

### 1. File Organization
- Use descriptive directory structures
- Include dates in batch operations
- Use meaningful filenames
- Enable metadata for tracking

### 2. Quality Settings
- Use `errorCorrectionLevel: "H"` for outdoor/damaged surfaces
- Use `size: 6` or higher for print materials
- Use `border: 4` minimum for proper scanning margins

### 3. Content Optimization
- Keep URLs as short as possible
- Use URL shorteners for long links
- Test QR codes before mass production
- Validate special characters in content

### 4. Batch Processing
- Group related QR codes in single batch operations
- Use consistent naming conventions
- Include type metadata for organization
- Generate manifests for tracking

## Future Enhancements (Planned)

The following advanced features are planned for future versions:

### Custom Styling (Roadmap)
- Logo embedding
- Custom colors and gradients
- Rounded corners and borders
- Different dot styles

### Analysis Tools (Roadmap)
- QR code decoding from images
- Quality assessment tools
- Content validation
- Optimization recommendations

### Template System (Roadmap)
- Pre-defined style templates
- Business, social, and event templates
- Template management tools

### Statistics and Analytics (Roadmap)
- Generation statistics
- Usage patterns
- Performance metrics
- Export capabilities

---

**Note:** This Python implementation focuses on reliable file generation and batch processing. For advanced styling and analysis features, see our TypeScript implementation at [mcp-server-qrcode-enhanced](https://github.com/myownipgit/mcp-server-qrcode-enhanced).

**Built with ❤️ upon the excellent foundation of [@jwalsh/mcp-server-qrcode](https://github.com/jwalsh/mcp-server-qrcode)**
