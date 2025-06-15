#!/usr/bin/env python3
"""
Enhanced QR Code MCP Server
Automatically saves PNG files to specified directories with complete integration

Built upon and enhanced from: @jwalsh/mcp-server-qrcode
Enhancements: Automatic PNG file saving, batch processing, metadata generation,
file management, and production-ready features.
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Sequence
import qrcode
from datetime import datetime

# MCP imports
try:
    from mcp.server import Server, NotificationOptions
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError:
    print("MCP library not found. Install with: pip install mcp")
    sys.exit(1)

# Server setup
server = Server("enhanced-qrcode")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available QR code tools with enhanced file saving capabilities"""
    return [
        types.Tool(
            name="generate_and_save_qrcode",
            description="Generate QR code and automatically save as PNG file to specified directory",
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The text content to encode in the QR code"
                    },
                    "output_directory": {
                        "type": "string", 
                        "description": "Directory path where the PNG file will be saved",
                        "default": "./qr_output/"
                    },
                    "filename": {
                        "type": "string",
                        "description": "Custom filename (without extension) or auto-generate if empty",
                        "default": ""
                    },
                    "errorCorrectionLevel": {
                        "type": "string",
                        "enum": ["L", "M", "Q", "H"],
                        "description": "Error correction level (L: 7%, M: 15%, Q: 25%, H: 30%)",
                        "default": "M"
                    },
                    "size": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 20,
                        "description": "Size of the QR code (1-20, affects box_size)",
                        "default": 5
                    },
                    "border": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 20,
                        "description": "Border size around QR code",
                        "default": 4
                    },
                    "include_metadata": {
                        "type": "boolean",
                        "description": "Generate metadata JSON file alongside PNG",
                        "default": True
                    },
                    "display_in_chat": {
                        "type": "boolean", 
                        "description": "Also display QR code in chat interface",
                        "default": True
                    }
                },
                "required": ["content"]
            }
        ),
        types.Tool(
            name="batch_generate_qrcodes",
            description="Generate multiple QR codes from JSON input and save all as PNG files",
            inputSchema={
                "type": "object",
                "properties": {
                    "qr_codes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "content": {"type": "string"},
                                "filename": {"type": "string", "default": ""},
                                "type": {"type": "string", "default": "general"}
                            },
                            "required": ["id", "content"]
                        },
                        "description": "Array of QR code specifications"
                    },
                    "output_directory": {
                        "type": "string",
                        "description": "Base directory for all generated files",
                        "default": "./qr_output/"
                    },
                    "errorCorrectionLevel": {
                        "type": "string",
                        "enum": ["L", "M", "Q", "H"],
                        "default": "M"
                    },
                    "size": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 20,
                        "default": 5
                    }
                },
                "required": ["qr_codes"]
            }
        ),
        types.Tool(
            name="list_generated_qrcodes",
            description="List all QR code files in a directory with metadata",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory to scan for QR code files",
                        "default": "./qr_output/"
                    }
                }
            }
        )
    ]

def create_qr_code_image(content: str, error_correction: str = "M", box_size: int = 10, border: int = 4) -> qrcode.QRCode:
    """Create QR code object with specified parameters"""
    
    # Map error correction levels
    error_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_levels.get(error_correction, qrcode.constants.ERROR_CORRECT_M),
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(content)
    qr.make(fit=True)
    
    return qr

def generate_filename(content: str, custom_filename: str = "", file_id: str = "") -> str:
    """Generate appropriate filename for QR code"""
    
    if custom_filename:
        return custom_filename
    
    if file_id:
        return f"qr_{file_id}"
    
    # Generate from content
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    content_preview = "".join(c for c in content[:20] if c.isalnum() or c in " -_").strip()
    content_preview = content_preview.replace(" ", "_")
    
    return f"qr_{timestamp}_{content_preview}"

def save_metadata(filepath: str, content: str, parameters: dict) -> str:
    """Save QR code metadata as JSON"""
    
    metadata = {
        "generated_date": datetime.now().isoformat(),
        "content": content,
        "parameters": parameters,
        "png_file": filepath,
        "file_size_bytes": os.path.getsize(filepath) if os.path.exists(filepath) else 0
    }
    
    metadata_path = filepath.replace('.png', '_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return metadata_path

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent | types.ImageContent]:
    """Handle tool calls for enhanced QR code generation"""
    
    if name == "generate_and_save_qrcode":
        return await handle_generate_and_save_qrcode(arguments or {})
    elif name == "batch_generate_qrcodes":
        return await handle_batch_generate_qrcodes(arguments or {})
    elif name == "list_generated_qrcodes":
        return await handle_list_generated_qrcodes(arguments or {})
    else:
        raise ValueError(f"Unknown tool: {name}")

async def handle_generate_and_save_qrcode(arguments: dict) -> list[types.TextContent | types.ImageContent]:
    """Generate QR code and save as PNG file with metadata"""
    
    content = arguments.get("content", "")
    output_directory = arguments.get("output_directory", "./qr_output/")
    custom_filename = arguments.get("filename", "")
    error_correction = arguments.get("errorCorrectionLevel", "M")
    size = arguments.get("size", 5)
    border = arguments.get("border", 4)
    include_metadata = arguments.get("include_metadata", True)
    display_in_chat = arguments.get("display_in_chat", True)
    
    if not content:
        return [types.TextContent(type="text", text="Error: Content cannot be empty")]
    
    # Ensure output directory exists
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = generate_filename(content, custom_filename)
    filepath = os.path.join(output_directory, f"{filename}.png")
    
    try:
        # Create QR code
        qr = create_qr_code_image(content, error_correction, size * 2, border)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save PNG file
        img.save(filepath)
        
        # Save metadata if requested
        metadata_path = ""
        if include_metadata:
            parameters = {
                "error_correction": error_correction,
                "size": size,
                "border": border,
                "box_size": size * 2
            }
            metadata_path = save_metadata(filepath, content, parameters)
        
        # Create response
        response = []
        
        # Add text response with file info
        file_info = f"""✅ QR Code Generated and Saved Successfully!

📁 **File Location**: {filepath}
📊 **File Size**: {os.path.getsize(filepath)} bytes
🔧 **Parameters**:
   - Content: {content[:50]}{'...' if len(content) > 50 else ''}
   - Error Correction: {error_correction}
   - Size: {size}
   - Border: {border}
"""
        
        if metadata_path:
            file_info += f"📋 **Metadata**: {metadata_path}\n"
        
        response.append(types.TextContent(type="text", text=file_info))
        
        # Display in chat if requested
        if display_in_chat:
            # Create a smaller version for chat display
            qr_display = create_qr_code_image(content, error_correction, 3, 2)
            img_display = qr_display.make_image(fill_color="black", back_color="white")
            
            # Convert to base64 for display
            import base64
            import io
            
            buffer = io.BytesIO()
            img_display.save(buffer, format='PNG')
            img_data = base64.b64encode(buffer.getvalue()).decode()
            
            response.append(types.ImageContent(
                type="image",
                data=img_data,
                mimeType="image/png"
            ))
        
        return response
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"❌ Error generating QR code: {str(e)}")]

async def handle_batch_generate_qrcodes(arguments: dict) -> list[types.TextContent]:
    """Generate multiple QR codes in batch"""
    
    qr_codes = arguments.get("qr_codes", [])
    output_directory = arguments.get("output_directory", "./qr_output/")
    error_correction = arguments.get("errorCorrectionLevel", "M")
    size = arguments.get("size", 5)
    
    if not qr_codes:
        return [types.TextContent(type="text", text="Error: No QR codes specified")]
    
    # Ensure output directory exists
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    
    results = []
    generated_files = []
    
    for qr_spec in qr_codes:
        qr_id = qr_spec.get("id", "")
        content = qr_spec.get("content", "")
        custom_filename = qr_spec.get("filename", "")
        qr_type = qr_spec.get("type", "general")
        
        if not content:
            results.append(f"❌ Skipped {qr_id}: No content")
            continue
        
        try:
            # Generate filename
            filename = generate_filename(content, custom_filename, qr_id)
            filepath = os.path.join(output_directory, f"{filename}.png")
            
            # Create and save QR code
            qr = create_qr_code_image(content, error_correction, size * 2, 4)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filepath)
            
            # Save metadata
            parameters = {
                "id": qr_id,
                "type": qr_type,
                "error_correction": error_correction,
                "size": size
            }
            metadata_path = save_metadata(filepath, content, parameters)
            
            results.append(f"✅ Generated {qr_id}: {filename}.png")
            generated_files.append({
                "id": qr_id,
                "type": qr_type,
                "filename": f"{filename}.png",
                "filepath": filepath,
                "metadata": metadata_path,
                "size_bytes": os.path.getsize(filepath)
            })
            
        except Exception as e:
            results.append(f"❌ Failed {qr_id}: {str(e)}")
    
    # Save batch manifest
    manifest = {
        "batch_date": datetime.now().isoformat(),
        "total_requested": len(qr_codes),
        "total_generated": len(generated_files),
        "output_directory": output_directory,
        "files": generated_files
    }
    
    manifest_path = os.path.join(output_directory, f"batch_manifest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    summary = f"""🎯 **Batch QR Code Generation Complete**

📊 **Summary**:
   - Requested: {len(qr_codes)}
   - Generated: {len(generated_files)}
   - Failed: {len(qr_codes) - len(generated_files)}

📁 **Output Directory**: {output_directory}
📋 **Batch Manifest**: {manifest_path}

**Results**:
{chr(10).join(results)}
"""
    
    return [types.TextContent(type="text", text=summary)]

async def handle_list_generated_qrcodes(arguments: dict) -> list[types.TextContent]:
    """List all QR code files in directory"""
    
    directory = arguments.get("directory", "./qr_output/")
    
    if not os.path.exists(directory):
        return [types.TextContent(type="text", text=f"❌ Directory not found: {directory}")]
    
    # Find all PNG files
    png_files = []
    metadata_files = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.png') and filename.startswith('qr_'):
            png_files.append(filename)
        elif filename.endswith('_metadata.json'):
            metadata_files.append(filename)
    
    png_files.sort()
    
    if not png_files:
        return [types.TextContent(type="text", text=f"📁 No QR code files found in {directory}")]
    
    file_list = [f"📁 **QR Code Files in {directory}**\n"]
    
    for png_file in png_files:
        filepath = os.path.join(directory, png_file)
        file_size = os.path.getsize(filepath)
        
        # Check for metadata
        metadata_file = png_file.replace('.png', '_metadata.json')
        has_metadata = metadata_file in metadata_files
        
        file_list.append(f"📄 **{png_file}**")
        file_list.append(f"   Size: {file_size} bytes")
        file_list.append(f"   Metadata: {'✅' if has_metadata else '❌'}")
        
        # Load metadata if available
        if has_metadata:
            try:
                metadata_path = os.path.join(directory, metadata_file)
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                
                content_preview = metadata.get('content', '')[:50]
                if len(metadata.get('content', '')) > 50:
                    content_preview += '...'
                
                file_list.append(f"   Content: {content_preview}")
                file_list.append(f"   Generated: {metadata.get('generated_date', 'Unknown')}")
            except:
                pass
        
        file_list.append("")
    
    file_list.append(f"**Total Files**: {len(png_files)} PNG files, {len(metadata_files)} metadata files")
    
    return [types.TextContent(type="text", text="\n".join(file_list))]

async def main():
    """Main server function"""
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="enhanced-qrcode",
                server_version="2.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())