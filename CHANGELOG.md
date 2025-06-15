# Changelog

All notable changes to the Enhanced QR Code MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-06-16

### Added
- **Complete Enhanced QR Code MCP Server** built upon [@jwalsh/mcp-server-qrcode](https://github.com/jwalsh/mcp-server-qrcode)
- **Automatic PNG file generation** to specified directories
- **Three new MCP tools**:
  - `generate_and_save_qrcode` - Single QR code generation with file saving
  - `batch_generate_qrcodes` - Multiple QR codes in one operation
  - `list_generated_qrcodes` - File management and listing
- **JSON metadata generation** for each QR code with:
  - Generation timestamp
  - Content and parameters
  - File size and location
- **Batch processing capabilities** with manifest generation
- **Custom filename support** with auto-generation fallback
- **Directory management** with automatic creation
- **Multiple error correction levels** (L, M, Q, H)
- **Scalable sizes and borders** (1-20 range)
- **Comprehensive test suite** with 4 test functions
- **Complete documentation** with usage examples
- **Automated setup script** for easy installation
- **MCP client configuration** examples
- **Production-ready features**:
  - Error handling and validation
  - File organization and tracking
  - Performance optimization
  - Comprehensive logging

### Enhanced from Original
- **File Output**: Changed from chat-only display to automatic PNG file saving
- **Metadata**: Added comprehensive JSON metadata tracking
- **Batch Processing**: Added multi-QR generation capabilities
- **File Management**: Added directory organization and file listing
- **Configuration**: Added extensive customization options
- **Testing**: Added complete test suite with validation
- **Documentation**: Added comprehensive documentation and examples

### Technical Details
- **Python 3.8+** compatibility
- **MCP Protocol 1.0+** compliance
- **Dependencies**: mcp, qrcode[pil], pillow
- **Architecture**: Async MCP server with file I/O integration
- **Performance**: ~50ms single QR + file save, ~100ms batch processing per code

### Files Added
- `src/enhanced_qrcode_server.py` - Main MCP server implementation
- `tests/test_server.py` - Comprehensive test suite
- `examples/mcp_config.json` - MCP client configuration
- `examples/usage_examples.md` - Detailed usage examples
- `setup.sh` - Automated installation script
- `requirements.txt` - Python dependencies
- `LICENSE` - MIT License with original attribution
- `CONTRIBUTING.md` - Contribution guidelines
- `README.md` - Complete project documentation
- `.gitignore` - Project-specific ignore patterns

### Attribution
- Built upon the excellent foundation of [@jwalsh/mcp-server-qrcode](https://github.com/jwalsh/mcp-server-qrcode)
- Maintains full compatibility with MCP protocol specifications
- Adds significant enhancements while preserving original functionality

---

## Versioning Notes

**Version 2.0.0** represents a major enhancement over the original MCP QR code server:
- **v1.x**: Original @jwalsh/mcp-server-qrcode (chat display only)
- **v2.0.0**: Enhanced version with automatic file generation and comprehensive features

The version jump to 2.0.0 reflects the significant additional functionality while maintaining backward compatibility with the MCP protocol.