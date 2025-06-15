#!/bin/bash

# Enhanced QR Code MCP Server Setup Script

echo "🚀 Setting up Enhanced QR Code MCP Server..."

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🔧 Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Make the server script executable
chmod +x src/enhanced_qrcode_server.py

# Create default output directory
mkdir -p qr_output

# Test the installation
echo "🧪 Testing installation..."
python3 -c "import qrcode, mcp; print('✅ All dependencies installed successfully')"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Add the MCP configuration to your client:"
echo "   Copy contents of examples/mcp_config.json to your MCP client configuration"
echo ""
echo "2. Test the server:"
echo "   python3 src/enhanced_qrcode_server.py"
echo ""
echo "3. Run tests:"
echo "   python3 tests/test_server.py"
echo ""
echo "4. Use with MCP client to generate QR codes with automatic file saving"
echo ""
echo "🔧 Enhanced Features:"
echo "  ✅ Automatic PNG file saving to specified directories"
echo "  ✅ Metadata generation with each QR code"
echo "  ✅ Batch processing capabilities"
echo "  ✅ File listing and management"
echo "  ✅ Custom filename support"
echo "  ✅ Multiple error correction levels"
echo "  ✅ Scalable sizes and borders"
echo ""